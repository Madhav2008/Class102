import cv2
import dropbox
import random
import time

startTime = time.time()

def Picture():
    number = random.randint(0,100)
    PicObject = cv2.VideoCapture(0)
    webcam = True
    while(webcam):
        ret,frame = PicObject.read()
        imageName = "NewPicture" + str(number) + ".png"
        cv2.imwrite(imageName, frame)
        webcam = False
    return imageName
    print("Picture Captured")
    PicObject.release()
    cv2.destroyAllWindows()

def UploadFiles(imageName):
    accessToken = "wHnbGJiEPrkAAAAAAAAAAR-eTtU50J-lf_ST7-ZLTRx1wqGQUO8fOjY6diVAnSrQ"
    source = imageName
    destination = "/Class102/" + imageName
    dbx = dropbox.Dropbox(accessToken)
    file = open(source,"rb")
    dbx.files_upload(file.read(),destination, mode = dropbox.files.WriteMode.overwrite)
    print("File Has Been Uploaded")

def main():
    while(True):
        if((time.time()- startTime )>= 5):
            name = Picture()
            UploadFiles(name)

main()
