import os
import shutil

# Loop through all the files in a folder
directory = '/home/shared/Mammiferes_raw'

if os.path.exists(directory):

    for dirpath, dirnames, filenames in os.walk(directory):
        for i, filename in enumerate(filenames):
            if(filename.endswith(('.jpg', '.jpeg', '.png', 'JPG', 'JPEG', 'PNG'))):
                dir_name = os.path.basename(dirpath)
                len_dir = len(str(len(os.listdir(dirpath))))
                new_name = f"{dir_name}_{str(i).zfill(len_dir)}.jpg"
                shutil.copy(os.path.join(dirpath, filename), os.path.join('/home/shared/Dataset_wildlens/Footprints', new_name))
else:
    print(f"Directory {directory} does not exist.")