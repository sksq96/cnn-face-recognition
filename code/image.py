#!/usr/bin/env python2


import os
import sys
import pickle
from time import time

import cv2
import numpy as np
np.set_printoptions(precision=2)

from encode import encode

# for each image, add all encoded faces
def encodeAllFaces(imgs):
	faces = []
	for img in imgs:
		frame = cv2.imread(img)
		encoding = encode(frame)
		faces.extend(encoding)
		print("-- Processed {}: {} --".format(img, len(encoding)))
	
	# faces = [encode(cv2.imread(img)) for img in imgs]
	return np.array(faces)


def save(obj, file=str(int(time()))):
	pk = 'pickle/' + file + '.pk'
	pickle.dump(obj, open(pk, 'w'))

def main():
	imgs = sys.argv[1:]
	faces = encodeAllFaces(imgs)
	save(faces)


if __name__ == '__main__':
	main()

