# @Author: shubham
# @Date:   2016-09-13 19:31:15
# @Last Modified by:   Shubham Chandel
# @Last Modified time: 2017-04-26 15:04:50


folder="cluster"



# emply aligned
# sudo chmod 777 -R data/$folder/aligned
# rm -rfr data/$folder/aligned/*


# align landmarks, store in aligned
# openface/./util/align-dlib.py data/$folder/raw align outerEyesAndNose data/$folder/aligned --size 96

# extract features
# openface/./batch-represent/main.lua -outDir data/$folder/nfeature -data data/$folder/cluster

# train the classifier
# code/./classifier.py train data/$folder/nfeature

# test the training
code/./classifier.py infer data/$folder/nfeature/classifier.pkl data/$folder/test/*


# webcam stuff
# python webcam.py $folder tushar
# openface/./demos/classifier_webcam.py data/$folder/feature/classifier.pkl

