from flask import Flask
import ghhops_server as hs
import rhino3dm as rdm
import math
from load_model_rhino import runDaylightPrediction

# utilties:
# calculate area
# (X[i], Y[i]) are coordinates of i'th point.
# This code is contributed by
# Smitha Dinesh Semwal
def polygonArea(X, Y, n):
 
    # Initialize area
    area = 0.0
 
    # Calculate value of shoelace formula
    j = n - 1
    for i in range(0,n):
        area += (X[j] + X[i]) * (Y[j] - Y[i])
        j = i   # j is previous vertex to i
 
    # Return absolute value
    return int(abs(area / 2.0))

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
        hs.HopsNumber("windowWidth", "Window Width", "Width of Window"),
        hs.HopsNumber("windowHeight", "Window Height", "Height of Window"),
    ],
    outputs=[
        hs.HopsNumber("UDIPrediction", "UDI Prediction", "Prediction of UDI for room")
    ]
)
def getUDIPrediction(roomBoundary, windowWidth,windowHeight):

    #convert to polyline to be able to measure distances
    myPolyline = roomBoundary.ToPolyline()
    
    point0: rdm.Point3d = myPolyline[0]
    point1: rdm.Point3d = myPolyline[1]
    point2: rdm.Point3d = myPolyline[2]
    point3: rdm.Point3d = myPolyline[3]

    # calculating distances
    sideA = point0.DistanceTo(point1)
    sideB = point1.DistanceTo(point2)
    sideC = point2.DistanceTo(point3)
    sideD = point3.DistanceTo(point0)

    # calculating orientation
    # get first vector
    vX = point1.X - point0.X
    vY = point1.Y - point0.Y
    vZ = point1.Z - point0.Z 

    fVector = rdm.Vector3d(vX,vY,vZ)

    #compute north vector
    nVector = rdm.Vector3d(0.0,0.0,0.0)

    # calculate angle according to x access
    # based on https://stackoverflow.com/questions/42258637/how-to-know-the-angle-between-two-vectors
    radAngle = math.atan2(fVector.X-nVector.X, fVector.Y-nVector.Y) - math.pi*0.5
    degAngle = abs(math.degrees(radAngle))

    if degAngle <= 180 and degAngle >= 90:
        orientation = abs(degAngle - 180)
    elif degAngle <= 90 and degAngle >= 0 and radAngle < 0:
        orientation = abs(degAngle - 180)
    elif degAngle <= 90 and degAngle >= 0 and radAngle > 0:
        orientation = degAngle + 180
    elif degAngle  <= 270 and degAngle >= 180:
        orientation = (360 - degAngle) + 180

    # calcute area:
    X = [point0.X, point1.X, point2.X, point3.X]
    Y = [point0.Y, point1.Y, point2.Y, point3.Y]
    n = len(X)
    area = polygonArea(X, Y, n)

    prediction = runDaylightPrediction(sideA,sideB,sideC,sideD,windowWidth,windowHeight,orientation,area)
    #print(prediction)

    myPredictions = []
    for p in prediction:
        fValue = float(p)
        if fValue < 0.0:
            fValue = 0.0
            myPredictions.append(fValue)
        else:
            myPredictions.append(fValue)

    print(orientation)

    return myPredictions

if __name__ == "__main__":
    app.run()
