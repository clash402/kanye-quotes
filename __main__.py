from tkinter import *
import requests as req


# DATA MANAGER
def get_quote():
    res = req.get(url="https://api.kanye.rest")
    res.raise_for_status()
    return res.json()["quote"]


# UI
def update_quote_label():
    quote = get_quote()
    canvas.itemconfig(quote_label, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
bg_image = PhotoImage(file="./images/background.png")
canvas.create_image(150, 207, image=bg_image)
quote_label = canvas.create_text(150, 207, text="Kanye Quote", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_image = PhotoImage(file="./images/kanye.png")
kanye_button = Button(image=kanye_image, highlightthickness=0, command=update_quote_label)
kanye_button.grid(row=1, column=0)

window.mainloop()
