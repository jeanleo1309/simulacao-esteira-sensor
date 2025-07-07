import tkinter as tk
import random
import threading
import time

contador = 0
executando = False

def iniciar_esteira():
    global executando
    if not executando:
        executando = True
        status_label.config(text="🟢 Esteira Ligada")
        threading.Thread(target=simular_esteira).start()

def parar_esteira():
    global executando
    executando = False
    status_label.config(text="🔴 Esteira Parada")

def resetar_contador():
    global contador
    contador = 0
    contador_label.config(text=f"Objetos contados: {contador}")

def simular_esteira():
    global contador
    while executando:
        objeto = random.choice([True, False])
        if objeto:
            contador += 1
            contador_label.config(text=f"Objetos contados: {contador}")
        time.sleep(1)

# Interface
janela = tk.Tk()
janela.title("Simulação de Esteira com Sensor")
janela.geometry("350x200")

contador_label = tk.Label(janela, text="Objetos contados: 0", font=("Arial", 14))
contador_label.pack(pady=10)

status_label = tk.Label(janela, text="🔴 Esteira Parada", font=("Arial", 12))
status_label.pack()

btn_iniciar = tk.Button(janela, text="Iniciar Esteira", command=iniciar_esteira, bg="green", fg="white")
btn_iniciar.pack(pady=5)

btn_parar = tk.Button(janela, text="Parar Esteira", command=parar_esteira, bg="red", fg="white")
btn_parar.pack(pady=5)

btn_resetar = tk.Button(janela, text="Resetar Contador", command=resetar_contador)
btn_resetar.pack(pady=5)

janela.mainloop()
