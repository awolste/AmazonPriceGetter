import tkinter as tk
from tkinter import filedialog, Text
import os
import scraper

urlList = []


def add_item():
    newUrl = urlBox.get("1.0", "end")
    # newUrl = 'https://www.amazon.com/gp/product/B087JB656Q/ref=ox_sc_saved_title_1?smid=ATVPDKIKX0DER&psc=1'
    if newUrl not in urlList:
        urlList.append(newUrl)
    for url in urlList:
        try:
            data = scraper.scrape(url)
        except:
            error = tk.Label(canvas, text="Must Enter URL")
            error.pack()
            return
        if data:
            price = tk.Label(canvas, text=data['price'])
            price.pack()


root = tk.Tk()

canvas = tk.Canvas(root, height=400, width=300, bg='#f0f0f0')
canvas.pack()

urlBox = tk.Text(canvas, height=5, width=50, highlightbackground='black')
urlBox.pack()

# frame = tk.Frame(root, bg='#000000')
# frame.place(relwidth=.8, relheight=.8, relx=.1, rely=.1)

updatePrice = tk.Button(root, text="Get Price", padx=10, pady=5, fg='orange', bg='black', command=add_item)
updatePrice.pack()

root.mainloop()
