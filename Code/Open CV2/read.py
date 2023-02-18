import cv2 as cv
img=cv.imread('Photos/cat.jpg')               #cv.imread -> takes address of image 
cv.imshow('Cat',img)                          #cv.imshow -> need two arguments name of image and variable in which image is readed 
cv.waitKey(0)   


#Reading Videos:

capture=cv.VideoCapture('Videos/vid.mp4')       #VideoCapture(Address of video)
while True: 
    isTrue, frame=capture.read()                 #capture.read reads frame by frame, isTrue is boolean 
    cv.imshow('Video',frame)                      #to display each frame
    if cv.waitKey(20) & 0xFF==ord('d'):           #to stop infinite loop of video
        break
capture.release()                                #release capture                 
cv.destroyAllWindows()                           #close window

