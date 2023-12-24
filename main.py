from tkinter import *
import pandas as pd
from random import choice

data = pd.read_csv("./data/french_words.csv")
words_to_learn = data.to_dict(orient="records")
current_card = {}
#--------------------CONSTANTS---------------------#
BACKGROUND_COLOR = "#B1DDC6"
#------------Cycle Words On Button Click-----------#
def next_card():
     global current_card, flip_timer
     window.after_cancel(flip_timer)
     current_card = choice(words_to_learn)  # Access kist to pick a random value. display value from french list by current_card["French"]
     canvas.itemconfig(card_title, text="French", fill="black")
     canvas.itemconfigure(card_word, text=current_card["French"], fill="black")
     canvas.itemconfig(card_background, image=card_front_img)
     flip_timer = window.after(3000, flip_card)  # Delay of 3 seconds before flipping card


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


#---------------------UI SETUP---------------------#
window = Tk()
window.title("Flash Kards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card) # Delay of 3 seconds before flipping card

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
# Card side attributes
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

# Text on Canvas
card_title = canvas.create_text(400, 150, text="placeholder", font=("Ariel", 40, "italic"))
card_word = cycle_words = canvas.create_text(400, 263, text="placeholder", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Butons
wrong_button_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)
right_button_img = PhotoImage(file="./images/right.png")
known_button = Button(image=right_button_img, highlightthickness=0, command=next_card)
known_button.grid(column=1, row=1)

next_card()
window.mainloop()
