import numpy as np
from math import sin, cos, sqrt
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Функцкия построения фазового портрета
def draw_f_plot(x, y):
	plt.plot(x, y)
	plt.title("Фазовый портрет")
	plt.xlabel('x')
	plt.ylabel('x`')
	plt.grid()
	plt.show()

# Функция построения графика решения
def draw_plot(x, y, t):
	plt.plot(t, x, label = 'x')
	plt.plot(t, y, label = 'x`')
	plt.title("Решение дифференциального уравнения")
	plt.xlabel('t')
	plt.ylabel('x')
	plt.legend()
	plt.grid()
	plt.show()

# Параметры осциллятора 
# x'' + g* x' + w^2* x = f(t) 
# w - частота
# g - затухание
w = sqrt(5.2)
g = 0

# Точка, в которой заданы начальные условия
t0 = 0 # Начальный момент времени 
tmax = 61 # Конечный момент времени 
dt = 0.05 # Шаг изменения времени

# Интервал, в котором решается задача
t = np.arange(t0, tmax, dt)

# Начальные условия
# x(t0) = x0
x0 = 0.5
y0 = -1.5

# Вектор начальных условий
v0 = np.array([x0, y0])

# Правая часть уравнения f(t)
def F(t):
	f = 0
	return f

# Вектор-функция f(t, x)
# для решения системы дифференциальных уравнений
# x' = y(t, x)
# где x - искомый вектор
def dx(x, t):
	dx1 = x[1]
	dx2 = -w* w* x[0] - g * x[1] - F(t)
	return [dx1, dx2]

# Решаем дифференциальные уравнения
# с начальным условием x(t0) = x0
# на интервале t
# с правой частью, заданной y
# и записываем решение в матрицу x
x = odeint(dx, v0, t)

# Переписываем отдельно //x в y1, x' в y2
xpoint = [elem[0] for elem in x] 
ypoint = [elem[1] for elem in x]

# Построим фазовый портрет
draw_f_plot(xpoint, ypoint)

# Построим график решений
draw_plot(xpoint, ypoint, t)






