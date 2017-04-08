# @Author: shubham
# @Date:   2016-09-13 19:31:15
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2017-04-05 18:26:10


# python webcam.py classdemo tushar

sudo chmod 777 -R data/classdemo/aligned
rm -rfr data/classdemo/aligned/*

openface/./util/align-dlib.py data/classdemo/raw align outerEyesAndNose data/classdemo/aligned --size 96
openface/./batch-represent/main.lua -outDir data/classdemo/feature -data data/classdemo/aligned
code/./classifier.py train data/classdemo/feature

# code/./classifier.py infer data/classdemo/feature/classifier.pkl data/classdemo/test/*
openface/./demos/classifier_webcam.py data/classdemo/feature/classifier.pkl

