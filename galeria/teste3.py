import customtkinter as ctk
from PIL import Image, ImageTk 
import tkinter as tk

ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.titulo=ctk.CTkLabel(self,text="Benvenuti nella mia galleria", font=("italic", 30))
        self.titulo.place(x=100, y=10)
        
        self.vitas = "/Users/DanielSilva/Documents/desktop/Desktop/galeria/vitas.png"
        self.vitas1 = Image.open(self.vitas)
        self.vitas1 = ImageTk.PhotoImage(self.vitas1)
        self.vitas1 = ctk.CTkLabel(self, image=self.vitas1, text='')
        self.vitas1.place(x=150, y=50)
        
        self.frame = None
        self.bind("<Button-1>", self.var)


    def var(self, event):
        if self.frame is None: #se o frame não existe  crie um ctk.CTkFrame
            self.frame = ctk.CTkFrame(self, width=600, height=100, fg_color="white")
            #self.frame.place(x=event.x, y=event.y)isso faça que crie aonde o mause clicar
            self.frame.place(x=0,y=550)
        else:#se ja exite destrua-o
            self.frame.destroy()
            self.frame = None
app=App()
#app.configure(fg_color="black")cor de fundo
app.geometry(f"600x600") 
app.title("Galleria")
app.mainloop()
