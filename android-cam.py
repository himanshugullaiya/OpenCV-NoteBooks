import requests
import cv2
from sys import exit
from matplotlib import pyplot as plt
import numpy as np

url = "http://192.168.0.88:8080/shot.jpg"

cap = cv2.VideoCapture(0);e
while True:
     img_resp = requests.get(url)
     img_arr = np.array(bytearray(img_resp.content), dtype= np.uint8)
     img = cv2.imdecode(img_arr, -1)

     # ............change color to grey.................
     # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     # cv2.imshow("Android Cam", gray)

     cv2.imshow("Android Cam", img)
     if cv2.waitKey(1) == ord('q'):
         cv2.destroyAllWindows()
         exit(0)


