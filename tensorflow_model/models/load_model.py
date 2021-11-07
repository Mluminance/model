from flask import Flask
import tensorflow as tf
import pandas as pd
import numpy as np
import os
import json
import sys

#path = os.path.join(sys.path[0], "log\DA_dnn_10-4.json")
#print(path)
# inputData = np.array([4,9,5,9.5,2.3,3.4,0,45])


def runDaylightPrediction(sideA,sideB,sideC,sideD,wWidth,wLength,Orient,IlluArea):

    json_file = open('DA_dnn_10-4.json', 'r')
    print(json_file)

    loaded_model_json = json_file.read()
    print(loaded_model_json)
    json_file.close()

    # loading model 
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    loaded_model.load_weights('DA_dnn_10-4.h5')
    loaded_model.summary() 

    inputData = np.array([sideA,sideB,sideC,sideD,wWidth,wLength,Orient,IlluArea])

    prediction = loaded_model.predict( np.expand_dims(inputData, axis=0) )[0][0] 

    return prediction