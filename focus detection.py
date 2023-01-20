import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
import uuid
import os
import time
import matplotlib
model = torch.hub.load('ultralytics/yolov5', 'custom', path='C:/Users/Ali Abdilahi/yolov5/runs/train/exp16/weights/last.pt', force_reload=True)
model.conf = 0.25  # confidence threshold (0-1)
model.iou = 0.2
cap = cv2.VideoCapture(0)
focusedCounter =0
downCounter =0
leftCounter =0
rightCounter =0
secondsCounter = 0
infocus = []
ReadState = []
lastcall = "empty"
starttime = time.time()
currenState =0
unfocusedCounter=0
linefoc = []
foc = 0
lineunfo = []
unfoc =0 
machineState = 0
while cap.isOpened():
    ret, frame = cap.read()
    # Make detections 
    results = model(frame)
    color=(0,255,0)
    thickness = 2
    org = (10, 40)
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    on=""
    if(machineState==1):
        on="True"
    else:
        on="False"
    cv2.putText(frame, "Detection: "+on, org, font,fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('YOLO', np.squeeze(results.render()))
    data =[results.pandas().xyxy[0]]
    if data:
        for i in data:
            if len(i.name.values) == 1:
                machineState = 1
                if i.name.values[0] == "focused":
                    focusedCounter+=1
                    foc +=1
                    currenState = 1
                else:
                    currenState = 0
                    unfocusedCounter+=1
                    if i.name.values[0] == "right":
                        rightCounter+=1
                    elif i.name.values[0] == "left":
                        leftCounter+=1
                    elif i.name.values[0] == "down":
                        downCounter+=1
            else:
                machineState = 0
    timenow= time.time()
    if timenow-starttime>1:
        starttime=time.time()
        linefoc.append(foc)
        lineunfo.append(unfocusedCounter)
        secondsCounter+=1
        if(machineState==1):
            ReadState.append(1)
        else:
            ReadState.append(0)
        foc = 0
        unfocusedCounter = 0


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

print("done")

lines = [focusedCounter,downCounter,leftCounter,rightCounter,secondsCounter,ReadState,linefoc,lineunfo]

with open('DataSave.txt', 'w') as f:
    for line in lines:
        f.write(str(line))
        f.write('\n')
