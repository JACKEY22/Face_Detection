import dlib 
import cv2 as cv 

def Get_My_Face
detector = dlib.get_frontal_face_detector()
cap = cv.VideoCapture(2)
count = 1
while 1:
    _, image = cap.read()
    if not _:
        break
    if detector(image):
        faces = detector(image)
        face = faces[0]
        face_ = image[face.top():face.bottom(), face.left():face.right()]
        cv.imwrite('./before_images/my_faces/' + str(count) + '.jpg', face_)

        
        cv.rectangle(image, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()),color=(255,255,255), thickness=2, lineType=cv.LINE_AA)
        cv.imshow('Croping...', image)
        cv.waitKey(30)
        count += 1
        if count == 238:
            break
    else:
        cv.imshow('Croping...', image)
        cv.waitKey(30)