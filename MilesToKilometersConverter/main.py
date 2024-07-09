from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(width=500, height=300)

input = Entry()
output = Label(text="0")
miles_label = Label(text="miles")
equal_to_label = Label(text="is equal to")
km_label = Label(text="Km")
calculate_button = Button(text="Calculate")

input.grid(column=1, row=0)
output.grid(column=1, row=1)
miles_label.grid(column=2, row=0)
equal_to_label.grid(column=0, row=1)
km_label.grid(column=2, row=1)
calculate_button.grid(column=1, row=2)

def calculate():
    miles = int(input.get())
    km = miles*1.6
    output.config(text=str(km))

calculate_button.config(command=calculate)

window.mainloop()