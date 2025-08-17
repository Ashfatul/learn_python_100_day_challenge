import pandas as pd
from tkinter import *
import random, time

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv('./data/french_words.csv')
learn = data.to_dict(orient='records')


window = Tk()
window.title('Flash')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file='./images/card_front.png')
card_back_image = PhotoImage(file='./images/card_back.png')
card = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0,column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))


def next_word():
    global learn
    word = random.choice(learn)
    
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=word['French'])

    time.sleep(3)
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=word['English'])

wrong_image = PhotoImage(file='./images/wrong.png')
unknown = Button(image=wrong_image, highlightthickness=0, command=next_word)
unknown.grid(row=1, column=0)


right_image = PhotoImage(file='./images/right.png')
known = Button(image=right_image, highlightthickness=0, command=next_word)
known.grid(row=1, column=1)

next_word()

window.mainloop()