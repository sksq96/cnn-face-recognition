# -*- coding: utf-8 -*-
# @Author: shubham
# @Date:   2016-08-27 19:42:11
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2017-03-31 05:52:50

import cv2
import sys
import os
from time import sleep

STEP = 20
directory = '/home/shubham/Documents/MTProject/OpenFace/data/{}/raw/{}'.format(int(time.time()) sys.argv[1].capitalize())
if not os.path.exists(directory):
	os.makedirs(directory)

video_capture = cv2.VideoCapture(0)
for i in range(400):
	ret, frame = video_capture.read()
	cv2.imshow('Video', frame)
	if i%STEP == 0:
		print("DEBUG[+]: Training: {}".format(i//STEP))
		cv2.imwrite('{}/{}_{}.jpg'.format(directory, sys.argv[1].capitalize(), i), frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

