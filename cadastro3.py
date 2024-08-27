#por favor ignore os mil comentarios 
#per favore ignorate i mille commenti
import customtkinter  as  ctk
#perguntas, por que classe?


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

def testuno():
    print("oiii, fofura totoza")

        #Cria um frame         #define o tamanho do frame  #fg é foregrund color    #Circuferencia Reduzir corner_radius=0

frame = ctk.CTkFrame(width=400, height=60, fg_color="transparent")
frame.place(x=0,y=0)

            #isso é uma var no caso o "b"
b=ctk.CTkLabel( text="Benvenuto al regitro site web", font=("arial",28) )
b.place(x=20,y=15)#tamanho do frame 

        #-------

nome=ctk.CTkLabel(text="Come ti chiami?" ) #Loro chiamano Daniel, ma preferisco come la chiama mia moglie, Dani
nome.place(x=150,y=79)


nome2=ctk.CTkEntry(width=250)#negocio ae de cima com o tamanaho 250 
nome2.place(x=80,y=100)#tamanho desse negocio ai de cima

#---
        #Parole d'ordine
parole= ctk.CTkEntry( text="Escrivi la parole d'ordine" )
parole.place(x=148,y=174)

parole2=ctk.CTkEntry(width=250, show="*")
parole2.place(x=78,y=200)

        #--------
        #Solo un pulsante :)

butto=ctk.CTkButton(text="Fatto")
butto.place(x=80,y=299)

def ns(self):
    nome =  nome2.get()
    senha = parole2.get()
    #assd
    if nome == senha:
        ctk.CTkLabel(self,text="la password e il nome non possono essere gli stessi", fg_color="red").place(x=10, y=10)
                                                                                      #perche non rosso?
    else:
        print("oi")


app =  ctk()
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