from src.skeletonization import ZhangSuenSkeletonization
from src.image_loader import ImageLoader
# Load the input image
image_loader = ImageLoader()
image = image_loader.load_image('input_image.png')
# Apply the Zhang-Suen skeletonization technique
skeletonization = ZhangSuenSkeletonization()
skeleton = skeletonization.skeletonize(image)
# Save the output image
cv2.imwrite('output_image.png', skeleton)