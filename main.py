from tkinter import *
from tkinter import colorchooser
from perceptron import *
root = Tk()
root.title("Color")
root.geometry("800x800")


perceptron = Perceptron()
perceptron.training()


def color():
    my_color = colorchooser.askcolor()
    color = list(my_color[0])
    perceptron.normalizar(color)
    pick = perceptron.result(color)
    my_label = Label(root,text=my_color).pack(pady=10)
    my_label2 = Label(root,text=f"You picked  {pick[0]}", font=("Helvetica",32),bg=my_color[1]).pack()

my_button= Button(root, text="Pick a color", command=color).pack()




root.mainloop()