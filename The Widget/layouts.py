from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)




window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=500)
window.config(padx=300, pady=300 )

#Label
my_label = Label(text="I am a Label", font=("Arial", 24,"bold"))
my_label.config(text="New Text")
my_label.grid(column= 0, row=0)

#button
button = Button(text="Click me", command=button_clicked)
button.grid(column= 1, row=1)

new_button = Button(text="new_button")
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column= 3, row=2)
window.mainloop()


