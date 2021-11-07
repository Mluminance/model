from flask import Flask
import ghhops_server as hs
import rhino3dm as rdm
import math



#import load_model as lm

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
        hs.HopsString("UDIPrediction", "UDI Prediction", "Prediction of UDI for room")
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

    #print(degAngle)
    #print((radAngle))

    if degAngle <= 180 and degAngle >= 90:
        myAngle = abs(degAngle - 180)
    elif degAngle <= 90 and degAngle >= 0 and radAngle < 0:
        myAngle = abs(degAngle - 180)
    elif degAngle <= 90 and degAngle >= 0 and radAngle > 0:
        myAngle = degAngle + 180
    elif degAngle  <= 270 and degAngle >= 180:
        myAngle = (360 - degAngle) + 180

    print("this is my starting angle")
    print(degAngle)
    #print(radAngle)
    print("this is my orientation")
    print(myAngle)

    #print("this is a test")

    return "hello Karim"

if __name__ == "__main__":
    app.run()
