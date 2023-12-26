from tkinter import *
from tkinter import messagebox
import pandas as pd
from random import choice

#-----------------Global Dictionaries-----------------#
words_to_learn = {}
current_card = {}
#--------------------CONSTANTS---------------------#
BACKGROUND_COLOR = "#B1DDC6"
#-------------Try Exceptions Edge Cases-----------#
window = Tk()
def is_csv_empty(file_path):
    try:
        data = pd.read_csv("./data/words_to_learn.csv")
        return data.empty
    except pd.errors.EmptyDataError:
        return True # File is empty if EmptyDataError is triggered

try:
#-------------------LOAD CSV DATA------------------#
    if is_csv_empty("./data/words_to_learn.csv"):
        messagebox.showinfo(title="Oops!", message="You have learned all the words on this Dictionary!\nTry a new set or a new Language!")
        window.destroy()
    else:
        pass
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")
    
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


def is_known():
    words_to_learn.remove(current_card)
    if not words_to_learn:
        data = pd.DataFrame(words_to_learn)
        data.to_csv("./data/words_to_learn.csv", index=False)
        messagebox.showinfo(title="YOU DID IT!", message="You have learned all the words on this Dictionary! Try a new set or a new Language!")
        window.destroy()
    data = pd.DataFrame(words_to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


#---------------------UI SETUP---------------------#

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
known_button = Button(image=right_button_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()
window.mainloop()
