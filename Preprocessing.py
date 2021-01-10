import os, dlib
import cv2 as cv 
import numpy as np

# before_image_dir --> after_image_dir 
def preprocess_image(before_image_dir, after_image_dir): 
    detector = dlib.get_frontal_face_detector()
    image_width = 200 
    image_height = 200 
    for dir in os.listdir(before_image_dir):

        count = 1 
        for file in os.listdir(os.path.join(before_image_dir, dir)):
            
            image_path = os.path.join(before_image_dir, dir, file)
            image = cv.imread(image_path)
            image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            image = cv.resize(image, (image_width, image_height), cv.INTER_CUBIC)

            if detector(image):
                if not os.path.exists(os.path.join(after_image_dir, dir)):
                    os.mkdir(os.path.join(after_image_dir, dir))

                image_path_out = os.path.join(after_image_dir, dir) + '/' + str(count) + '.jpg'
                cv.imwrite(image_path_out, image)
                count += 1 

def flip_images(after_image_dir):
    for dir in os.listdir(after_image_dir):
        for file in os.listdir(os.path.join(after_image_dir, dir)):
            image_path =  os.path.join(after_image_dir, dir, file)
            image = cv.imread(image_path)
            image_flip = cv.flip(image, 1)
            cv.imwrite(os.path.join(after_image_dir, dir) + '/flip_' + file, image_flip)

def main():
    after_images_dir = os.path.join(os.getcwd(), 'after_images')
    if not os.path.exists(after_images_dir):
        os.mkdir(after_images_dir)


    preprocess_image('before_images','after_images')
    flip_images(after_images_dir)

main()