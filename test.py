# Import the required library
'''
from tkinter import*

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Add a label widget
label1 = Label(win, text='Label1', bg = "black", font=("Calibri, 15"))
label1.grid(column=1, row=2)

label2 = Label(win, text='Label2', bg = "green",font=("Calibri, 15"))
label2.grid(column=3, row=5)

label3 = Label(win, text='Laasdsdadasasddabel3Laasdsdadasasddabel3Laasdsdadasasddabel3Laasdsdadasasddabel3', bg = "red",font=("Calibri, 15"))
label3.grid(column=5, row=8)

label4 = Label(win, text='Label4',bg = "white", font=("Calibri, 15"))
label4.grid(column=7, row=11)

# set size of the window and add row and column
win.rowconfigure(8, weight=3)
win.columnconfigure(11)

win.mainloop()
'''
import random

def select_two_random_elements(lst):
    if len(lst) < 2:
        return None  # Not enough elements in the list

    return random.sample(lst, 2)

# Example usage:
my_list = [1, 2, 3]
selected_elements = select_two_random_elements(my_list)
print("Selected elements:", selected_elements)