import bpy
# settings may apear unused, but attaches path to scripts to the system,
# allowing for importing other local scripts
import scripts.interface
from scripts.object_helper import clean_duplicate_objs, duplicate_object

C = bpy.context
D = bpy.data
O = bpy.ops

def create_difference(obj1, obj2):
    """Create a boolean difference between two objects.

    Parameters
    ----------
    obj1 : bpy.types.Object
        The first object to use for operation.
    obj2 : bpy.types.Object
        The second object to use for operation.
    """
    obj1.select_set(True)
    C.view_layer.objects.active = obj1

    # Create new difference modifier and apply it between obj1 and obj2
    bool_mod = C.active_object.modifiers.new(name="Boolean", type='BOOLEAN')
    bool_mod.object = obj2
    bool_mod.solver = 'FAST'
    bool_mod.operation = 'DIFFERENCE'

    O.object.modifier_apply(modifier=bool_mod.name)

def create_intersection(obj, inner):
    """Create a boolean intersection between two objects.

    Parameters
    ----------
    obj : bpy.types.Object
        The object for intersection.
    inner : bpy.types.Object
        The inner object.
    """
    inner.select_set(True)
    C.view_layer.objects.active = inner

    # Create new intersection modifier and apply it to the obj and intersection object
    # (inner) is the result of the initial intersection between the two objs
    bool_mod = C.active_object.modifiers.new(name="Boolean", type='BOOLEAN')
    bool_mod.object = obj
    bool_mod.solver = 'FAST'
    bool_mod.operation = 'INTERSECT'
    O.object.modifier_apply(modifier=bool_mod.name)

def create_overlap(gt, pred):
    """Handle the entire boolean operations to get a final product of an intersection object,
    and the two differences (false negative & false positive).

    Parameters
    ----------
    gt : bpy.types.Object
        The ground truth object.
    pred : bpy.types.Object
        The predicted object.
    """
    # Get the number of the current frame operated on and duplicate objs for temporary
    # working objects
    num = gt.name.split('_')[-1]
    inner = duplicate_object(gt, f'inner_{num}')
    temp = duplicate_object(pred, f'temp_{num}')

    # Perform operations needed for end product: starting with creating the true positives
    # by making intersection between prediction and ground-truth (inner at this stage is
    # the duplicate of ground-truth). After this, create difference of both objs with the
    # true positives and clean-up temporary working objects from scene.
    create_intersection(pred, inner)
    create_difference(pred, gt)
    create_difference(gt, temp)
    clean_duplicate_objs()
