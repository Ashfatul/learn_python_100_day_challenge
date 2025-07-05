# import tkinter

# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(800, 500)

# label = tkinter.Label(text="Hello there", font=("italic", 20, "bold"))
# label.pack(side="right", expand=1)



# infinity args

# from ast import arg


# def sum(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total




# print(sum(1,5,2))


# print(sum(1,5,2,5,9,2))


# print(sum(1,5,2,4,3))


# print(sum(1,5,2,4,3,6,7,8,9,10))







from cProfile import label
from tkinter import *

window = Tk()
window.title("Minutes To Second Converter")
window.minsize(400, 500)
window.config(padx=50, pady=50)

# label = Label(text="Hello there", font=("italic", 20, "bold"))
# label.pack(side="left", expand=1)

# count = 0
# def clicked():
#     global count
#     label.config(text=f"clicked {count} times")
#     count += 1

# text = Entry()
# text.pack(side="left", expand=1)

# value =""
# def getValue():
#     value = text.get()
#     label.config(text=value)

# button = Button(text="Click Me", command=getValue)
# button.pack(side="right", expand=1)

min_input = Entry()
min_input.grid(column=1, row=0)
min_input.config(validate="key", validatecommand=(window.register(lambda P: P.isdigit()), '%P'))

text1 = Label()
text1.grid(column=2, row=0)
text1.config(text="Minutes")


text2 = Label()
text2.grid(column=1, row=1)
text2.config(text="Is Equal To")

sec = 0
text3 = Label()
text3.grid(column=2, row=1)
text3.config(text=f"{sec} Seconds")


def calc():
    input_val = min_input.get()
    res = int(input_val) * 60
    text3.config(text=f"{res} Seconds")

calculate = Button()
calculate.grid(column=1, row=2)
calculate.config(text="Calculate", command=calc)


window.mainloop()