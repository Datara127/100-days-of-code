from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/en_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)


def flip_card():
    canvas.itemconfig(card_title, text="Russian", fill="white")
    canvas.itemconfig(card_word, text=current_card["Russian"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknown_image = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=unknown_image, highlightthickness=0, command=flip_card)
unknown_btn.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_btn = Button(image=check_image, highlightthickness=0, command=next_card)
check_btn.grid(row=1, column=1)
next_card()

window.mainloop()
