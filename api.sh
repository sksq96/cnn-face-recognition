# @Author: shubham
# @Date:   2016-09-13 19:31:15
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2017-03-31 05:51:08

# sudo chmod 777 -R data/hworld/aligned
# rm -rfr data/hworld/aligned/*

# openface/./util/align-dlib.py data/hworld/raw align outerEyesAndNose data/hworld/aligned --size 96
# openface/./batch-represent/main.lua -outDir data/hworld/feature -data data/hworld/aligned

openface/./demos/classifier_webcam.py data/hworld/feature/classifier.pkl
# openface/./demos/classifier.py infer data/hworld/feature/classifier.pkl data/hworld/test/*

# code/./classifier.py train data/hworld/feature
# code/./classifier.py infer data/hworld/feature/classifier.pkl data/hworld/test/*

