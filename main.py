from tkinter import *
from tkinter import filedialog
global filename


window = Tk()
window.title("Text files")
window.geometry("600x600")
window.config(bg="dark blue")

#Lable for text area
l1 = Label(window, text="My weekend activities")
l1.pack()

# Name of textfile
filename = 'My_Weekend_activities.txt'

# Creating and defining the buttons
def clicked_create():
    global filename
    if filename == 'Weekend_activities.txt':
        filename = filedialog.asksaveasfile(mode='w')
    if filename != None:
        data = e1.get('1.0','end')
        filename.write(data)
button_create = Button(window, text="Create textfile", command=clicked_create).place(x=10, y=180)

def display_textfile():
    global filename
    filename = filedialog.askopenfile(mode='r')
    if filename != None:
        text = filename.read()
        e1.insert('0.0', text)
        e1.focus()
button_display = Button(window, text="Display", command=display_textfile).place(x=135, y=180)

def append():
    with open('Weekend_activities.txt', 'a') as text:
        text.write(e1.get('1.0','end'))

button_append = Button(window, text="Append Data", command=append).place(x=215, y=180)

def clear():
    e1.delete(1.0, END)
    e1.update()
button_clear = Button(window, text="Clear", command=clear).place(x=330, y=180)


def quit():
    window.destroy()
button_quit = Button(window, text="Quit", command=quit).place(x=395, y=180)


e1 = Text(window, height=8, width=40)
e1.pack()



window.mainloop()