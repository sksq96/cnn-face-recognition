#!/usr/bin/env python2

import os
import sys
import pickle
from time import time

import cv2
import numpy as np
np.set_printoptions(precision=2)

from encode import encode

def encodeVideo(file, step=20):
	cap = cv2.VideoCapture(file)
	faces, idx = [], 0
	
	while True:
		running, frame = cap.read()
		if not running:
			break
		
		idx += 1
		if idx%step != 0:
			continue
		
		encoding = encode(frame)
		faces.extend(encoding)
		print("-- Processed {} frame: {} --".format(idx, len(encoding)))
	
	return np.array(faces)

def save(obj, file=str(int(time()))):
	pk = 'pickle/' + file + '.pk'
	pickle.dump(obj, open(pk, 'w'))

def main():
	file = sys.argv[1]
	faces = encodeVideo(file, 10)
	save(faces)

if __name__ == '__main__':
	main()

