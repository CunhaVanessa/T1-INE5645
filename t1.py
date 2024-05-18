import multiprocessing
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse
import random
import time
import logging

# Função para configurar o logger
def configure_logging(debug):
    if debug:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Cria o parser
parser = argparse.ArgumentParser(description='Programa para controlar sensores e atuadores.')

# Adiciona os argumentos
parser.add_argument('--sensores', type=int, required=True, help='Número de sensores.')
parser.add_argument('--atuadores', type=int, required=True, help='Número de atuadores.')
parser.add_argument('--eventos', type=int, required=False, help='Número de eventos sensoriais para terminar o programa.')
parser.add_argument('--debug', action='store_true', help='Ativa o modo debug.')

# Analisa os argumentos
args = parser.parse_args()

# Configura o logging com base no argumento de debug
configure_logging(args.debug)

# Retorna a confirmação de args.sensores e args.atuadores escolhidos
logging.info(f'Número de sensores: {args.sensores}')
logging.info(f'Número de atuadores: {args.atuadores}')

class CentralControle:
    def __init__(self, atuadores, lock):
        self.atuadores = multiprocessing.Manager().dict({i: 0 for i in range(atuadores)})
        self.lock = lock
        self.eventos = multiprocessing.Value('i', 0)

    def alterar_nivel_atividade(self, atuador, nivel_atividade):
        logging.debug(f'Tentando alterar atuador {atuador} para nível {nivel_atividade}')
        with self.lock:
            self.atuadores[atuador] = nivel_atividade
        time.sleep(random.uniform(2, 3))
        with self.lock:
            self.atuadores[atuador] = 0  # Reseta o atuador após o tempo
        return random.random() >= 0.2  # Retorna True se não houve falha (80% de chance de sucesso)

    def enviar_mensagem_painel(self, atuador, nivel_atividade):
        with self.lock:
            logging.debug(f"Alterando: {atuador} com valor {nivel_atividade}")
        time.sleep(1)  # Mantém a mensagem no painel por 1 segundo
        return random.random() >= 0.2  # Retorna True se não houve falha (80% de chance de sucesso)

    def processar_dado_sensorial(self, ds, atuadores):
        atuador = ds % atuadores
        nivel_atividade = random.randint(0, 100)

        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = []
            futures.append(executor.submit(self.alterar_nivel_atividade, atuador, nivel_atividade))
            futures.append(executor.submit(self.enviar_mensagem_painel, atuador, nivel_atividade))

            results = [future.result() for future in as_completed(futures)]
            if not all(results):
                with self.lock:
                    logging.error(f"Falha: {atuador}")

        with self.lock:
            self.eventos.value += 1
            logging.debug(f'Evento {self.eventos.value}: Atuador {atuador} processado')

def sensor(c_central, atuadores, eventos):
    while eventos is None or c_central.eventos.value < eventos:
        try:
            dado_sensorial = random.randint(0, 1000)
            logging.debug(f'Sensor gerou dado sensorial: {dado_sensorial}')
            c_central.processar_dado_sensorial(dado_sensorial, atuadores)
            time.sleep(random.randint(1, 5))
        except Exception as e:
            logging.error(f"Erro ao processar o sensor: {e}")

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
