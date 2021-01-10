import dlib, os, pickle, joblib
import cv2 as cv 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from Preprocessing import image_to_array

def train_model():
    
    # split dataset
    x, y = image_to_array('./after_images')
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # train model
    model = LogisticRegression(
        max_iter=2000,
        solver='saga',
        random_state=True,
        multi_class='multinomial'
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)

    # save model
    joblib.dump(model, 'model1.pkl') 

def Recognize_faces():
    # load model
    model = joblib.load('model1.pkl')

    # compare faces
    detector = dlib.get_frontal_face_detector()
    cap = cv.VideoCapture(0)
    while 1:
        _, image = cap.read()
        if not _:
            break
        if detector(image):
            faces = detector(image)
            face = faces[0]

            face_ = image[face.top():face.bottom(), face.left():face.right()]
            face_ = cv.resize(face_,(200,200))
            face_ = np.array(face_).astype('float32')
            face_ = face_ / 255
            face_ = face_.reshape(-1)
            
            if model.predict([face_]) == [0]:
                cv.rectangle(image, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()),color=(255,255,255), thickness=2, lineType=cv.LINE_AA)
                cv.putText(image, "others",(face.left(),face.top()),  cv.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 3)

            elif model.predict([face_]) == [1]:
                cv.rectangle(image, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()),color=(255,255,255), thickness=2, lineType=cv.LINE_AA)
                cv.putText(image, "mine",(face.left(),face.top()),  cv.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 3)

            elif model.predict([face_]) == [2]:
                cv.rectangle(image, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()),color=(255,255,255), thickness=2, lineType=cv.LINE_AA)
                cv.putText(image, "mom",(face.left(),face.top()),  cv.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 3)

            cv.imshow('detecting...', image)
            cv.waitKey(10)
        else:
            cv.imshow('detecting...', image)
            cv.waitKey(10)
    cap.release()
    
# train_model()
Recognize_faces()