#por favor ignore os mil comentarios 
#per favore ignorate i mille commenti
import customtkinter  as  ctk
from PIL import Image, ImageTk 
import tkinter as tk

#c#tk.set_appearance_mode("Dark")
#ctk.set_default_color_theme("black")

    
class App(ctk.CTk): #criando a classe App que recebe o ctk
    def __init__(self):
        super().__init__()
        
        self.image_path3 = 'oip.png'#var armazenando a imagem
        self.image3 = Image.open(self.image_path3)#para abrir  a imagem
        self.image3 = ImageTk.PhotoImage(self.image3)#convertendo para uma imagem tk
        self.imagem3 = ctk.CTkLabel(self, image=self.image3, text='')#criação da label
        self.imagem3.place(x=1600, y=0)   


            #isso é uma var no caso o "b"
        self.b=ctk.CTkLabel(self, text="Benvenuto al regitro site web!", font=("arial",28,"italic") )
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

        self.parole3=ctk.CTkEntry(self,width=250, placeholder_text="Confermare la parole d'ordine", show="*")
        self.parole3.place(x=70,y=200)

        #--------
        #Solo un pulsante :)
#aka
        self.butto=ctk.CTkButton(self,text="Fatto", command=self.testuno)
        self.butto.place(x=120,y=300)

        self.idade= ctk.CTkSwitch(self, onvalue="+18", offvalue="-18", text="Maior de 18?")
        self.idade.place(x=120,y=250)
        



#sofia, como eu queria, mas do que queria, dou minha vida só para estar nos céus dos braços teus

        #-------
        #io sono, tu sei, lui è, lei è, noi siamo, voi siete, loro sono
#------------------------------------------ proprio una bella immagine

 #11   
    def testuno(self):
        nome=  self.nome.get()
        senha= self.parole2.get()
        email= self.nome2.get()
        idadee= self.idade.get()
        senha2= self.parole3.get()


        if nome !="" and senha !="" and email !="" and idadee != "" and senha != email and senha != nome and idadee=="+18" and senha==senha2:
            self.frame_cadastro=ctk.CTkFrame(self, width=260, height=260, fg_color="white", bg_color="black")
            self.frame_cadastro.place(x=59, y=15)
            self.titulo=ctk.CTkLabel(self.frame_cadastro, text="La registrazione è stata effettuata.", font=("italic", 15), text_color="black")
            self.titulo.place(x=19, y=30)
            self.botaott=ctk.CTkButton(self.frame_cadastro, text="Prontto", command=self.destroy)
            self.botaott.place(x=55,y=200)
            
        elif nome==senha or email ==senha:
            self.labelula=ctk.CTkLabel(self,text="la password e il nome non possono essere gli stessi.", fg_color="red")
            self.labelula.place(x=10, y=340)
            #perche non rosso?
            self.after(3000, self.labelula.destroy)
        
        elif senha != senha2:
            self.labelula=ctk.CTkLabel(self,text="La password non corrisponde.", fg_color="red")
            self.labelula.place(x=10, y=377)
            #perche non rosso?
            self.after(3000, self.labelula.destroy)
        
        elif idadee=="-18":
            self.idasas=ctk.CTkLabel(self,text="Non puoi entrare.", fg_color="red")
            self.idasas.place(x=10, y=377)
            #perche non rosso?
            self.after(3000, self.labelula.destroy)  
        
        elif senha == "" or senha2=="":
            self.idasas=ctk.CTkLabel(self,text="Non posso lasciare vuoto.", fg_color="red")
            self.idasas.place(x=10, y=377)
            #perche non rosso?
            self.after(3000, self.labelula.destroy)  

        else:   
            self.labelula=ctk.CTkLabel(self,text="qualcosa non va, riprova.",fg_color="red")
            self.labelula.place(x=10, y=377)  
            self.after(3000, self.labelula.destroy)

            
app = App() # app esta recebendo a classe App
#geometry define o tamanho da tela
app.configure(fg_color="black")
app.geometry(f"400x400") #tamnho, o que esta dentro das aspas são variaveis

#app.configure(background="#4169e1")#era para mudar a cor de fundo, nem precisa mais 
#a tela não pode ser alterada
#app.resizable(False,False)#comando diferente # o 0,0 pode ser subistituido por false ou true, não deixa o 
#app ser maximizado , comando novo, gostei porem não achei utilidade
#criar o loop normal do tkinter
app.title("Supermercati a Genova")

#io amo a l'italia, dispiache di non
#essere italinao :(
app.mainloop()#o looop, não apegue isso porque é o loop