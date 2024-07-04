from pathlib import Path
import sys
import os
import bpy

# Shortcuts for commonly used Blender contexts and operations
A = bpy.app
C = bpy.context
D = bpy.data
O = bpy.ops

# Determine the script path based on whether Blender is running in background mode
script_path = Path(os.getcwd()) if A.background else (Path(D.data.filepath).parents[1] / 'scripts')

# Add the script path and original path to sys.path for imports
if str(script_path) not in sys.path:
    sys.path.append(str(script_path))

# Import custom functions from various modules
import scripts.interface as s
from scripts.material import set_material, set_hue, create_child_material, color_nuclei
from scripts.boolean_ops import create_overlap
from scripts.scene_helper import set_indicator, set_gradient_color, change_text
from scripts.mode import Mode
from scripts.parse import read_trackmate
from scripts.lineage import track_child, track_ancestor, get_track
from scripts.shapekey import hide_in_render, apply_shape_key
from scripts.object_helper import (import_object, rename_nuclei, set_origin_nuclei, find_object, duplicate_object, set_interpolation,
                                   clean_duplicate_objs, find_collection, ObjectNotFoundException, CollectionNotFoundException)

# Initialize global variables
mitosis_nuclei = {}
data_frame = []

class Transparant(Mode):
    """
    Mode that compares predictions by Boolean operations. End-result is an intersecting object
    containing True Positives, and two objects that are only predicted in one of the two predictions
    which we call False Negatives and False Positives.
    """
    def init_dicts(self):
        """
        Mode specific objects/materials needed to be created or changed.
        """
        dicts = {}
        dicts['texts'] = {}
        dicts['materials'] = {
            'True Positive': (0.0, 0.0, 0.8, 1.0, 'OPAQUE'), 
            'False Negative': (0.035, 1.0, 0.8, 0.35, 'BLEND'), 
            'False Positive': (0.6, 1.0, 0.8, 0.35, 'BLEND')
        }
        if s.SHOW_TEXT:
            dicts['hide_obj'] = {'Gradient_Bar': True, 'Metrics': False}
        else:
            dicts['hide_obj'] = {'Gradient_Bar': True, 'Metrics': True, 'Frame': True}
        dicts['objs'] = {s.GT_NAME: s.DATA1, s.PRED_NAME: s.DATA2}
        return dicts
    
    def import_obj(self, obj_name, data, i):
        """
        Mode specific way of importing organoid objects.
        
        Parameters
        ----------
        obj_name : str
            Name of object to import/create.
        data : Any
            Data source for the object.
        i : int
            Index of current frame needed to be imported.
        """
        nuclei = import_object(obj_name, data, False, i)
        set_origin_nuclei(nuclei, obj_name, i)

    def set_scene(self, i):
        """
        Mode specific code for importing each frame.

        Parameters
        ----------
        i : int
            Enumerator of current frame.
        """
        try:
            inner = find_object(f'inner_{i}')
        except ObjectNotFoundException:
            # If the inner object does not exist, perform boolean operations
            try:
                gt_obj = find_object(f'gt_{i}')
                comp_obj = find_object(f'pred_{i}')

                create_overlap(gt_obj, comp_obj)

                inner = find_object(f'inner_{i}')
            except ObjectNotFoundException:
                print(f'Setting up frame {i} suspended')

            # Set materials for objects based on the boolean operation results
            set_material(inner, 'True Positive')
            set_material(gt_obj, 'False Negative')
            set_material(comp_obj, 'False Positive')  
            super().set_scene(i)

class Microscopy(Mode):
    """
    Mode that compares raw microscopy data with a prediction. End-result is an transparant overlay
    containing microscopy data, and an object that contains the segmentation. The former is automated
    but is not a perfect representation of the nuclei in space.
    """
    def init_dicts(self):
        """
        Mode specific objects/materials needed to be created or changed.
        """
        dicts = {}
        dicts['texts'] = {}
        dicts['materials'] = {'Ground-Truth': (0.0, 0.0, 0.8, 0.15, 'BLEND'), 'Prediction': (0.6, 1.0, 0.8, 1.0, 'OPAQUE')}
        if s.SHOW_TEXT:
            dicts['hide_obj'] = {'Gradient_Bar': True, 'Metrics': True, 'Frame': False}
        else:
            dicts['hide_obj'] = {'Gradient_Bar': True, 'Metrics': True, 'Frame': True}
        dicts['objs'] = {s.GT_NAME: s.DATA1, s.PRED_NAME: s.DATA2}
        return dicts
    
    def import_obj(self, obj_name, data, i):
        """
        Mode specific way of importing organoid objects.
        
        Parameters
        ----------
        obj_name : str
            Name of object to import/create.
        data : Any
            Data source for the object.
        i : int
            Index of current frame needed to be imported.
        """
        nuclei = import_object(obj_name, data, False, i)
        set_origin_nuclei(nuclei, obj_name, i)

    def set_scene(self, i):
        """
        Mode specific code for importing each frame.

        Parameters
        ----------
        i : int
            Enumerator of current frame.
        """
        # Compute the relative index of the current frame.
        index = i - s.START

        # Compute metrics for the current frame objects.
        try:
            pred_obj = find_object(f'pred_{i}')
            gt_obj = find_object(f'gt_{i}')
            
            set_material(pred_obj, 'Prediction')
            set_material(gt_obj, 'Ground-Truth')
        except ObjectNotFoundException:
            print(f'Setting up frame {i} suspended')
        super().set_scene(i)

class Gradient(Mode):
    """
    Mode that compares predictions by coloring the predicted organoid. End-result is a prediction
    colored using a specific metric, and the volume being transparent.
    """
    def init_dicts(self):
        """
        Mode specific objects/materials needed to be created or changed.
        """
        dicts = {}
        dicts['texts'] = {}
        dicts['materials'] = {'Ground-Truth': (0.0, 0.0, 0.8, 0.3, 'BLEND')}
        if s.SHOW_TEXT:
            dicts['hide_obj'] = {'Gradient_Bar': False, 'Indicator': False, 'Metrics': True}
        else:
            dicts['hide_obj'] = {'Gradient_Bar': False, 'Indicator': False, 'Metrics': True, 'Frame': True} 
        dicts['objs'] = {s.GT_NAME: s.DATA1, s.PRED_NAME: s.DATA2}
        return dicts
            
    def set_scene(self, i):
        """
        Mode specific code for importing each frame.

        Parameters
        ----------
        i : int
            Enumerator of current frame.
        """
        # Compute the relative index of the current frame.
        index = i - s.START

        # Compute metrics for the current frame objects.
        try:
            pred_obj = find_object(f'pred_{i}')
            gt_obj = find_object(f'gt_{i}')
            
            set_hue(pred_obj, s.METRICS[i][s.HUE_METRIC.value[0]])
            set_material(gt_obj, 'Ground-Truth')
        except ObjectNotFoundException:
            print(f'Setting up frame {i} suspended')
        set_indicator(s.METRICS[i][s.HUE_METRIC.value[0]], s.LENGTH * index)
        change_text(s.HUE_METRIC.value[1], 'Metric')
        set_gradient_color('Gradient')
        super().set_scene(i)

    def import_obj(self, obj_name, data, i):
        """
        Mode specific way of importing organoid objects.
        
        Parameters
        ----------
        obj_name : str
            Name of object to import/create.
        data : Any
            Data source for the object.
        i : int
            Index of current frame needed to be imported.
        """
        nuclei = import_object(obj_name, data, False, i)
        set_origin_nuclei(nuclei, obj_name, i)

    def post_import(self):
        """
        Mode specific code to be run after importing all frames.
        """
        try:
            indicator = find_object('Indicator')
            mat_obj = find_object('Mat_2')
            mat_name = find_object('Mat_2_name')
            mat_obj.hide_render = False
            mat_name.hide_render = False            
        except ObjectNotFoundException:
            print('Setting indicator object suspended')
        set_interpolation(indicator, 'CONSTANT')

class Tracked(Mode):
    def init_dicts(self):
        """
        Mode specific objects/materials needed to be created or changed.
        """
        global data_frame
        data_frame = read_trackmate()
        dicts = {}
        dicts['texts'] = {}
        dicts['materials'] = {
            'Not Predicted': (0.45, 0.4, 0.8, 0.8, 'OPAQUE'), 
            'False Prediction': (0.8, 0.75, 0.8, 1.0, 'OPAQUE')
        }
        if s.SHOW_TEXT:
            dicts['hide_obj'] = {'Gradient_Bar': False, 'Metrics': True, 'Indicator': True}
        else:
            dicts['hide_obj'] = {'Gradient_Bar': False, 'Metrics': True, 'Indicator': True, 'Frame': True}
        dicts['objs'] = {s.GT_NAME: s.DATA1, s.PRED_NAME: s.DATA2}
        return dicts

    def import_obj(self, obj_name, data, i):
        """
        Mode specific way of importing organoid objects.
        
        Parameters
        ----------
        obj_name : str
            Name of object to import/create.
        data : Any
            Data source for the object.
        i : int
            Index of current frame needed to be imported.
        """
        nuclei = import_object(obj_name, data, True, i)
        set_origin_nuclei(nuclei, obj_name, i)
        rename_nuclei(nuclei, data_frame, i + s.FRAME_OFFSET)

    def set_scene(self, i):
        """
        Mode specific code for importing each frame.

        Parameters
        ----------
        i : int
            Enumerator of current frame.
        """
        index = i - s.START   
        try:
            coll = find_collection(f"Frame_{i}")      
            for obj in coll.all_objects[:]:
                if s.GT_NAME in obj.name or s.PRED_NAME in obj.name:
                    color_nuclei(obj, i)
        except CollectionNotFoundException:
            print(f'Setting up frame {i} suspended')
        super().set_scene(i)

class Timelapse(Mode):
    """
    Mode that shows the movement of organoids over time. This mode separates all nuclei,
    tracks them and links them using colors, or shades of colors if cell division occurs.
    """
    def init_dicts(self):
        """
        Mode specific objects/materials needed to be created or changed.
        """
        global data_frame
        data_frame = read_trackmate()
        dicts = {}
        dicts['texts'] = {}
        dicts['materials'] = {}
        for i in range(0, 5):
            dicts['materials'].update({f'Track {i+1}': (0.2 * i, 1.0, 0.8, 1.0, 'BLEND')})
        if s.SHOW_TEXT:
            dicts['hide_obj'] = {'Gradient_Bar': True, 'Legend': True, 'Metrics': True}
        else:
            dicts['hide_obj'] = {'Gradient_Bar': True, 'Legend': True, 'Metrics': True, 'Frame': True}
        dicts['objs'] = {s.GT_NAME: s.DATA1}
        return dicts
    
    def import_obj(self, obj_name, data, i):
        """
        Mode specific way of importing organoid objects.
        
        Parameters
        ----------
        obj_name : str
            Name of object to import/create.
        data : Any
            Data source for the object.
        i : int
            Index of current frame needed to be imported.
        """
        nuclei = import_object(obj_name, data, True, i)
        set_origin_nuclei(nuclei, obj_name, i)
        rename_nuclei(nuclei, data_frame, i + s.FRAME_OFFSET)

    def set_scene(self, i):
        """
        Mode specific code for importing each frame.

        Parameters
        ----------
        i : int
            Enumerator of current frame.
        """
        index = i - s.START   
        divided_nuclei = []
        try:
            coll = find_collection(f"Frame_{i}")      
            mesh_objects = [obj for obj in coll.all_objects if obj.type == 'MESH']
            for obj in mesh_objects:                
                # Show objects when needed in sequence render
                if index == 0:
                    track_id = get_track(data_frame, obj.name.split('.')[0])
                    set_material(obj, f'Track {track_id}')
                else:
                    ancestor_id = track_ancestor(data_frame, obj.name.split('.')[0])
                    if ancestor_id is None:
                        divided_nuclei.append(obj.name)
                hide_in_render(obj, index, s.LENGTH)
            mitosis_nuclei[i] = divided_nuclei
            divided_nuclei = []
        except CollectionNotFoundException:
            print(f'Setting up frame {i} suspended')

    def post_import(self):
        """
        Mode specific code to be run after importing all frames.
        """
        for i in range(s.START, s.END):
            index = i - s.START   
            try:
                coll = find_collection(f"Frame_{i}")         
                mesh_objects = [obj for obj in coll.all_objects if obj.type == 'MESH']
                for obj in mesh_objects:     
                    # Apply shrinkwrap modifiers to allow for parents of this object to morph
                    child_id = track_child(data_frame, obj.name.split('.')[0])
                    if child_id is not None:
                        try:
                            child = find_object(str(child_id))
                            if obj.material_slots:
                                mat_name = obj.material_slots[obj.active_material_index].material.name
                                set_material(child, mat_name)
                            apply_shape_key(obj, child, index) 
                        except ObjectNotFoundException:
                            print(f'Setting shrinkwrap keyframe from {child_id} to {obj.name} suspended')
                    else:
                        sign = 1
                        for div_nucleus in mitosis_nuclei[i+1]:
                            sign *= -1
                            try:
                                child = find_object(str(div_nucleus))
                                dupl_obj = duplicate_object(obj, f'{obj.name}-{div_nucleus}')
                                apply_shape_key(dupl_obj, child, index) 
                                child_mat = create_child_material(obj, sign * 0.04)
                                set_material(child, child_mat)
                                set_material(dupl_obj, child_mat)
                            except ObjectNotFoundException:
                                print(f'Setting shrinkwrap keyframe from {child_id} to {obj.name} suspended')
                        obj.name = f'{obj.name}.'
                        clean_duplicate_objs()
            except CollectionNotFoundException:
                print(f'Setting up shape keys for frame {i} suspended')

# Uncomment to profile performance
# import cProfile
# cProfile.run('t.visualize()', sort='cumulative')

# Code to create an object from the original convoluted data
# out = s.src_3d / "binary.obj"
# try:
#     data = read_img(s.src3, 42)
#     create_contour_obj(data, out)
# except IndexError:
#     pass
