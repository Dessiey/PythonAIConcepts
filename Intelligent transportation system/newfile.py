import json
 import logging
 
 from flask import Flask, redirect, flash, request
 
 from secrets import SECRET_KEY
 
 CAM_DATA_PATH = "/data/<a href="http://cameras.json">cameras.json</a>"  #  mount JSON to /data/ on container launch
 CAM_ID_KEY = "CAMERA_ID"
 CAM_IP_FIELD = "CAMERA_IP"
 CAM_ID_PARAM = "cam_id"
 
 app = Flask(__name__)
 app.secret_key = SECRET_KEY
 
 
 def load_data(path):
    with open(path, "r") as fin:
        data = <a href="http://json.loads">json.loads</a>(<a href="http://fin.read">fin.read</a>())
 
    return data
 
 
 def get_camera_by_id(data, key, val):
    #  return camera data that matches requested camera ID
    for row in data:
        if str(row[key]) == str(val):
            return row
    #  camera not found
    return None
 
 
 @<a href="http://app.route">app.route</a>("/")
 def return_camera_url():
    """
    Redirect client to camera feed
    """
 
    # temp debugging to understand dropped requests
    <a href="http://logging.info">logging.info</a>(request)
 
    #  Parse URL for camera ID
    cam_id = <a href="http://request.args.get">request.args.get</a>(CAM_ID_PARAM)
 
    if cam_id:
        #  Get camera data from source JSON
        cam = get_camera_by_id(data, CAM_ID_KEY, cam_id)
 
        if cam:
            ip = cam[CAM_IP_FIELD]
 
            #  Redirect to camera feed
            <a href="http://logging.info">logging.info</a>(f"return {ip}")
 
            return f"&lt;h1&gt;&lt;a href=\"http://{ip}\"&gt;Click here to view camera feed for camera {cam_id}&lt;/a&gt;&lt;/h1&gt;"
 
        return f"Camera ID {cam_id} not found :/"
 
    else:
        return "No camera specified."
 
 
 if __name__ == "__main__":
    <a href="http://logging.basicConfig">logging.basicConfig</a>(filename='<a href="http://error.log">error.log</a>',level=<a href="http://logging.DEBUG">logging.DEBUG</a>)
 
    data = load_data(CAM_DATA_PATH)
 app.run(debug=True, host="0,0,0,0")
</body>

</html>a