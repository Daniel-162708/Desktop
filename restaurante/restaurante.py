import customtkinter as ctk
from PIL import Image, ImageTk 
import tkinter as tk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.frame1=ctk.CTkFrame(self, width=500,height=550, bg_color="White")
        self.frame1.place(x=40,y=200)

app = App()
app.geometry("1920x1080") 
app.title("Restaurante")
app.mainloop()
