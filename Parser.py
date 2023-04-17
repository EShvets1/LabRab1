import xlsxwriter
import os
from bs4 import BeautifulSoup #импортируем библиотеку BeautifulSoup
import requests #импортируем библиотеку requests

def parse():
    url = 'https://omsk.mlsn.ru/pokupka-nedvizhimost' #передаем необходимы URL адрес
    page = requests.get(url) #отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) #смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") #передаем страницу в bs4

    block = soup.findAll('div', class_='content-container') #находим  контейнер с нужным классом
    description = [] #информация о квартирах
    for data in block: #проходим циклом по содержимому контейнера
        if data.find(class_='btn-maps-button'):
            description.append(data.text)

    excel = xlsxwriter.Workbook("Kv.xlsx") #работа с таблицей
    ws = excel.add_worksheet()
    columns = 0 #столбцы в таблице
    row = 0 #строки в таблице
    for item in description:
        ws.write(row, columns, item)
        row += 1
    columns += 1
    row = 0

    excel.close()

os.system("Kv.xlsx")