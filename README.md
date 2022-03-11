# MLuminance
Instant daylight autonomy generation for a single room with one window located in Copenhagen.
Winner of the "Best Overall Hack" at the AEC Tech Hackathon 2021
![InstantDA](https://github.com/Mluminance/model/blob/main/resources/images/Readme_img/InstantDA.gif)

## Running the instant daylighting model
Requires the following:
* Rhino 7
* [Hops component for Grasshopper](https://developer.rhino3d.com/guides/compute/hops-component/) (See [CPython in Grasshopper Guide](https://github.com/mcneel/compute.rhino3d/tree/master/src/ghhops-server-py) for all required libraries)
* [Visual Studio Code](https://code.visualstudio.com/)
* Python version 3.10.2 
* Tensorflow version 2.8.0

Steps to run grasshopper and python files:
1. Open "InstantDaylight.gh" in Grasshopper
2. Open "app.py" in Visual Studio Code and edit the file paths to the tensorflow model under "# Load tensorflow model". Run the python code and check the terminal for the path to the hops server (default: http://127.0.0.1:5000/)
![Visual Studio Screenshot](https://github.com/Mluminance/model/blob/main/resources/images/Readme_img/visualstudio.png)
3. Double click "Instant Daylight Autonomy" in the Grasshopper model and paste in hops server path followed by "instantda" (http://127.0.0.1:5000/instantda).
![Set hops server path](https://github.com/Mluminance/model/blob/main/resources/images/Readme_img/setpath.png)
4. Draw a closed polyline with four vertices within the mesh space in Rhino. The mesh is most accurate when centered around the origin. Set the curve to "Room Curve" in the Grasshopper file. If daylight autonomy mesh does not immediately show up, change the slider values to start.
5. Change the slider values (in Grasshopper or the Remote Control Panel in Rhino) or move the control points to see the change in daylight autonomy instantly.


## Training Data Generation (WIP)
Traing data was generated using Ladybug Tools and the Pollination Cloud service. 

Room was created using a pseudo random seed value to change the following inputs:
* Four room coordinates (four random points on a randomly generated circle)
* Room height
* Room orientation
* Window width ratio
* Window height ratio

The analysis mesh is a 30x30 grid centered around the origin.

## Training the neural network model (WIP)