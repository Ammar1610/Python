# to draw into the images 

import cv2 as cv 
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')          #np.zeros((height,width,shape),dtype)   here uint8 is for images
#cv.imshow("Blank",blank)                         #blank img will be obtained
#blank[:]=255,0,0                                  #whole blank img will be of specified colour
#blank[100:200]=255,0,0                             #range can be defiened for colour
#blank[100:200,400:500]=255,0,0
#cv.imshow("Blank",blank)

#to insert a rectangle with border into an image

#cv.rectangle(blank,(0,0),(400,250),(255,0,0),4)                                #cv.rectangle(img,point1,point2,colour,thickness of border)
#cv.rectangle(blank,(0,0),(400,250),(255,0,0),cv.FILLED)                        #cv.filled will fill color into the inserted box 
#cv.rectangle(blank,(0,0),(400,250),(255,0,0),-1)                               #thickness = -1, works same as cv.filled  
#cv.rectangle(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,0,0),-1)    #instead of co-ordinate of points we can give it as a refernce to parent img where      
#cv.imshow("rectangle in a img",blank)                                           #in shape 0=x,1=y whole divide by 2 means half of parent image

# to insert a circle

# cv.circle(blank,(blank.shape[0]//2,blank.shape[1]//2),40,(255,0,0),thickness=-1)        #cv.circle(img,centre point,radius,colour,thickness)
# cv.imshow("Circle",blank)


# to insert a line
# cv.line(blank,(0,0),(blank.shape[0]//2,blank.shape[1]//2),(255,0,0),thickness=1)           #cv.line(img,point1,point2,colour,thickness)
# cv.imshow("Line",blank) 


#to insert text

cv.putText(blank,"Text",(100,0),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)              #cv.putText(img,text,point,font,scaling,colour,thickness)
cv.imshow("Text",blank)
cv.waitKey(0)