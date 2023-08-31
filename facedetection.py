import cv2

face_cascade=cv2.CascadeClassifier(r'C:\Users\ramch\OneDrive\Desktop\finaljarvis\codsoft_tasks\haarcascade_frontalface_default.xml')
img=cv2.imread(r'C:\Users\ramch\OneDrive\Desktop\finaljarvis\codsoft_tasks\WIN_20230517_16_35_07_Pro.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4) 

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
cv2.imshow('img',img)
cv2.waitKey()