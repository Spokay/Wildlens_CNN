import os
import argparse
from typing import Tuple
from PIL import Image

  
images_extension = [".png", ".jpeg", ".jpg", ".gif", ".bmp", ".tiff"]

def resize_img(folder_path: str, newsize: Tuple[int, int], destination_folder_path: str):

    if not os.path.exists(destination_folder_path):
        os.makedirs(destination_folder_path)

    for root, _, files in os.walk(folder_path):
		
        for file in files:
			
            lower_ext = os.path.splitext(file)[1].lower()
			
            if lower_ext in images_extension:
		
                image = Image.open(os.path.join(root, file))
					
                subfolder = os.path.basename(root)
                filename = os.path.splitext(file)[0]

                image = image.resize(newsize)

                if not os.path.exists(os.path.join(destination_folder_path, subfolder)):
                    os.makedirs(os.path.join(destination_folder_path, subfolder))

                image.save(os.path.join(destination_folder_path, subfolder, filename) + ".jpg")



parser = argparse.ArgumentParser(description="Delete all non-jpg files in a folder and save them as jpg")


parser.add_argument("-f", "--folder_path", type=str, help="Path to the folder containing the files")
parser.add_argument("-w", "--resize_image_width", type=int, help="Resized image desired width")
parser.add_argument("-ht", "--resize_image_height", type=int, help="Resized image desired height")
parser.add_argument("-d", "--destination_folder_path", type=str, help="Path to the folder that will contain the files")

args = parser.parse_args()


if __name__ == "__main__":

    print("Deleting all non-jpg files in the folder and saving them as jpg")

    resize_img(args.folder_path, (args.resize_image_width, args.resize_image_height), args.destination_folder_path)
