import cv2

def ClickPic():
    picObject = cv2.VideoCapture(0)
    webcam = True
    while(webcam):
        ret,frame = picObject.read()
        cv2.imwrite("NewPicture.png",frame)
        webcam = False
        print("Picture Clicked")
    picObject.release()
    cv2.destroyAllWindows()
    
ClickPic()
