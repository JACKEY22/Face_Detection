import dlib, os
import cv2 as cv 
 
def get_my_faces(others_count, before_mine_dir):
    detector = dlib.get_frontal_face_detector()
    cap = cv.VideoCapture(0)
    count = 1
    while 1:
        _, image = cap.read()
        if not _:
            break
        if detector(image):
            # detect faces
            faces = detector(image)
            face = faces[0]

            # get face image
            face_ = image[face.top():face.bottom(), face.left():face.right()]
            cv.imwrite(before_mine_dir + '/' + str(count) + '.jpg', face_) 

            # visualize
            cv.rectangle(image, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()),color=(255,255,255), thickness=2, lineType=cv.LINE_AA)
            cv.imshow('Croping...', image)
            cv.waitKey(30)
            count += 1

            # limit counts
            if count == others_count: 
                break
        else:
            cv.imshow('Croping...', image)
            cv.waitKey(30)

def main():
    before_images_dir = os.path.join(os.getcwd(), 'before_images')
    before_others_dir = os.path.join(before_images_dir, 'others')
    others_count = len(os.listdir(before_others_dir))

    before_mine_dir = os.path.join(before_images_dir, 'mom')  # change 'name' into your name!
    if not os.path.exists(before_mine_dir):
        os.mkdir(before_mine_dir)
    
    get_my_faces(others_count, before_mine_dir)
        
main()