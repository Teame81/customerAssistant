from tkinter import *

window = Tk()

window.title("Lollo <3")

lbl = Label(window, text="Hej min kära!", font=("Arial Bold", 50) )
lbl.grid(column = 0, row = 0)

window.geometry('900x100')

def btnClick():
    lbl.configure(text = " Jag älskar dig Lollo <3")

btn = Button(window, text = "Tryck här!", bg = "pink", fg = "red", command = btnClick)
btn.grid(column = 1 , row = 0)


window.mainloop()

