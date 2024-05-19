import subprocess
import psutil
import time
import logging
import unittest
import argparse

# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

class TesteProgramaParalelo(unittest.TestCase):
    def run_and_monitor(self, command, max_memory_limit, max_cpu_limit, duration=None):
        # Inicia o processo
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pid = process.pid
        logging.info(f'Processo iniciado com PID: {pid} para o comando: {" ".join(command)}')

        # Monitoramento de recursos
        proc = psutil.Process(pid)
        memory_usage = []
        cpu_usage = []

        start_time = time.time()
        try:
            while process.poll() is None:
                # Opcionalmente limitar a duração do monitoramento
                if duration and (time.time() - start_time) > duration:
                    process.terminate()
                    logging.warning("Processo terminado devido ao tempo de execução excedido.")
                    break

                # Obtém o uso de memória e CPU
                mem_info = proc.memory_info()
                cpu_percent = proc.cpu_percent(interval=1)

                memory_usage.append(mem_info.rss)
                cpu_usage.append(cpu_percent)

                logging.info(f'Memória usada: {mem_info.rss / (1024 * 1024):.2f} MB')
                logging.info(f'CPU usada: {cpu_percent:.2f}%')

                time.sleep(1)

            # Aguarda o término do processo e coleta os resultados
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                logging.info('O processo terminou corretamente.')
            else:
                logging.error(f'O processo terminou com código de erro {process.returncode}.')
                logging.error(stderr.decode())

        except psutil.NoSuchProcess:
            logging.error('O processo não existe mais.')

        except Exception as e:
            logging.error(f'Erro ao monitorar o processo: {e}')

        end_time = time.time()

        # Resultados do monitoramento
        max_memory = max(memory_usage) / (1024 * 1024)
        logging.info(f'Máximo de memória usada: {max_memory:.2f} MB')

        max_cpu = max(cpu_usage)
        logging.info(f'Máximo de CPU usada: {max_cpu:.2f}%')

        total_time = end_time - start_time
        logging.info(f'Tempo total de execução: {total_time:.2f} segundos')

        # Verificação de critérios
        self.assertLess(max_memory, max_memory_limit, f"O uso de memória excedeu {max_memory_limit} MB")
        self.assertLess(max_cpu, max_cpu_limit, f"O uso de CPU excedeu {max_cpu_limit}%")

        return total_time

    def run_test(self, sensores, atuadores, eventos, duration, test_type):
        command = ["python3", "t1.py", "--sensores", str(sensores), "--atuadores", str(atuadores)]
        if eventos:
            command.extend(["--eventos", str(eventos)])
        if test_type in ["escalabilidade_vertical", "escalabilidade_horizontal"]:
            return self.run_and_monitor(command, 512, 90, duration)
        else:
            return self.run_and_monitor(command, 512, 90)

    def teste_longa_duracao(self):
        logging.info("Iniciando Teste de Longa Duração")

        # Executa com a configuração aumentada
        total_time = self.run_test(5, 5, 1000, None, "longa_duracao")

        logging.info("Teste de Longa Duração concluído com sucesso\n")
        return total_time

    def teste_tempo_resposta(self):
        logging.info("Iniciando Teste de Tempo de Resposta")

        # Executa com a configuração aumentada
        total_time = self.run_test(5, 3, 100, None, "tempo_resposta")

        logging.info("Teste de Tempo de Resposta concluído com sucesso\n")
        return total_time

    def teste_escalabilidade_vertical(self):
        logging.info("Iniciando Teste de Escalabilidade Vertical")

        # Executa com a configuração aumentada por 1 minuto
        total_time = self.run_test(20, 5, None, 60, "escalabilidade_vertical")  # Limite de duração de 1 minuto

        # Aqui, podemos usar logs ou contadores para verificar o número de eventos processados
        logging.info(f"Teste de Escalabilidade Vertical processou eventos em 1 minuto.")

        logging.info("Teste de Escalabilidade Vertical concluído com sucesso\n")
        return total_time

    def teste_escalabilidade_horizontal(self):
        logging.info("Iniciando Teste de Escalabilidade Horizontal")

        # Executa com a configuração aumentada por 1 minuto
        total_time = self.run_test(5, 20, 20, None, "escalabilidade_horizontal")  # Limite de duração de 1 minuto

        # Aqui, podemos usar logs ou contadores para verificar o número de eventos processados
        logging.info(f"Teste de Escalabilidade Horizontal processou eventos em 1 minuto.")

        logging.info("Teste de Escalabilidade Horizontal concluído com sucesso\n")
        return total_time

    def teste_eficiencia(self):
        logging.info("Iniciando Teste de Eficiência")
        # Execução sequencial (para comparação)
        seq_time = self.run_test(1, 1, 10, None, "longa_duracao")
        # Execução paralela
        par_time = self.run_test(5, 5, 10, None, "longa_duracao")
        
        # Calculando a aceleração
        speedup = seq_time / par_time
        logging.info(f"Aceleração (Speedup): {speedup:.2f}")

        # Calculando a eficiência
        num_processadores = 5
        eficiencia = speedup / num_processadores
        logging.info(f"Eficiência: {eficiencia:.2f}")

        logging.info("Teste de Eficiência concluído com sucesso\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Executa testes de desempenho e escalabilidade.')
    parser.add_argument('--teste', type=str, choices=['longa_duracao', 'tempo_resposta', 'escalabilidade_vertical', 'escalabilidade_horizontal', 'eficiencia'], required=True, help='Escolha qual teste executar')
    args = parser.parse_args()

    suite = unittest.TestSuite()
    if args.teste == 'longa_duracao':
        suite.addTest(TesteProgramaParalelo("teste_longa_duracao"))
    elif args.teste == 'tempo_resposta':
        suite.addTest(TesteProgramaParalelo("teste_tempo_resposta"))
    elif args.teste == 'escalabilidade_vertical':
        suite.addTest(TesteProgramaParalelo("teste_escalabilidade_vertical"))
    elif args.teste == 'escalabilidade_horizontal':
        suite.addTest(TesteProgramaParalelo("teste_escalabilidade_horizontal"))
    elif args.teste == 'eficiencia':
        suite.addTest(TesteProgramaParalelo("teste_eficiencia"))

    runner = unittest.TextTestRunner()
    runner.run(suite)