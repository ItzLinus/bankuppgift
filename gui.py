from tkinter import *

window = Tk()
window.title("Bank UI")
lblwidth = 700
window.geometry('500x600')
window.configure(bg="seashell2")


lbl1 = Label(window, text="▶ B͏a͏n͏k͏ o͏f͏ J͏a͏p͏a͏n͏ ◀", bg="seashell2", fg="sandy brown", font="Helvetica 16 bold")
lbl1.pack()

#txt = Entry(window,width=20)
#txt.pack()

def saldo():

    lbl1.configure(text="This ur saldo==¤)=")

btn = Button(window, text="Saldo", command=saldo)

window.mainloop()