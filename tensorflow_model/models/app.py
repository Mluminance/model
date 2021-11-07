from flask import Flask
import ghhops_server as hs
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import rhino3dm as rdm


import load_model as lm

# register hops app as middleware
app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/getUDIPrediction",
    name="Get UDI prediction",
    description="Predicts the UDI of a given room object",
    #icon="learncarbon_logo_without_text.png",
    inputs=[
        hs.HopsCurve("roomBoundary", "Room Boundary Curve", "Closed curve representing the room boundary"),
        hs.HopsNumber("windowWidth", "windowWidth", "Width of Window"),
        hs.HopsNumber("windowHeight", "Window Height", "Height of Window")
    ],
    outputs=[
        hs.HopsNumber("C02_Prediction", "C02_Prediction", "CO2 prediction")
    ]
)
def getUDIPrediction(constructionType,buildingType,location,area,floorCount):
    # fetch Prediction data from myML
    fetchedPrediction = myMl.RunPredictionOp1(constructionType,buildingType,location,area,floorCount)
    print("prediction done!")
    print("fetched prediction data")
    return fetchedPrediction