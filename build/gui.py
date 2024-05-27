
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Project\coffee\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    750.0,
    0.0,
    1000.0,
    600.0,
    fill="#675BEB",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    336.0,
    267.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    336.0,
    356.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    331.0,
    444.0,
    image=image_image_3
)

canvas.create_text(
    279.0,
    432.0,
    anchor="nw",
    text="Đăng nhập",
    fill="#FFFFFF",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    173.0,
    95.0,
    anchor="nw",
    text="TLUCoffee",
    fill="#675BEB",
    font=("Inter Bold", 60 * -1)
)

canvas.create_text(
    159.0,
    168.0,
    anchor="nw",
    text="Phần mềm quản lý quán cà phê TLU",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

canvas.create_text(
    230.0,
    525.0,
    anchor="nw",
    text="© Cao Trung Hiếu 2024",
    fill="#595959",
    font=("Inter", 18 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    212.0,
    355.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    211.0,
    267.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    779.0,
    300.0,
    image=image_image_6
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    355.5,
    267.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=235.0,
    y=252.0,
    width=241.0,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    355.5,
    356.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=235.0,
    y=341.0,
    width=241.0,
    height=28.0
)
window.resizable(False, False)
window.mainloop()