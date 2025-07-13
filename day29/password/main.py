import tkinter as tk
from tkinter import messagebox
import pyperclip
from passwordGen import *

spacer = "    ||    "


window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, anchor="center", image=logo_img)
canvas.grid(column=1, row=0)

webLabel = tk.Label(text="Website:")
webLabel.grid(column=0, row=1)

webUrl = tk.Entry(width=40)
webUrl.grid(column=1, row=1, columnspan=2)
webUrl.focus()


emailLabel = tk.Label(text="Email/Username:")
emailLabel.grid(column=0, row=2)

emailAddr = tk.Entry(width=40)
emailAddr.grid(column=1, row=2, columnspan=2)
emailAddr.insert(0, "ashfatul@gmail.com")

passLabel = tk.Label(text="Password:")
passLabel.grid(column=0, row=3)

passInput = tk.Entry(width=25)
passInput.grid(column=1, row=3)

def generateNewPass():
    passInput.delete(0, tk.END)
    passInput.insert(0, genPass)

passGen = tk.Button(text="Gen Password", width=10, command=generateNewPass)
passGen.grid(column=2, row=3)

def storeData():
    if (len(webUrl.get()) > 0 and len(emailAddr.get()) > 0 and len(passInput.get()) > 0):
        if messagebox.askyesno(title="Sure to save?", message=f"You are about to save\nWebsite: {webUrl.get()}\nEmail: {emailAddr.get()}\nPassword: {passInput.get()}"):
            dataFile = open('./data.txt', 'a')
            dataFile.write(spacer.join([webUrl.get(), emailAddr.get(), passInput.get()]) + "\n")
            dataFile.close()
            webUrl.delete(0, tk.END)
            pyperclip.copy(passInput.get())
            passInput.delete(0, tk.END)

            messagebox.showinfo(title='Saved', message='Your password has been saved successfully \n and COPID TO YOUR CLIPBOARD :)')
    else:
        messagebox.showerror(title="Missing Data", message="Check if all fileds are filled")

    webUrl.focus()

storeBtn = tk.Button(text="Add", width=36, command=storeData)
storeBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()