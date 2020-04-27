from hyperlpr import *

import cv2
import time

image = cv2.imread("db3.jpg")
t1 = time.time()
print(HyperLPR_plate_recognition(image))
t2 = time.time() - t1
t = round(t2* 1000, 2)
print(f'spent {t} ms')

