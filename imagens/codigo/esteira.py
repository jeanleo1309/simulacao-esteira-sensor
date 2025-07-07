```python
import time
import random

contador = 0

print("Iniciando simulação da esteira...\n")
for i in range(20):  # Simula 20 ciclos
    objeto_passando = random.choice([True, False])
    
    if objeto_passando:
        contador += 1
        print(f"🔴 Objeto detectado! Total: {contador}")
    else:
        print("⚪ Nenhum objeto na esteira.")

    time.sleep(1)  # Espera 1 segundo antes do próximo ciclo

print(f"\n✅ Simulação finalizada. Objetos contados: {contador}")
