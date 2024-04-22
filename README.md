# T1-INE5645
Esse projeto é parte da avaliação da disciplina INE5645 - da UFSC, que implementa em código python o algoritmo conforme os requisitos do PDF `INE5645_trabalho1.pdf`. 


# Acadêmicos
- Gabriel Terra
- Pedro
- Vanessa Cunha - 17100926

# Em andamento:
- [x] Modelo produtor/consumidor: O código implementa o modelo produtor/consumidor. Os sensores (produtores) geram dados aleatórios e a Central de Controle (consumidor) processa esses dados.
- [x]  Pool de threads: O código usa o módulo multiprocessing para criar processos separados para cada sensor. No entanto, não está claro se a Central de Controle opera sobre várias unidades de processamento, como exigido.
- [x]  Fork-join: O código não implementa explicitamente o modelo fork-join. Para cada dado sensorial recebido, a Central de Controle define um atuador e um nível de atividade, mas não há divisão explícita de tarefas em subtarefas que são então reunidas.
- [x] Falhas: O código não implementa a possibilidade de falhas na execução das subtarefas.
- [x] Exclusão mútua: O código usa um multiprocessing.Lock para garantir a exclusão mútua ao acessar a tabela de atuadores, o que está de acordo com os requisitos.
- [x]  Parametrização: O número de sensores e atuadores é parametrizável, mas está codificado diretamente no código. Seria melhor se esses valores pudessem ser passados como argumentos para o programa.
- [X] Impressão na tela: O código imprime as alterações no nível de atividade do atuador, mas não garante que nada seja impresso por 1 segundo após a mensagem.

# Requisitos

- [x] Python 3.6 ou superior.
- [x] Biblioteca `random`.
- [x] Biblioteca `time`.
- [x] Biblioteca `threading`.

# Execução

Para executar o código, basta rodar o arquivo `t1.py` no terminal.

```
python t1.py
```

ou

```
python3 t1.py
```
