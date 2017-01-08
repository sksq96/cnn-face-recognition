#!/usr/bin/env python2

import openface

dlibFacePredictor='/root/openface/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
networkModel='/root/openface/openface/models/openface/nn4.small2.v1.t7'

align = openface.AlignDlib(dlibFacePredictor)
net = openface.TorchNeuralNet(networkModel, 96)

