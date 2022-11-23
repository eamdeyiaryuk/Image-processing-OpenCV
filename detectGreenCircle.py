import cv2
import numpy

camera = cv2.VideoCapture(1)
camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.0)
camera.set(cv2.CAP_PROP_EXPOSURE,-9.0)

kernel = numpy.ones((2,2),numpy.uint8)

while True:
    check,frame = camera.read()
    blur_frame = cv2.blur(frame,(10,10))
   #hsv = cv2.cvtColor(blur_frame,cv2.COLOR_BGR2HSV)

    lower = numpy.array([0,30,10])       #green
    upper = numpy.array([20,180,80])     #green 

    #lower = numpy.array([36,147,97])       #green
    #upper = numpy.array([145,255,232])     #green 

    mask = cv2.inRange(blur_frame,lower,upper)
    mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=2) #OPEN Morphological
    
    circles = cv2.HoughCircles(mask,cv2.HOUGH_GRADIENT,1,70,param1=50,param2=10,minRadius=10,maxRadius=50)

    font = cv2.FONT_HERSHEY_SIMPLEX

    if circles is not None:
        circles = numpy.uint16(numpy.around(circles))
        for i in circles[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)  # draw the outer circle
           # cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)    # draw the center of the circle
            cv2.putText(frame, 'GREEN', (i[0], i[1]),font, 0.7, (48, 95, 44), 2, cv2.LINE_AA)
            print("yeah")

    cv2.imshow("camera",frame)
    cv2.imshow("mask",mask)  


    if cv2.waitKey(1) & 0xFF == ord("e"):
        break


cv2.destroyAllWindows()    
