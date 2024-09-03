import tkinter as ttk

var= ttk.Tk() #
var_para_o_frame= ttk.Frame(var,pady= 300,padx=300, background=("#41D1CC")) #criei o frame da janela
var_para_o_frame.grid() #
contador=0

def soma(): #função de soma
    global contador 
    contador+=1
    valores.configure(text=f"{contador}",foreground="Red")
    print(contador)

var.title("Ola")#titulo

teste=ttk.Label(var_para_o_frame, text="Eu Te Amo Sofia", font=("bold",50), background="#41D1CC", foreground="white")#print
teste.grid(column=0,row=0)

#botão de soma
valores=ttk.Button(var_para_o_frame, text="Soma",command=soma)
valores.grid(column=0, row=2)

botao=ttk.Button(var_para_o_frame, text="sair", command=var.destroy)
botao.grid(column=0, row=5)

var.mainloop()#loop