import numpy as np
from scipy.ndimage import label
import skimage.metrics

def metrics_dictionary(img1, img2):
    """
    Calculates various metrics based on two images.

    Parameters
    ----------
    img1 : numpy.ndarray
        First input image in numpy array format.
    img2 : numpy.ndarray
        Second input image in numpy array format.

    Returns
    -------
    dict
        Dictionary containing calculated metrics.
    """
    metrics = {}
    
    truth, count_truth = label(img1)
    pred, count_pred = label(img2)

    are, prec, rec = calculate_are(truth, pred)

    f1 = 1 - are

    metrics['ji'] = calculate_jaccard(truth, pred)
    metrics['ji_vals'] = compare_labeled_volumes(truth, pred)
    metrics['nuclei_truth'] = count_truth
    metrics['nuclei_pred'] = count_pred
    metrics['iou'] = iou(truth, pred)
    metrics['precision'] = prec
    metrics['recall'] = rec
    metrics['f1'] = f1

    return metrics

def calculate_are(truth, pred):
    """
    Calculates adapted Rand error, precision, and recall.

    Parameters
    ----------
    truth : numpy.ndarray
        Ground truth labels.
    pred : numpy.ndarray
        Predicted labels.

    Returns
    -------
    tuple
        Adapted Rand error, precision, and recall.
    """
    return skimage.metrics.adapted_rand_error(truth, pred)

def iou(mask1, mask2):
    """
    Calculates Intersection over Union (IoU) score.

    Parameters
    ----------
    mask1 : numpy.ndarray
        First binary mask.
    mask2 : numpy.ndarray
        Second binary mask.

    Returns
    -------
    float
        Intersection over Union (IoU) score.
    """
    mask1 = mask1[:, :, :, 0] if mask1.shape[-1] == 3 else mask1
    mask2 = mask2[:, :, :, 0] if mask2.shape[-1] == 3 else mask2

    if mask1.shape != mask2.shape:
        raise ValueError("Input masks must have the same size.")

    intersection = np.logical_and(mask1, mask2)
    union = np.logical_or(mask1, mask2)

    iou_val = np.sum(intersection) / np.sum(union)
    return iou_val

def frequency(values):
    """
    Returns unique values in the array and their frequency of occurrence.

    Parameters
    ----------
    values : numpy.ndarray
        1D array of values.

    Returns
    -------
    tuple
        A tuple containing frequencies and corresponding labels.
    """
    lbls = np.unique(values)
    freq = np.array([np.sum(values == l) for l in lbls])
    return freq, lbls

def compare_labeled_volumes(truth, prediction):
    """
    Compares labelled volumes by performing a Jaccard Index (JI) calculation over all of 
    the labelled regions in the provided volumes.

    Parameters
    ----------
    truth : numpy.ndarray
        Ground truth labels.
    prediction : numpy.ndarray
        Predicted labels.

    Returns
    -------
    list of tuple
        A list of tuples containing truth label, prediction label, and Jaccard Index (JI).
    """
    tlabels = np.unique(truth)[1:]
    ji = []
    try:
        for label in tlabels:
            x, y, z = np.where(truth == label)
            values = prediction[x, y, z]
            freq, lbl = frequency(values)
            if lbl[0] == 0:
                freq[0] = 0
            mx = freq.max()
            mlbl = lbl[np.where(freq == mx)[0][0]]

            xp, _, _ = np.where(prediction == mlbl)
            ji.append((label, mlbl, 2 * mx / (len(x) + len(xp))))
        return ji
    except ValueError:
        print(f'There was a mismatch in the expected amount of labels in the data (3), and the labeled data provided ({tlabels.shape})')
        return

def calculate_jaccard(truth, prediction):
    """
    Calculates the Jaccard Index (JI) score between ground truth and predicted masks.

    Parameters
    ----------
    truth : numpy.ndarray
        Ground truth labels.
    prediction : numpy.ndarray
        Predicted labels.

    Returns
    -------
    float
        Jaccard Index (JI) score.
    """
    ji_values = compare_labeled_volumes(truth, prediction)
    try:
        final_values = [t[2] for t in ji_values]
        ji = sum(final_values) / len(final_values) if len(final_values) > 0 else 0
        return ji
    except TypeError:
        print('Could not calculate Jaccard index')

def confusion_matrix(truth, prediction):
    """
    Compute the confusion matrix between ground truth and predicted labels.

    Parameters
    ----------
    truth : numpy.ndarray
        Ground truth labels.
    prediction : numpy.ndarray
        Predicted labels.

    Returns
    -------
    tuple
        Confusion matrix as a 2D numpy array and corresponding labels.
    """
    tlabels = np.unique(truth)
    plabels = np.unique(prediction)

    num_classes = max(tlabels.max(), plabels.max()) + 1

    conf_matrix = np.zeros((num_classes, num_classes), dtype=np.int)
    labels = np.arange(num_classes)

    return conf_matrix, labels
