from tkinter import*
from tkinter.simpledialog import*
window = Tk()
window.title("Klubnichka.script//V1.0.1")
c=Canvas(window, width=400,height=400, bg='white')
mas=[]
def Klubnika():
    for i in range(5):
        a = int(askstring('1,2,3,4,5','mas['+str(i)+']='))
    for i in range(5):
        Lbox.insert(END,mas[i])
from tkinter import*
window=Tk()
mas=[]
Lbl=Label(text='Write a massive')
Lbl.pack()
Ent=Entry()
Ent.pack()
Btn=Button(text='Write a massive')
Btn.pack()
Lbox=Listbox()
Lbox.pack()
mas=[]
def Malinka():
    a = Ent.get()
    mas = a.split()
    for i in mas:
        Lbox.insert(END,int)
#klubnichka.script//.py
print("Klubnichka.script1.0.1//")
print("Hello world")
num = int(input())
print(oct(num))
a = int(input(""))
b = int(input(""))
if a==b:
    print(True)
else:
    print(False)
#finction V2:
if a is b:
    print("a is b --",True,"//")
else:
    print("a is b -- ",False,"//")



