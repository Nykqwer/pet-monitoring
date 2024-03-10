
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\pet-monitoring\added\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1032x655")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 655,
    width = 1032,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1032.0,
    655.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    19.9998779296875,
    425.00018310546875,
    647.9998404979706,
    427.00018298625946,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=727.0,
    y=425.0,
    width=284.0,
    height=72.66717529296875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=727.0,
    y=504.0,
    width=284.0,
    height=72.66717529296875
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    870.0,
    161.0,
    image=image_image_1
)

canvas.create_text(
    217.0,
    35.0,
    anchor="nw",
    text="Pet’s Information",
    fill="#0BBC8B",
    font=("RobotoRoman Bold", 34 * -1)
)

canvas.create_text(
    252.0,
    446.0,
    anchor="nw",
    text="Recommendation",
    fill="#0BBC8B",
    font=("RobotoRoman SemiBold", 26 * -1)
)

canvas.create_rectangle(
    697.0,
    73.66262817382812,
    699.0,
    585.3191528320312,
    fill="#EFEFEF",
    outline="")

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    175.0,
    146.0,
    image=image_image_2
)

canvas.create_text(
    118.0,
    140.0,
    anchor="nw",
    text="Nah I’d Win",
    fill="#030303",
    font=("RobotoRoman SemiBold", 20 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    508.0,
    146.0,
    image=image_image_3
)

canvas.create_text(
    451.0,
    140.0,
    anchor="nw",
    text="Maltese",
    fill="#030303",
    font=("RobotoRoman SemiBold", 20 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    508.0,
    254.0,
    image=image_image_4
)

canvas.create_text(
    451.0,
    248.0,
    anchor="nw",
    text="60 KG",
    fill="#030303",
    font=("RobotoRoman SemiBold", 20 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    176.0,
    254.0,
    image=image_image_5
)

canvas.create_text(
    119.0,
    248.0,
    anchor="nw",
    text="4 years old",
    fill="#030303",
    font=("RobotoRoman SemiBold", 20 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    175.0,
    357.0,
    image=image_image_6
)

canvas.create_text(
    118.0,
    351.0,
    anchor="nw",
    text="Skin issues",
    fill="#030303",
    font=("RobotoRoman SemiBold", 20 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    334.0,
    564.0,
    image=image_image_7
)

canvas.create_text(
    183.0,
    543.0,
    anchor="nw",
    text="Need more frequent playtime \nand short walks",
    fill="#000000",
    font=("RobotoRoman SemiBold", 22 * -1)
)
window.resizable(False, False)
window.mainloop()
