from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"

#---------------------UI SETUP---------------------#
window = Tk()
window.title("Flash Kards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

# Text on Canvas
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Butons
wrong_button_img = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_button_img, highlightthickness=0)
unknown_button.grid(column=0, row=1)
right_button_img = PhotoImage(file="./images/right.png")
known_button = Button(image=right_button_img, highlightthickness=0)
known_button.grid(column=1, row=1)


window.mainloop()
