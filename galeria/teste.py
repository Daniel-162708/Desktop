
import customtkinter as ctk
from PIL import Image, ImageTk 
import tkinter as tk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.titulo = ctk.CTkLabel(self, text="Benvenuti nella mia galleria", font=("italic", 30))
        self.titulo.place(x=100, y=10)
        
        self.vitas = "/Users/DanielSilva/Documents/desktop/Desktop/galeria/vitas.png"
        self.vitas1 = Image.open(self.vitas)
        self.vitas1 = ImageTk.PhotoImage(self.vitas1)
        self.vitas1 = ctk.CTkLabel(self, image=self.vitas1, text='')
        self.vitas1.place(x=240, y=150)

        self.bind("<Button-1>", self.var)

    def var(self, event):
        # Obtendo as coordenadas do clique
        x = event.x
        y = event.y
        print(f"Clique detectado na posição: ({x}, {y})")

app = App()
app.configure(fg_color="black")
app.geometry("600x600") 
app.title("Galleria")
app.mainloop()
