import pytest
import cv2
import numpy as np
from src.skeletonization import ZhangSuenSkeletonization
def test_skeletonization()
    # Create a test image
    image = np.zeros((100, 100), dtype=np.uint8)
    image[20:80, 20:80] = 255
    # Apply the Zhang-Suen skeletonization technique
    skeletonization = ZhangSuenSkeletonization()
    skeleton = skeletonization.skeletonize(image)
    # Check the output
    assert np.sum(skeleton) > 0