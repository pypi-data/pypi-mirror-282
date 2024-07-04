import math
import numpy as np
from scipy.optimize import linear_sum_assignment

def calculate_distance(coords1, coords2):
    """
    Helper function that calculates the Euclidean distance between two 3D coordinates.

    Parameters
    ----------
    coords1 : tuple
        First set of coordinates (x, y, z).
    coords2 : tuple
        Second set of coordinates (x, y, z).
    
    Returns
    -------
    float
        The Euclidean distance between the two sets of coordinates.
    """
    return math.sqrt(sum((c1 - c2)**2 for c1, c2 in zip(coords1, coords2)))

def min_cost(df, list_points):
    """
    Helper function to calculate a matrix of all distances for coordinates of nuclei 
    in Blender to coordinates found in the tracking file. Minimum cost assignment 
    is done via the Hungarian algorithm and returned.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the coordinates of nuclei in Blender.
    list_points : list
        List of coordinates found in the tracking file.
    
    Returns
    -------
    dict
        A dictionary mapping coordinates to their corresponding IDs.
    """
    # Calculate distance matrix
    distance_matrix = np.array([[calculate_distance(df.loc[i, ['x', 'y', 'z']], point) for point in list_points] for i in df.index])
    # Apply Hungarian algorithm
    _, col_ind = linear_sum_assignment(distance_matrix)

    # Retrieve results
    optimal_assignment = {list_points[j]: df.loc[i, 'id'] for i, j in enumerate(col_ind, start=df.index.min())}
    return optimal_assignment

def rename_obj(obj, min_cost_mat):
    """
    Helper function to rename a nuclei to fit their match as calculated by the 
    Hungarian algorithm. This method requires the min_cost_mat as calculated by the
    min_cost() function and renames the object to its corresponding ID in the tracking file.

    Parameters
    ---------- 
    obj : bpy.types.Object
        The object to be renamed.
    min_cost_mat : dict
        A dictionary mapping coordinates to their corresponding IDs.
    """
    coords = (obj.location.x, obj.location.y, obj.location.z)
    formatted_coords = tuple(round(coord, 2) for coord in coords)
    
    # Rename objects to their correct ID as found in the mastodon track file.
    # Try-catch can be invoked when the tracking file or mesh prediction mispredicts,
    # which is not uncommon in scenarios like cell division.
    try:
        obj_id = min_cost_mat[formatted_coords]
    except KeyError:
        obj_id = 'Not_Found'

    obj.name = f"{obj_id}"
    