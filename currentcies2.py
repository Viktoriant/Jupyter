# Попытка сделать просмотр курса валют в удобном виде

import tkinter as tk               # импортировать модуль Tkinter
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import pandas as pd 
import requests
import xmltodict

# Создание главного окна
window = tk.Tk()                      # переменной окна window 
window.geometry("700x700")
window.title("Программа анализа XML файлов")

# Создание меток вывода
label_00 = tk.Label(text = "Файл:")
label_00.grid(row=0, column=0, padx=10, pady=10, sticky='e') # Менеджер .grid()

label_01 = tk.Label(text = "")
label_01.grid(row=0, column=1, sticky="w")  # Параметр sticky="" n e s w

label_10 = tk.Label(text = "Строк:")
label_10.grid(row=1, column=0, padx=10, pady=10, sticky='e')

label_11 = tk.Label(text = "")
label_11.grid(row=1, column=1, sticky="w")

label_20 = tk.Label(text = "Столбцов:")
label_20.grid(row=2, column=0, padx=10, pady=10, sticky='e')

label_21 = tk.Label(text = "")
label_21.grid(row=2, column=1, sticky="w")

# Создание текстового вывода с прокруткой
output_text = st(height = 30, width = 60)
output_text.grid(row=3, column=1, padx=5, pady=10, sticky='w')


# Диалог открытия файла
def do_dialog():
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    data = xmltodict.parse(response.content)
  
    my_array = []
    i = 1
    
    for item in data['ValCurs']['Valute']:        
        my_set = [item['CharCode'], item['Name'], item['Value'],'\n'];
        my_array.append(my_set)         
        l = len(my_set[1])
        n = 45 - l
        l2 =" " * n
        output_text.insert(tk.END,  my_set[0] + ' ' +  my_set[1] + l2 +  my_set[2] + '\n')         
        i = i +1           
    label_11['text'] =str(i)
    return url
    
# Обработчик нажатия кнопки
def process_button():   
    file_name = do_dialog()
    label_01['text'] = file_name
    label_21['text'] = 3
   
    mb.showinfo(title=None, message="Готово")
    
# Создание кнопки
button = tk.Button(window, text="Прочитать файл", command=process_button)
button.grid(row=4,column=1)

#Запуск цикла mainloop
window.mainloop()

