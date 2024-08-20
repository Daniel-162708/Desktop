import tkinter as ttk

var= ttk.Tk()
var.geometry("600x600")
frame= ttk.Frame(var, pady=12,padx=12,background="#008b8b")

var.title("Supermercati a Genova")
h1=ttk.Label(frame, text="Salve mio signiore, ciao mia signora, Benvenuto al registro site web ", background="#008b8b", foreground="white")
h1.grid(column=4,row=0)

h2=ttk.Label(frame)

frame.grid()

var.mainloop()