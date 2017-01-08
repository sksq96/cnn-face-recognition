#!/usr/bin/env python2

import sys
import pickle

import numpy as np
np.set_printoptions(precision=2)
from sklearn.cluster import DBSCAN

from pprint import pprint
from collections import Counter

def load(pk):
	return pickle.load(open(pk, 'r'))


def cluster(encoding, eps=0.5, min_samples=2):
	db = DBSCAN(eps=eps, min_samples=min_samples).fit(encoding)
	print("Number of people: {}".format(len(set(db.labels_))))
	pprint(Counter(db.labels_))
	

def clusterGrid(encoding, eps=0.5, min_samples=2):
	headcount = 0
	for i in xrange(1, 1000):
		eps = i/1000.0
		db = DBSCAN(eps=eps, min_samples=min_samples).fit(encoding)
		headcount = max(headcount, len(set(db.labels_)))
	print("Number of people: {}".format(headcount))


def main():
	file = sys.argv[1]
	encoding = load(file)
	cluster(encoding, 0.4, 10)
	# clusterGrid(encoding)


if __name__ == '__main__':
	main()

