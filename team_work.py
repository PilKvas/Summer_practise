import pandas as pd
import os

# изменяем настройки вывода таблицы
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.expand_frame_repr = False

city = "krasnodar"


# функция обрабатывающая файлы
def fileSearch(city):
    # формируем путь к файлам
    path = "meteo\\" + city
    # создаём пустой DataFrame
    newTable = pd.DataFrame()
    # перебираем все файлы в котологе
    for filename in os.listdir(path):
        # преобразуем файл типа csv в объект типа pandas
        table = pd.read_csv(os.path.join(path, filename), index_col=0)
        # извлекаем из названия файла дату и добавляем её в словарь
        newRow = filename.split("_")
        newRow.pop(0)
        newRow[1] = newRow[1].replace(".csv", "")
        time = ".".join(newRow[::-1])
        data = {"Дата": time}
        # создаём отдельную таблицу с ветро и находи среднее значение
        tableWind = table.loc[:, "Ветер вечером":"Ветер днём"]
        tableWind = tableWind.applymap(lambda x: reform(x))
        avarageWind = tableWind.mean(axis=0)
        data.update(avarageWind)
        # находи среднее значение таблицы без ветра
        avarageOther = table.mean(numeric_only=True)
        data.update(avarageOther)
        # соединяем таблицы
        newData = pd.DataFrame([data])
        newTable = pd.concat([newTable, newData])
    # задаёми индекс по дате
    newTable = newTable.set_index("Дата")
    return newTable


# реформатируем данные таблицы исключая символы из значений
def reform(value):
    num = "".join(ch for ch in value if ch.isdigit())
    if num == "":
        return 0
    else:
        return float(num)


# выводим таблицу
def createTable(city):
    table = fileSearch(city)
    print(table)


createTable(city)