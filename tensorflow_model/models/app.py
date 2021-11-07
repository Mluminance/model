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
        hs.HopsNumber("UDIPrediction", "UDI Prediction", "Prediction of UDI for room")
    ]
)
def getUDIPrediction(roomBoundary: rdm.PolylineCurve, windowWidth: float,windowHeight: float):

    #convert to polyline to be able to measure distances

    myPolyline = roomBoundary.ToPolyline()
    # my points
    point0: rdm.Point3d = myPolyline[0]
    point1: rdm.Point3d = myPolyline[1]
    point2: rdm.Point3d = myPolyline[2]
    point3: rdm.Point3d = myPolyline[3]

    # calculating distances
    sideA = point0.DistanceTo(point1)
    sideB = point1.DistanceTo(point2)
    sideC = point2.DistanceTo(point3)
    sideD = point3.DistanceTo(point0)

    # calculate orientation
    




    # get all 4 lengths of roomBoundary

    # fetch Prediction data from myML
    fetchedPrediction = myMl.RunPredictionOp1(sideA,sideB,sideC,sideD,windowWidth,windowHeight)
    print("prediction done!")
    print("fetched prediction data")
    return fetchedPrediction