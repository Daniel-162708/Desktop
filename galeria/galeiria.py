import customtkinter as ctk
from PIL import Image, ImageTk 
import tkinter as tk

ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # self.titulo=ctk.CTkLabel(self,text="Benvenuti nella mia galleria", font=("italic", 30))
        # self.titulo.place(x=100, y=10)
        # #vitas
        # self.vitas = "/Users/DanielSilva/Documents/desktop/Desktop/galeria/vitas.png"
        # self.vitas1 = Image.open(self.vitas)
        # self.vitas1 = ImageTk.PhotoImage(self.vitas1)
        # self.vitas1 = ctk.CTkLabel(self, image=self.vitas1, text='')
        # self.vitas1.place(x=150, y=50)
        # #keith
        # self.keith = "/Users/DanielSilva/Documents/desktop/Desktop/galeria/keithemerson.jpg"
        # self.keith1 = Image.open(self.keith)
        # self.keith1 = ImageTk.PhotoImage(self.keith1)
        # self.keith1 = ctk.CTkLabel(self, image=self.keith1, text='')
        # self.keith1.place(x=150, y=50)
        # #freddie
        # self.freddie = "/Users/DanielSilva/Documents/desktop/Desktop/galeria/freddie.jpg"
        # self.freddie1 = Image.open(self.freddie)
        # self.freddie1 = ImageTk.PhotoImage(self.freddie1)
        # self.freddie1 = ctk.CTkLabel(self, image=self.freddie1, text='')
        # self.freddie1.place(x=150, y=50)

        self.imagens=['/Users/DanielSilva/Documents/desktop/Desktop/galeria/freddie.jpg',
                      "/Users/DanielSilva/Documents/desktop/Desktop/galeria/keithemerson.jpg",
                      "/Users/DanielSilva/Documents/desktop/Desktop/galeria/vitas.png"
                      ]
        self.imagem_index=0
        self.atualizar_imagem()
        self.bot_esq = ctk.CTkButton(self, text="<" ,hover_color="White", width=30, command=self.mudar_imagem )
        self.bot_esq.place(x=50,y=235)
    


    def atualizar_imagem(self):
        # Carregar e definir a nova imagem
        imagem_path = self.imagens[self.imagem_index]
        self.img = Image.open(imagem_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.teste = ctk.CTkLabel(self, image=self.img, text='')
        self.teste.place(relx=.5, rely=.5, anchor='center')
        

    def mudar_imagem(self):
        # Mudar para a próxima imagem
        global imagem_index
        self.imagem_index = (self.imagem_index+1)
        self.atualizar_imagem()
        


app=App()
#app.configure(fg_color="black")cor de fundo
app.geometry(f"600x600") 
app.title("Galleria")
app.mainloop()
