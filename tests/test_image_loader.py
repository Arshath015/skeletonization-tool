import pytest
import cv2
from src.image_loader import ImageLoader
def test_image_loader()
    # Load a test image
    image_loader = ImageLoader()
    image = image_loader.load_image('test_image.png')
    # Check the output
    assert image is not None