# @Author: Shubham Chandel
# @Date:   2016-11-20 05:21:06
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2016-11-20 05:39:55

# openface/./mycode/vectorsImage.py mydata/test/*
# openface/./mycode/tsne.py mydata/test/*


sudo chmod 777 -R mydata/aligned
rm -rfr mydata/aligned/*

openface/./util/align-dlib.py mydata/raw align outerEyesAndNose mydata/aligned --size 96
openface/./batch-represent/main.lua -outDir mydata/feature -data mydata/aligned
openface/./util/tsne.py mydata/feature --names q w e r t y

