import os
import Folder
from datetime import datetime, timedelta

"""
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_rate = float(cap.get(5))

    out = cv2.VideoWriter(str(file_name) + ".mp4", cv2.VideoWriter_fourcc(*'mp4v'), frame_rate,
                          (frame_width, frame_height))"""

path = "/Volumes/SECURITY_CAM/"

s = "00:00:00"

x = datetime.strptime(s, "%H:%M:%S")
y = x.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
print(y)
z = y - x
print(z.seconds)

