#!/usr/bin/env python2

import os
import sys
import pickle

import numpy as np
np.set_printoptions(precision=2)
from sklearn.cluster import DBSCAN

import cv2
import openface

dlibFacePredictor='/root/openface/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
networkModel='/root/openface/openface/models/openface/nn4.small2.v1.t7'

imgDim=96

align = openface.AlignDlib(dlibFacePredictor)
net = openface.TorchNeuralNet(networkModel, imgDim)

def getReps(bgrImg):
	try:
		rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
		bb = align.getAllFaceBoundingBoxes(rgbImg)
		alignedFaces = [align.align(imgDim, rgbImg, box, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE) for box in bb]
		reps = [net.forward(alignedFace) for alignedFace in alignedFaces]
		return reps
	except:
		return None

def getRep(bgrImg):
	try:
		rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
		bb = align.getLargestFaceBoundingBox(rgbImg)
		alignedFace = align.align(imgDim, rgbImg, bb, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)	
		rep = net.forward(alignedFace)
		return rep
	except:
		return None

print("***Video Processing***")

idx = 0
vectors = []
cap = cv2.VideoCapture(sys.argv[1])

while True:
	ret, frame = cap.read()
	if ret is False:
		break
	
	idx += 1
	if idx%20 != 0:
		continue	
	
	reps = getReps(frame)
	if reps is not None:
		if len(reps) > 0:
			print(len(reps))
			vectors.extend(reps)
	
	# cv2.imshow('', frame)
	# if cv2.waitKey(1) & 0xFF == ord('q'):
	# 	break

# print(idx)

fileDir = os.path.dirname(os.path.realpath(__file__))
pkFile = sys.argv[1].split('/')[-1] + '.pk'
pkFile = fileDir + '/{}'.format(pkFile)
pickle.dump(vectors, open(pkFile, 'w'))

