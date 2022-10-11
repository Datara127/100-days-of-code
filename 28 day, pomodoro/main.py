from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    checkbox_label.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #

def count_start():
    global reps
    marks = ""
    for _ in range(reps // 2):
        marks += "✓"
    checkbox_label.config(text=marks)
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
        reps = 1
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        count_start()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=100, padx=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, font=(FONT_NAME, 32, "bold"), fill="white", text="00:00")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

checkbox_label = Label(font=(FONT_NAME, 32), bg=YELLOW, fg=GREEN)
checkbox_label.grid(row=3, column=1)

button_start = Button(text="start", highlightthickness=0, command=count_start)
button_start.grid(row=2, column=0)

button_reset = Button(text="reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=2, column=2)

window.mainloop()
