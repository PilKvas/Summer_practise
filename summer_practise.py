
import pandas as pd 
import os
import matplotlib.pyplot as plt 



city = input('Введите город: ') # Ввод города 
year = input('Введите год: ') # Ввод года 


def plot(city, year): # Основная функция 
    array_month= [] # Задаем списки для будущего графика
    array_day = []
    array_night = []
    path = 'C:\\Users\\hm10b\\Desktop\\python\\meteo\\' + city # Переменная для пути
    for filename in os.listdir(path): # цикл, который перебирает все файлы из папки 
        if year in filename: # Добавлаем условие, чтобы работать только с файлами определенного города и года 
            table = pd.read_csv(os.path.join(path, filename), index_col=0) # Считываем csv файл
            filename = (filename.replace('.csv', ' ')).replace('_', ' ') # эта строчка оставляют только смысловую часть названия файла
            month = [str(s) for s in filename.split() if s.isdigit()] # Получаем список с годом и месяцем в формате [2017, 6]
            average_day = table['Температура днём'].mean() # Находим среднее значание столба Температура днём
            average_night = table['Температура вечером'].mean() # Находим среднее значание столба Температура вечером
            array_day.append(average_day) # Добавляем в массив наши значения 
            array_night.append(average_night)
            array_month.append(month[-1])
    # Блок для графика 
    plt.plot(array_month,array_day,array_night)  # Создаем график 
    plt.title('Средняя температура') # Задаем название графика
    plt.grid() # Добавляем сетку 
    plt.xlabel('Месяц') # Даем название оси x
    plt.ylabel('Температура') # Даем название оси y 
    plt.legend(['Средняя температура днём', 'Средняя температура вечером'], loc ="upper left") # Отображаем легенду 
    plt.show() # Показываем таблицу 

print(plot(city, year))
    # df = pd.DataFrame({'Месяц': array_month,'Средняя температура днём':array_day, 'Средняя температура вечером':array_night}) # Создаем DataFrame со значениями, которые мы должны представить в графике
    # df = df.set_index(['Месяц']) # Меняем столбец индексов на стобец Месяц
    # array_month.sort()
# def num_Months_To_Strings(array_month_numbers):
#     for i in range(len(array_month_numbers)):
#             # print(array_month_numbers)
#             # match array_month_numbers[i]:
#             #     case 1:
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Январь')
#             #     case 2: 
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Февраль')
#             #     case 3:
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Март')
#             #     case 4: 
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Апрель')
#             #     case 5:
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Май')
#             #     case 6: 
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Июнь')
#             #     case 7:
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Июль')
#             #     case 8: 
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Август')
#             #     case 9:
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Сентябрь')
#             #     case 10:
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Октябрь')
#             #     case 11:
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Ноябрь')
#             #     case 12:
#             #         array_month_numbers.pop(i)
#             #         array_month_numbers.append('Декабрь')
#             if array_month_numbers[i] == 1:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Январь')
#             if array_month_numbers[i] == 2:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Февраль')
#             if array_month_numbers[i] == 3:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Март')
#             if array_month_numbers[i] == 4:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Апрель')
#             if array_month_numbers[i] == 5:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Май')
#             if array_month_numbers[i] == 6:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Июнь')
#             if array_month_numbers[i] == 7:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Июль')
#             if array_month_numbers[i] == 8:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Август')
#             if array_month_numbers[i] == 9:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Сентябрь')
#             if array_month_numbers[i] == 10:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Октябрь')
#             if array_month_numbers[i] == 11:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Ноябрь')
#             if array_month_numbers[i] == 12:
#                 array_month_numbers.pop(i)
#                 array_month_numbers.append('Декабрь')
#     return array_month_numbers




