import regression2
import numpy as np
import matplotlib.pyplot as plt

def estimate(dist):
    a,b,c=regression2.regression()
    step_estimate = a/(dist-c)+b
   
    return step_estimate
pos = [333000, 280000, 254000, 239000, 229000, 222000, 217000, 213000, 209500]
dist = [2.003, 2.987, 4.041, 5.055, 6.016, 6.996, 7.937, 9.04, 9.995]
residual=[]
for i in range(9):
    #print(estimate(dist[i])-pos[i])
    residual.append(estimate(dist[i])-pos[i])

plt.figure(figsize=(8, 6))
plt.scatter(dist, residual, color='blue', label='Data Points')
plt.xlabel('Distance (m)')
plt.ylabel('Residual (step)')
plt.title('Residual vs. Distance')
plt.legend()
plt.show()

