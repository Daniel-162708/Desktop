import customtkinter as ctk
from PIL import Image, ImageTk 
import tkinter as tk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        

app = App()
app.geometry("600x600") 
app.title("Restaurante")
app.mainloop()
