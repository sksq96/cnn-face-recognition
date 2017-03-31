# @Author: shubham
# @Date:   2016-09-13 19:31:15
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2017-03-31 06:14:02

# sudo chmod 777 -R data/Classdemo/aligned
# rm -rfr data/Classdemo/aligned/*

openface/./util/align-dlib.py data/Classdemo/raw align outerEyesAndNose data/Classdemo/aligned --size 96
openface/./batch-represent/main.lua -outDir data/Classdemo/feature -data data/Classdemo/aligned

# code/./classifier.py train data/Classdemo/feature
# code/./classifier.py infer data/Classdemo/feature/classifier.pkl data/Classdemo/test/*
# openface/./demos/classifier_webcam.py data/Classdemo/feature/classifier.pkl

