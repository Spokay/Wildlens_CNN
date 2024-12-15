from pathlib import PosixPath

from PIL import Image


def transform_image_type_to_jpg(images: list[PosixPath]) -> None:
    i = 0
    for image in images:
        img = Image.open(image)
        # The image object is used to save the image in jpg format
        img.save(str(i)+'.jpg')