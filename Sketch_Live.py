import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)

cv.namedWindow('sketch')

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)


    image=cv.GaussianBlur(gray,(7,7),0)

    image=cv.Canny(image,20,60)
    ret,image=cv.threshold(image,238,255,cv.ADAPTIVE_THRESH_MEAN_C)

    cv.imshow("original",frame)
    cv.imshow("sketch",image)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()