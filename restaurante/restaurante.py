import customtkinter as ctk 
from PIL import Image, ImageTk
import tkinter as tk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.frame1 = ctk.CTkFrame(self, width=700, height=500, fg_color="white")
        self.frame1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.textoa = ctk.CTkLabel(self.frame1, text="Bentornato", font=("italic", 30), text_color="black")
        self.textoa.place(x=156, y=10)

        self.image_path = 'restaurante/image.png'
        self.image3 = Image.open(self.image_path)
        self.image3 = ImageTk.PhotoImage(self.image3)
        self.imagem3 = ctk.CTkLabel(self.frame1, image=self.image3, text='')
        self.imagem3.place(x=430, y=10)

        self.texto = ctk.CTkLabel(self.frame1, text="Nome * ", font=("italic", 20), text_color="black")
        self.texto.place(x=40, y=70)
        self.nome = ctk.CTkEntry(self.frame1, width=400, height=30)
        self.nome.place(x=40, y=100)

        self.texto2 = ctk.CTkLabel(self.frame1, text="Parole d'odire * ", font=("italic", 20), text_color="black")
        self.texto2.place(x=40, y=170)
        self.parole = ctk.CTkEntry(self.frame1, width=300, height=30, show="*")
        self.parole.place(x=40, y=200)

        self.texto3 = ctk.CTkLabel(self.frame1, text="Confirmação * ", font=("italic", 20), text_color="black")
        self.texto3.place(x=40, y=270)
        self.parole2 = ctk.CTkEntry(self.frame1, width=300, height=30, show="*") 
        self.parole2.place(x=40, y=300)

        self.bot = ctk.CTkButton(self.frame1, text="Pronto", hover_color="green", corner_radius=10, height=40, command=self.tuti)
        self.bot.place(x=40, y=400)

    def tuti(self):
        nome = self.nome.get()
        parole = self.parole.get()
        parole2 = self.parole2.get()

        self.texto.configure(text_color="black")
        self.texto2.configure(text_color="black")
        self.texto3.configure(text_color="black")

        validacao = True

        if nome == "":
            self.texto.configure(text_color="red")
            validacao = False
        
        if parole == "":
            self.texto2.configure(text_color="red")
            validacao = False
        
        if parole2 == "":
            self.texto3.configure(text_color="red")
            validacao = False

        if nome == parole:
            self.texto.configure(text_color="red")
            self.texto2.configure(text_color="red")
            validacao = False
        
        if parole != parole2:
            self.texto2.configure(text_color="red")
            self.texto3.configure(text_color="red")
            validacao = False

        if validacao and (parole == parole2) and len(parole)>7 and len(parole2)> 7 :
            self.frame1.destroy()

        else:
            print("Erro de validação")

app = App()
app.geometry("1920x1080")
app.title("Ristorante")
app.mainloop()
