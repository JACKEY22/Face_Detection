import os, dlib
import cv2 as cv 
import numpy as np


def preprocess_image(before_image_dir, after_image_dir):
    image_width = 200 
    image_height = 200 
    for dir in os.listdir(before_image_dir):
        count = 1 
        for file in os.listdir(os.path.join(before_image_dir, dir)):
            if file:
                image_path = os.path.join(before_image_dir, dir, file)
                image = cv.imread(image_path)
                image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
                image = cv.resize(image, (image_width, image_height), cv.INTER_CUBIC)
                image_path_out = os.path.join(after_image_dir, dir) + '/' + str(count) + '.jpg'
                cv.imwrite(image_path_out, image)
                count += 1 

def image_to_array(image_dir):
    image_array_data=[]
    label=[]

    for dir in os.listdir(image_dir):
        for file in os.listdir(os.path.join(image_dir,dir)):
            image_path = os.path.join(image_dir, dir, file)
            image = cv.imread(image_path)
            image = np.array(image).astype('float32')
            image = image / 255
            image = image.reshape(-1)
            image_array_data.append(image)
            if dir == 'faces':
                label.append(0)
            else:
                label.append(1)

    return image_array_data, label


# preprocess_image('./before_images', './after_images')



