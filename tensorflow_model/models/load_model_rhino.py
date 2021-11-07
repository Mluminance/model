from flask import Flask
import tensorflow as tf
import pandas as pd
import numpy as np
import os
import json
import sys
from tensorflow.keras.models import model_from_json

#path = os.path.join(sys.path[0], "log\DA_dnn_10-4.json")
#print(path)
# inputData = np.array([4,9,5,9.5,2.3,3.4,0,45])


def runDaylightPrediction(sideA,sideB,sideC,sideD,wWidth,wHeight,orient,area):

    # Set current working directory
    #cwd = '/content/drive/MyDrive/Daylight Autonomy'
    #cwd = os.path.join(sys.path[0], "models/DA_CNN.json")
    #print("working directory")
    #print(cwd)
    print(os.getcwd())
    # Load CNN model
    json_file = open('model/tensorflow_model/models/DA_CNN.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    print("loaded json")
    
    loaded_model.load_weights('model/tensorflow_model/models/DA_CNN.h5')

    # test case dictionary. Can be any list or array as long as the order is correct and is shaped to (1,8)
    """
    test_case = {
        'SideA': 4.7,
        'SideB': 8.0,
        'SideC': 6.0,
        'SideD': 9.52,
        'WindowWidth': 2.87,
        'WindowLength': 1.25,
        'Orientation': 45,
        'Area': 45
    }
    """
    inputs = [sideA,sideB,sideC,sideD,wWidth,wHeight,orient,area]


    # converting dictionary to 2D vector of size (1,8)
    input_data = np.array(inputs).reshape(1,-1)

    # predict input array, returns a 4D vector of size (1, 30, 31, 1)
    test_pred = loaded_model.predict(input_data)
    test_pred = test_pred.reshape(30,31)
    test_pred = np.flipud(test_pred)
    #test_pred = np.fliplr(test_pred)

    # reshape to 1D vector for honeybee to recolor mesh
    output = test_pred.ravel() 

    return list(output)
    

"""
def runDaylightPrediction(sideA,sideB,sideC,sideD,wWidth,wHeight,orient,area):

    json_file = open('DA_dnn_10-4.json', 'r')
    print(json_file)

    loaded_model_json = json_file.read()
    print(loaded_model_json)
    json_file.close()

    # loading model 
    loaded_model = tf.keras.models.model_from_json(loaded_model_json)
    loaded_model.load_weights('DA_dnn_10-4.h5')
    loaded_model.summary() 

    inputData = np.array([sideA,sideB,sideC,sideD,wWidth,wHeight,orient,area])

    prediction = loaded_model.predict( np.expand_dims(inputData, axis=0) )[0][0] 

    return prediction
"""