import scripts.interface as s
import datetime
import bpy
import sys
from pathlib import Path

# For simple readability, these variables are used to address Blender contexts, scenes, objects, or operators.
A = bpy.app
C = bpy.context
D = bpy.data

start_time = None

O = bpy.ops

def render_progress_callback(scene):
    """
    Function to print out progress bar while rendering animation.

    Parameters
    ----------
    scene : bpy.types.Scene
        The current scene being rendered.
    """
    global start_time

    frame = scene.frame_current
    total_frames = scene.frame_end
    if total_frames == 0:
        progress = 1
    else:
        progress = frame / total_frames
    bar_length = 40
    prog_bar = int(bar_length * progress)

    current_time = datetime.datetime.now()
    elapsed_time = (current_time - start_time).total_seconds()
    time_per_frame = elapsed_time / (frame - scene.frame_start + 1)
    remaining_frames = total_frames - (frame - scene.frame_start + 1)
    estimated_remaining_time = remaining_frames * time_per_frame

    remaining_time_str = str(datetime.timedelta(seconds=int(estimated_remaining_time)))

    sys.stdout.write(f"\rRendering: [{'=' * prog_bar}{' ' * (bar_length - prog_bar)}] {int(progress * 100)}%\nRemaining time: {remaining_time_str}\n")
    sys.stdout.flush()

def optimize_render_settings():
    """
    Function to optimize render settings for faster rendering.
    """
    C.scene.render.use_motion_blur = False  # Disable motion blur if not needed
    C.scene.render.use_simplify = True  # Enable scene simplification for faster preview renders
    C.scene.render.use_border = False  # Disable rendering of a specific region to render the entire frame

def render_video():
    """
    Renders a video to the specified path file, starting at frame 'start' and ending at frame 'end'.

    Parameters
    ----------
    path : str
        The file path where the video will be saved.
    start : int
        The starting frame of the video.
    end : int
        The ending frame of the video.
    """
    global start_time

    C.scene.render.filepath = str(Path(s.SRC_VID / s.FILENAME))
    C.scene.frame_start = s.S_FRAME
    C.scene.frame_end = s.E_FRAME
    C.scene.render.engine = 'BLENDER_EEVEE'
    C.scene.render.image_settings.file_format = 'FFMPEG'
    C.scene.render.ffmpeg.format = 'MPEG4'
    C.scene.render.ffmpeg.codec = 'H264'

    render_samples()

    # Optimize rendering settings
    optimize_render_settings()

    start_time = datetime.datetime.now()

    # Set the callback function for the render progress
    A.handlers.render_pre.append(render_progress_callback)

    # Render animation
    O.render.render(animation=True)

    # Remove the callback function after rendering is complete
    A.handlers.render_pre.remove(render_progress_callback)

def render_samples():
    """
    Sets the render samples for Eevee render engine. This has influence 
    on how complex the final animation is. More samples allows for more
    soft shadowing and anti-aliasing, both not that important in our 
    use case.

    - samples (int): The number of render samples to set. Renderer takes
    time-steps for sample sizes of 26. So optimize by using a multiple of
    26 for maximum samples in minimum render time.
    """
    # Access the render settings for the Eevee render engine
    render_settings = C.scene.eevee

    # Set the render samples
    render_settings.taa_render_samples = s.SAMPLES