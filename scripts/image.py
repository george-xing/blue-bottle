import os
import urllib
from datetime import datetime

filename = datetime.now().strftime("%Y_%m_%d_%H_%M") + "_img.jpg"
path = "images"
full_filename = os.path.join(path, filename)
urllib.urlretrieve("http://zaarly-bluebottle-cam.s3.amazonaws.com/bbline.jpg", full_filename)
