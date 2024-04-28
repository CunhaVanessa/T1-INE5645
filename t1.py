import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import argparse
import random
import time

# Cria o parser
parser = argparse.ArgumentParser(description='Programa para controlar sensores e atuadores.')

# Adiciona os argumentos
parser.add_argument('--sensores', type=int, required=True, help='Número de sensores.')
parser.add_argument('--atuadores', type=int, required=True, help='Número de atuadores.')
parser.add_argument('--eventos', type=int, required=False, help='Número de eventos sensoriais para terminar o programa.')

# Analisa os argumentos
args = parser.parse_args()

# Retorna a confirmação de args.sensores e args.atuadores escolhidos
print(f'Número de sensores: {args.sensores}')
print(f'Número de atuadores: {args.atuadores}')

class CentralControle:
    def __init__(self, atuadores, lock):
        self.atuadores = [0] * atuadores
        self.lock = lock
        self.eventos = multiprocessing.Value('i', 0)

    def processar_dado_sensorial(self, ds, atuadores):
        atuador = ds % atuadores
        nivel_atividade = random.randint(0, 100)

        with self.lock:
            self.atuadores[atuador] = nivel_atividade
            self.eventos.value += 1

        print(f"Atuador {atuador} com valor {nivel_atividade}")
        time.sleep(random.uniform(2, 3))

def sensor(c_central, atuadores, eventos):
    while eventos is None or c_central.eventos.value < eventos:
        try:
            dado_sensorial = random.randint(0, 1000)
            c_central.processar_dado_sensorial(dado_sensorial, atuadores)
            time.sleep(random.randint(1, 5))
        except Exception as e:
            print(f"Erro ao processar o sensor: {e}")

# Cria um lock
lock = multiprocessing.Lock()

# Cria uma instância de CentralControle
c_central = CentralControle(args.atuadores, lock)

# Cria um ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=args.sensores)

# Usa o executor para executar a função sensor em paralelo
for i in range(args.sensores):
    executor.submit(sensor, c_central, args.atuadores, args.eventos)

# Espera todas as tarefas terminarem
executor.shutdown(wait=True)