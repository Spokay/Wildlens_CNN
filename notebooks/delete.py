import os
from random import shuffle

files = os.listdir("/home/shared/Dataset_wildlens/Animals/")

shuffle(files)

first_80 = files[:80]

for file in first_80 :
    os.remove(os.path.join("/home/shared/Dataset_wildlens/Animals/",file))
    