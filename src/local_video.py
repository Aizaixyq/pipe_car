import cv2


print("视频检测开始")
url = 'http://192.168.3.18:8081/'

# 读取视频流
cap = cv2.VideoCapture(url)

while cap.isOpened():
    ret_flag, img_camera = cap.read()
    
    image = img_camera
    # 2.图像灰度化
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_copy = image.copy()

    # 3.对比度增强
    cache = cv2.createCLAHE(3, (8, 8))
    dst = cache.apply(gray)

    # 4.高斯平滑(降噪)
    gauss = cv2.GaussianBlur(image, (3, 3), 0)

    # 5.Canny算子边缘检测
    canny = cv2.Canny(gauss, 75, 255)

    # 6.形态学操作，连接相同裂纹
    # kener核
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 膨胀图像
    dilated = cv2.dilate(canny, kernel, iterations=1)
    # 腐蚀图像
    erode = cv2.erode(canny, kernel, iterations=1)
    # 闭运算
    closed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    # 7.寻找最大连通域
    # 寻找图像的轮廓
    contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # 圈出图像轮廓
    cv2.drawContours(closed, contours, -1, (0, 255, 255), 1)
    cv2.drawContours(image, contours, -1, (0, 0, 255), 3)

    cv2.imshow("camera", img_camera)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    
# 释放所有摄像头
cap.release()

# 删除窗口
cv2.destroyAllWindows()
