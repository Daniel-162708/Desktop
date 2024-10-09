import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #1
        self.botao1=ctk.CTkButton(self, width=73, height=53, text="<=",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='1': self.tuti(v))
        self.botao1.place(x=5,y=439)#50,30
        
        self.botao2=ctk.CTkButton(self, width=73, height=53, text="0",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='0': self.tuti(v))
        self.botao2.place(x=20+80-19,y=439)#50,30

        self.botao3=ctk.CTkButton(self, width=73, height=53, text=",",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v=',': self.tuti(v))
        self.botao3.place(x=76+20+80-19,y=439)#50,30

        self.igual=ctk.CTkButton(self, width=80, height=109, text="=",fg_color="#0078D4" ,hover_color="#3C3C3C", command=lambda v='=': self.tuti(v))        
        self.igual.place(x=200+29+12-8,y=382)#50,30

        #2        
        self.botao12=ctk.CTkButton(self, width=73, height=53, text="1",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='1': self.tuti(v))
        self.botao12.place(x=5,y=383)#50,30
        
        self.botao13=ctk.CTkButton(self, width=73, height=53, text="2",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='2': self.tuti(v))
        self.botao13.place(x=20+80-19,y=383)#50,30
        
        self.botao14=ctk.CTkButton(self, width=73, height=53, text="3",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='3': self.tuti(v))
        self.botao14.place(x=76+20+80-19,y=383)#50,30

        #3
        self.botao4=ctk.CTkButton(self, width=73, height=53, text="4",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='4': self.tuti(v))
        self.botao4.place(x=5,y=327)#50,30
        
        self.botao5=ctk.CTkButton(self, width=73, height=53, text="5",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='5': self.tuti(v))
        self.botao5.place(x=20+80-19,y=327)#50,30
        
        self.botao6=ctk.CTkButton(self, width=73, height=53, text="6",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='6': self.tuti(v))
        self.botao6.place(x=76+20+80-19,y=327)#50,30

        self.botao7=ctk.CTkButton(self, width=80, height=53, text="+",fg_color="#1C1C1C" ,hover_color="#3C3C3C", command=lambda v='+': self.tuti(v))
        self.botao7.place(x=76+20+80-19+60+15+1,y=327)#50,30

        #4
        self.botao8=ctk.CTkButton(self, width=73, height=53, text="7",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='7': self.tuti(v))
        self.botao8.place(x=5,y=271)#50,30
        
        self.botao9=ctk.CTkButton(self, width=73, height=53, text="8",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='8': self.tuti(v))
        self.botao9.place(x=20+80-19,y=271)#50,30
        
        self.botao10=ctk.CTkButton(self, width=73, height=53, text="9",fg_color="#2D2D2D" ,hover_color="#3C3C3C", command=lambda v='9': self.tuti(v))
        self.botao10.place(x=76+20+80-19,y=271)#50,30

        self.botao11=ctk.CTkButton(self, width=80, height=53, text="-",fg_color="#1C1C1C" ,hover_color="#3C3C3C", command=lambda v='-': self.tuti(v))
        self.botao11.place(x=76+20+80-19+60+15+1,y=271)#50,30

        #5
        self.botao20=ctk.CTkButton(self, width=73, height=53, text="%",fg_color="#1C1C1C" ,hover_color="#3C3C3C", command=lambda v='%': self.tuti(v))
        self.botao20.place(x=5,y=215)#50,30
        
        self.botao21=ctk.CTkButton(self, width=73, height=53, text="¹/²",fg_color="#1C1C1C" ,hover_color="#3C3C3C", command=lambda v='1/2': self.tuti(v))
        self.botao21.place(x=20+80-19,y=215)#50,30
        
        self.botao22=ctk.CTkButton(self, width=73, height=53, text="/",fg_color="#1C1C1C" ,hover_color="#3C3C3C", command=lambda v='/': self.tuti(v))
        self.botao22.place(x=76+20+80-19,y=215)#50,30

        self.botao23=ctk.CTkButton(self, width=80, height=53, text="x",fg_color="#1C1C1C" ,hover_color="#3C3C3C", command=lambda v='.': self.tuti(v))
        self.botao23.place(x=76+20+80-19+60+15+1,y=215)#50,30

        #6
        self.frame = ctk.CTkFrame(self, width=299, height=180)
        self.frame.place(x=10,y=20)
        self.label1=ctk.CTkLabel(self.frame, text= '0', font=("",80))
        self.label1.place(x=76+20+80-19+60+15+1,y=70)

    def tuti(self,nome):
    
        self.label1.configure(text=nome)


        

app=App()
app.geometry("318x502")#700 700
app.title("Calculadora")

app.mainloop()
