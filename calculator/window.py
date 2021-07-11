from tkinter import *


import tkinter.font as font
def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("411x823")
window.configure(bg = "#212020")
canvas = Canvas(
    window,
    bg = "#212020",
    height = 823,
    width = 411,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    0, 291, 0+411, 291+532,
    fill = "#f0f0f3",
    outline = "")

button_img_0 = PhotoImage(file = f"button_img_0.png")
button_text_font_0 = font.Font(family='Oswald-Medium', size=int(36.0))
b0 = Button(
    image = button_img_0,
    text = '1',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b0.place(
    x = 38, y = 631,
    width = 72,
    height = 70)

button_img_1 = PhotoImage(file = f"button_img_1.png")
button_text_font_1 = font.Font(family='Oswald-Medium', size=int(36.0))
b1 = Button(
    image = button_img_1,
    text = '2',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b1.place(
    x = 128, y = 631,
    width = 71,
    height = 70)

button_img_2 = PhotoImage(file = f"button_img_2.png")
button_text_font_2 = font.Font(family='Oswald-Medium', size=int(36.0))
b2 = Button(
    image = button_img_2,
    text = '3',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b2.place(
    x = 218, y = 631,
    width = 71,
    height = 70)

button_img_3 = PhotoImage(file = f"button_img_3.png")
button_text_font_3 = font.Font(family='Oswald-Medium', size=int(36.0))
b3 = Button(
    image = button_img_3,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b3.place(
    x = 308, y = 631,
    width = 71,
    height = 70)

button_img_4 = PhotoImage(file = f"button_img_4.png")
button_text_font_4 = font.Font(family='Oswald-Medium', size=int(36.0))
b4 = Button(
    image = button_img_4,
    text = '4',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b4.place(
    x = 38, y = 537,
    width = 72,
    height = 70)

button_img_5 = PhotoImage(file = f"button_img_5.png")
button_text_font_5 = font.Font(family='Oswald-Medium', size=int(36.0))
b5 = Button(
    image = button_img_5,
    text = '5',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b5.place(
    x = 128, y = 537,
    width = 71,
    height = 70)

button_img_6 = PhotoImage(file = f"button_img_6.png")
button_text_font_6 = font.Font(family='Oswald-Medium', size=int(36.0))
b6 = Button(
    image = button_img_6,
    text = '6',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b6.place(
    x = 218, y = 537,
    width = 71,
    height = 70)

button_img_7 = PhotoImage(file = f"button_img_7.png")
button_text_font_7 = font.Font(family='Oswald-Medium', size=int(36.0))
b7 = Button(
    image = button_img_7,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b7.place(
    x = 308, y = 537,
    width = 71,
    height = 70)

button_img_8 = PhotoImage(file = f"button_img_8.png")
button_text_font_8 = font.Font(family='Oswald-Medium', size=int(36.0))
b8 = Button(
    image = button_img_8,
    text = '7',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b8.place(
    x = 38, y = 443,
    width = 72,
    height = 70)

button_img_9 = PhotoImage(file = f"button_img_9.png")
button_text_font_9 = font.Font(family='Oswald-Medium', size=int(36.0))
b9 = Button(
    image = button_img_9,
    text = '8',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b9.place(
    x = 128, y = 443,
    width = 71,
    height = 70)

button_img_10 = PhotoImage(file = f"button_img_10.png")
button_text_font_10 = font.Font(family='Oswald-Medium', size=int(36.0))
b10 = Button(
    image = button_img_10,
    text = '9',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b10.place(
    x = 218, y = 443,
    width = 71,
    height = 70)

button_img_11 = PhotoImage(file = f"button_img_11.png")
button_text_font_11 = font.Font(family='Oswald-Medium', size=int(36.0))
b11 = Button(
    image = button_img_11,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_11,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b11.place(
    x = 308, y = 443,
    width = 71,
    height = 70)

button_img_12 = PhotoImage(file = f"button_img_12.png")
button_text_font_12 = font.Font(family='Oswald-Medium', size=int(36.0))
b12 = Button(
    image = button_img_12,
    text = 'C',
    compound = 'center',
    fg = '#898989',
    font = button_text_font_12,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b12.place(
    x = 38, y = 349,
    width = 72,
    height = 70)

button_img_13 = PhotoImage(file = f"button_img_13.png")
button_text_font_13 = font.Font(family='Oswald-Medium', size=int(36.0))
b13 = Button(
    image = button_img_13,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_13,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b13.place(
    x = 308, y = 349,
    width = 71,
    height = 70)

button_img_14 = PhotoImage(file = f"button_img_14.png")
button_text_font_14 = font.Font(family='Oswald-Medium', size=int(36.0))
b14 = Button(
    image = button_img_14,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_14,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b14.place(
    x = 218, y = 349,
    width = 71,
    height = 70)

button_img_15 = PhotoImage(file = f"button_img_15.png")
button_text_font_15 = font.Font(family='Oswald-Medium', size=int(36.0))
b15 = Button(
    image = button_img_15,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_15,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b15.place(
    x = 128, y = 349,
    width = 71,
    height = 70)

button_img_16 = PhotoImage(file = f"button_img_16.png")
button_text_font_16 = font.Font(family='Oswald-Medium', size=int(36.0))
b16 = Button(
    image = button_img_16,
    text = '0',
    compound = 'center',
    fg = '#728ab7',
    font = button_text_font_16,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b16.place(
    x = 39, y = 725,
    width = 250,
    height = 70)

button_img_17 = PhotoImage(file = f"button_img_17.png")
button_text_font_17 = font.Font(family='Oswald-Medium', size=int(36.0))
b17 = Button(
    image = button_img_17,
    text = '',
    compound = 'center',
    fg = 'white',
    font = button_text_font_17,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = 'flat')

b17.place(
    x = 308, y = 725,
    width = 71,
    height = 70)

canvas.create_text(
    312.5, 229.0,
    text = "1260",
    fill = "#f2f2f4",
    font = ("Oswald-Medium", int(64.0)))

window.resizable(False, False)
window.mainloop()
