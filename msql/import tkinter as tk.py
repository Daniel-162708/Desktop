import tkinter as tk
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuração dos botões da calculadora (deixado como está no seu código)

        # Botões
        self.botao1 = ctk.CTkButton(self, width=73, height=53, text="<=", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao1.place(x=5, y=439)

        self.botao2 = ctk.CTkButton(self, width=73, height=53, text="0", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao2.place(x=20+80-19, y=439)

        self.botao3 = ctk.CTkButton(self, width=73, height=53, text=",", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao3.place(x=76+20+80-19, y=439)

        self.igual = ctk.CTkButton(self, width=80, height=109, text="=", fg_color="#0078D4", hover_color="#3C3C3C")
        self.igual.place(x=200+29+12-8, y=382)

        self.botao4 = ctk.CTkButton(self, width=73, height=53, text="1", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao4.place(x=5, y=383)

        self.botao5 = ctk.CTkButton(self, width=73, height=53, text="2", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao5.place(x=20+80-19, y=383)

        self.botao6 = ctk.CTkButton(self, width=73, height=53, text="3", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao6.place(x=76+20+80-19, y=383)

        self.botao7 = ctk.CTkButton(self, width=73, height=53, text="4", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao7.place(x=5, y=327)

        self.botao8 = ctk.CTkButton(self, width=73, height=53, text="5", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao8.place(x=20+80-19, y=327)

        self.botao9 = ctk.CTkButton(self, width=73, height=53, text="6", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao9.place(x=76+20+80-19, y=327)

        self.botao10 = ctk.CTkButton(self, width=80, height=53, text="+", fg_color="#1C1C1C", hover_color="#3C3C3C")
        self.botao10.place(x=76+20+80-19+60+15+1, y=327)

        self.botao11 = ctk.CTkButton(self, width=73, height=53, text="7", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao11.place(x=5, y=271)

        self.botao12 = ctk.CTkButton(self, width=73, height=53, text="8", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao12.place(x=20+80-19, y=271)

        self.botao13 = ctk.CTkButton(self, width=73, height=53, text="9", fg_color="#2D2D2D", hover_color="#3C3C3C")
        self.botao13.place(x=76+20+80-19, y=271)

        self.botao14 = ctk.CTkButton(self, width=80, height=53, text="-", fg_color="#1C1C1C", hover_color="#3C3C3C")
        self.botao14.place(x=76+20+80-19+60+15+1, y=271)

        self.botao15 = ctk.CTkButton(self, width=73, height=53, text="%", fg_color="#1C1C1C", hover_color="#3C3C3C")
        self.botao15.place(x=5, y=215)

        self.botao16 = ctk.CTkButton(self, width=73, height=53, text="²/¹", fg_color="#1C1C1C", hover_color="#3C3C3C")
        self.botao16.place(x=20+80-19, y=215)

        self.botao17 = ctk.CTkButton(self, width=73, height=53, text="/", fg_color="#1C1C1C", hover_color="#3C3C3C")
        self.botao17.place(x=76+20+80-19, y=215)

        self.botao18 = ctk.CTkButton(self, width=80, height=53, text="x", fg_color="#1C1C1C", hover_color="#3C3C3C")
        self.botao18.place(x=76+20+80-19+60+15+1, y=215)

        # Frame da barra
        self.bar_frame = ctk.CTkFrame(self, width=299, height=30, fg_color="#0078D4")
        self.bar_label = ctk.CTkLabel(self.bar_frame, text="I'm a bar!", text_color="white")
        self.bar_label.pack(expand=True, fill='both')

        # Adiciona o frame da barra dentro do frame principal
        self.frame = ctk.CTkFrame(self, width=299, height=180)
        self.frame.place(x=10, y=20)
        self.bar_frame.place(x=10, y=20)  # Inicialmente visível

        # Botão para alternar a visibilidade da barra
        self.toggle_button = ctk.CTkButton(self, text="Toggle Bar", command=self.toggle_bar)
        self.toggle_button.place(x=10, y=500)

    def toggle_bar(self):
        if self.bar_frame.winfo_ismapped():
            self.slide_out()
        else:
            self.slide_in()

    def slide_out(self):
        # Anima a barra saindo para fora da tela
        self._slide_bar(self.bar_frame.winfo_y(), self.winfo_height(), -1)

    def slide_in(self):
        # Anima a barra entrando na tela
        self._slide_bar(self.winfo_height(), 20, 1)

    def _slide_bar(self, start_y, end_y, direction):
        # Move a barra gradualmente
        step = 5 * direction  # O passo do movimento
        delay = 10  # Atraso em milissegundos

        def update_position():
            current_y = self.bar_frame.winfo_y()
            if (direction == 1 and current_y <= end_y) or (direction == -1 and current_y >= end_y):
                self.bar_frame.place(y=current_y + step)
                self.after(delay, update_position)
            else:
                self.bar_frame.place(y=end_y)
                # Se movendo para fora, também pode adicionar um place_forget após a animação
                if direction == -1:
                    self.bar_frame.place_forget()

        update_position()

app = App()
app.geometry("318x550")  # Ajuste a altura para acomodar o botão
app.title("Calculadora")
app.mainloop()
