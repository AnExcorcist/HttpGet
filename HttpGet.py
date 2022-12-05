from tkinter import *
import customtkinter, itertools, requests
from itertools import *

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("400x350")
root.title("HttpGet")
root.iconbitmap("Logo.ico")

def changedark():
    customtkinter.set_appearance_mode(entry3.get())

frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both", expand=True)

entry3 = customtkinter.CTkEntry(master=root, placeholder_text="Dark/Light")
entry3.pack(pady=10, padx=10)

buttonchangelight = customtkinter.CTkButton(master=root, text="Set Mode", command=changedark)
buttonchangelight.pack(pady=10, padx=10)



entry1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Url Here")
entry1.pack(pady=10, padx=10)

entry2 = customtkinter.CTkEntry(master=frame1, placeholder_text="File Name")
entry2.pack(pady=10, padx=10)

def gethttp():
    r = requests.get(entry1.get())
    with open (str(entry2.pack()), "w+") as f:
        f.write(r.text)

def gethead():
    r = requests.head(entry1.get())
    with open(str(entry2.pack()), "w+") as f:
        f.write(str(r.headers))

buttonget = customtkinter.CTkButton(master=frame1, text="GetInfo", command = gethttp)
buttonget.pack(pady=10, padx=10)

buttonhead = customtkinter.CTkButton(master=frame1, text="GetHeaders", command=gethead)
buttonhead.pack(pady=10, padx=10)


root.mainloop()