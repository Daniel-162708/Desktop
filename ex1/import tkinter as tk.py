import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.current_input = ""
        self.result = 0
        self.operation = ""

        # Configuração dos botões
        self.create_buttons()
        
        # Frame para mostrar resultados
        self.frame = ctk.CTkFrame(self, width=299, height=180)
        self.frame.place(x=10, y=20)
        self.label1 = ctk.CTkLabel(self.frame, text='0', font=("", 80))
        self.label1.place(x=76 + 20 + 80 - 19 + 60 + 15 + 1, y=70)

    def create_buttons(self):
        # Criar botões numerais
        for i in range(10):
            button = ctk.CTkButton(self, width=73, height=53, text=str(i),
                                    fg_color="#2D2D2D", hover_color="#3C3C3C",
                                    command=lambda v=str(i): self.tuti(v))
            button.place(x=5 + (i % 3) * 80, y=271 - (i // 3) * 53)
        
        # Criar botões de operação
        operations = {'+': self.set_operation, '-': self.set_operation, '*': self.set_operation, '/': self.set_operation}
        for i, op in enumerate(operations.keys()):
            button = ctk.CTkButton(self, width=80, height=53, text=op,
                                    fg_color="#1C1C1C", hover_color="#3C3C3C",
                                    command=lambda v=op: self.set_operation(v))
            button.place(x=245, y=271 - i * 53)

        # Botões adicionais
        self.botao_igual = ctk.CTkButton(self, width=80, height=109, text="=",
                                          fg_color="#0078D4", hover_color="#3C3C3C",
                                          command=self.calculate)
        self.botao_igual.place(x=200 + 29 + 12 - 8, y=382)
        
        self.botao_clear = ctk.CTkButton(self, width=80, height=53, text="C",
                                          fg_color="#C72C28", hover_color="#3C3C3C",
                                          command=self.clear)
        self.botao_clear.place(x=245, y=215)

    def tuti(self, value):
        self.current_input += value
        self.label1.configure(text=self.current_input)

    def set_operation(self, operation):
        if self.current_input:
            self.result = float(self.current_input)
            self.current_input = ""
            self.operation = operation
            self.label1.configure(text="0")

    def calculate(self):
        if self.current_input and self.operation:
            if self.operation == '+':
                self.result += float(self.current_input)
            elif self.operation == '-':
                self.result -= float(self.current_input)
            elif self.operation == '*':
                self.result *= float(self.current_input)
            elif self.operation == '/':
                if float(self.current_input) != 0:
                    self.result /= float(self.current_input)
                else:
                    self.label1.configure(text="Error")
                    return
            self.label1.configure(text=str(self.result))
            self.current_input = ""
            self.operation = ""

    def clear(self):
        self.current_input = ""
        self.result = 0
        self.operation = ""
        self.label1.configure(text="0")

app = App()
app.geometry("318x502")
app.title("Calculadora")

app.mainloop()
