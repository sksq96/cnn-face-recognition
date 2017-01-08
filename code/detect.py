#!/usr/bin/env python2

import os
import sys
import pickle
from time import time

import cv2
import numpy as np
np.set_printoptions(precision=2)

from encode import detect

def detectFaces(file, step=20):
	cap = cv2.VideoCapture(file)
	_, frame = cap.read()
	
	file = 'viz/' + str(int(time())) + '.avi'
	fourcc = cv2.cv.CV_FOURCC(*'XVID')
	out = cv2.VideoWriter(file, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
	
	idx = 0
	while True:
		running, frame = cap.read()
		if not running:
			break
		
		idx += 1
		if idx%step != 0:
			continue
		
		frame = detect(frame)
		out.write(frame)
		print("-- Processed {} frame --".format(idx))
	

def main():
	file = sys.argv[1]
	detectFaces(file, 100)
	

if __name__ == '__main__':
	main()

