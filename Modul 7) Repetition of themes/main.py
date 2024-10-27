from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

for c in range(3): root.columnconfigure(index=c, weight=1)
for r in range(3): root.rowconfigure(index=r, weight=1)

def click():
    print("Hello")

for r in range(3):
    for c in range(3):
        btn = ttk.Button(text="Ok", command=click)
        btn.grid(row=r, column=c, ipadx=0, ipady=0, padx=0, pady=0, sticky=NSEW)

root.mainloop()