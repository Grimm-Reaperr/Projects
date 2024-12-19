from tkinter import *

def button_clicked():
    print("Button Clicked")
    new_text = int(input.get())
    result = str(new_text * 1.60934)
    output.config(text=result)
    print(result)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=200)
window.config(padx=10,pady=10)

input = Entry(width=10)
input.grid(column=1, row=0)
print(input.get())


lable_miles = Label(text="Miles")
lable_miles.grid(column=2, row=0)

lable_equal = Label(text="is equal to")
lable_equal.grid(column=0, row=1)

output = Label(text="0")
output.grid(column=1, row=1)

lable_km = Label(text="Km")
lable_km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1,row=2)








window.mainloop()
