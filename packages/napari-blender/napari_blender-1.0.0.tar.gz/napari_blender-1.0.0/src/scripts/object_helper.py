import math
import io
from contextlib import redirect_stdout
import bpy
from mathutils import Vector
import math

# Importing scripts from the project
import scripts.interface as s
from scripts.parse import create_obj, clean_data, create_contour_obj
from scripts.rename import min_cost, rename_obj

# Blender context shortcuts
C = bpy.context
D = bpy.data
O = bpy.ops

def remesh_objects(obj, vert_count):
    """
    Helper function to set the amount of vertices in an object to vert_count.
    This code is useful to get a uniform vertex count over objects that have to
    morph into one another.

    Parameters
    ----------
    obj : bpy.types.Object
        The object whose vertices need to be adjusted.
    vert_count : int
        The desired number of vertices for the object.
    """
   
    if len(obj.data.vertices) > vert_count:
        # Apply the decimate modifier to ensure a certain number of vertices
        O.object.mode_set(mode='OBJECT')

        decimate_modifier = obj.modifiers.new(name="Decimate", type='DECIMATE')
        decimate_modifier.ratio = vert_count / len(obj.data.vertices)

        obj.select_set(True)
        C.view_layer.objects.active = obj
        
        # Apply the modifier
        O.object.modifier_apply(modifier="Decimate")
        
    if len(obj.data.vertices) < vert_count:
        obj.select_set(True)
        C.view_layer.objects.active = obj

        mesh = obj.data

        subdiv_num = int(math.ceil((vert_count-len(obj.data.vertices))/3))
        step = int(math.floor(len(obj.data.vertices)/subdiv_num))
        for i in range(0,subdiv_num):
            mesh.polygons[i*step].select = True
            
        O.object.mode_set(mode='EDIT')
        O.mesh.subdivide()

        O.object.mode_set(mode='OBJECT')
        O.object.select_all(action='DESELECT')

    # This method may end on a couple vertices too few or too much, recursive
    # calling fixes this problem.
    while len(obj.data.vertices) != vert_count:
        remesh_objects(obj, vert_count)
    
    # Shade object smooth for cleaner render object
    # Commented out for aesthetic reasons, for now.
    # with C.temp_override(selected_editable_objects=[obj]):
    #     O.object.shade_smooth()

def get_all_coords(nuclei):
    """
    Function to get coordinates for all objects in a frame.
    This code facilitates the minimum cost Hungarian algorithm implementation.

    Parameters
    ----------
    nuclei : list
        List of objects in the scene/frame.
    
    Returns
    -------
    list
        A list of coordinates for all objects in the specified collection.
    """
    all_coords = []
    for obj in nuclei:
        coords = (obj.location.x, obj.location.y, obj.location.z)

        # Format to set amount of decimals to minimize rounding errors in comparison
        formatted_coords = tuple(round(coord, 2) for coord in coords)
        all_coords.append(formatted_coords)
    return all_coords

def clean_duplicate_objs():
    """
    Clean up duplicate objects in the scene.
    """
    # Get all objects in the scene
    all_objects = D.objects

    # Iterate through objects and delete those with a dot in their name,
    # since objects with names that exist in the scene are named using "name".001,
    # this cleans up already imported objects.
    for obj in all_objects:
        if ("." in obj.name or "temp" in obj.name) and obj.type == "MESH":
            D.objects.remove(obj, do_unlink=True)

def import_object(name, data, use_groups, index):
    """
    Create an object in the scene.

    Parameters
    ----------
    name : str
        Name of the object.
    data : numpy.ndarray
        Data to create the object from.
    use_groups : bool
        Whether to use split groups, creates a single or multiple objects.
    index : int
        Index of the current frame.

    Returns
    -------
    list
        A list of objects created in the scene.
    """
    try:
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            obj = find_object(name)
        return obj
    except ObjectNotFoundException:
        dim_name = name + '.obj'
        obj_src = s.SRC_3D / dim_name
        # First check if object is already made as 3D object in default directory,
        # if so, import without additional computations.
        if obj_src.is_file():
            print(f'Note: Object {str(obj_src)} already exists as 3D object, importing this.\nIf other 3D object is desired, delete existing one, or change its name.')
            stdout = io.StringIO()
            with redirect_stdout(stdout):
                O.wm.obj_import(filepath=str(obj_src), use_split_groups= use_groups)                 
        # If there is not yet a 3D object of this object, create it from the source data.
        else:
            try:
                data = clean_data(data,index)
                parts = name.split('_')
                original_name = '_'.join(parts[:-1])
                if s.CREATE_GROUND_TRUTH and s.GT_NAME == original_name + '_':
                    create_contour_obj(data, obj_src)
                else:
                    create_obj(data,obj_src)
                stdout = io.StringIO()
                with redirect_stdout(stdout):
                    O.wm.obj_import(filepath=str(obj_src), use_split_groups= use_groups)
            except IndexError:
                print('Index error, no object created')
                return
            
        imported_object = C.selected_objects[0]
        num = name.rsplit('_', 1)[-1]
        # Rename the object
        if s.PRED_NAME is not None and s.PRED_NAME in name and not use_groups:
            imported_object.name = f'pred_{num}'
        elif s.GT_NAME in name and not use_groups:
            imported_object.name = f'gt_{num}'

    return [obj for obj in C.selected_objects if obj.type == 'MESH']
    
def set_origin_nuclei(nuclei, name, i):
    """
    Sets the origin point for a group of nuclei objects and creates a parent empty object.

    This function calculates the average location of a group of nuclei objects, sets their origins
    to the average location, and then creates a new empty object to parent all nuclei objects to.

    Parameters
    ----------
    nuclei : list
        A list of Blender objects representing the nuclei.
    name : str
        The name of the empty object that will be created to parent all nuclei objects.
    """
    index = i - s.START

    acc_location = Vector((0, 0, 0))
    for obj in nuclei:
        O.object.select_all(action='DESELECT')
        obj.select_set(True)
        obj['Group_ID'] = obj.name.split('.')[0]
        obj.rotation_euler = ( 0.0, 0.0, 0.0)
        O.object.origin_set(type='ORIGIN_GEOMETRY')
        acc_location += obj.location

    # Calculate average location (center of mass)
    num_objects = len(nuclei)
    if num_objects > 0:
        average_location = acc_location / num_objects
    else:
        print("No mesh objects selected.")
    
    # Create a new empty object to parent all imported meshes
    O.object.empty_add()
    empty_object = C.object
    empty_object.location = average_location
    
    # Parent all mesh objects to the empty object
    for obj in nuclei:
        O.object.select_all(action='DESELECT')
        obj.select_set(True)
        O.object.parent_no_inverse_set(keep_transform=True)
    
    empty_object.name = name
    empty_object.location = Vector((0,0,0))
    empty_object.scale = ( 0.045, 0.045, 0.045 )   

    set_rotation(empty_object, s.LENGTH * index, s.LENGTH + s.LENGTH * index)
    set_interpolation(empty_object,'LINEAR')

def scale_object(obj):
    """
    Scale, rotate and set object to the origin of the scene.

    Parameters
    ----------
    obj : bpy.types.Object
        Object to manipulate.
    """
    C.view_layer.objects.active = obj
    ob = C.selected_objects[-1]
    # Set rotation of object to 0 degrees on all axes. Importing an image is often
    # done using an automatic 90 degree x-axis rotation, which hampers the renaming of nuclei.
    ob.rotation_euler = ( 0.0, 0.0, 0.0)
    # Set the origin to geometry, this places the object to 0,0,0 in the scene
    O.object.origin_set(type='GEOMETRY_ORIGIN')
    # Scale object to fit the camera of the scene.
    ob.scale = ( 0.045, 0.045, 0.045 )
    
def rename_nuclei(objects, data_frame, i):
    """
    Scale, rotate, create submeshes and rename all nuclei from original 3D object.

    Parameters
    ----------
    objects: list
        List of objects to manipulate.
    data_frame: pandas.DataFrame
        DataFrame containing the tracking data.
    i: int 
        Index of the current frame.
    """
    nuclei = objects
    filt_nuclei = []

    for ob in nuclei:
        if len(ob.data.vertices) < 50:
            # Select and delete the object
            D.objects.remove(ob, do_unlink=True)
        else:  
            filt_nuclei.append(ob)
                    
    # get all coordinates of nuclei objects and calculate the minimum cost
    # id allocation using the Hungarian algorithm
    all_coords = get_all_coords(filt_nuclei)
    min_cost_mat = min_cost(data_frame.loc[data_frame['frame'] == i-1], all_coords)
    
    # go over all objects to properties and manipulate them
    for obj in filt_nuclei:
        # set all objects to have the same vertex count
        remesh_objects(obj, 1000)

        # rename objects in Blender to their id as given by tracking file
        rename_obj(obj, min_cost_mat)

def set_rotation(obj, start, end):
    """
    Sets keyframes for rotation of an object.

    Parameters
    ----------
    obj : bpy.types.Object
        The object to rotate.
    start : int
        Frame number on which to start the rotation.
    end : int
        Frame number on which to end the rotation.
    """
    # Set keyframes for rotation
    obj.rotation_euler.z = math.radians(0)  # Set rotation to 0 degrees in radians
    obj.keyframe_insert(data_path="rotation_euler", index=2, frame=start)

    obj.rotation_euler.z = math.radians(360)  # Set rotation to 360 degrees in radians
    obj.keyframe_insert(data_path="rotation_euler", index=2, frame=end)

def set_parent(parent, child):
    """
    Sets a parent-child relationship between two objects. Useful for 
    getting multiple objects to follow the same keyframes, or hiding
    them in the same line of code.

    Parameters
    ----------
    parent : bpy.types.Object
        The parent object.
    child : bpy.types.Object
        The child object.
    """
    child.select_set(True)
    parent.select_set(True)
    O.object.parent_set(type='OBJECT', keep_transform=True)

def duplicate_object(obj, name):
    """
    Duplicate the object and rename the duplicated object.

    Parameters
    ----------
    obj : bpy.types.Object
        Object to duplicate.
    name : str
        Name for the duplicated object.
    
    Returns
    -------
    bpy.types.Object
        The duplicated object.
    """
    obj.select_set(True)
    C.view_layer.objects.active = obj
    
    # Duplicate the selected object
    O.object.duplicate()
    
    # Get the newly duplicated object
    duplicated_obj = C.active_object
    
    # Rename the duplicated object
    duplicated_obj.name = name
    duplicated_obj.data.name = name

    return duplicated_obj

def find_object(name):
    """"
    Function to find an object in the scene, or raise an error
    if this object is not found.

    Parameters
    ----------
    name : str
        Name of the desired object.
    """
    obj = D.objects.get(name)
    if obj is not None:
        return obj
    else:
        print(f'Object {name} was not found')
        raise ObjectNotFoundException()
    
def find_collection(name):
    """
    Function to find a collection in the scene, or raise an error
    if this collection is not found.

    Parameters
    ----------
    name : str
        Name of the desired collection.
    """
    coll = D.collections.get(name)
    if coll is not None:
        return coll
    else:
        print(f'Collection {name} was not found')
        raise CollectionNotFoundException()
    
def set_interpolation(obj, style):
    """
    Set interpolation style for object animation.

    Parameters
    ----------
    obj : bpy.types.Object 
        The object to set interpolation for.
    style : str
        The style of interpolation, linear is used in most use cases.
    """
    fcurves = obj.animation_data.action.fcurves
    for fcurve in fcurves:
        for kf in fcurve.keyframe_points:
            kf.interpolation = style

    
class ObjectNotFoundException(Exception):
    """
    Custom exception for when an object is not found in the scene.
    """
    pass

class CollectionNotFoundException(Exception):
    """
    Custom exception for when a collection is not found in the scene.
    """
    pass
