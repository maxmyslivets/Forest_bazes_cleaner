""" Скрипт для выборочной очистки файла базы данных кадастровой службы """

import tkinter as tk
from tkinter import Label, ttk
from tkinter.constants import END
from chooseFile import choose_file

# создание класса окна приложения
class App(tk.Tk):

    # изначально запускаемая функция по умолчанию
    def __init__(self):
        super().__init__()

        # конфигурация окна
        self.title('Чистка файла базы')
        #self.geometry('300x250')
        
        # создание меню программы
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # создание меню файла
        fileMenu = tk.Menu(
            menubar,
            tearoff=0
        )

        self.textFile = []

        # добавление кнопок в меню файла
        fileMenu.add_command(
            label='Открыть файл',
            command = self.readFile
        )
        fileMenu.add_separator()
        fileMenu.add_command(
            label='Выход',
            command=self.destroy
        )

        menubar.add_cascade(
            label="File",
            menu=fileMenu
            )

        """
        # текстовое поле вывода файла
        textLabel = tk.Text(width=300, height=200)
        textLabel.pack(side='left')
        scroll = tk.Scrollbar(command=textLabel.yview)
        scroll.pack(side='left', fill='y')
        textLabel.config(yscrollcommand=scroll.set)
        """
        
        # конфигурация сетки
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(3, weight=1)

        # поля меток
        labelInfo = ttk.Label(self, text='Ввод номеров KV через запятую')
        labelInfo.grid(column=0, row=0, columnspan=2, sticky=tk.W, padx=5, pady=5)
        labelKV = ttk.Label(self, text='KV=')
        labelKV.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        # поле ввода номеров KV
        insertKVNumbers = ttk.Entry(width=40)
        insertKVNumbers.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        insertButton = ttk.Button(
            text = 'Убрать',
            command = print(self.textFile, insertKVNumbers.get())
        )
        insertButton.grid(column=3, row=1, sticky=tk.E, padx=5, pady=5)


    # чтение файла
    def readFile(self):
        self.textFile.append(str(choose_file()))
        

# запуск приложения
if __name__ == "__main__":
    app = App()
    app.mainloop()

