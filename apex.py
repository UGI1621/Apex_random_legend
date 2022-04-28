from tkinter import *
import random
from tkinter.font import BOLD
from PIL import ImageTk


def rand_choice():
    r_img = random.choice(img_list)
    canvas.itemconfig(canvas_img, image=r_img)


window = Tk()
window.title("Apex")
window.config(padx=10, pady=10, bg="darkred")

canvas = Canvas(window, height=800, width=800, bg="black")
canvas.pack()

img_main = ImageTk.PhotoImage(
    file=r"C:/Users/USER/OneDrive/Desktop/Self_study/Apex_random/logo.jpg")
canvas_img = canvas.create_image(400, 400, image=img_main)
canvas.create_text(400, 50, text="Random Legends", fill="red",
                   font=("a로케트", 20, BOLD))

img_list = []
for i in range(19):
    img = PhotoImage(
        file=f"C:/Users/USER/OneDrive/Desktop/Self_study/Apex_random/legend{i}.png")
    char_img = canvas.create_image(200, 200,)
    img_list.append(img)

button = Button(window, text="Who Is Campion", bg="red",
                fg='black', font=("a로케트", 15, BOLD), command=rand_choice)
button.place(x=303, y=700)


window.mainloop()
