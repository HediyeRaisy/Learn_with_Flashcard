from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"


try:
    data = pandas.read_csv("./data/to_learn.csv.csv").to_dict('records')
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv").to_dict('records')
rand = 0
def check():
    global rand
    data.remove(data[rand])
    to_learn = pandas.DataFrame(data)
    to_learn.to_csv("./data/to_learn.csv",index=False)
    clicked()


def clicked():

    global flip_timer,rand

    # print(data)
    window.after_cancel(flip_timer)
    rand = random.randint(1, 102)
    # print(data)
    # for key in record[rand]:
    canvas.itemconfig(word, text=f"{data[rand]['French']}",fill="black")
    canvas.itemconfig(title, text="French",fill="black")
    canvas.itemconfig(img, image=card_front)
    flip_timer = window.after(3000, flip , rand)

def flip(rand):

    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=f"{data[rand]['English']}",fill="white")
    canvas.itemconfig(img,image=card_back)
# ----------------------------------User Interface------------------------------------#
window = Tk()
window.title("Flashy")
window.after(1000,clicked)
flip_timer = window.after(3000,flip,rand)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
img = canvas.create_image(404, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"), fill="black")
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)
right_img = PhotoImage(file="./images/right.png")
check_button = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=check)
check_button.grid(row=1, column=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=clicked)
wrong_button.grid(row=1, column=0)

card_back = PhotoImage(file="./images/card_back.png")


window.mainloop()
