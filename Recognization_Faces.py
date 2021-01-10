import dlib, os, pickle, joblib
import cv2 as cv 
import numpy as np

def recognize_faces(version):
    # load model
    model = joblib.load(f'./model/model_{version}.pkl')

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

def main():
    version = 2 
    recognize_faces(version)

main()