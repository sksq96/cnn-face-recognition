# @Author: shubham
# @Date:   2016-09-13 19:31:15
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2016-11-20 05:29:12

# sudo chmod 777 -R mydata/aligned
# rm -rfr mydata/aligned/*

openface/./util/align-dlib.py mydata/raw align outerEyesAndNose mydata/aligned --size 96
openface/./batch-represent/main.lua -outDir mydata/feature -data mydata/aligned
# openface/./demos/classifier.py train mydata/feature
openface/./demos/classifier_webcam.py mydata/feature/classifier.pkl

