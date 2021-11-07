from flask import Flask
import tensorflow as tf
import pandas as pd
import numpy as np
import os
import json
import sys

#path = os.path.join(sys.path[0], "log\DA_dnn_10-4.json")
#print(path)

json_file = open('DA_dnn_10-4.json', 'r')
print(json_file)

loaded_model_json = json_file.read()
print(loaded_model_json)
json_file.close()

loaded_model = tf.keras.models.model_from_json(loaded_model_json)


loaded_model.load_weights('DA_dnn_10-4.h5')
loaded_model.summary() 
