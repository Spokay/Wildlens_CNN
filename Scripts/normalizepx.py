import os
import argparse
from typing import Tuple
import cv2

  
images_extension = [".png", ".jpeg", ".jpg", ".gif", ".bmp", ".tiff"]

def normalize_pixels(folder_path: str, destination_folder_path: str, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):

    if not os.path.exists(destination_folder_path):
        os.makedirs(destination_folder_path)

    for root, _, files in os.walk(folder_path):
		
        for file in files:
			
            lower_ext = os.path.splitext(file)[1].lower()
			
            if lower_ext in images_extension:
		
                image = cv2.imread(os.path.join(root, file))
                image = image/255.0
                image[..., 0] -= mean[0]
                image[..., 1] -= mean[1]
                image[..., 2] -= mean[2]

                image[..., 0] /= std[0]
                image[..., 1] /= std[1]
                image[..., 2] /= std[2] 
					
                subfolder = os.path.basename(root)
                filename = os.path.splitext(file)[0]

                if not os.path.exists(os.path.join(destination_folder_path, subfolder)):
                    os.makedirs(os.path.join(destination_folder_path, subfolder))

                cv2.imwrite(os.path.join(destination_folder_path, subfolder, filename) + ".jpg", image)



parser = argparse.ArgumentParser(description="Delete all non-jpg files in a folder and save them as jpg")


parser.add_argument("-f", "--folder_path", type=str, help="Path to the folder containing the files")
parser.add_argument("-d", "--destination_folder_path", type=str, help="Path to the folder that will contain the files")

args = parser.parse_args()


if __name__ == "__main__":

    print("Normalizing all images")

    normalize_pixels(args.folder_path, args.destination_folder_path)