#!/usr/bin/env python2

import cv2
import numpy as np

import dlib

import openface
from model import align, net


imgDim=96
def encode(bgrImg):
	try:
		rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
		bb = align.getAllFaceBoundingBoxes(rgbImg)
		alignedFaces = [align.align(imgDim, rgbImg, box, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE) for box in bb]
		encoding = [net.forward(alignedFace) for alignedFace in alignedFaces]
		return encoding
	except:
		return list()


face_detector = dlib.get_frontal_face_detector()
def ddetect(bgrImg):
	rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
	grayImg = cv2.cvtColor(rgbImg, cv2.COLOR_BGR2GRAY)
	bb = face_detector(rgbImg, 1)
	for box in bb:
		x1, y1, w1, h1 = box.left(), box.top(), box.right(), box.bottom()
		cv2.rectangle(bgrImg, (x1, y1), (w1, h1), (0, 321, 123), 3)
	return bgrImg

def detect(bgrImg):
	rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
	bb = align.getAllFaceBoundingBoxes(rgbImg)
	
	faces = []
	for box in bb:
		x, y, w, h = box.left(), box.top(), box.right(), box.bottom()
		faces.append(np.array(bgrImg[y: h, x: w]))
		cv2.rectangle(bgrImg, (x, y), (w, h), (0, 321, 123), 3)

	return bgrImg, faces


def getRep(bgrImg):
	try:
		rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)
		bb = align.getLargestFaceBoundingBox(rgbImg)
		alignedFace = align.align(imgDim, rgbImg, bb, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)	
		rep = net.forward(alignedFace)
		return rep
	except:
		return None

