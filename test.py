# -*- coding: utf-8 -*-
import os

file_dir = r"C:\Users\Mr.Wrong\Documents\GitHub\saliency-from-backproj\test_images"
L = []

for root, dirs, files in os.walk(file_dir):
    for file in files:
        if os.path.splitext(file)[1] == '.jpg':
            print(root)
            print(file)
            print(os.path.join(root, file))
