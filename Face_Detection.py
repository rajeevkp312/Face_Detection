import cv2
face_cap=cv2.CascadeClassifier("C:/Users/ASUS/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap=cv2.VideoCapture(0)   
while True:
    ret , video_data=video_cap.read()
    col=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100,100),
        flags=cv2.CASCADE_SCALE_IMAGE

    )
    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(255,0,100),2)
    cv2.imshow("FACE DETECTING",video_data )
    if cv2.waitKey(10)==ord("x"):
        break
video_cap.release()     