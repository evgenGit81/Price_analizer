# Price_analizer
Запускающий файл: project.py

Требования.
Программа написана на python 3.10
Требуемые библиотеки перечислены в файле requeremnts.txt

Назначение.
1) Программа предназначена для сбора и сведения данных из прайслистов файлов с расширением .csv (файлы должны иметь вид - price_*.csv, где "*"
любые символы и лежать в папке Data в коталге,где лежит программа) в одну общую таблицу, которая сохранятеся в файле output.html.
В выходной таблице добавляются столбцы с ценой за 1 кг и названием файлов из которых были взяты данные.
2) Поиска информации по названию продукта.
3) Сведение всех запросов по продуктам в одну таблицу с сортировкой по цене для каждого запроса.
4) Сохранение результирующей таблицы запросов с названием файла от пользователя в формате html/
   
   Пример использования.
   
   Доброго дня, пользователь!
Для поиска продукта введите его название ниже.
Для выхода из программы введите 'exit' или 'выход'.
Введите название продукта, по которому хотите найти информацию: филе
                    Название    Цена Фасовка          Файл Цена за кг.
№                                                                     
0       Филе пангасиуса б/ш     92.0     1.0   price_5.csv        92.0
1       Филе пангасиуса б/ш    287.0     3.0   price_7.csv       95.67
2       Филе пангасиуса б/ш    405.0     4.0   price_2.csv      101.25
3       Филе пангасиуса б/ш    103.0     1.0  price_jj.csv       103.0
4        Филе минтая б/ш б/к   535.0     4.0   price_0.csv      133.75
..                       ...     ...     ...           ...         ...
71          Филе судака н/ш   4015.0     3.0   price_0.csv     1338.33
72  Щука х/к филе с насечкой  4036.0     3.0   price_3.csv     1345.33
73  Щука х/к филе с насечкой  2691.0     2.0   price_7.csv      1345.5
74          Филе судака н/ш   2762.0     2.0   price_1.csv      1381.0
75          Филе судака н/ш   1395.0     1.0   price_2.csv      1395.0

[76 rows x 5 columns]
Введите название продукта, по которому хотите найти информацию: выход
Введите название файла (без расширения): результат по филе
Благодарю за использования программы!


Приятного использования!
