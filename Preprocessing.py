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

def image_to_array(after_image_dir):
    image_array_data=[]
    label=[]

    for dir in os.listdir(after_image_dir):
        for file in os.listdir(os.path.join(after_image_dir,dir)):
            image_path = os.path.join(after_image_dir, dir, file)
            image = cv.imread(image_path)
            image = np.array(image).astype('float32')
            image = image / 255
            image = image.reshape(-1)
            image_array_data.append(image)

            if dir == 'others':
                label.append(0)

            elif dir == 'mine':
                label.append(1)
            
            elif dir == 'mom':
                label.append(2)

    return image_array_data, label

def main():
    after_images_dir = os.path.join(os.getcwd(), 'after_images')
    if not os.path.exists(after_images_dir):
        os.mkdir(after_images_dir)

    preprocess_image('before_images','after_images')

main()