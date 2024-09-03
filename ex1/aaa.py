import customtkinter as ctk
from PIL import Image, ImageTk 
import tkinter as tk

ctk.set_appearance_mode("dark")

while True:
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.titulo=ctk.CTkLabel(self,text="Benvenuti nella mia galleria", font=("italic", 30))
        self.titulo.place(x=100, y=10)
        #vitas
        self.vitas = "/Users/DanielSilva/Documents/desktop/Desktop/galeria/vitas.png"
        self.vitas1 = Image.open(self.vitas)
        self.vitas1 = ImageTk.PhotoImage(self.vitas1)
        self.vitas1 = ctk.CTkLabel(self, image=self.vitas1, text='')
        self.vitas1.place(x=150, y=50)
        #keith
        self.keith = "/Users/DanielSilva/Documents/desktop/Desktop/galeria/keithemerson.jpg"
        self.keith1 = Image.open(self.keith)
        self.keith1 = ImageTk.PhotoImage(self.keith1)
        self.keith1 = ctk.CTkLabel(self, image=self.keith1, text='')
        self.keith.place(x=150, y=50)
        #freddie
        self.freddie = "/Users/DanielSilva/Documents/desktop/Desktop/galeria/freddie.jpg"
        self.freddie1 = Image.open(self.keith)
        self.freddie1 = ImageTk.PhotoImage(self.keith1)
        self.freddie1 = ctk.CTkLabel(self, image=self.keith1, text='')
        self.freddie1.place(x=150, y=50)


        self.bot_esq = ctk.CTkButton(self, text="<" ,hover_color="White", width=30 )
        self.bot_esq.place(x=50,y=235)
    def atualizar_imagem(self):
        # Carregar e definir a nova imagem
        imagem_path = self.imagens[self.imagem_index]
        imagem = Image.open(imagem_path)
        imagem = ImageTk.PhotoImage(imagem)
        self.imagem_label.configure(image=imagem)
        self.imagem_label.image = imagem  # Manter uma referência para evitar coleta de lixo

    def mudar_imagem(self):
        # Mudar para a próxima imagem
        self.imagem_index = (self.imagem_index + 1) % len(self.imagens)
        self.atualizar_imagem()

        
app=App()
#app.configure(fg_color="black")cor de fundo
app.geometry(f"600x600") 
app.title("Galleria")
app.mainloop()
