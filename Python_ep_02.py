from tkinter import *
from tkinter import ttk
from tkinter import messagebox

amount = 0

def withdraw():
    global amount
    decrease = T3.get(1.0,'end-1c')
    if int(decrease) > 0:
        amount -= int(decrease)
        if amount < 0:
            amount += int(decrease)
            messagebox.showwarning(title="Not enough money",message="your withdraw more than your money in bank")
        amountL1.config(text=amount)
    else:
        messagebox.showwarning(title="Type Error",message="please enter only number with out -,+,*,/")
        

def topup():
    global amount
    increase = T4.get(1.0,"end-1c")
    amount = amount + int(increase)
    amountL1.config(text=amount)
    messagebox.showinfo(title="Successfully",message="You topup is successfully")
    


GUI = Tk()
GUI.title('Bank')
GUI.geometry('500x500')

L1 = Label(GUI,text="This is bank").pack()

FB1 = Frame(GUI)
FB1.pack(pady=10)

L2 = Label(FB1, text='How much money in bank')
L2.pack()
amountL1 = Label(FB1, text=amount,fg='green')
amountL1.pack()

# =============================

FB2 = Frame(GUI)
FB2.pack(pady=20)

L3 = Label(FB2, text="withdraw",fg="red")
L3.pack(ipady=0)

T3 = Text(FB2, height=1, width=20)
T3.pack()

B3 = ttk.Button(FB2, text="withdraw", command=withdraw)
B3.pack(ipadx=20,pady=5)

# ==========================

FB3 = Frame(GUI)
FB3.pack(pady=10)

L4 = Label(FB3, text="Top up", fg="green")
L4.pack()

T4 = Text(FB3, height=1, width=20)
T4.pack()

B4 = ttk.Button(FB3, text="withdraw", command=topup)
B4.pack(ipadx=20,pady=5)



GUI.mainloop()
