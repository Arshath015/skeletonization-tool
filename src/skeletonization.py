import cv2
import numpy as np
class ZhangSuenSkeletonization:
    def __init__(self):
        pass
    def skeletonize(self, image):
        # Apply thresholding to the input image
        _, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # Apply the Zhang-Suen skeletonization technique
        while True:
            # Mark the pixels to be removed
            marked = np.zeros_like(thresh)
            for i in range(1, thresh.shape[0] - 1):
                for j in range(1, thresh.shape[1] - 1):
                    if thresh[i, j] == 255:
                        # Check the 8-neighbors
                        neighbors = [thresh[i - 1, j], thresh[i + 1, j], thresh[i, j - 1], thresh[i, j + 1],
                                      thresh[i - 1, j - 1], thresh[i - 1, j + 1], thresh[i + 1, j - 1], thresh[i + 1, j + 1]]
                        # Count the number of 0-1 transitions in the 8-neighborhood
                        transitions = sum(1 for k in range(8) if neighbors[k] == 0 and neighbors[(k + 1) % 8] == 255)
                        # Check the conditions for removing the pixel
                        if (2 <= sum(neighbors) <= 6) and (transitions == 1):
                            # Check the conditions for the 2-4-5-6 pixels
                            if (i + j) % 2 == 0:
                                if (neighbors[0] * neighbors[2] * neighbors[4] == 0) or (neighbors[2] * neighbors[4] * neighbors[6] == 0):
                                    marked[i, j] = 255
                            else:
                                if (neighbors[0] * neighbors[2] * neighbors[6] == 0) or (neighbors[0] * neighbors[4] * neighbors[6] == 0):
                                    marked[i, j] = 255
            # Remove the marked pixels
            thresh[marked == 255] = 0
            # Check for convergence
            if np.sum(marked) == 0:
                break
        return thresh