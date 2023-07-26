from tkinter import *
import random
import pandas

# ---------------------------- CONSTANTS ------------------------ #
BACKGROUND_COLOR = "#B1DDC6"
FR = ("Ariel", 40, "italic")
FR_TEXT = ("Ariel", 60, "bold")
random_choice = {}
data_dict = {}
# ---------------------------- FUNCTIONALITY ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global random_choice, flip_timer
    window.after_cancel(flip_timer)
    random_choice = random.choice(data_dict)
    fr_word = random_choice["French"]
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(fr_text, text=fr_word, fill="black")
    canvas.itemconfig(fr, text="French", fill="black")
    flip_timer = window.after(4000, func=flip)

def is_known():
    data_dict.remove(random_choice)
    df = pandas.DataFrame(data_dict)
    df.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

def flip():
    global random_choice
    en_word = random_choice["English"]
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(fr, text="English", fill="white")
    canvas.itemconfig(fr_text, text=f"{en_word}", fill="white")
# ---------------------------- SAVING PROGRESS ------------------------------- #


# ---------------------------- UI ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(4000, func=flip)
#canvas
old_image = PhotoImage(file="../flash-card-project-start/images/card_front.png")
new_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(height=526, width=800)
canvas_image = canvas.create_image(400, 268, image=old_image)
fr = canvas.create_text(400, 150, text="French", font=FR)
fr_text = canvas.create_text(400, 263, text="", font=FR_TEXT)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)


#buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()



