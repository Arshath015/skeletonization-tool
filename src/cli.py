import argparse
from src.skeletonization import ZhangSuenSkeletonization
from src.image_loader import ImageLoader
class CLI:
    def __init__(self):
        pass
    def run(self):
        parser = argparse.ArgumentParser(description='Zhang-Suen Skeletonization CLI')
        parser.add_argument('input_image', help='Input image filename')
        parser.add_argument('output_image', help='Output image filename')
        args = parser.parse_args()
        image_loader = ImageLoader()
        skeletonization = ZhangSuenSkeletonization()
        image = image_loader.load_image(args.input_image)
        skeleton = skeletonization.skeletonize(image)
        cv2.imwrite(args.output_image, skeleton)