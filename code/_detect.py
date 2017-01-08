#!/usr/bin/env python2

import os
import sys
import pickle

import numpy as np
np.set_printoptions(precision=2)
# from sklearn.cluster import DBSCAN

import cv2
import openface


imgDim=96

dlibFacePredictor='/root/openface/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
align = openface.AlignDlib(dlibFacePredictor)

def getReps(bgrImg):
	rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
	bb = align.getAllFaceBoundingBoxes(rgbImg)
	for box in bb:
		x1, y1, w1, h1 = box.left(), box.top(), box.right(), box.bottom()
		cv2.rectangle(bgrImg, (x1, y1), (w1, h1), (0, 321, 123), 3)
	return bgrImg


print("***Video Processing***")


idx = 0
cap = cv2.VideoCapture(sys.argv[1])
ret, frame = cap.read()

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame.shape[1], frame.shape[0]))

while True:
	ret, frame = cap.read()
	if ret is False:
		break
	
	idx += 1
	if idx%10 != 0:
		continue
	
	frame = getReps(frame)
	out.write(frame)
	
	# cv2.imshow('Video', frame)
	# if cv2.waitKey(100) & 0xFF == ord('q'):
		# break

# print(idx)

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

