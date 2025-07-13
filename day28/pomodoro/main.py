
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 7

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
from cProfile import label
from tkinter import *

window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=30, background=YELLOW)
window.minsize(height=500, width=600)
window.columnconfigure([0,1,2,3,4], weight=1)

canvas = Canvas(width=200, height=223, background=YELLOW, highlightthickness=0)
bgImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=bgImg)
timeText = canvas.create_text(100, 130, text="00:00", fill="white", font=("Arial", 35, "bold"))
canvas.grid(column=2, row=2)


title = Label(text="Timer", font=("Arial", 50, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=2, row=1)

checkmarks = ""

showCheckMark = Label(text=checkmarks, fg=GREEN, bg=YELLOW, font=("Arial", 20, "bold"))
showCheckMark.grid(column=2, row=3, pady=50)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
timer_id = None
pomodotoCount = 0

def count_down(count):
    global pomodotoCount, timer_id
    if count > 0:
        timer_id = window.after(1000, count_down, count-1)
        canvas.itemconfig(timeText, text=f"{count//60:02}:{count%60:02}")

    else:
        pomodotoCount += 1
        startCountDown()


    if pomodotoCount == 0 or pomodotoCount == 2 or pomodotoCount == 4 or pomodotoCount == 6:
        title.config(text="Work", fg=GREEN)
    elif pomodotoCount == 1 or pomodotoCount == 3 or pomodotoCount == 5:
        title.config(text="Break", fg=PINK)
    elif pomodotoCount == 7:
        title.config(text="Long Break", fg=RED)
    
    
    if pomodotoCount == 1 or pomodotoCount == 3 or pomodotoCount == 5 or pomodotoCount == 7:
        global checkmarks
        checkmarks = "✓" * (pomodotoCount // 2 + 1)
        showCheckMark.config(text=checkmarks)

    return

def startCountDown():
    global pomodotoCount
    if pomodotoCount == 0 or pomodotoCount == 2 or pomodotoCount == 4 or pomodotoCount == 6:
        count_down(WORK_MIN)
    elif pomodotoCount == 1 or pomodotoCount == 3 or pomodotoCount == 5:
        count_down(SHORT_BREAK_MIN)
    elif pomodotoCount == 7:
        count_down(LONG_BREAK_MIN)
    elif pomodotoCount == 8:
        title.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timeText, text=f"00:00")
        pomodotoCount = 0
        global checkmarks
        checkmarks = ""
        showCheckMark.config(text=checkmarks)
        return
    else:
        return
    
def resetCountDown():
    global pomodotoCount, timer_id
    pomodotoCount = 0
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timeText, text=f"00:00")
    global checkmarks
    checkmarks = ""
    showCheckMark.config(text=checkmarks)
    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None

    return

start_btn = Button(text="Start", command=startCountDown)
start_btn.grid(column=1, row=3, pady=50)

reset_btn = Button(text="Reset", command=resetCountDown)
reset_btn.grid(column=3, row=3, pady=50)

window.mainloop()