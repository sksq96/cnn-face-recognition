#!/usr/bin/env python2

import os
import sys
import pickle
from time import time

import cv2
import numpy as np
np.set_printoptions(precision=2)

from encode import detect

def face_detection(file, step=1, video=False, save=False):
	cap = cv2.VideoCapture(file)
	_, frame = cap.read()
	
	file = 'viz/' + str(int(time())) + '.avi'
	fourcc = cv2.cv.CV_FOURCC(*'XVID')
	out = cv2.VideoWriter(file, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
	
	faces_dir = 'viz/' + str(int(time())) + '/'
	os.makedirs(faces_dir)

	idx = 0
	while True:
		running, frame = cap.read()
		if not running:
			break
		
		idx += 1
		if idx%step != 0:
			continue
		
		frame, faces = detect(frame)
		
		if video: out.write(frame)

		if save:
			for i, face in enumerate(faces):
			 	cv2.imwrite('{}/{}_{}.jpg'.format(faces_dir, str(int(time())), i), face)

		print("-- Processed {} frame --".format(idx))
	

def main():
	file = sys.argv[1]
	face_detection(file, step=5, video=True, save=True)

	
if __name__ == '__main__':
	main()

