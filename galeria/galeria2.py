import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root

        # Usando caminhos absolutos para as imagens
        self.images = [
            'C:/Users/DanielSilva/Documents/desktop/Desktop/galeria/1.jpg',
            'C:/Users/DanielSilva/Documents/desktop/Desktop/galeria/2.jpg',
            'C:/Users/DanielSilva/Documents/desktop/Desktop/galeria/3.jpg'
        ]
        self.current_image_index = 0

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=20)

        self.prev_button = tk.Button(root, text="Anterior", command=self.show_prev_image)
        self.prev_button.pack(side=tk.LEFT, padx=20)
        self.entry=tk.Entry(root,width=30)
        self.entry.pack(side=tk.BOTTOM, padx=20)
        self.next_button = tk.Button(root, text="Próximo", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT, padx=20)

        self.show_image()  # Exibir a primeira imagem na inicialização

    def show_image(self):
        if self.images:
            image_path = self.images[self.current_image_index]
            print(f"Tentando abrir a imagem: {image_path}")  # Para depuração
            try:
                image = Image.open(image_path)
                image = image.resize((500, 500), Image.LANCZOS)  # Usar LANCZOS para melhor qualidade
                self.photo = ImageTk.PhotoImage(image)
                self.image_label.config(image=self.photo)
                self.image_label.image = self.photo
                print("Imagem exibida com sucesso.")  # Para depuração
            except Exception as e:
                print(f"Erro ao abrir a imagem: {e}")

    def show_prev_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index - 1) % len(self.images)
            self.show_image()

    def show_next_image(self):
        if self.images:
            self.current_image_index = (self.current_image_index + 1) % len(self.images)
            self.show_image()

root = tk.Tk()
root.title("Galeria de Imagens")
root.geometry("600x600")  # Ajuste a largura para comportar a imagem e os botões
app = App(root)
root.mainloop()
