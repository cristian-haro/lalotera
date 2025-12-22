import random
import tkinter as tk
from tkinter import messagebox

class LaLoteraApp:
    def __init__(self, master):
        self.master = master
        master.title("Tablero de Lotería 01-99")
        master.state('zoomed')
        #master.configure(bg="#f4f4f9")
                # --- COLORES ---
        master.bg_principal = "#1e1e2e"
        master.bg_tarjeta = "#2b2b3b"
        master.accent_color = "#89b4fa"
        master.text_color = "#cdd6f4"
        master.btn_success = "#a6e3a1"
        master.btn_danger = "#f38ba8"
        master.btn_warning = "#fab387"
        master.configure(bg=master.bg_principal)

        # Lógica del juego
        self.bolsa = list(range(1, 101))
        random.shuffle(self.bolsa)
        self.salidos = []

        self.crear_widgets()

    def crear_widgets(self):
        # Encabezado
        header = tk.Frame(self.master, bg="#34495e", pady=15)
        header.pack(fill="x")
        # tk.Label(header, text="Seguro que toca", font=("Arial", 20, "bold"), fg="white", bg="#34495e").pack()

        # Visualización del número grande
        self.display_numero = tk.Label(self.master, text="--", font=("Arial", 120, "bold"), 
                                       fg="#d35400", bg="#1e1e2e")
        self.display_numero.pack(pady=10)

        # Botones
        btn_frame = tk.Frame(self.master, bg="#1e1e2e")
        btn_frame.pack(pady=10)

        self.btn_sacar = tk.Button(btn_frame, text="SACAR NÚMERO", command=self.sacar_numero, 
                                   font=("Arial", 16, "bold"), bg="#2ecc71", fg="white", 
                                   padx=40, pady=10, relief="flat", cursor="hand2")
        self.btn_sacar.pack(side=tk.LEFT, padx=10)

        self.btn_reset = tk.Button(btn_frame, text="REINICIAR", command=self.reiniciar, 
                                   font=("Arial", 12), bg="#e74c3c", fg="white", relief="flat", cursor="hand2")
        self.btn_reset.pack(side=tk.LEFT, padx=10)

        # Contenedor del Tablero
        self.tablero_frame = tk.Frame(self.master, bg="#1e1e2e", bd=1, relief="solid", padx=10, pady=10)
        self.tablero_frame.pack(pady=20)

        self.labels_numeros = {}
        for i in range(1, 101):
            lbl = tk.Label(self.tablero_frame, text=f"{i:02d}", font=("Arial", 11, "bold"), 
                           width=4, height=2, bg="#1e1e2e", fg="#bdc3c7", relief="flat", 
                           highlightthickness=1, highlightbackground="#ecf0f1")
            lbl.grid(row=(i-1)//10, column=(i-1)%10, padx=2, pady=2)
            self.labels_numeros[i] = lbl

    def sacar_numero(self):
        if not self.bolsa:
            messagebox.showinfo("Fin", "¡Se terminaron los números!")
            return

        num = self.bolsa.pop(0)
        self.salidos.append(num)
        
        # Actualizar Interfaz inmediatamente
        self.display_numero.config(text=f"{num:02d}")
        
        # Marcar en el tablero: fondo amarillo y texto oscuro
        self.labels_numeros[num].config(bg="#f1c40f", fg="#2c3e50")

    def reiniciar(self):
        if messagebox.askyesno("Confirmar", "¿Deseas reiniciar todo el tablero para una nueva partida?"):
            self.bolsa = list(range(1, 101))
            random.shuffle(self.bolsa)
            self.salidos = []
            self.display_numero.config(text="--")
            for lbl in self.labels_numeros.values():
                lbl.config(bg="#ffffff", fg="#bdc3c7")

if __name__ == "__main__":
    root = tk.Tk()
    app = LaLoteraApp(root)
    root.mainloop()