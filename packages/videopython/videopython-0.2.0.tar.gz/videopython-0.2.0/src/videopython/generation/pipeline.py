import cv2
import numpy as np
from PIL import Image

from videopython.base.transforms import Resize
from videopython.generation import ImageToVideo, TextToImage

N_ITERATIONS = 11
PRMOPT = "Sunset at the sea, cimenatic view"


def main():
    text_to_image = TextToImage()
    image_to_video = ImageToVideo()

    target_height = 576
    target_width = 1024

    base_image = text_to_image.generate_image(PRMOPT)
    image = cv2.resize(np.asarray(base_image), (target_width, target_height))

    video = image_to_video.generate_video(image)

    for i in range(N_ITERATIONS - 1):
        print(f"Generating {i+2}/{N_ITERATIONS}...")
        video += image_to_video.generate_video(Image.fromarray(video.frames[-1]))

    video.save()


if __name__ == "__main__":
    main()
