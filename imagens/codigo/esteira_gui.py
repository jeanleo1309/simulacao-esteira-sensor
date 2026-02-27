import tkinter as tk
import random

class SimuladorEsteira:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulação de Esteira com Sensor")
        self.root.geometry("350x220")

        self.contador = 0
        self.executando = False
        self.probabilidade_objeto = 0.6  # 60% de chance de objeto

        # Labels
        self.contador_label = tk.Label(root, text="Objetos contados: 0", font=("Arial", 14))
        self.contador_label.pack(pady=10)

        self.status_label = tk.Label(root, text="🔴 Esteira Parada", font=("Arial", 12))
        self.status_label.pack()

        # Botões
        tk.Button(root, text="Iniciar Esteira", command=self.iniciar_esteira,
                  bg="green", fg="white").pack(pady=5)

        tk.Button(root, text="Parar Esteira", command=self.parar_esteira,
                  bg="red", fg="white").pack(pady=5)

        tk.Button(root, text="Resetar Contador", command=self.resetar_contador).pack(pady=5)

    def iniciar_esteira(self):
        if not self.executando:
            self.executando = True
            self.status_label.config(text="🟢 Esteira Ligada")
            self.simular_esteira()

    def parar_esteira(self):
        self.executando = False
        self.status_label.config(text="🔴 Esteira Parada")

    def resetar_contador(self):
        self.contador = 0
        self.contador_label.config(text="Objetos contados: 0")

    def simular_esteira(self):
        if self.executando:
            objeto = random.random() < self.probabilidade_objeto
            if objeto:
                self.contador += 1
                self.contador_label.config(
                    text=f"Objetos contados: {self.contador}"
                )

            # Executa novamente após 1000ms (1 segundo)
            self.root.after(1000, self.simular_esteira)


if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorEsteira(root)
    root.mainloop()
