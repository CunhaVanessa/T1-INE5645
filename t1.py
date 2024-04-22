import multiprocessing
import random
import time

N_SENSORES = 5  # Número de sensores
N_ATUADORES = 3  # Número de atuadores

class CentralControle:
    def __init__(self):
        self.atuadores = multiprocessing.Array('i', [0] * N_ATUADORES)
        self.lock = multiprocessing.Lock()

    def processar_dado_sensorial(self, ds):
        atuador = ds % N_ATUADORES
        nivel_atividade = random.randint(0, 100)

        with self.lock:
            self.atuadores[atuador] = nivel_atividade

        print(f"Atuador {atuador} com valor {nivel_atividade}")
        time.sleep(random.uniform(2, 3))

        with self.lock:
            self.atuadores[atuador] = 0
        print(f"Alterando: Atuador {atuador} com valor 0")

def sensor(c_central):
    while True:
        dado_sensorial = random.randint(0, 1000)
        c_central.processar_dado_sensorial(dado_sensorial)
        time.sleep(random.randint(1, 5))

def main():
    central = CentralControle()
    processes = []

    for _ in range(N_SENSORES):
        p = multiprocessing.Process(target=sensor, args=(central,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()
