
import cv2
# cv2.namedWindow("ShowImage1",cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.namedWindow("ShowImage1",cv2.WINDOW_AUTOSIZE)
# cv2.resizeWindow("ShowImage1",1024,768)
cv2.moveWindow("ShowImage1",0,0)
image1=cv2.imread("H:\\\MikePorjects\\medias\\Test.jpg")
cv2.imshow("ShowImage1",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
