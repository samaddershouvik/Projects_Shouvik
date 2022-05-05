import cv2

#loading the face cascade classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#capturing video, 0 for using the webcam
cap = cv2.VideoCapture(0)

while True:
    #cap.read( will return two variable first is flag other is frame of the video
    _, img =cap.read()

    #converting each frame to grey scale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detecting faces
    faces = face_cascade.detectMultiScale(grey, 1.1, 4)
    i=0
    #making a rectangle and the counter for each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255),2)
        i+=1
        cv2.putText(img,'Face: '+str(i),(x,y-12),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    #displaying the frames with the boxes
    cv2.imshow('img',img)

    #exit key for display(ESC)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

#End frame capturing
cap.release()