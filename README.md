# T1-INE5645

Esse projeto é parte da avaliação da disciplina INE5645 - da UFSC, que implementa em código Python o algoritmo conforme os requisitos do PDF `INE5645_trabalho1.pdf`.

## Acadêmicos

- Gabriel Terra
- Pedro
- Vanessa Cunha - 17100926

## Dúvidas

- [x] Falhas na execução das subtarefas: O código agora simula falhas durante a execução das subtarefas, com uma probabilidade de 20% de falha em cada operação.
- [x] Fork-join: O modelo fork-join está implicitamente presente no código. Cada tarefa de processamento de dados sensoriais (fork) é seguida por uma operação de "join" na Central de Controle, agregando os resultados.
- [x] Impressão de mensagens no painel: O código imprime uma mensagem cada vez que um atuador é alterado e garante que nada seja impresso por 1 segundo após a impressão da mensagem, usando `time.sleep(1)`.
- [x] Divisão de tarefas em subtarefas: A divisão de tarefas está implicitamente presente, pois cada tarefa de processamento de dados sensoriais envolve duas operações independentes: alterar o nível de atividade do atuador e enviar a mudança ao painel.

## Requisitos

- [x] Python 3.6 ou superior.
- [x] Biblioteca `random` (incluída na biblioteca padrão).
- [x] Biblioteca `time` (incluída na biblioteca padrão).
- [x] Biblioteca `multiprocessing` (incluída na biblioteca padrão).
- [x] Biblioteca `concurrent.futures` (incluída na biblioteca padrão).
- [x] Biblioteca `argparse` (incluída na biblioteca padrão).

## Execução

Para executar `t1.py` é necessário ter Python 3.6 ou superior instalado. As bibliotecas necessárias já estão incluídas na biblioteca padrão do Python, portanto, não édeve ser necessário instalá-las separadamente, mas por precaução listamos elas acima.

Para rodar o programa, utilize os seguintes comandos, informando apenas o número de sensores e atuadores:

```sh
python t1.py --sensores 10 --atuadores 5
```

Ou no Mac:

```sh
python3 t1.py --sensores 10 --atuadores 5
```

Também é possível informar o número de sensores, atuadores e o número máximo de eventos para execução em testes rápidos:

```sh
python t1.py --sensores 10 --atuadores 5 --eventos 10
```

Ou no Mac:

```sh
python3 t1.py --sensores 10 --atuadores 5 --eventos 10
```
