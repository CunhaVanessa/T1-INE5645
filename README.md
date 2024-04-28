# T1-INE5645
Esse projeto é parte da avaliação da disciplina INE5645 - da UFSC, que implementa em código python o algoritmo conforme os requisitos do PDF `INE5645_trabalho1.pdf`. 


# Acadêmicos
- Gabriel Terra
- Pedro
- Vanessa Cunha - 17100926

# Dúvidas:
- [x] Falhas na execução das subtarefas: O código atual não simula falhas durante a execução das subtarefas. Você pode adicionar essa funcionalidade adicionando um bloco try/except dentro da função processar_dado_sensorial e lançando uma exceção com uma probabilidade de 20%.
- [x] Fork-join: O código atual não implementa explicitamente o modelo fork-join. No entanto, você pode argumentar que o modelo fork-join está implicitamente presente, pois cada tarefa de processamento de dados sensoriais (que pode ser vista como uma tarefa "fork") é seguida por uma operação de "join" quando os resultados são agregados na Central de Controle.
- [x] Impressão de mensagens no painel: O código atual imprime uma mensagem cada vez que um atuador é alterado, mas não garante que nada seja impresso por 1 segundo após a impressão da mensagem. Você pode adicionar essa funcionalidade usando a função time.sleep(1) após a impressão da mensagem.
- [x] Divisão de tarefas em subtarefas: O código atual não divide explicitamente a tarefa de processamento de dados sensoriais em subtarefas. No entanto, você pode argumentar que a divisão de tarefas está implicitamente presente, pois cada tarefa de processamento de dados sensoriais envolve duas operações independentes: alterar o nível de atividade do atuador e enviar a mudança ao painel.

# Requisitos
- [x] Python 3.6 ou superior.
- [x] Biblioteca `random`.
- [x] Biblioteca `time`.
- [x] Biblioteca `multiprocessing`.
- [x] Biblioteca `concurrent.futures`.
- [x] Biblioteca `argparse`.

# Execução

Para executar `t1.py` é necesário primeiro baixar as bibliotecas citadas na seção acima, desta maneira:


```
pip install random
pip install time
pip install multiprocessing
pip install concurrent.futures
pip install argparse
```

ou se estiver no Mac:

```
pip3 install random
pip3 install time
pip3 install multiprocessing
pip3 install concurrent.futures
pip3 install argparse
```


Agora com todas as depedências instaladas você pode rodar `t1.py` das seguintes maneiras:

Informando apenas o número de sensores e atuadores:

```
python t1.py --sensores 10 --atuadores 5

```
ou no Mac:

```
python3 t1.py --sensores 10 --atuadores 5

```

Ou também informando o número de sensores, atuadores e o número máximo de eventos que queira que sejam executados, em caso de testes rápidos:

```
python t1.py --sensores 10 --atuadores 5 --eventos 10

```
ou no Mac:

```
python3 t1.py --sensores 10 --atuadores 5 --eventos 10

```