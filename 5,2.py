import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# загрузка данных
data = np.load('average_ratings.npy')

# названия рецептов
recipes = ['waffle iron french toast', 'zwetschgenkuchen bavarian plum cake', 'lime tea']

# создание диапазона дат
dates = pd.date_range(start='2019-01-01', end='2021-12-30', freq='D')

# построение графика
fig, ax = plt.subplots()
ax.plot(dates, data[:, 0], label=recipes[0])
ax.plot(dates, data[:, 1], label=recipes[1])
ax.plot(dates, data[:, 2], label=recipes[2])

# добавление подписей осей и заголовка
ax.set_xlabel('Дата')
ax.set_ylabel('Средний рейтинг')
ax.set_title('Изменение среднего рейтинга трех рецептов')

# добавление легенды
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

# настройка major_locator и minor_locator горизонтальной оси
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_minor_locator(mdates.MonthLocator())

# форматирование горизонтальной оси
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.xaxis.set_minor_formatter(mdates.DateFormatter('%b'))

plt.show()