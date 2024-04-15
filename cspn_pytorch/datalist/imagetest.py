import cv2
import os

# image=open('/home/ewing/dataset/kitti_test/data/2011_10_03_drive_0027_sync/image_02/groundtruth/0000000005.png','r')
# image=cv2.imread('/home/ewing/dataset/kitti_test/data/2011_10_03_drive_0027_sync/image_02/groundtruth/0000000005.png')
# print(image.shape)
# cv2.imshow('img',image)
# cv2.waitKey()

from PIL import Image
import numpy as np

# 加载图像
image = Image.open("/home/ewing/dataset/kitti_test/data/2011_10_03_drive_0027_sync/image_02/groundtruth/0000000005.png")

# 输出图像的模式（如 "RGB" 表示红绿蓝三通道，"L" 表示灰度图）
print("Image Mode:", image.mode)

# 转换图像为NumPy数组
image_data = np.array(image)

# 输出数组的数据类型，这表明了每个像素值的存储方式
print("Data Type of Image Array:", image_data.dtype)

# 输出像素值的范围
print("Min Pixel Value:", np.min(image_data))
print("Max Pixel Value:", np.max(image_data))
