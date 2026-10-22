import os
import cv2
from PIL import Image

image_folder = "output"
video_name = 'LPFH_video.webm'

images = sorted([img for img in os.listdir(image_folder)])
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'VP80')

video = cv2.VideoWriter(video_name, fourcc, 24, (width,height))

for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)

cv2.destroyAllWindows()
video.release()