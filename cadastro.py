import tkinter as ttk

var=   ttk.Tk()
var.geometry("600x600")
frame= ttk.Frame(var, pady=5,padx=5,background="red")

var.title("Supermercati a Genova")

h1=ttk.Label(frame, text="Salve mio signiore, ciao mia signora, Benvenuto al registro site web ")
h1.grid(sticky="w",column=1,row=0)

var.mainloop()