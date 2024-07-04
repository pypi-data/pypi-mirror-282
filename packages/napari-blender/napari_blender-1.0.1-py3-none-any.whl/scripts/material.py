import colorsys
import bpy
import scripts.interface as s

D = bpy.data

def hsv_to_rgb(color):
    """
    Convert HSV color representation to RGB.

    Parameters
    ----------
    color : tuple
        A tuple containing hue, saturation, and value components.

    Returns
    -------
    tuple
        RGB color tuple.
    """
    h, s, v = color
    return colorsys.hsv_to_rgb(h, s, v)

def rgb_to_hsv(color):
    """
    Convert RGB color representation to HSV.

    Parameters
    ----------
    color : tuple
        A tuple containing red, green, and blue components.

    Returns
    -------
    tuple
        HSV color tuple.
    """
    r, g, b = color
    return colorsys.rgb_to_hsv(r, g, b)

def create_material(mat_name, color, blend):
    """
    Create a material with the given name and color.

    Parameters
    ----------
    mat_name : str
        Name of the material.
    color : tuple
        HSV color tuple (hue, saturation, value, alpha).
    blend : str
        Blend mode for the material.
    """
    if mat_name in D.materials:
        print(f'Material {mat_name} already exists in this scene')
    else:
        new_material = D.materials.new(name=mat_name)
        new_material.use_nodes = True
        tree = new_material.node_tree
        nodes = tree.nodes
        links = tree.links

        for node in nodes:
            nodes.remove(node)

        principled = nodes.new(type='ShaderNodeBsdfPrincipled')
        material_output = nodes.new(type='ShaderNodeOutputMaterial')
        links.new(principled.outputs['BSDF'], material_output.inputs['Surface'])

        r, g, b = hsv_to_rgb(color[:3])
        principled.inputs['Base Color'].default_value = (r, g, b, 1.0)
        principled.inputs["Alpha"].default_value = color[3]

        new_material.blend_method = blend
        new_material.shadow_method = 'NONE'
        if blend == 'BLEND':
            new_material.use_backface_culling = True

def create_child_material(obj, shift):
    """
    Create a material based on another objects color by shifting the hue.

    Parameters
    ----------
    obj : bpy.types.Object
        The object whose material to adapt.
    shift : float
        Amount to change the hue value with.

    Returns
    -------
    str
        The name of the changed material.
    """
    if obj.material_slots:
        mat = obj.material_slots[obj.active_material_index].material
        new_material = mat.copy()
        new_material.name = mat.name + f"_{shift}"

        principled = new_material.node_tree.nodes["Principled BSDF"]
        h, s, v = rgb_to_hsv(principled.inputs["Base Color"].default_value[:3])
        r, g, b = hsv_to_rgb((h+shift, s, v))
        principled.inputs["Base Color"].default_value = (r, g, b, principled.inputs["Base Color"].default_value[-1])
        return new_material.name
    else:
        print("No materials assigned to the object.")

def color_nuclei(parent, i):
    """
    Color nuclei based on a given metric value.

    Parameters
    ----------
    parent : bpy.types.Object
        The parent object.
    i : int
        Index for the metric value.
    """
    ji_vals = s.METRICS[i]['ji_vals']
    children_objs = parent.children

    for child_obj in children_objs:
        group_id = child_obj.get("Group_ID")
        if group_id is not None:
            try:
                group_id = int(group_id)
            except ValueError:
                print(f"Warning: Invalid group_id {group_id} for object {child_obj.name}")
                continue

            if s.GT_NAME in parent.name:
                matching_tuples = [t for t in ji_vals if t[0] == group_id]
                if not matching_tuples or matching_tuples[0][1] == 0:
                    set_material(child_obj, 'Not Predicted')  
                    print(f'{group_id} not predicted')
                else:
                    print(f'Should be removed')
                    D.objects.remove(child_obj, do_unlink=True)

            if s.PRED_NAME in parent.name:
                print(f'pred found in obj: {child_obj.name}')
                matching_tuples = [t for t in ji_vals if t[1] == group_id]
                if matching_tuples:
                    set_hue(child_obj, matching_tuples[0][2])
                else:
                    set_material(child_obj, 'False Prediction')
        else:
            print(f"Warning: Group_ID not found for object {child_obj.name}")

def clamp_hue(ji):
    """
    Clamp the hue value to a specific range.

    Parameters
    ----------
    ji : float
        The hue value to clamp [0..1].

    Returns
    -------
    float or None
        Clamped hue value.
    """
    if ji is not None and 0 <= ji <= 1:
        new_value = ji * 0.3
        return new_value
    else:
        print(f"Jaccard index should be within the range [0, 1] but was {ji}")
        return None

def set_hue(obj, metric):
    """
    Set the hue of an object based on a metric value.

    Parameters
    ----------
    obj : bpy.types.Object
        The object to set the hue.
    metric : float
        Metric value to determine the hue [0..1].
    """
    try:
        hue = clamp_hue(metric)
        create_material(f'Base_hue_{hue:.2f}', (hue, 1, 0.43, 1.0), 'OPAQUE')
        set_material(obj, f'Base_hue_{hue:.2f}')
    except TypeError:
        print(f'Could not create material with hue {hue}')

def set_material(obj, mat_name):
    """
    Set material to an object.

    Parameters
    ----------
    obj : bpy.types.Object
        Object to set the material to.
    mat_name : str
        Material to set. If None, it removes any existing materials.
    """
    try:
        mat = find_material(mat_name)
        if obj.data.materials:
            obj.data.materials[0] = mat
        else:
            obj.data.materials.append(mat)
    except MaterialNotFoundException:
        pass

def find_material(mat_name):
    """
    Find a material by its name.

    Parameters
    ----------
    mat_name : str
        Name of the material.

    Returns
    -------
    bpy.types.Material
        The material, if present, otherwise raise error.
    """
    mat = D.materials.get(mat_name)
    if mat is not None:
        return mat
    else:
        print(f'Material {mat_name} not found')
        raise MaterialNotFoundException()

class MaterialNotFoundException(Exception):
    """
    Custom exception for material not found in the scene.
    """
    pass
