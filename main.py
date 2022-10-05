from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
all_checkmarks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    global all_checkmarks
    all_checkmarks = ""
    checkmark_label.config(text=all_checkmarks)
    canvas.itemconfig(canvas_timer, text="00:00")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global rep
    rep += 1
    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        timer_label.config(fg=RED, text="Break")
    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        timer_label.config(fg=PINK, text="Break")
    else:
        count_down(WORK_MIN*60)
        timer_label.config(fg=GREEN, text="Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        global rep
        if rep % 2 == 0:
            global all_checkmarks
            all_checkmarks += "✅"
            checkmark_label.config(text=all_checkmarks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.minsize(width=200, height=224)
window.title("Pomodoro")
window.config(padx=80, pady=80, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="./pomodoro-app/tomato.png")
canvas.create_image(100, 112, image=img)
canvas_timer = canvas.create_text(100, 130, text="00:00", fill="white",
                                  font=(FONT_NAME, 26, "bold"))
canvas.grid(column=2, row=2)

timer_label = Label(fg=GREEN, text="Timer", bg=YELLOW,
                    font=(FONT_NAME, 26, "bold"))
timer_label.grid(column=2, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

checkmark_label = Label(bg=YELLOW)
checkmark_label.grid(column=2, row=4)

window.mainloop()
