import bpy
import scripts.interface as s
from scripts.material import create_material, set_material
from scripts.object_helper import find_object, find_collection, CollectionNotFoundException, ObjectNotFoundException

# Access Blender's context, data, operations, and scene
A = bpy.app
C = bpy.context
D = bpy.data
O = bpy.ops

def recalculate_text(scene):
    """
    Recalculate text for the current frame.

    Parameters
    ----------
    scene : bpy.types.Scene
        The scene in which rendering is performed.
    """
    if s.LENGTH > 0:
        frame = s.START + C.scene.frame_current // s.LENGTH
    else:
        frame = s.START + C.scene.frame_current
    change_text(f'Frame: {frame}','Frame')
    try:
                # change_text(f"Metrics: \n# nuclei GT: {s.METRICS[frame]['nuclei_truth']}\n# nuclei predicted: {s.METRICS[frame]['nuclei_pred']}\n\nIoU: {s.METRICS[frame]['iou']:.2f}\nJI: {s.METRICS[frame]['ji']:.2f}\nPrecision: {s.METRICS[frame]['precision']:.2f}\nRecall: {s.METRICS[frame]['recall']:.2f}\nF1-score: {s.METRICS[frame]['f1']:.2f}",'Metrics')
        change_text(f"Metrics: \n\nIoU: {s.METRICS[frame]['iou']:.2f}\nJI: {s.METRICS[frame]['ji']:.2f}\nPrecision: {s.METRICS[frame]['precision']:.2f}\nRecall: {s.METRICS[frame]['recall']:.2f}\nF1-score: {s.METRICS[frame]['f1']:.2f}",'Metrics')
    except KeyError:
        pass
    
def register():
    """
    Register frame change handler.
    """
    A.handlers.frame_change_post.append(recalculate_text)

def unregister():
    """
    Unregister frame change handler if it exists.
    """
    try:
        A.handlers.frame_change_post.remove(recalculate_text)
    except ValueError:
        print("Handler recalculate_text not found in frame_change_post, skipping removal.")


def change_text(text, text_name):
    """
    Changes the text of a specified text object in the scene.

    Parameters
    ----------
    text : str
        The new text to set.
    text_name : str
        The name of the text object to modify.
    """
    # Find the text object by name
    try:
        text_obj = find_object(text_name)
        text_obj.data.body = text
    except ObjectNotFoundException:
        print('Changing text suspended')


def clamp_indicator(metric):
    """
    Clamp the indicator value.

    Parameters
    ----------
    metric : float
        The metric value to clamp.
    
    Returns
    -------
    float
        Clamped metric value.
    """
    # Check if value is within the range [0, 1]
    if metric is not None and 0 <= metric <= 1:
        # Rescale the value to the range [0.335, 0].
        # This is the hue that represents a dark green color
        # that will show a prediction to be perfect
        new_value = -0.34 + (0.36 + 0.34) * metric
        return new_value
    else:
        print(f"Metric should be within the range [0, 1] but was {metric}")
        return 0


def set_indicator(metric, frame=None):
    """
    Set the indicator based on metric value.

    Parameters
    ----------
    metric : float
        The metric value.
    frame : int, optional
        The frame to set the keyframe.
    """
    try:
        ind = find_object('Indicator')
        # Get, and change, the z-coordinate of the metric indicator object. Since it
        # is clamped to a path, the clamped value will set the indicator to the relative
        # position indicating the metric value on the metric bar.
        z = clamp_indicator(metric)
        ind.delta_location = (0, 0, z)
        # If a frame is given, set it as keyframe for when to reach that value
        if frame is not None:
            ind.keyframe_insert(data_path="delta_location", index=-1, frame=frame, group="Delta Transform")
    except ObjectNotFoundException:
        print('Setting metric indicator suspended')


def change_scene_obj(dicts):
    """
    Helper function that applies changes to the scene based on a dictionary generated
    by different visualization modes. This arranges the scene to be ready for that mode.

    Parameters
    ----------
    dicts : dict
        Dictionary containing multiple dictionaries, indicating the required starting
        conditions for the visualization mode.
    """
    # Get sub-dictionaries that indicate respective imports
    texts = dicts['texts']
    materials = dicts['materials']
    hide_obj = dicts['hide_obj']
        
    # Change all text objects indicated
    for text_name, text in texts.items():
        change_text(text, text_name)

    # Generate all indicated materials
    for count, (mat_name, values) in enumerate(materials.items()):
        # Check if material contains the correct number of parameters
        if len(values) == 5:
            create_material(mat_name, values[:4], values[-1])
            # Set this material to be correctly displayed in the color legend
            set_legend_color(mat_name, count+1)
        else:
            print('Material color object does not contain the correct amount of values.:\n(Hue,Saturation,Value,Alpha,Material Blend Mode)')
    
    # After creating materials, hide unused legend items from render.
    hide_legend_items(len(materials))

    # (Un)Hide all objects indicated
    for obj_name, hide in hide_obj.items():
        try:
            # First check if name is collection, before checking if it is an object
            coll = find_collection(obj_name)
            coll.hide_render = hide
        except CollectionNotFoundException:
            try:
                obj = find_object(obj_name)
                obj.hide_render = hide
            except ObjectNotFoundException:
                print(f'Changing hide render setting to {hide} failed')

def set_gradient_color(mode):
    """
    In the Gradient visualization mode, the Gradient material is complicated and 
    always already included in the scene. Set this material to the legend, and
    change needed text to fit this.

    Parameters
    ----------
    mode : str
        The visualization mode that is set to the program.
    """
    match mode:
        case 'Gradient': 
            num = 2
        case 'Colored Nuclei':
            num = 3
        case  _:
            num = 0
    try:
        mat_obj = find_object(f'Mat_{num}')
        mat_obj.hide_render = False
        set_material(mat_obj, 'Gradient')
        mat_text = find_object(f'Mat_{num}_name')
        mat_text.hide_render = False
        change_text('Prediction',f'Mat_{2}_name')
    except ObjectNotFoundException:
        pass

def set_legend_color(mat_name, num):
    """
    Function to set a legend item to be a color, and display it's correct name.

    Parameters
    ----------
    mat_name : str
        Material name that will be set to the text.
    num : int
        Enumerator of what legend item should be set.
    """
    # The legend items are named 'Mat_{1,2,3}', and will be changed in sequence
    change_text(mat_name, f'Mat_{num}_name')
    try:
        mat_obj = find_object(f'Mat_{num}')
        mat_obj.hide_render = False
        mat_text = find_object(f'Mat_{num}_name')
        mat_text.hide_render = False
        set_material(mat_obj, mat_name)
    except ObjectNotFoundException:
        pass  

def hide_legend_items(count):
    """
    Function that is called to hide unused legend items from render.

    Parameters
    ----------
    count : int
        Number of legend items that will be used.
    """
    # Run loop that removes used legend items from the {1,2,3} domain.
    for i in range(1+count,4):
        try:
            mat_obj = find_object(f'Mat_{i}')
            mat_obj.hide_render = True
            mat_text = find_object(f'Mat_{i}_name')
            mat_text.hide_render = True
        except ObjectNotFoundException:
            pass
