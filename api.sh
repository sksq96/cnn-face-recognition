# @Author: shubham
# @Date:   2016-09-13 19:31:15
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2017-03-31 17:39:42

# sudo chmod 777 -R data/classdemo/aligned
# rm -rfr data/classdemo/aligned/*

# python webcam.py classdemo shubham

# openface/./util/align-dlib.py data/classdemo/raw align outerEyesAndNose data/classdemo/aligned --size 96
# openface/./batch-represent/main.lua -outDir data/classdemo/feature -data data/classdemo/aligned

# code/./classifier.py train data/classdemo/feature
# code/./classifier.py infer data/classdemo/feature/classifier.pkl data/classdemo/test/*
openface/./demos/classifier_webcam.py data/classdemo/feature/classifier.pkl

