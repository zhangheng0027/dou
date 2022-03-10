# import cv2
import cv2

cap = cv2.VideoCapture('E:\\test\\1.mp4')


if cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        exit

    f1 = cv2.cvtColor(frame[135:135+24, 21:21+28], cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(f1, 185, 255, cv2.THRESH_BINARY)

    cv2.imshow("image", binary)

    # #
    p2 = frame[139:139 + 21, 687:687 + 21]
    f2 = cv2.cvtColor(p2, cv2.COLOR_RGB2GRAY)
    ret, binary = cv2.threshold(f2, 160, 255, cv2.THRESH_BINARY)
    cv2.imshow("image1", binary)
    cv2.waitKey(0)
    #
    # cv2.imwrite("E:/test/picture/p1_2.jpg", img_gray)
    #
    # # cv2.imshow("img_gray", img_gray)
    # print("success")
else:
    print("读取失败")
