""" выбора файла в дирректории. Возвращает результат чтения списком строк """

from tkinter.filedialog import askopenfile

def choose_file():

    # задаем разрешенный формат файла
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    # вызываем окно выбора файла и открываем файл
    file = askopenfile(
        title="Выбрать файл",
        initialdir='/',
        filetypes=filetypes
    )

    if file:
        # чтение текстового файла
        return file.read()

    # если проблема с чтением файла: сообщение об ошибке
    else:
        from tkinter.messagebox import showerror
        showerror(title="Ошибка", message="Ошибка в чтении файла")