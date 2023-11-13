import cv2
import numpy as np


def load_and_preprocess_image(image_path: str, resize_dim: tuple = (256, 256)) -> np.ndarray:
    """
    Load and preprocess the image.

    Parameters:
    - image_path (str): Path to the input image file.
    - resize_dim (tuple): Desired dimensions for resizing the image. Default is (256, 256).

    Returns:
    - preprocessed_image (numpy.ndarray): Preprocessed image as a NumPy array.
    """
    # Load image using OpenCV
    image = cv2.imread(image_path)

    # Resize the image to a standard dimension
    image = cv2.resize(image, resize_dim)

    return image

def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Normalize pixel values of the image to be in the range [0, 1].

    Parameters:
    - image (numpy.ndarray): Input image as a NumPy array.

    Returns:
    - normalized_image (numpy.ndarray): Normalized image.
    """
    # Normalize pixel values to be between 0 and 1
    normalized_image = image.astype(np.float32) / 255.0

    return normalized_image

def apply_median_blur(image: np.ndarray, kernel_size: int = 5) -> np.ndarray:
    """
    Apply median blur to the image to reduce noise.

    Parameters:
    - image (numpy.ndarray): Input image as a NumPy array.
    - kernel_size (int): Size of the median filter kernel. Default is 5.

    Returns:
    - blurred_image (numpy.ndarray): Image after applying median blur.
    """
    # Apply median blur to reduce noise
    blurred_image = cv2.medianBlur(image, kernel_size)

    return blurred_image

def apply_histogram_equalization(image: np.ndarray) -> np.ndarray:
    """
    Apply histogram equalization to improve contrast.

    Parameters:
    - image (numpy.ndarray): Input image as a NumPy array.

    Returns:
    - equalized_image (numpy.ndarray): Image after applying histogram equalization.
    """
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization to improve contrast
    equalized_image = cv2.equalizeHist(gray_image)

    return equalized_image

def preprocess_image(image_path: str) -> np.ndarray:
    """
    Load, preprocess, and enhance the input image using a series of preprocessing steps.

    Parameters:
    - image_path (str): Path to the input image file.

    Returns:
    - preprocessed_image (numpy.ndarray): Preprocessed image as a NumPy array.
    """
    # Load and preprocess the image
    image = load_and_preprocess_image(image_path)

    # Normalize pixel values
    normalized_image = normalize_image(image)

    # Apply median blur to reduce noise
    blurred_image = apply_median_blur(normalized_image)

    # Apply histogram equalization to improve contrast
    equalized_image = apply_histogram_equalization(blurred_image)

    return equalized_image
