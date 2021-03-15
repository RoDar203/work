import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

alpha = 0.01 # коэффициент заболеваемости
beta = 0.02 # коэффициент выздоровления
N = 11900 # общая численность популяции
I0 = 290 # количество инфицированных особей в начальный момент времени t0 = 0
R0 = 52 # количество здоровых особей с иммунитетом в начальный момент времени t0 = 0
S0 = N - R0 # количество восприимчивых к болезни особей в начальный момент времени t0 = 0

# I(0) <= I
def dy_more(x, t):
    dy1 = 0
    dy2 = - beta * x[1]
    dy3 = beta * x[1]
    return [dy1, dy2, dy3]

# I(0) > I 
def dy_less(x, t):
    dy1 = alpha * x[0]
    dy2 = alpha * x[0] - beta * x[1]
    dy3 = beta * x[1]
    return [dy1, dy2, dy3]

def draw_plot(S, I, R, t):
    plt.plot(t, S, label = 'S(t)')
    plt.plot(t, I, label = 'I(t)')
    plt.plot(t, R, label = 'R(t)')
    plt.title("Динамика изменения числа людей в каждой из трех групп")
    plt.legend()
    plt.grid()
    plt.show()

# временной промежуток
t0 = 0
t = np.arange(0, 200, 0.01)

y0 = np.array([S0, I0, R0]) # вектор начальных значений

y = odeint(dy_more, y0, t)

S = [elem[0] for elem in y] 
I = [elem[1] for elem in y] 
R = [elem[2] for elem in y] 

draw_plot(S, I, R, t)


y = odeint(dy_less, y0, t)

S = [elem[0] for elem in y] 
I = [elem[1] for elem in y] 
R = [elem[2] for elem in y] 

draw_plot(S, I, R, t)


