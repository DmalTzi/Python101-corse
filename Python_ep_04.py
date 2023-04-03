from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from datetime import datetime
import os
import csv

filetypes = (
        ('csv file', '*.csv'),
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

fontsR = ("Roboto Mono",10)

gui = Tk()
gui.geometry('500x700')
gui.title('โปรแกรมบันทึกรายรับรายจ่าย')

FR1 = ttk.LabelFrame(gui, text='entry area')
FR1.pack()

def saveFile():
    global path
    path = fd.asksaveasfilename(initialfile="Untitle", defaultextension=".csv", filetypes=filetypes)
    FN.config(text=f"{os.path.basename(path)}")
    LSt.config(text='')
    

BNF = ttk.Button(FR1, text="New file", command=saveFile)
BNF.grid(row=0, column=0)

def pathFile():
    global path
    path = fd.askopenfilename(title='Opne file',filetypes=filetypes)
    FN.config(text=f"{os.path.basename(path)}")
    LSt.config(text='')

BOF = ttk.Button(FR1, text="Open file", command=pathFile)
BOF.grid(row=1, column=0)

FR2 = ttk.LabelFrame(FR1, text='File Name')
FR2.grid(row=0,column=1,padx=20)
FN = ttk.Label(FR2, text='',font=fontsR)
FN.pack(ipadx=20)

LCat = ttk.Label(FR1, text='Catagory or menu',font=fontsR)
LCat.grid(row=2,column=0,sticky='e')
cat_String = StringVar()
ECat = ttk.Entry(FR1, textvariable=cat_String)
ECat.grid(row=2 ,column=1,ipadx=30,pady=5)

LAm = ttk.Label(FR1, text='Amount', font=fontsR)
LAm.grid(row=3, column=0, sticky='e')
Am_String = StringVar()
EAm = ttk.Entry(FR1, textvariable=Am_String)
EAm.grid(row=3, column=1,ipadx=30,pady=5)

LSt = ttk.Label(FR1, text='', foreground='green', font=fontsR)
LSt.grid(row=4, column=0,columnspan=2, pady=5)

def saveData():
    try:
        Cat_data = cat_String.get()
        Am_data = int(Am_String.get())

        timed = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        data = timed,Cat_data,Am_data
        try:
            with open(path, 'a', encoding='utf-8') as file:
                fw = csv.writer(file)
                fw.writerow(data)
                cat_String.set('')
                Am_String.set('')
                LSt.config(text='Data has saved')
        except Exception as e:
            print(e)
            messagebox.showwarning(title='Path Now found', message='Please select path')
    except Exception as e:
        print(e)
        messagebox.showerror(title='Type Error', message='Entry only int')

BAdd = ttk.Button(FR1, text='Add data', command=saveData)
BAdd.grid(row=5, column=0,columnspan=2, ipadx=20)

FR3 = ttk.Labelframe(gui, text='Info')
FR3.pack()

def showInfo():
    LSt.config(text='')
    If.delete('1.0',END)
    path = fd.askopenfilename(title='Opne file',filetypes=filetypes)
    # path = os.path.basename(path)
    with open(path, 'r', encoding='utf-8') as file:
        frcsv = csv.reader(file)
        data = list(frcsv)
        for i in data:
            If.insert(END,i)
            If.insert(END,'\n')
        

BSIf = ttk.Button(FR3, text='Open file to show',command=showInfo)
BSIf.grid(row=0, column=0, sticky='w', padx=10)

If = Text(FR3, width=45, height=10, font=fontsR)
If.grid(row=1, column=0, sticky='nsew')

IfSc = ttk.Scrollbar(FR3, orient='vertical',command=If.yview)
IfSc.grid(row=1, column=1, sticky='ns')
If['yscrollcommand'] = IfSc.set


gui.mainloop()