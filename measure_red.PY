import cv2
import numpy as np

cap=cv2.VideoCapture(1)

l1=15

while 1:
    ret,frame=cap.read()
    new_frame=frame.copy()
    kernel=np.ones((5,5),np.uint8)
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower = np.array([160,100,20])
    upper = np.array([179,255,255])
    mask=cv2.inRange(hsv,lower,upper) 

    mask=~mask
       
    thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    
    contours, heirarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    with_contours = cv2.drawContours(frame, contours, -1,(255,0,255),3)
    
    
    
    c=[]
    area=int()
    
    for c in contours:
      x, y, w, h = cv2.boundingRect(c)
      area=cv2.contourArea(c)
    if (area) > 100:
      cv2.rectangle(with_contours,(x,y), (x+w,y+h), (0,0,0), 2)
      cv2.line(with_contours,(x,y), (x+w,y+h), (0,0,0), 1)
      cv2.line(with_contours,(x,y+h), (x+w,y), (0,0,0),1 )     
      
      
      b2r=y
      rx=l1/h
      b2=rx*w   
      

      
      cv2.putText(frame, "Width {} cm".format(round(b2, 1)), (int(x+100), int(y+20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2)     
    


    
 
 
 
    cv2.imshow('',frame)
    
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()    
