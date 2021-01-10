import dlib, os, pickle, joblib
import cv2 as cv 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

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

def train_model(version):
    
    # split dataset
    x, y = image_to_array('./after_images')
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # train model
    model = LogisticRegression(
        max_iter=3000,
        solver='saga',
        random_state=True,
        multi_class='multinomial'
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    # save model
    joblib.dump(model, f'./model/model_{version}.pkl') 

def main():
    version = 2
    train_model(version)

main()