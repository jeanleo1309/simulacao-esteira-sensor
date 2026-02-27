import tkinter as tk
import random
import time

class SimuladorEsteira:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Contagem Industrial")
        self.root.geometry("400x300")
        self.root.configure(bg="#1e1e1e")

        self.contador = 0
        self.executando = False
        self.velocidade = 1000
        self.probabilidade_objeto = 0.6
        self.inicio = None

        # Título
        tk.Label(root, text="SIMULADOR DE ESTEIRA",
                 font=("Arial", 16, "bold"),
                 bg="#1e1e1e", fg="white").pack(pady=10)

        # Contador
        self.contador_label = tk.Label(root,
                                       text="Objetos contados: 0",
                                       font=("Arial", 14),
                                       bg="#1e1e1e",
                                       fg="#00ffcc")
        self.contador_label.pack()

        # Status
        self.status_label = tk.Label(root,
                                     text="🔴 Parado",
                                     font=("Arial", 12),
                                     bg="#1e1e1e",
                                     fg="red")
        self.status_label.pack(pady=5)

        # Velocidade
        tk.Label(root, text="Velocidade (ms):",
                 bg="#1e1e1e",
                 fg="white").pack()

        self.velocidade_scale = tk.Scale(root,
                                         from_=200,
                                         to=2000,
                                         orient="horizontal",
                                         bg="#1e1e1e",
                                         fg="white")
        self.velocidade_scale.set(1000)
        self.velocidade_scale.pack()

        # Botões
        tk.Button(root, text="Iniciar",
                  command=self.iniciar,
                  bg="green", fg="white").pack(pady=5)

        tk.Button(root, text="Parar",
                  command=self.parar,
                  bg="red", fg="white").pack(pady=5)

        tk.Button(root, text="Resetar",
                  command=self.resetar).pack(pady=5)

        # Taxa
        self.taxa_label = tk.Label(root,
                                   text="Taxa: 0 obj/min",
                                   bg="#1e1e1e",
                                   fg="yellow")
        self.taxa_label.pack(pady=5)

    def iniciar(self):
        if not self.executando:
            self.executando = True
            self.status_label.config(text="🟢 Rodando", fg="green")
            self.inicio = time.time()
            self.simular()

    def parar(self):
        self.executando = False
        self.status_label.config(text="🔴 Parado", fg="red")

    def resetar(self):
        self.contador = 0
        self.contador_label.config(text="Objetos contados: 0")
        self.taxa_label.config(text="Taxa: 0 obj/min")

    def simular(self):
        if self.executando:
            self.velocidade = self.velocidade_scale.get()

            falha_sensor = random.random() < 0.05  # 5% falha

            if not falha_sensor:
                objeto = random.random() < self.probabilidade_objeto
                if objeto:
                    self.contador += 1
                    self.contador_label.config(
                        text=f"Objetos contados: {self.contador}"
                    )

            self.calcular_taxa()

            self.root.after(self.velocidade, self.simular)

    def calcular_taxa(self):
        if self.inicio:
            tempo = (time.time() - self.inicio) / 60
            if tempo > 0:
                taxa = int(self.contador / tempo)
                self.taxa_label.config(text=f"Taxa: {taxa} obj/min")


if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorEsteira(root)
    root.mainloop()
