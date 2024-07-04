import sys
import os
from pathlib import Path
import bpy
from napari_video.napari_video import VideoReaderNP
import math

A = bpy.app
D = bpy.data
O = bpy.ops     
# Set path to where the scripts are, this differs when ran in command line or from Blender.
script_path = Path(os.getcwd()) if A.background else (Path(D.filepath).parents[1] / 'scripts')

# Add the script path and original path to sys.path for imports
if str(script_path) not in sys.path:
    sys.path.append(str(script_path))


def open_blend():
    # Open the main Blender file if running in background mode
    if A.background:
        filepath = str(Path(__file__).parents[1] / 'scenes' / "render_scene.blend")
        try:
            O.wm.open_mainfile(filepath=filepath)
            print(f"File opened successfully: {filepath}")
        except Exception as e:
            print(f"Error opening file: {e}")

# Import custom functions and classes from various modules
from scripts.metrics import metrics_dictionary
from scripts.parse import clean_data, downscale_image_by_sampling
from scripts.compare import Transparant, Gradient, Tracked, Timelapse, Microscopy
from scripts.enums import MODES
from scripts.render import render_video

# Initialize global variables for configuration and data
LENGTH = None
FRAME_OFFSET = 41
START = None
END = None
S_FRAME = 0
E_FRAME = None
SAMPLES = None
METRICS = {}

renderer = None

# Define paths to source images and files
DATA1 = None
DATA2 = None
SRC_3D = Path(__file__).parents[1] / '3d'
TRACK = None
SRC_VID = None
FILENAME = None
GT_NAME = None
PRED_NAME = None
SHOW_TEXT = None
HUE_METRIC = None
CREATE_GROUND_TRUTH = None
SAVE_SCENE = None
SCENE_NAME = None

def set_values(dict, viewer, mode):
    """
    Set global values from a dictionary and initialize processing.

    Parameters:
    -----------
    dict : dict
        Dictionary containing configuration values.
    viewer : Napari viewer instance
        Napari viewer instance.
    mode : str
        Visualization mode.
    """
    global TRACK, START, END, LENGTH, SAMPLES, METRICS, E_FRAME, SRC_VID, FILENAME, DATA1, DATA2, GT_NAME, PRED_NAME, SHOW_TEXT, HUE_METRIC
    for k, v in dict.items():
        globals()[k] = v
    if DATA1 is not None:
        GT_NAME += "_"
        if DATA2 is not None:
            PRED_NAME += "_"
            if GT_NAME == PRED_NAME:
                PRED_NAME = "pred-" + PRED_NAME
            # If both images are there, calculate metrics of comparison.
            for i in range(START, END + 1):
                clean_data1 = clean_data(DATA1, i)
                clean_data2 = clean_data(DATA2, i)
                METRICS[i] = metrics_dictionary(clean_data1, clean_data2)
            # Scale the data down for quicker computation, and to keep objects
            # in the frame.
            scale = max(math.floor(DATA2.shape[1] / 150), 1)
            DATA2 = downscale_image_by_sampling(DATA2, scale)
        scale = max(math.floor(DATA1.shape[1] / 150), 1)
        DATA1 = downscale_image_by_sampling(DATA1, scale)
        E_FRAME = (END - START) * LENGTH + LENGTH
        visualize(viewer, mode)
    if SAVE_SCENE:
        O.wm.save_as_mainfile(filepath=str(Path(Path(__file__).parents[1] / 'scenes' / SCENE_NAME)))
    O.wm.quit_blender()

    # print_globals()

def visualize(viewer, mode):
    """
    Visualize the data in Blender based on the selected mode.

    Parameters:
    -----------
    viewer : Napari viewer instance
        Napari viewer instance.
    mode : str
        Visualization mode.
    """
    open_blend()
    # Revert the main file to the original state, this combats not being able
    # to run the script multiple times in a row.
    match mode:
        case MODES.Transparant:
            tr = Transparant()
            tr.visualize()
        case MODES.Gradient:
            gr = Gradient()
            gr.visualize()
        case MODES.Tracked:
            tr = Tracked()
            tr.visualize()
        case MODES.Timelapse:
            tl = Timelapse()
            tl.visualize()
        case MODES.Microscopy:
            mc = Microscopy()
            mc.visualize()
        case _:
            print("Invalid mode")
    render_video()
    display(viewer)

def display(viewer):
    """
    Display the rendered video in the Napari viewer.

    Parameters:
    -----------
    viewer : Napari viewer instance
        Napari viewer instance.
    """
    path = str(Path(SRC_VID / FILENAME))
    vr = VideoReaderNP(path)
    ratio = 1.5 * DATA1.shape[2] / vr.shape[2]
    
    # Add the image to the existing viewer
    viewer.add_image(vr, name='Loaded Video', scale=(1.0, ratio, ratio))

def print_globals():
    """
    Print global variables for debugging purposes.
    """
    global_vars = globals()
    for k, v in global_vars.items():
        print(f"{k}: {v}")
