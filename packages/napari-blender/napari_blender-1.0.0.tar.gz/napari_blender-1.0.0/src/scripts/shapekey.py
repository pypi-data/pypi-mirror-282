import numpy as np
from scipy.optimize import linear_sum_assignment
import bpy
import scripts.interface as s

# Define commonly used Blender contexts for readability
C = bpy.context
D = bpy.data
O = bpy.ops

def hide_in_render(obj, count, length):
    """
    Hide an object in renders for a specific range of frames.

    Parameters
    ----------
    obj : bpy.types.Object
        The object to hide in renders.
    count : int
        The frame count to determine when to hide and show the object.
    length : int
        The length of time the object should be rendered.
    """
    # Show object and set keyframe
    obj.hide_render = False
    obj.keyframe_insert(data_path='hide_render', frame=length * count)

    # Hide object and set keyframe after specified time
    obj.hide_render = True
    obj.keyframe_insert(data_path='hide_render', frame=length + length * count)
    
    # Hide all child objects initially to be morphed by ancestors
    if count > 0:
        # Set keyframes for hide_render property
        obj.hide_render = True
        obj.keyframe_insert(data_path='hide_render', frame=0)

def apply_shape_key(obj, target, index):
    """
    Set shape key to morph one object into another.

    Parameters
    ----------
    obj : bpy.types.Object
        The object to morph.
    target : bpy.types.Object
        The object to morph into.
    index : int
        The index of the current frame.
    """
    # Ensure the target object has the same number of vertices as the object
    # if len(obj.data.vertices) != len(target.data.vertices):
    #     print(f'{len(obj.data.vertices)} != {len(target.data.vertices)}')
    #     print(f"Error: Objects ({obj.name} & {target.name}) have different number of vertices.")
    #     return

    obj.shape_key_add(from_mix=False)
    obj.shape_key_add(name='Morph')

    # Get the coordinates of vertices for both objects
    obj_vertices = np.array([vert.co for vert in obj.data.vertices])
    target_vertices = np.array([vert.co for vert in target.data.vertices])

    # Calculate the cost matrix (Euclidean distance between vertices)
    cost_matrix = np.linalg.norm(obj_vertices[:, np.newaxis] - target_vertices, axis=2)

    # Use Hungarian algorithm to find the minimum cost vertex mapping
    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    # Apply the shape key by mapping vertices from the target to the object
    for i, j in zip(row_ind, col_ind):
        w = target.data.vertices[j]
        obj.data.shape_keys.key_blocks['Morph'].data[i].co = w.co
    
    set_shape_keys(obj, target, index)

def set_shape_keys(obj, target, index):
    """
    Helper function to set the frames at which the shape keys need to be a certain value.

    Parameters
    ----------
    obj : bpy.types.Object
        The object to morph.
    target : bpy.types.Object
        The object to morph into.
    index : int
        The index of the current frame.
    """
    start_loc = obj.location
    start, end = s.LENGTH * index, s.LENGTH + s.LENGTH * index
    obj.keyframe_insert(data_path="location", frame=start)
    obj.location = target.location
    obj.keyframe_insert(data_path="location", frame=end)
    obj.location = start_loc

    shape_key = obj.data.shape_keys.key_blocks["Morph"]
    shape_key.keyframe_insert("value", frame=start)
    shape_key.value = 1
    shape_key.keyframe_insert("value", frame=end)
