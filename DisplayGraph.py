from matplotlib import pyplot as plt
import numpy as np
from ast import literal_eval


with open('DataSave.txt') as f:
    lines = [line.rstrip('\n') for line in f]
focusedCounter= int(lines[0])
downCounter= int(lines[1])
leftCounter= int(lines[2])
rightCounter= int(lines[3])
secondsCounter = int(lines[4])
machineState = literal_eval(lines[5])
linefo = literal_eval(lines[6])
lineunfoc = literal_eval(lines[7])

print(lines)
total = focusedCounter+downCounter+leftCounter+rightCounter
size = np.array([focusedCounter/total, downCounter/total, leftCounter/total, rightCounter/total])

labels = ['Focused','Looking down','Looking left','Looking Right']
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
plt.figure(1)
#plt.subplot(1)
patches, texts = plt.pie(size, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.title("Activities")
plt.tight_layout()

plt.figure(2)
#plt.subplot(
time = np.arange(0,secondsCounter)
plt.step(time, machineState)
plt.title("Detection State of the machine of time")
plt.xlabel("Time")
plt.ylabel("Detection State")

plt.figure(3)
graph = []
for i in range(len(time)):
    graph.append(linefo[i]- lineunfoc[i])
    
plt.plot(time, graph)
plt.title("User's focus over time")
plt.xlabel("Time")
plt.ylabel("User focus state")

plt.show()