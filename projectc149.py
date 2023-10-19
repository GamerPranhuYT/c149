from tkinter import *

import random

root = Tk()

root.title("Random Word Generator")
root.geometry("500x500")
root.configure(background="yellow")

label1 = Label(root)

def random_word():
    alpha_list = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G" "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    random_number1 = random.randint(0, 25)
    random_number2 = random.randint(0, 25)
    random_number3 = random.randint(0, 25)
    random_number4 = random.randint(0, 25)
    random_number5 = random.randint(0, 25)
    print(random_number1, random_number2, random_number3, random_number4, random_number5)
    random_alpha1 = alpha_list[random_number1]
    random_alpha2 = alpha_list[random_number2]
    random_alpha3 = alpha_list[random_number3]
    random_alpha4 = alpha_list[random_number4]
    random_alpha5 = alpha_list[random_number5]
    label1["text"] = random_alpha1+random_alpha2+random_alpha3+random_alpha4+random_alpha5

btn = Button(root, text="Random Word Generator", command=random_word, bg="blue")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()