import numpy as np
import matplotlib.pyplot as plt

# загрузка данных
data = np.load('average_ratings.npy')

# названия рецептов
recipes = ['waffle iron french toast', 'zwetschgenkuchen bavarian plum cake', 'lime tea']

# построение графика
fig, ax = plt.subplots()
ax.plot(data[:, 0], label=recipes[0])
ax.plot(data[:, 1], label=recipes[1])
ax.plot(data[:, 2], label=recipes[2])

# добавление подписей осей и заголовка
ax.set_xlabel('Номер дня')
ax.set_ylabel('Средний рейтинг')
ax.set_title('Изменение среднего рейтинга трех рецептов')

# добавление легенды
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.show()