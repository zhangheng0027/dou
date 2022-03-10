import cv2

cap = cv2.VideoCapture('E:\\test\\1.mp4')

if cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        exit
    p1 = frame[144:144+21, 27:27 + 21]
    cv2.imwrite("E:/test/picture/p1.jpg", p1)

    p2 = frame[139:139 + 21, 687:687 + 21]
    cv2.imwrite("E:/test/picture/p2.jpg", p2)

    img_gray = cv2.cvtColor(p2, cv2.COLOR_RGB2GRAY)

    cv2.imwrite("E:/test/picture/p1_2.jpg", img_gray)

    # cv2.imshow("img_gray", img_gray)
    print("success")
else:
    print("读取失败")
