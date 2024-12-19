# def add(*args):
#     add = 0
#     for n in args:
#         add += n
#     return add
#
# print(add(1,2,3))

# def calculate(n,**kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# calculate(5, add= 3, multiply = 5)

# class Car:
#
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#
# my_car = Car(make="Nissan")
# print(my_car.make)
def test(*args):
    print(args)

test(1,2,3,5)



import tkinter
window = tkinter.Tk()
window.title("My First GUI ")
window.minsize(width=500, height=300)


lable = tkinter.Label(text="My first Label", font= ("Arial", 20, "bold"))
lable.pack()

#lable["text"] = "New_text"
#lable.config(text="New text ")
def button_clicked():
    print(" I got clicked")
    data = input.get()
    lable["text"] = data

button = tkinter.Button(text= "Click me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=10)
input.insert(tkinter.END, string="here is the text")
input.pack()

text = tkinter.Text(height=15, width=15)
text.focus()
text.insert(tkinter.END,  " Long fucking essay" )
print(text.get("1.0", tkinter.END))
text.pack()

def spin_box():
    print("Spin Box")

spin = tkinter.Spinbox(from_=0 , to=10 ,width=5 , command=spin_box)
spin.pack()

def check_button_used():
    print(checked_state.get())
checked_state = tkinter.IntVar()
checked_button = tkinter.Checkbutton(text="Is On ? ", variable=checked_state , command=check_button_used())
checked_state.get()
checked_button.pack()

def radi0_button_used():
    print(radio_state.get())
radio_state = tkinter.IntVar()
radio_button1 = tkinter.Radiobutton(text="option1", value=1, variable=radio_state,command=radi0_button_used())
radio_button2 = tkinter.Radiobutton(text="option2",value=2 ,variable=radio_state,command=radi0_button_used())
radio_button1.pack()
radio_button2.pack()






window.mainloop()
