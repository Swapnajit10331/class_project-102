import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        result=False
    return image_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadfiles(image_name):
    access_token="sl.BLd_CNySzlaXGz3h40eS7QTpak83vBnzHiQAAIX_aJ6kwiZ4NwcPUcrz-wtDfDHh1vgGmES66rJDdirQy7XuVxnGoqWnSNN-Q-vFSBD-CcO5NerWC3KS2Zytee3kQUXE2DCpNM"
    file=image_name
    filefrom=file
    fileto="/newfolder1/"+(image_name)
    dbx=dropbox.Dropbox(access_token)
    with open(filefrom,"rb")as f:
        dbx.filesupload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("fileuploaded")

def  main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            uploadfiles(name)

main()
            
