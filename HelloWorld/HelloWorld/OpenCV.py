
import cv2
import sqlite3
casc_path="D:\\Tools\\PYTHON\\OpenCV\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml"
facesCascade = cv2.CascadeClassifier(casc_path)
image1=cv2.imread("H:\\MikePorjects\\medias\\Test.jpg")
image1_height=image1.shape[0]
image1_width=image1.shape[1]
print("Src h = %d w = %d" % (image1_height,image1_width))
window_height = image1_height // 8
window_width = image1_width // 8
print("Dst h = %d w = %d" % (window_height,window_width))
image2 = cv2.resize(image1,(window_width,window_height), 0, 0, cv2.INTER_AREA);
# image2 = cv2.resize(image1,(0,0),0.5,0.5,cv2.INTER_AREA);
# window_height = image2.shape[0]
# window_width = image2.shape[1]
# print(window_height,window_width)
faces = facesCascade.detectMultiScale(image2,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
cv2.rectangle(image2,(10,window_height - 20),(110,window_height),(0,0,0),-1)
cv2.putText(image2,"Find " + str(len(faces)) + " face!",(10,window_height - 5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
count = 0
for (x,y,w,h) in faces:
    count +=1
#    cv2.namedWindow("ShowFace")
#    cv2.resizeWindow("ShowFace",200,200)
    filename = "H:\\MikePorjects\\medias\\face" + str(count) + ".jpg"
    imagetemp = image2[y:y+h,x:x+w]
    imageface = cv2.resize(imagetemp,(200,200),0,0,cv2.INTER_CUBIC);
#    cv2.imshow("ShowFace",imageface)
    cv2.imwrite(filename,imageface,[int(cv2.IMWRITE_JPEG_QUALITY),100])
    cv2.rectangle(image2,(x,y),(x+w,y+h),(128,255,0),2)    
cv2.namedWindow("ShowImage2",cv2.WINDOW_NORMAL)
cv2.resizeWindow("ShowImage2",(window_width,window_height))
cv2.moveWindow("ShowImage2",0,0)
cv2.imshow("ShowImage2",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
