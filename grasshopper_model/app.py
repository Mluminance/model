from flask import Flask
import ghhops_server as hs

import os
import numpy as np
from tensorflow.keras.models import model_from_json
from tensorflow.keras.layers import Activation, LeakyReLU
from keras.utils.generic_utils import get_custom_objects

get_custom_objects().update({'leaky-relu': Activation(LeakyReLU(alpha=0.2))})

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/instantda",
    name="InstantDA",
    description="Create daylight autonomy distribution",
    inputs=[
        hs.HopsNumber("x1", "x1", "First x coordinate"),
        hs.HopsNumber("y1", "y1", "First y coordinate"),
        hs.HopsNumber("x2", "x2", "Second x coordinate"),
        hs.HopsNumber("y2", "y2", "Second y coordinate"),
        hs.HopsNumber("x3", "x3", "Third x coordinate"),
        hs.HopsNumber("y3", "y3", "Third y coordinate"),
        hs.HopsNumber("x4", "x4", "Fourth x coordinate"),
        hs.HopsNumber("y4", "y4", "Fourth y coordinate"),
        hs.HopsNumber("Room Height", "h", "Room Height"),
        hs.HopsNumber("Window Width", "ww", "Window Width Ratio"),
        hs.HopsNumber("Window Height", "wh", "Window Height Ratio"),
        hs.HopsNumber("Window Orientation", "wo", "Window Orientation relative to north")
    ],
    outputs=[
        hs.HopsNumber("Daylight Autonomy", "DA", "Predicted Daylight Autonomy")
    ]
)
def instantda(x1,y1,x2,y2,x3,y3,x4,y4,h,ww,wh,wo):
    # Normalize input data
    domain = np.array([[-7.5,7.5], [-7.5,7.5], [-7.5,7.5], [-7.5,7.5],
                       [-7.5,7.5], [-7.5,7.5], [-7.5,7.5], [-7.5,7.5],
                       [2,3.5], [0.2,0.95], [0.2,0.95], [0,360]])
    d_avg = domain.mean(axis=1)
    d_std = domain.std(axis=1)

    input = np.array([x1,y1,x2,y2,x3,y3,x4,y4,h,ww,wh,wo])
    input = (input - d_avg) / d_std
    
    DA = loaded_model.predict(input.reshape(1,-1))
    DA_list = DA.reshape(1,-1)
    DA_list = [float(i) for i in DA_list[0]]

    return DA_list

if __name__ == "__main__":
    # Load tensorflow model
    json_file = open("DA_model.json", 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json, custom_objects={'Activation': Activation(LeakyReLU())})
    loaded_model.load_weights("DA_weights.h5")

    app.debug = True
    app.run()