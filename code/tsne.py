#!/usr/bin/env python2

import os
import sys
import pickle
from pprint import pprint
from time import time

import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE


def load(pk):
	return pickle.load(open(pk, 'r'))


def tSNE(encoding):
	print("-- t-sne --")
	X_pca = PCA(n_components=50).fit_transform(encoding, encoding)
	tsne = TSNE(n_components=2, init='random', random_state=0)
	return tsne.fit_transform(X_pca)

def plot(tsne, file=str(int(time()))):
	print("-- plot --")
	plt.scatter(tsne[:, 0], tsne[:, 1])
	plt.savefig('viz/' + file + '.jpg')
	

def main():
	file = sys.argv[1]
	encoding = load(file)
	tsne = tSNE(encoding)
	plot(tsne)


if __name__ == '__main__':
	main()

