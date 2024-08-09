import cv2
path = r"D:\memories\uttarakhand\VID20240607091852.mp4"
video = cv2.VideoCapture(path)

while (True):
    state , frame = video.read()
    if not state: break
    frame = cv2.resize(frame,(0,0), fx=.25 , fy=.25)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)

    # cv2.imshow('video',frame)
    # cv2.imshow('video b/w',gray)
    # cv2.imshow('video rgb',rgb)
    # cv2.imshow('video hsv',hsv)

    #stacking frames
    s1 = cv2.hconcat([frame , cv2.merge([gray,gray,gray])])
    s2 = cv2.hconcat([rgb , hsv])
    f = cv2.vconcat([s1,s2])
    
    h , w ,_ = f.shape

    #adding text
    f = cv2.putText(f,"Orignal",(25,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    f = cv2.putText(f,"Grayscale",(w//2 + 25,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    f = cv2.putText(f,"RGB",(25,h//2+50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    f = cv2.putText(f,"HSV",(w//2 +25,h//2+50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    
    cv2.imshow('frame',f)
    if cv2.waitKey(10) == ord ('q'):
        break