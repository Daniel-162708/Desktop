#por favor ignore os mil comentarios 
#per favore ignorate i mille commenti
import customtkinter  as  ctk
from tkinter import *

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
    
class App(ctk.CTk): #criando a classe App que recebe o ctk
    def __init__(self):
        super().__init__()

        #Cria um frame         #define o tamanho do frame  #fg é foregrund color    #Circuferencia Reduzir corner_radius=0
        self.frame = ctk.CTkFrame(self,width=400, height=60, fg_color="transparent")
        self.frame.place(x=0,y=0)

            #isso é uma var no caso o "b"
        self.b=ctk.CTkLabel(self.frame, text="Benvenuto al regitro site web", font=("arial",28) )
        self.b.place(x=20,y=15)#tamanho do frame 

        #-------

        self.nome=ctk.CTkEntry(self, width=250 ,placeholder_text="Come ti chiami?" ) #Loro chiamano Daniel, ma preferisco come la chiama mia moglie, Dani
        self.nome.place(x=70,y=79)

        self.nome2=ctk.CTkEntry(self,width=250,placeholder_text="Email")#negocio ae de cima com o tamanaho 250 
        self.nome2.place(x=70,y=120)#tamanho desse negocio ai de cima

        #--

        #Parole d'ordine
        self.parole2=ctk.CTkEntry(self,width=250, placeholder_text="Parole d'ordine", show="*")
        self.parole2.place(x=70,y=161)

        #--------
        #Solo un pulsante :)

        self.butto=ctk.CTkButton(self,text="Fatto", command=self.tuti)
        self.butto.place(x=120,y=200)
#------------------------------------------ proprio una bella immagine

 #11   
    def tuti(self):
        self.testuno()
        self.ns()

 #11   
    def testuno(self):
        nome=  self.nome.get()
        senha= self.parole2.get()
        email= self.nome2.get()

        if nome !="" and senha !="" and email !="":
            app.destroy()
        else:
            self.labelula=ctk.CTkLabel(self.frame,text="qualcosa non va, riprova",
                                        fg_color="red")
            self.labelula.place(x=10, y=30)  
            self.after(3000, self.labelula.destroy) 
#11

    def ns(self):
        nome = self.nome2.get()
        senha =self.parole2.get()
        #assd
        if nome == senha:
            self.labelula=ctk.CTkLabel(self,text="la password e il nome non possono essere gli stessi", fg_color="red")
            self.labelula.place(x=10, y=10)
            #perche non rosso?
            self.after(3000, self.labelula.destroy)
        else:
            print("oi")
    

app = App() # app esta recebendo a classe App
#geometry define o tamanho da tela
app.geometry("400x400")#tamnho, o que esta dentro das aspas são variaveis

#app.configure(background="#4169e1")#era para mudar a cor de fundo, nem precisa mais 
#a tela não pode ser alterada
app.resizable(False,False)#comando diferente # o 0,0 pode ser subistituido por false ou true, não deixa o 
#app ser maximizado , comando novo, gostei porem não achei utilidade
#criar o loop normal do tkinter
app.title("Supermercati a Genova")

#io amo a l'italia, dispiache di non
#essere italinao :(
app.mainloop()#o looop, não apegue isso porque é o loop