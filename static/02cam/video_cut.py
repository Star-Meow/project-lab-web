import cv2
videoFile = "cam02.mp4"
outputFile = 'cam02_'
vc = cv2.VideoCapture(videoFile)
c = 1
if vc.isOpened():
    rval, frame = vc.read()
else:
    print('openerror!')
    rval = False

timeF = 1  #視頻幀計數間隔次數
while rval:
    print(1)
    #print(c)
    rval, frame = vc.read()
    if c % timeF == 0:
        print(2)
        cv2.imwrite(outputFile + str(int(c / timeF)) + '.jpg', frame)
    c += 1
    cv2.waitKey(1)
vc.release()