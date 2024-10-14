import os
import csv
import pathlib
import pandas as pd
import numpy as np


class PriceMachine():
    
    def __init__(self):
        self.data = []
        self.result_of_requests = pd.DataFrame()
    
    def load_prices(self, file_path=''):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        readed_dict = []
        pp = pathlib.Path("Data")
        """Собираем данные из всех файлов в один список элементы которого словари из строк файлов"""
        for ff in pp.rglob("price_*.csv"):
            with open(ff, 'rt') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row.update([['файл', f'{ff.name}']])
                    readed_dict.append(row)
        print(readed_dict)
        """Создаем список словарей с новыми названиями"""
        for n in range(len(readed_dict)):
            new_data_list = []
            new_dict = {'Название': 0, 'Цена': 0, 'Фасовка': 0, 'Файл': 0}
            for n in range(len(readed_dict)):
                for key in readed_dict[n].keys():
                    if key == 'название' or key == 'продукт' or key == 'товар' or key == 'наименование':
                        new_dict.update({'Название': readed_dict[n][key]})
                    elif key == 'цена' or key == 'розница':
                        new_dict.update({'Цена': readed_dict[n][key]})
                    elif key == 'фасовка' or key == 'вес' or key == 'масса':
                        new_dict.update({'Фасовка': readed_dict[n][key]})
                    elif key == 'файл':
                        new_dict.update({'Файл': readed_dict[n][key]})
                new_data_list.append(new_dict)
                new_dict = {'Название': 0, 'Цена': 0, 'Фасовка': 0, 'Файл': 0}
        """Для более быстрой и удобной обработки создаем таблицу pandas"""
        dataf = pd.DataFrame(new_data_list)
        """Для расчета и добавления цены за кг приводим к формату float соответсвующе столбцы и добавляем столбец"""
        dataf['Цена'] = dataf['Цена'].astype(float)
        dataf['Фасовка'] = dataf['Фасовка'].astype(float)
        dataf['Цена за кг.'] = (dataf['Цена'] / dataf['Фасовка']).round(2)
        """Сортируем по цене за кг. в порядке возрастания"""
        dataf = dataf.sort_values('Цена за кг.')
        """Перезапишем уже отсортированную таблицу с новыми индексами в переменную self.data"""
        df1 = pd.Series(dataf['Название'], index=(f for f in range(len(dataf['Название']))))
        df2 = pd.Series(dataf['Цена'], index=(f for f in range(len(dataf['Цена']))))
        df3 = pd.Series(dataf['Фасовка'], index=(f for f in range(len(dataf['Фасовка']))))
        df4 = pd.Series(dataf['Файл'], index=(f for f in range(len(dataf['Файл']))))
        df5 = pd.Series(dataf['Цена за кг.'], index=(f for f in range(len(dataf['Цена за кг.']))))
        self.data = pd.DataFrame([df1, df2, df3, df4, df5]).T
        self.data.index.name = '№'
        return self.data


    def export_to_html(self, fname='output.html'):
        """Вывод в формат HTML в виде таблицы"""
        if fname != 'output.html':
            self.result_of_requests.to_html(fname)
        else:
            self.data.to_html(fname)


    def find_text(self, text):
        # Для поиска написанного с маленькой буквы
        text = text[0:(len(text)-1)]
        # Для поиска с большой буквы
        text2 = text.capitalize()
        mask = np.column_stack([self.data['Название'].str.contains(f'{text}')])
        mask2 = np.column_stack([self.data['Название'].str.contains(f'{text2}')])
        # создание таблицы по поиску с маленькой буквы
        output_info1 = self.data.loc[mask.any(axis=1)]
        # создания таблицы по поиску с заглавной буквы
        output_info2 = self.data.loc[mask2.any(axis=1)]
        # объединенная таблица отсортированныая по цене за 1 кг
        output_info = pd.concat([output_info1, output_info2])
        output_info = output_info.sort_values('Цена за кг.')
        diap = len(output_info['Цена'])
        output_info.index = range(0, diap)
        self.result_of_requests = pd.concat([self.result_of_requests, output_info])
        diap2 = len(self.result_of_requests['Цена'])
        self.result_of_requests.index = range(0, diap2)
        self.result_of_requests.index.name = '№'


        return self.result_of_requests


pm = PriceMachine()
print(pm.load_prices())
print("Доброго дня, пользователь!")
print("Для поиска продукта введите его название ниже.")
print("Для выхода из программы введите 'exit' или 'выход'.")

while True:
    inc_text = input("Введите название продукта, по которому хотите найти информацию: ")
    if inc_text == 'exit' or inc_text == 'выход':
        req_fname = input("Введите название файла (без расширения): ")
        pm.export_to_html(fname=f'{req_fname}.html')
        pm.export_to_html()
        break
    else:
        print(pm.find_text(inc_text))
        
print('Благодарю за использования программы! ')

