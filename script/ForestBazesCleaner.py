from tkinter.filedialog import askopenfile
import time

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

textFile = choose_file()
print(textFile)

KVNumbers = input('Введите номера KV через запятую: ').split(',')

textFileList = str(textFile).split('\n\n')
#print(textFileList)

KVList = []

for i in textFileList:
    for kv in KVNumbers:
        if 'KV='+kv+'\t' in i:
            KVList.append(i)

for i in KVList:
    if i in textFileList:
        textFileList.remove(i)

with open('newBazeFile_{}.txt'.format(str(round(time.time()))), 'w') as newFile:
    for i in textFileList:
        newFile.write(i+"\n\n")

#print(textFileList)