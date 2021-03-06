
import pandas as pd 
import matplotlib.pyplot as plt 

city = 'rostov' # Ввод города 
year = '1998' # Ввод года 



def plot(city, year): # Основная функция 
    array_month= [] # Задаем списки для будущего графика
    array_day = []
    array_night = []
    array_month_cal = []
    path = 'meteo//' + city # Переменная для пути
    for filename in os.listdir(path): # цикл, который перебирает все файлы из папки 
        if year in filename: # Добавлаем условие, чтобы работать только с файлами определенного года 
            table = pd.read_csv(os.path.join(path, filename), index_col=0) # Считываем csv файл
            filename = (filename.replace('.csv', ' ')).replace('_', ' ') # эта строчка оставляют только смысловую часть названия файла
            month = [int(s) for s in filename.split() if s.isdigit()] # Получаем список с годом и месяцем в формате [2017, 6]
            average_day = table['Температура днём'].mean() # Находим среднее значание столба Температура днём
            average_night = table['Температура вечером'].mean() # Находим среднее значание столба Температура вечером
            array_day.append(average_day) # Добавляем в массив наши значения 
            array_night.append(average_night)
            array_month.append(month[-1])
    # Блок для графика
    array_month.sort() 
    for i in array_month:
        array_month_cal.append(month_dict[i])
    print(array_month)
    df = pd.DataFrame({'Месяц':array_month,'Средняя температура днём':array_day, 'Средняя температура вечером':array_night}) # Создаем DataFrame со значениями, которые мы должны представить в графике
    df = df.set_index(['Месяц']) # Меняем столбец индексов на стобец Месяц
    print(df)
    plt.figure(figsize= (14,12))
    plt.plot(df)  # Создаем график 
    plt.title('Средняя температура') # Задаем название графика
    plt.grid() # Добавляем сетку 
    plt.xlabel('Месяц') # Даем название оси x
    plt.ylabel('Температура') # Даем название оси y 
    plt.legend(['Средняя температура днём', 'Средняя температура вечером'], loc ="upper left") # Отображаем легенду 
    plt.show() # Показываем таблицу 

print(plot(city, year))
