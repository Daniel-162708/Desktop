import customtkinter as ctk
import tkinter as tk

#perguntas, por que classe?

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
class App(ctk.CTk): #criando a classe App que recebe o ctk
    def __init__(self):
        super().__init__()
        #Cria um frame         #define o tamanho do frame  #fg é foregrund color    #Circuferencia Reduzir corner_radius=0
        self.frame = ctk.CTkFrame(self,width=400, height=60, fg_color="transparent")
        self.frame.place(x=0,y=0)

        self.h1=ctk.CTkLabel(self.frame, text="Benvenuto al regitro site web", font=("arial",28) )
        self.h1.place(x=20,y=15)

        #-------

        self.h2=ctk.CTkLabel(self, text="Come ti chiami?" )
        self.h2.place(x=12,y=79)

        self.entry=ctk.CTkEntry(self,width=250)
        self.entry.place(x=12,y=100)
        
        self.h2=ctk.CTkLabel(self, text="Escrivi la parole d'ordine" )
        self.h2.place(x=12,y=174)

        self.entry=ctk.CTkEntry(self,width=250)
        self.entry.place(x=12,y=200)

        #--------

        self.butto=ctk.CTkButton(self,text="Fatto")
        self.butto.place(x=70,y=299)

    def colr_tm():
        self.colorn= ctk.CTkLabel(self,text="Colores", bgcolor="transparent", text_color=["#000","#fff"])
 


app = App() # app esta recebendo a classe App "comando entre aspas diferente"
#geometry define o tamanho da tela
app.geometry("400x400")

app.configure(background="#4169e1")#era para mudar a cor de fundo
#a tela não pode ser alterada
app.resizable(False,False)#comando diferente # o 0,0 pode ser subistituido por false ou true, não deixa o app ser maximizado 
#criar o loop normal do tkinter
app.title("Supermercati a Genova")

app.mainloop()