# import cv2
import time
import cv2

from ai.ocr import orcCount


def getP1Card(frame1):

    frame1 = frame1[142:156, 26:44]
    cvt = cv2.cvtColor(frame1, cv2.COLOR_RGB2GRAY)
    a, thr = cv2.threshold(cvt, 170, 255, cv2.THRESH_BINARY)
    cv2.imshow("image", thr)
    cv2.waitKey(0)
    pass



if __name__ == '__main__':
    frame = cv2.imread("picture/frame_43.0.jpg")
    getP1Card(frame)







# cap = cv2.VideoCapture('E:\\test\\1.mp4')



#
# if cap.isOpened():
#     count = 1
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         count += 1
#
#         if count % 32 != 0:
#             continue
#
#         cv2.imwrite("E:/test/picture/frame_" + str(count / 32) + ".jpg", frame)
#         # cv2.imshow("image", frame)
#         # cv2.waitKey(0)
#
#         # f1 = cv2.cvtColor(frame[135:135+24, 21:21+28], cv2.COLOR_RGB2GRAY)
#         # ret, binary = cv2.threshold(f1, 187, 255, cv2.THRESH_BINARY)
#         #
#         # cv2.imshow("image", binary)
#         #
#         # # #
#         # p2 = frame[139:139 + 21, 687:687 + 21]
#         # f2 = cv2.cvtColor(p2, cv2.COLOR_RGB2GRAY)
#         # ret1, binary1 = cv2.threshold(f2, 160, 255, cv2.THRESH_BINARY)
#         # cv2.imshow("image1", binary1)
#
#         # cv2.waitKey(0)
#         #
#         # cv2.imwrite("E:/test/picture/frame.jpg", frame)
#         #
#         # # cv2.imshow("img_gray", img_gray)
#         # print("success")
# else:
#     print("读取失败")