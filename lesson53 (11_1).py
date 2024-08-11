# Домашнее задание по теме "Обзор сторонних библиотек Python"

import matplotlib.pyplot as plt
import math

print('Рисуем функцию СИНУС c matplotlib.pyplot')
input('Приступим?')
# Рисуем функцию СИНУС c matplotlib.pyplot
x = [x for x in range(-180, 181)]
y = [math.sin(math.radians(y)) for y in range(-180, 181)]

fig, sinus_ = plt.subplots(figsize = (12,6))
sinus_.set_title('Синус')
sinus_.set_xlabel('градусы')
sinus_.plot(x,y)
plt.show()
print('сохраняем рисунок как файл Figure1.png')
input('?')
# сохраняем рисунок как файл Figure1.png
fig.savefig('.\\Figure1.png', transparent=None)
#########################################################
print('Сохранили')
input('Рисуем функцию КОСИНУС c matplotlib.pyplot и numpy?')
# Рисуем функцию КОСИНУС c matplotlib.pyplot и numpy
import numpy as np

x = np.arange(0, 5, 0.1) # список последовательно от 0 до 5 с шагом 0.1
y = np.cos(x) # применяем cos к каждому элементу списка

plt.plot(x, y) # строим кривую
plt.show()

input('А теперь анимируем функцию построения окружности c matplotlib.animation и numpy?')
# Анимируем функцию построения c matplotlib.pyplot и numpy

from matplotlib.animation import FuncAnimation

class CircleAnimation:
  def __init__(self, size_x, size_y, title):
    self.fig, self.ax = plt.subplots(figsize=(size_x, size_y))
    self.xdata = []
    self.ydata = []
    self.ax.set_title(title)
    self.ln, = plt.plot([], [], 's', color='green')


  def init_func(self):
    self.ax.set_xlim(-1.2, 1.2)
    self.ax.set_ylim(-1.2, 1.2)
    return self.ln,

  def update_func(self, frame):
    self.xdata.append(np.cos(frame))
    self.ydata.append(np.sin(frame))
    self.ln.set_data(self.xdata, self.ydata)
    return self.ln,

circle = CircleAnimation(7, 7, 'Окружность')
animation = FuncAnimation(
  circle.fig,
  circle.update_func,
  frames=np.linspace(0, 2 * np.pi, 128),
  init_func=circle.init_func, blit=False)

plt.show()

#
input('поработаем с картинкой что сохранили вначале?')
from PIL import Image, ImageFilter

figure = Image.open('Figure1.png')
figure.show()

input('Показать размеры картинки?')
print(f'Ширина: {figure.size[0]} Высота: {figure.size[1]}')
input('Слишком большой, уменьшим?')
figure = figure.reduce(3)
print(f'Теперь ширина: {figure.size[0]} Высота: {figure.size[1]}')
figure.show()
input('Отзеркалим? ')
figure = figure.transpose(Image.FLIP_LEFT_RIGHT)
figure.show()
input('Сделаем черно-белой?')
figure = figure.convert('L')
figure.show()

print('В качестве комментария: \nТам ещё полно всего, времени на коддинг мало')