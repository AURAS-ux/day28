import math
from tkinter import *
from math import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
stop = False
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(txtTimer, text="00:00")
    checkmarkLabel.config(text="")
    titleLabel.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def StartTimer():
    global reps
    reps += 1
    if reps % 8 == 0:
        CountDownTimer(20 * 60)
        titleLabel.config(text="Break", foreground=RED)
    elif reps % 2 == 0:
        CountDownTimer(5 * 60)
        titleLabel.config(text="Break", foreground=PINK)
    elif reps % 2 != 0:
        CountDownTimer(25 * 60)
        titleLabel.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def CountDownTimer(counter):
    minutes = floor(counter / 60)
    seconds = counter % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(txtTimer, text=f"{minutes}:{seconds}")
    if counter > 0:
        global timer
        timer = window.after(10, CountDownTimer, counter - 1)
    else:
        StartTimer()
        checkmarks = ""
        work_sessions = math.floor(reps / 2)
        for i in range(work_sessions):
            checkmarks += "✓"
        checkmarkLabel.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(background=YELLOW, width=400, height=450)
window.resizable(False, False)

tomatoPNG = PhotoImage(file="tomato.png")

titleLabel = Label(background=YELLOW, text="TIMER", font=(FONT_NAME, 50, "bold"), fg=GREEN)
titleLabel.place(x=100, y=0)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomatoPNG)
txtTimer = canvas.create_text(100, 130, text="", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.place(x=100, y=70)

statButton = Button(text="Start", font=(FONT_NAME, 14, "normal"), command=StartTimer)
statButton.place(x=40, y=360)

stopButton = Button(text="Reset", font=(FONT_NAME, 14, "normal"), command=resetTimer)
stopButton.place(x=300, y=360)

checkmarkLabel = Label(background=YELLOW, font=(FONT_NAME, 20, "bold"), fg=GREEN)
checkmarkLabel.place(x=160, y=380)
window.mainloop()
