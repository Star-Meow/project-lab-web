import cv2

videoFile = "cam01.mp4"
outputFile = 'cam01_'
vc = cv2.VideoCapture(videoFile)
c = 1
start_frame = 19  # 从第28帧开始保存图片
if vc.isOpened():
    rval, frame = vc.read()
else:
    print('openerror!')
    rval = False

timeF = 1  # 视频帧计数间隔次数
while rval:
    rval, frame = vc.read()
    if c >= start_frame:
        img_number = c - start_frame + 1
        cv2.imwrite(outputFile + "{:02d}.jpg".format(img_number), frame)
    c += 1
    cv2.waitKey(1)
vc.release()
