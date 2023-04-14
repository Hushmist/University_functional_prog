import datetime
import numpy as np
from tkinter import *
from PIL import Image,ImageTk

def _calendar():
    now_date = datetime.datetime.now()
    date_list = np.array([now_date])
    print(date_list)

    date_list = np.append(date_list, now_date.day)
    print(date_list)

    date_list = np.append(date_list, now_date.hour)
    date_list = date_list.reshape(3,1)
    print(date_list)

    date_list = np.append(date_list, datetime.datetime(2023, 1, 1))
    print(date_list.any())

    new_date_list = date_list.copy()
    print(new_date_list)

    print(now_date.timestamp())

# _calendar()

def load_image(_image):
    _image = Image.open(_image)
    _image = _image.resize((300, 300), Image.ANTIALIAS)
    _image = ImageTk.PhotoImage(_image)
    return _image

def my_logo2():
    root = Tk()
    root.title("Hushmist")
    root.geometry("800x600")

    canvas = Canvas(root, width=800, height=600)
    canvas.pack()

    php = load_image("./data/php.png")
    laravel = load_image("./data/laravel2.png")

    canvas.create_image(300, 200, image=php)
    canvas.create_image(500, 400, image=laravel) 

    text_label = Label(root, text="Hushmist", background="#ADD8E6", foreground="#0000FF", font=("Arial", 32), padx=10)
    text_label.place(relx=0.5, rely=0.5, anchor="center") # cen

    root.mainloop()

my_logo2()
