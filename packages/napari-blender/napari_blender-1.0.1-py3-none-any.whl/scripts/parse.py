import numpy as np
import trimesh
from skimage import measure
from skimage.filters import threshold_otsu
import cv2 as cv

import scripts.interface as s
from scripts.trackmate import trackmate_peak_import
import os

import numpy as np

def clean_data(data, frame=None):
    """
    Cleans and preprocesses image data.

    This function accepts image data as a NumPy array and performs preprocessing steps such as
    selecting a specific frame, converting to grayscale, and scaling pixel values.

    
    Parameters
    ----------
    data : numpy.ndarray
        The input image data as a NumPy array.
    frame : int, optional
        The frame index to select from the image data.
    
    Returns
    -------
    numpy.ndarray
        Preprocessed image data.
    """
    if frame is not None:
        try:
            if data.ndim == 3:
                # If data has 3 dimensions, return as is
                result = data
            elif data.ndim == 4:
                # If data has 4 dimensions, select specific frame
                result = data[frame, :, :, :]
            elif data.ndim == 5:
                # If data has 5 dimensions, convert to grayscale
                result = np.dot(data[frame,:,:,:,:3], [0.299, 0.587, 0.114])
            else:
                raise ValueError("Data array must have either 3, 4 or 5 dimensions")
            
            # Check if result data type is uint8
            if result.dtype != np.uint8:
                # Scale pixel values to uint8 range [0, 255]
                min_val = np.min(result)
                max_val = np.max(result)
                scaled_image = ((result - min_val) * 255 / (max_val - min_val)).astype(np.uint8)
                return scaled_image
            return data  # Return preprocessed data
        except IndexError:
            print(f'Could not read data, image stack does not contain index {frame}')
    
    return data  # Return original data if no frame specified

def read_trackmate():
    """
    Reads track data from a TrackMate XML file.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the track data.
    """
    # Import track data using a custom function (trackmate_peak_import)
    # code gathered (but bugfixed) from https://github.com/hadim/pytrackmate
    df = trackmate_peak_import(s.TRACK, True)
    
    return df


def extract_mesh(data):
    """
    Extracts mesh data from a segmented .tif file.

    Parameters
    ----------
    path : str
        Path to the segmented .tif file.
    
    Returns
    -------
    tuple
        Tuple containing vertices and faces of the extracted mesh.S
    """
    # Marching cubes algorithm to extract surfaces
    verts, faces, _, _ = measure.marching_cubes(data)
    return verts, faces


def refine_mesh(verts, faces):
    """
    Refines the mesh by applying Laplacian smoothing.

    Parameters
    ----------
    verts : numpy.ndarray
        Vertices of the mesh.
    faces : numpy.ndarray
        Faces of the mesh.
    
    Returns
    -------
    trimesh.Trimesh
        The smoothed mesh.
    """
    # Convert to trimesh object
    mesh = trimesh.Trimesh(vertices=verts, faces=faces)
    
    # Apply Laplacian smoothing
    smooth_mesh = trimesh.smoothing.filter_laplacian(mesh, iterations=5)

    return smooth_mesh


def export_to_obj(vertices, faces, group, vert_count, fname):
    """
    Exports mesh data to an OBJ file.

    Parameters
    ----------
    vertices : numpy.ndarray
        Vertices of the submesh.
    faces : numpy.ndarray
        Faces of the submesh.
    group : int
        Group number for the submesh that we want to create now.
    vert_count : int
        Vertex count for the entire object until now.
    fname : str
        Name of the OBJ file to export.
    """
    if not os.path.exists(os.path.dirname(fname)):
        os.makedirs(os.path.dirname(fname))
        
    with open(fname, 'w' if not os.path.exists(fname) else 'a') as f:
        # Write group statement
        f.write(f"g {group}\n")

        # Write vertices
        for vertex in vertices:
            f.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")

        # Write faces
        for face in faces:
            f.write(f"f {' '.join([str(i + vert_count + 1) for i in face])}\n")

def create_obj(data, fname):
    """
    Single method to complete reading a prediction from labeled data
    and to export it to a 3D object

    Parameters
    ----------
    data : numpy.ndarray
        Labeled data from .tif file.
    fname : str
        Filename to export 3D object to.
    """
    vals = np.unique(data)[1:]  # Exclude 0 from unique values
    vert_count = 0

    for i, val in enumerate(vals):
        last_filter = (data == val).astype(int)
        filt = data * last_filter
        verts, faces = extract_mesh(filt)
        mesh =  refine_mesh(verts,faces)
    
        export_to_obj(mesh.vertices, mesh.faces, i+1, vert_count, fname)
        vert_count += len(verts)
  

def downscale_image_by_sampling(image, factor):
    """
    Downscales the input image by sampling every nth pixel in each dimension.

    Parameters
    ----------
    image : numpy.ndarray
        Input image as a NumPy array.
    factor : int
        Factor by which to downscale (e.g., 2 for half, 4 for quarter).
    
    Returns
    -------
    numpy.ndarray
        Downscaled image as a NumPy array.
    """
    if image.ndim == 4:  # Multichannel image (e.g., RGB)
        return image[:, ::factor, ::factor, :]
    else:  # Grayscale image
        return image[:, ::factor, ::factor]

# def create_volume(data):
    # import open3d as o3d
    # pcd = o3d.geometry.PointCloud()
    # pcd.points = o3d.utility.Vector3dVector(data.astype(np.float64))
    # o3d.io.write_point_cloud("sync.ply", pcd)
    # # vertices = data
    # # print(data.shape)
    # # vertices = np.array([tuple(e) for e in vertices], dtype=[('x', '<f4'), ('y', '<f4'), ('z', '<f4')])
    # # el = PlyElement.describe(vertices, 'vertex',{'some_property': 'f8'},{'some_property': 'u4'})
    # # # text = True: save in ascii format
    # # PlyData([el], text=True).write("test.ply") 

def create_contour(data, thresh):
    """
    Method to get the contours of a single slice (2D numpy array) of data.

    Parameters
    ----------
    data : numpy.ndarray
        Numpy array representation of a single z slice of data.
    thresh : int
        Threshold with which to threshold this slice.

    Returns
    -------
    numpy.ndarray
        Binary Numpy array containing the location of the contours (edges of nuclei).
    """
    # Threshold the data and make it binary
    _, thresh = cv.threshold(data, thresh, 255, 0)
    # Find contours (corresponds with nuclei) on this binary data, cv.RETR_EXTERNAL
    # is used to return the non-overlapping items per slice.
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    contour_image = np.zeros_like(data)

    # Sanitize slices by only allowing contours that are >= 15 pixels in area. This may lose
    # a very small edge of the nucleus but this is counteracted by how the 3D object is created,
    # namely using marching cubes.
    for contour in contours:
        area = cv.contourArea(contour)
        if area >= 15:
            cv.drawContours(contour_image, [contour], -1, (255), 1)
    return contour_image

def create_contour_data(data):
    """
    Method to yield the numpy array representation of only the contours found
    in the convoluted original data.

    Parameters
    ----------
    data : numpy.ndarray
        Numpy array representation of the convoluted original data.
    
    Returns
    -------
    numpy.ndarray
        Cleaned numpy array data containing the rough contours of nuclei.
    """
    # # Sanitize data without changing topology by erosion and dilation, this step
    # # elimates the heavy amount of background noise
    # eroded = ndi.grey_erosion(data, size=(3,3,3))
    # dilated = ndi.grey_dilation(eroded, size=(3,3,3))

    # Threshold image using industry standard (Otsu thresholding), with threshold
    # taken from the middle z slice. This is done since the middle z-slice will
    # contain part of the organoid, where the 1st slice will be only noise
    middle_slice = int(data.shape[2]/2)
    otsu = threshold_otsu(data[:,:,middle_slice])
    binary = data > otsu

    # opened = ndi.binary_opening(binary)

    data = data * binary

    # Take the gradient of this image and expand it to a numpy containing the gradient
    # of each pixel in each direction. A nucleus is a connected object so all of the x,y,z
    # frames will have a heavy gradient.
    gradient = np.gradient(data)
    magnitudes = (np.sqrt(sum(np.square(g) for g in gradient))).astype(np.uint8)

    # Stack contours for each z slice and export to object.
    contours = np.zeros(magnitudes.shape)
    for z in range(magnitudes.shape[2]):
        contours[:,:,z] = create_contour(magnitudes[:,:,z], otsu)

    return contours

def create_contour_obj(data, fname):
    """"
    Function to completely create a 3D contour object from data.

    Parameters
    ----------
    data : numpy.ndarray
        Numpy array representation of the convoluted original data.
    fname : str
        Filename to export 3D object to.
    """
    contours = create_contour_data(data)
    create_obj(contours, fname)
