from tkinter import *

import webbrowser
from core import *

def btn_clicked():
    print("Button Clicked")

#here
def OpenHelp():
    webbrowser.open("about.html")

def OpenEmail():
      webbrowser.open("mailto:?to=sumitmusale077@gmail.com&subject=Report_US_any_Problem", new=1) 

window = Tk()
#here
window.title("Virtual Mouse")
window.iconbitmap("Mouse.ico")
window.geometry("648x402")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 402,
    width = 648,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    324.0, 201.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = window.quit,
    relief = "flat")

b0.place(
    x = 331, y = 225,
    width = 236,
    height = 63)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command =automatic,
    relief = "flat")

b1.place(
    x = 330, y = 110,
    width = 234,
    height = 65)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = OpenEmail,
    relief = "flat")

b2.place(
    x = 362, y = 368,
    width = 72,
    height = 30)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command =OpenHelp,
    relief = "flat")

b3.place(
    x = 260, y = 371,
    width = 59,
    height = 22)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 468, y = 369,
    width = 82,
    height = 26)

window.resizable(False, False)
window.mainloop()
