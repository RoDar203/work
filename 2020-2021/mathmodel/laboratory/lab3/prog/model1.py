import numpy as np
from math import sin, cos
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x0 = 61000
y0 = 45000

v0 = np.array([x0, y0])

t0 = 0
tmax = 1
dt =0.05

t = np.arange(t0, tmax, dt)

a = 0.28
b = 0.83
c = 0.31
h = 0.75

def P(t):
    p = 1.5*sin(t)
    return p

def Q(t):
    q = 1.5*cos(t)
    return q

def syst(y, t):
    dy1 = - a*y[0] - b*y[0]*y[1] + P(t)
    dy2 = - c*y[0]*y[1] - h*y[1] + Q(t)
    return [dy1, dy2]

y = odeint(syst, v0, t)

xpoint = [elem[0] for elem in y] 
ypoint = [elem[1] for elem in y]

plt.title("Model 2")
plt.plot(t, xpoint, label = 'Army X')
plt.plot(t, ypoint, label = 'Army Y')

plt.xlabel('time')
plt.ylabel('Count of Army')
plt.legend()
plt.grid()
plt.show()