import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(10,100),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.putText(img,"Mercury",(120,180),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Venus",(200,170),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Earth",(290,170),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Mars",(390,170),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Jupiter",(500,70),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Saturn",(800,130),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Uranus",(975,130),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))
cv2.putText(img,"Neptune",(1120,140),cv2.FONT_HERSHEY_COMPLEX,0.3,(255,255,255))

cv2.imshow("Solar System Image",img)
cv2.imwrite("Solar_System_Image.jpg",img)
cv2.waitKey(0)