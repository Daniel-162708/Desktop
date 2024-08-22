import tkinter as ttk

var= ttk.Tk()
var.geometry("600x600")
frame= ttk.Frame(var, pady=12,padx=12,background=("#00bfff"))
frame.pack()
var.configure(background="#4169e1")

var.title("Supermercati a Genova")
h1=ttk.Label(frame, text="Salve mio signiore, ciao mia signora, Benvenuto al registro site web ",bg="#00bfff", foreground="white")
h1.pack()
h1.grid(column=0,row=0)

h2=ttk.Entry(var,bg="white")
h2.pack(pady="200")

var.mainloop()