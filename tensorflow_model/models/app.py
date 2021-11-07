from flask import Flask
import ghhops_server as hs
import rhino3dm as rdm



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
        hs.HopsNumber("roomBoundary", "Room Boundary Curve", "Closed curve representing the room boundary"),
        hs.HopsNumber("windowWidth", "Window Width", "Width of Window"),
        hs.HopsNumber("windowHeight", "Window Height", "Height of Window"),
    ],
    outputs=[
        hs.HopsString("UDIPrediction", "UDI Prediction", "Prediction of UDI for room")
    ]
)
def getUDIPrediction(roomBoundary, windowWidth,windowHeight):

    #convert to polyline to be able to measure distances

    #myPolyline = roomBoundary.ToPolyline()
    # my points
    """
    point0: rdm.Point3d = myPolyline[0]
    point1: rdm.Point3d = myPolyline[1]
    point2: rdm.Point3d = myPolyline[2]
    point3: rdm.Point3d = myPolyline[3]

    # calculating distances
    sideA = point0.DistanceTo(point1)
    sideB = point1.DistanceTo(point2)
    sideC = point2.DistanceTo(point3)
    sideD = point3.DistanceTo(point0)
    """

    # calculating orientation
    # get first vector
    #fVector: rdm.Vector3d = point1 - point0
    
    print("this is a test")
    
    return "hello Karim"

if __name__ == "__main__":
    app.run()
