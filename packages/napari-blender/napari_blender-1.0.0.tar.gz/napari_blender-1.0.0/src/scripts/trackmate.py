# Gathered from https://github.com/hadim/pytrackmate
# The library did not function correctly and has thus the necessary funtions
# have been imported and bugfixed

import xml.etree.cElementTree as et
import numpy as np
import pandas as pd

def trackmate_peak_import(trackmate_xml_path, get_tracks=False):
    """
    Import detected peaks with TrackMate Fiji plugin.

    Parameters
    ----------
    trackmate_xml_path : str
        TrackMate XML file path.
    get_tracks : bool
        Whether to include tracks.
    
    Returns
    -------
    pandas.DataFrame
        DataFrame containing the imported peak data.
    """
    # Parse the XML file
    root = et.fromstring(open(trackmate_xml_path).read())

    # Define object labels mapping [CHANGED] to fit own format
    object_labels = {
        'FRAME': 'frame',
        'POSITION_X': 'x',
        'POSITION_Y': 'y',
        'POSITION_Z': 'z',
        'ID': 'id',
    }

    # Extract features
    features = root.find('Model').find('FeatureDeclarations').find('SpotFeatures')
    
    # Original line [not functioning]:
    # features = [c.get('feature') for c in features.getchildren()] + ['ID']

    features = [c.get('feature') for c in list(features)] + ['ID']

    # Extract spots
    spots = root.find('Model').find('AllSpots')
    trajs = pd.DataFrame([])
    objects = []
    for frame in spots.findall('SpotsInFrame'):
        for spot in frame.findall('Spot'):
            single_object = []
            for label in features:
                single_object.append(spot.get(label))
            objects.append(single_object)

    # Create DataFrame from extracted objects
    trajs = pd.DataFrame(objects, columns=features)
    trajs = trajs.astype(float)

    # Apply initial filtering
    initial_filter = root.find("Settings").find("InitialSpotFilter")
    trajs = filter_spots(trajs,
                         name=initial_filter.get('feature'),
                         value=float(initial_filter.get('value')),
                         isabove=True if initial_filter.get('isabove') == 'true' else False)

    # Apply filters
    spot_filters = root.find("Settings").find("SpotFilterCollection")
    for spot_filter in spot_filters.findall('Filter'):
        trajs = filter_spots(trajs,
                             name=spot_filter.get('feature'),
                             value=float(spot_filter.get('value')),
                             isabove=True if spot_filter.get('isabove') == 'true' else False)

    # Rename columns and add track numbers
    trajs = trajs.loc[:, object_labels.keys()]
    trajs.columns = [object_labels[k] for k in object_labels.keys()]
    trajs['track'] = np.arange(trajs.shape[0])

    # Get tracks if specified
    if get_tracks:
        filtered_track_ids = [int(track.get('TRACK_ID')) for track in root.find('Model').find('FilteredTracks').findall('TrackID')]
        label_id = 0
        trajs['track'] = np.nan
        tracks = root.find('Model').find('AllTracks')
        for track in tracks.findall('Track'):
            track_id = int(track.get("TRACK_ID"))
            if track_id in filtered_track_ids:
                spot_ids = [(edge.get('SPOT_SOURCE_ID'), edge.get('SPOT_TARGET_ID'), edge.get('EDGE_TIME')) for edge in track.findall('Edge')]
                spot_ids = np.array(spot_ids).astype('float')[:, :2]
                spot_ids = set(spot_ids.flatten())
                trajs.loc[trajs["id"].isin(spot_ids), "track"] = label_id
                label_id += 1
        single_track = trajs.loc[trajs["track"].isnull()]
        trajs.loc[trajs["track"].isnull(), "track"] = label_id + np.arange(0, len(single_track))

    # Convert certain columns to integer
    for row in ['frame', 'id', 'track']:
        trajs[row] = trajs[row].astype(int)

    return trajs

def filter_spots(spots, name, value, isabove):
    """
    Filter spots based on a certain condition.

    Parameters:
    Parameters
    ----------
    spots : pandas.DataFrame
        DataFrame containing spots data.
    name : str
        Feature name.
    value : float
        Threshold value.
    isabove : bool
        If True, filter spots above the threshold, otherwise below.
    
    Returns
    -------
    pandas.DataFrame
        Filtered DataFrame.
    """
    if isabove:
        spots = spots[spots[name] > value]
    else:
        spots = spots[spots[name] < value]
    return spots
