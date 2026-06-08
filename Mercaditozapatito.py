from queue import Queue
from threading import Thread
import random
import time

print("Bienvenidos al Mercadito Zapatito")

fila = Queue()
historial = []

clientes = [
    "Juanito Pérez",
    "Anita López",
    "Luisito García",
    "Pedrito Ramírez",
    "Lupita Hernández",
    "Carlitos Martínez",
    "Rosita Torres",
    "Dieguito Sánchez",
    "Elenita Flores",
    "Miguelito Vargas"
]

random.shuffle(clientes)

for cliente in clientes:
    fila.put(cliente)

def caja(nombre_caja):
    while not fila.empty():

        cliente = fila.get()

        print(f"{nombre_caja} está atendiendo a {cliente}")

        tiempo = random.randint(1, 3)
        time.sleep(tiempo)

        historial.append(cliente)

        print(f"{cliente} terminó su compra en {nombre_caja}\n")

cajita_blanco = Thread(
    target=caja,
    args=("Cajita Zapatito Blanco",)
)

cajita_azul = Thread(
    target=caja,
    args=("Cajita Zapatito Azul",)
)

cajita_blanco.start()
cajita_azul.start()

cajita_blanco.join()
cajita_azul.join()

print("Historial de clientes atendidos")

for i, cliente in enumerate(historial, start=1):
    print(f"{i}. {cliente}")

print("\nTodos los clientesitos han sido atendidos")