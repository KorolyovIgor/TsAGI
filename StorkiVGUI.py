import os
from tkinter import filedialog as fd
from tkinter import Tk
from tkinter import Button
from tkinter import Label

def dobav(search, znd, index = 0):
    if search in line:
##        print(lines.index(line), line, end='')
        lines.insert(lines.index(line)+index, znd)
#
def button_clicked():
    print("Hello World!")

#
def close():
    root.destroy()
    root.quit()

root = Tk()
#root.title("Hello World!")
#root.geometry('300x40')
#button = Button(root, text="Press Me", command=button_clicked)
#button.pack(fill=BOTH)
#root.protocol('WM_DELETE_WINDOW', close)
NC = fd.askdirectory()
##fd.destroy()
##fd.quit()

##NC = input('Введите адрес папки с NC программами: ')



NCSname = 'ncprogramms_shtorki' # Название папки с изменнеными файлами
if not os.path.isdir(os.path.join(NC, NCSname)): # Создание папки для изменненых копий
    NCS = os.mkdir(os.path.join(NC, NCSname))

names = os.listdir(NC) # Возвращает имена файлов в папке 
nameswo = []
for name in names:          # Цикл который отделяет .mpf от файлов если он имеется
    if name.endswith('.mpf'):
        name1 = name.replace('.mpf', '')
        nameswo.append(name1)

for filename in nameswo:
    s = open(os.path.join(NC, filename+'.mpf'), 'r')
    lines = s.readlines()
    for line in lines:
        dobav('G0 X', 'M69\n', 1)
    for line in lines[::-1]:
        dobav('M09', 'M68\n')
    s2 = open(os.path.join(NC, NCSname, filename+'_st.mpf'), 'w') 
    s2.write(''.join(lines))
    s2.close()
    s.close()

##print(f'Программы перезаписаны с изменениями в папку {NCSname}')

root.title('Завершение')
lbl = Label(root, text = f'Программы перезаписаны с изменениями в папку {NCSname}')
root.geometry('450x50')
button = Button(root, text='Ok', command=close)
lbl.pack()
button.pack()
root.protocol('WM_DELETE_WINDOW', close)
root.mainloop()


