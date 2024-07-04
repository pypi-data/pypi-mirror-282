def track_ancestor(df, obj_id):
    """
    Finds the ancestor ID of a given ID in the DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the track data.
    obj_id : str
        The ID for which to find the ancestor.

    Returns
    -------
    str or None
        The ancestor ID if found, otherwise None.
    """
    # First check if the original object has been found
    if 'Not_Found' in obj_id:
        print('Not found nucleus can not have an ancestor')
        return None
    # Get the row corresponding to the desired id
    row = df.loc[df['id'] == int(obj_id)]

    if not row.empty:
        track = row['track'].iat[0]
        frame = row['frame'].iat[0]
        # Filter rows where track and frame match the desired values
        ancestor_row = df[(df['track'] == track) & (df['frame'] == frame - 1)]

        if not ancestor_row.empty:
            ancestor_id = ancestor_row['id'].iat[0]
            return ancestor_id
        print(f"No ancestor found for {obj_id}.")
    else:
        print(f"ID {obj_id} not found in the DataFrame.")
    return None

def track_child(df, obj_id):
    """
    Finds the child ID of a given ID in the DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the track data.
    obj_id : str
        The ID for which to find the child.

    Returns
    -------
    str or None
        The child ID if found, otherwise None.
    """
    # First check if the original object has been found
    if 'Not_Found' in obj_id:
        print('Not found nucleus can not have a child')
        return None
    # Get the row corresponding to the desired id
    row = df.loc[df['id'] == int(obj_id)]

    if not row.empty:
        track = row['track'].iat[0]
        frame = row['frame'].iat[0]
        # Filter rows where track and frame match the desired values
        child_row = df[(df['track'] == track) & (df['frame'] == frame + 1)]

        if not child_row.empty:
            child_id = child_row['id'].iat[0]
            return child_id
        else:
            print(f"No child found for {obj_id}.")
    else:
        print(f"ID {obj_id} not found in the DataFrame.")
    return None

def get_track(df, obj_id):
    """
    Finds the track ID of a given ID in the DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the track data.
    obj_id : str
        The ID for which to find the child.

    Returns
    -------
    str or None
        The track ID if found, otherwise None.
    """
    # First check if the original object has been found
    if 'Not_Found' in obj_id:
        print('Not found nucleus can not have a track')
        return None
    # Get the row corresponding to the desired id
    row = df.loc[df['id'] == int(obj_id)]

    if not row.empty:
        track = row['track'].iat[0]
        return track
    else:
        print(f"ID {obj_id} not found in the DataFrame.")
    return None
