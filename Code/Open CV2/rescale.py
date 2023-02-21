import cv2 as cv

def rescaleframe(frame,scale=0.2):              #frame is the variable having function read
    width=int(frame.shape[1] * scale)           #setting the width of video
    height=int(frame.shape[0] * scale)          #setting the height of video
    dimension=(width,height)

    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)       #cv.resize(soure of image,(width,height),interpolation=INTER_AREA)



img=cv.imread('Photos/cat_large.jpg')
cv.imshow("Cat",img)
frame=rescaleframe(img)
cv.imshow("Resized Cat",frame)


#For videos:

capture=cv.VideoCapture('Videos/vid.mp4')       
while True: 
    isTrue, frame=capture.read()  
    frame_resized=rescaleframe(frame)                                   #created new frame
    cv.imshow('Video',frame)            
    cv.imshow('Resized',frame_resized)                                  #showing new resized video                
    if cv.waitKey(20) & 0xFF==ord('d'):           
        break
capture.release()                            
cv.destroyAllWindows()  

