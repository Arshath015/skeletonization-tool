import cv2
class ImageLoader:
    def __init__(self):
        pass
    def load_image(self, filename):
        return cv2.imread(filename, cv2.IMREAD_GRAYSCALE)