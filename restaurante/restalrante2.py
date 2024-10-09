import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1920x1080")
        self.title("Ristorante")

        self.frame1 = ctk.CTkFrame(self, width=700, height=500, fg_color="white")
        self.frame1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.textoa = ctk.CTkLabel(self.frame1, text="Bentornato", font=("italic", 30), text_color="black")
        self.textoa.place(x=156, y=10)

        self.texto = ctk.CTkLabel(self.frame1, text="Nome * ", font=("italic", 20), text_color="black")
        self.texto.place(x=40, y=70)
        self.nome = ctk.CTkEntry(self.frame1, width=400, height=30)
        self.nome.place(x=40, y=100)

        self.texto2 = ctk.CTkLabel(self.frame1, text="Parole d'ordine * ", font=("italic", 20), text_color="black")
        self.texto2.place(x=40, y=170)
        self.parole = ctk.CTkEntry(self.frame1, width=300, height=30, show="*")
        self.parole.place(x=40, y=200)

        self.texto3 = ctk.CTkLabel(self.frame1, text="Confirmação * ", font=("italic", 20), text_color="black")
        self.texto3.place(x=40, y=270)
        self.parole2 = ctk.CTkEntry(self.frame1, width=300, height=30, show="*") 
        self.parole2.place(x=40, y=300)

        self.bot = ctk.CTkButton(self.frame1, text="Pronto", hover_color="green", corner_radius=10, height=40, command=self.tuti)
        self.bot.place(x=40, y=400)

        self.cart = []
        self.slide_index = 0
        self.menu_items = []

    def tuti(self):
        nome = self.nome.get()
        parole = self.parole.get()
        parole2 = self.parole2.get()

        self.texto.configure(text_color="black")
        self.texto2.configure(text_color="black")
        self.texto3.configure(text_color="black")

        validacao = True

        if nome == "":
            self.texto.configure(text_color="red")
            validacao = False
        
        if parole == "":
            self.texto2.configure(text_color="red")
            validacao = False
        
        if parole2 == "":
            self.texto3.configure(text_color="red")
            validacao = False

        if nome == parole:
            self.texto.configure(text_color="red")
            self.texto2.configure(text_color="red")
            validacao = False
        
        if parole != parole2:
            self.texto2.configure(text_color="red")
            self.texto3.configure(text_color="red")
            validacao = False

        if validacao and (parole == parole2):
            self.frame1.destroy()
            self.show_menu()  

        else:
            print("Erro de validação")

    def show_menu(self):
        self.menu_frame = ctk.CTkFrame(self, fg_color="white")
        self.menu_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        menu_title = ctk.CTkLabel(self.menu_frame, text="Menu do Restaurante", font=("italic", 30), text_color="black")
        menu_title.pack(pady=20)

        # Adicionando itens ao menu com imagens
        self.menu_items = [
            ("Pizza Margherita", 30.00, 'C:/Users/DanielSilva/Documents/desktop/Desktop/restaurante/1.jpg'),
            ("Lasanha", 35.00, 'C:/Users/DanielSilva/Documents/desktop/Desktop/restaurante/2.jpg'),
            ("Spaghetti Carbonara", 28.00, 'C:/Users/DanielSilva/Documents/desktop/Desktop/restaurante/3.jpg'),
            ("Tiramisu", 15.00, 'C:/Users/DanielSilva/Documents/desktop/Desktop/restaurante/4.jpg'),
            ("Água Mineral", 5.00, 'C:/Users/DanielSilva/Documents/desktop/Desktop/restaurante/5.jpg')
        ]

        self.canvas = tk.Canvas(self.menu_frame, width=500, height=300)
        self.canvas.pack(pady=20)

        self.load_slide_images()

        # Botão para o próximo slide
        next_button = ctk.CTkButton(self.menu_frame, text="Próximo", command=self.next_slide)
        next_button.pack(pady=5)

        # Botão para comprar item atual
        buy_button = ctk.CTkButton(self.menu_frame, text="Comprar", command=self.buy_item)
        buy_button.pack(pady=5)

        # Botão para finalizar a compra
        checkout_button = ctk.CTkButton(self.menu_frame, text="Finalizar Compra", command=self.checkout)
        checkout_button.pack(pady=20)

        exit_button = ctk.CTkButton(self.menu_frame, text="Sair", command=self.quit)
        exit_button.pack(pady=20)

        self.cart_label = ctk.CTkLabel(self.menu_frame, text="Carrinho de Compras:", font=("italic", 20), text_color="black")
        self.cart_label.pack(pady=20)

        self.cart_display = ctk.CTkLabel(self.menu_frame, text="", font=("Arial", 14), text_color="black")
        self.cart_display.pack(pady=10)

    def load_slide_images(self):
        self.image_labels = []
        for item, price, image_path in self.menu_items:
            img = Image.open(image_path)
            img = img.resize((500, 300))  # Redimensiona a imagem
            img_photo = ImageTk.PhotoImage(img)
            self.image_labels.append((item, price, img_photo))  # Mantém a referência da imagem e os dados do item

        self.show_image(self.slide_index)

    def show_image(self, index):
        self.canvas.delete("all")  # Limpa o canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_labels[index][2])  # Exibe a imagem

    def next_slide(self):
        self.slide_index = (self.slide_index + 1) % len(self.image_labels)  # Cicla pelos índices
        self.show_image(self.slide_index)

    def buy_item(self):
        item, price, _ = self.image_labels[self.slide_index]
        self.cart.append(f"{item} - R$ {price:.2f}")
        self.update_cart_display()

    def update_cart_display(self):
        if self.cart:
            items = "\n".join(self.cart)
            self.cart_display.configure(text=items)
        else:
            self.cart_display.configure(text="Carrinho vazio.")

    def checkout(self):
        if self.cart:
            total = sum(float(item.split(' - R$ ')[1]) for item in self.cart)
            summary = "\n".join(self.cart)
            checkout_message = f"Você comprou:\n{summary}\nTotal: R$ {total:.2f}"
            ctk.CTkMessageBox.showinfo("Finalizar Compra", checkout_message)
            self.cart.clear()  # Limpa o carrinho após a compra
            self.update_cart_display()
        else:
            ctk.CTkMessageBox.showwarning("Aviso", "Seu carrinho está vazio!")

app = App()
app.mainloop()
