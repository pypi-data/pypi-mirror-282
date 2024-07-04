from enum import Enum

class MODES(Enum):
    """
    Enumeration for different modes of visualization.

    Attributes:
    Transparant: Mode that compares predictions by Boolean operations.
    Gradient: Mode that compares predictions by coloring the predicted organoid.
    Tracked: Mode that tracks individual organoids over time.
    Timelapse: Mode that shows the movement of organoids over time.
    """
    Transparant = 'transparant'
    Microscopy = 'microscopy'
    Gradient = 'gradient'
    Tracked = 'tracked'
    Timelapse = 'timelapse'

class SAMPLES(Enum):
    """
    Enumeration for different sampling resolutions. Multiples of 26
    to leverage the batch size of Blender rendering to it's maximum.

    Attributes:
    Low: Low sampling resolution.
    Medium: Medium sampling resolution.
    High: High sampling resolution.
    """
    Low = 1
    Medium = 26
    High = 52

class ROTATION(Enum):
    """
    Enumeration for different rotation speeds.

    Attributes:
    No_Rotation: No rotation. Picture Mode.
    Very_Slow: Very slow rotation speed. 300 frames per rotation.
    Slow: Slow rotation speed. 200 frames per rotation.
    Normal: Normal rotation speed. 150 frames per rotation.
    Quick: Quick rotation speed. 100 frames per rotation.
    Very_Quick: Very quick rotation speed. 50 frames per rotation.
    """
    No_Rotation = 1
    Very_Slow = 300
    Slow = 200
    Normal = 150
    Quick = 100
    Very_Quick = 50
    
class METRIC(Enum):
    JI_Index = ('ji', 'Jaccard Index')
    IoU = ('iou', 'IoU')
    Precision = ('precision', 'Precision')
    Recall = ('recall', 'Recall')
    F1_Score = ('f1', 'F1 Score')

