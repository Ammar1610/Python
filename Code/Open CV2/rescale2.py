# This method is only for live feed like camera not for saved files
import cv2 as cv
 
capture=cv.VideoCapture('Videos/vid.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow("video",frame)
    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows()    
        
def changeRes(width,height):
    capture.set(3,height)
    capture.set(4,height) 