from tkinter import *
from tkinter import ttk
# Global vars
tab_num = 1

# Window
window = Tk()
window.title("Lollo <3")
window.geometry('900x150')

def btn2Click():
    global tab_num
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text = "Hamster " + str(tab_num))
    tab_num = tab_num + 1
    

btn2 = Button(window, text = "Add tabs", bg = "grey", fg = "black", command = btn2Click)
btn2.grid(column = 0 , row = 0)


# Tabs
tab_control = ttk.Notebook(window)
tab_control.pack()
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text = "Hamster " + str(tab_num))
tab_num = tab_num + 1
tab_control.add(tab2, text = "Hamster " + str(tab_num))
tab_num = tab_num + 1

# The label
lbl = Label(tab1, text="Hej min kära!", font=("Arial Bold", 50) )
lbl.grid(column = 0, row = 0)

# Buttons
def btnClick():
    lbl.configure(text = " Jag älskar dig Lollo <3 " + txt.get())
    txt.insert(INSERT,"LAMBI")


btn = Button(tab1, text = "Tryck här!", bg = "pink", fg = "red", command = btnClick)
btn.grid(column = 1 , row = 0)

def btn2Click():
    global tab_num
    tab = ttk.Frame(tab_control)
    tab_control.add(tab, text = "Hamster " + str(tab_num))
    tab_num = tab_num + 1
    

btn2 = Button(window, text = "Add tabs", bg = "grey", fg = "black", command = btn2Click)
btn2.grid(column = 0 , row = 0)

# Text entry
txt = Entry(tab1, width = 30, text = "Test")
txt.grid(column = 1, row = 2)
txt.focus()

#The loop


window.mainloop()