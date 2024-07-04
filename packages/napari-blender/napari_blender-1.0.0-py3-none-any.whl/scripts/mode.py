from abc import ABC, abstractmethod
import bpy
import scripts.interface as s
from scripts.scene_helper import change_scene_obj, register
from scripts.object_helper import set_rotation, find_collection, set_interpolation, CollectionNotFoundException
from scripts.shapekey import hide_in_render
from napari.qt.threading import thread_worker

C = bpy.context
D = bpy.data

class Mode(ABC):
    """
    Parent class for all modes of visualization.
    """
    @abstractmethod
    def init_dicts(self):
        """
        Method that will initialize the dictionaries of objects/materials to be created
        or changed before importing the scene.
        """
            
    @abstractmethod
    def import_obj(self, obj_name, src, i):
        """
        Method to import an object into the scene.
        
        Parameters
        ----------
        obj_name : str
            Name of object to import/create.
        src : str
            File location where data about object can be found.
        i : int
            Index of current frame needed to be imported.
        """

    def pre_import(self):
        """"
        Method that can be called to change the scene before importing frames.
        """
        # Register frame counter for rendering
        register()
        # Populate dictionaries using child implementation, and call method to change
        # scene according to their content.
        dicts = self.init_dicts()
        change_scene_obj(dicts)
        return dicts['objs']

    def post_import(self):
        """
        Method that can be called to change the scene after importing frames.
        """

    def set_scene(self, i):
        """
        Method that changes the scene per imported frame.

        Parameters
        ----------
        i : int
            Enumerator of which frame is being added in the loop, starts at 0
        """
        # Get index that corresponds with the absolute frame number
        index = i - s.START
        try:
            # Apply transformations to objects that are used in all methods
            coll = find_collection(f"Frame_{i}")
            for obj in coll.all_objects[:]:
                # if ('gt' in obj.name or 'inner' in obj.name or 'pred' in obj.name) and obj.type == "MESH":
                #     set_rotation(obj, s.LENGTH * index, s.LENGTH + s.LENGTH * index)
                #     set_interpolation(obj,'LINEAR')
                hide_in_render(obj, index, s.LENGTH)
        except CollectionNotFoundException:
            print(f'Setting up frame {i} suspended due to not finding collection \'Frame_{i}\'')

    # @thread_worker
    def visualize(self):
        """
        Code that calls the full-pipeline of visualization.
        """
        # Call pre-scene import code
        objs = self.pre_import()
        # Loop through frames
        for i in range(s.START, s.END + 1):
            # Create collections for each absolute frame number
            coll_target = D.collections.get(f"Frame_{i}")
            if coll_target is None:
                coll_target = D.collections.new(name=f"Frame_{i}")
                C.scene.collection.children.link(coll_target)

            C.view_layer.active_layer_collection = \
                C.view_layer.layer_collection.children[f"Frame_{i}"]
            
            # Go over the dictionary that contains desired object names and their
            # data source, and import them into the scene.
            for obj_name, data in objs.items():
                self.import_obj(obj_name+str(i), data, i)
            
            # Call child specific code for importing a frame at index i
            self.set_scene(i)
     
        # Call post-scene import code
        self.post_import()
