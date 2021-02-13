import cv2

video = cv2.VideoCapture('video/somi_lisa.mp4')

if(video.isOpened() == False):
    print('not load')


while (video.isOpened()):
    ret, frame = video.read()

    if ret == True:
        cv2.imshow('output', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break


video.release()
cv2.destroyAllWindows()