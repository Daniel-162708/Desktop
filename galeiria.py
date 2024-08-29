import customtkinter as ctk
from PIL import Image, ImageTk 
import tkinter as tk

class App(ctk.CTK):
    def __init__(self):
        super().__init__()




app=App()
app.configure(fg_color="black")
app.geometry(f"600x600") 
app.title("Galleria")
app.mainloop()
