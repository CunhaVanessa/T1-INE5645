# T1-INE5645
Esse projeto é parte da avaliação da disciplina INE5645 - da UFSC, que implementa em código python o algoritmo conforme os requisitos do PDF `INE5645_trabalho1´. 


# Acadêmicos
- Gabriel Terra
- Pedro
- Vanessa Cunha - 17100926

# Em andamento:

- [] Modelo produtor/consumidor: O código implementa o modelo produtor/consumidor. Os sensores (produtores) geram dados aleatórios e a Central de Controle (consumidor) processa esses dados.

- [] Pool de threads: O código usa o módulo multiprocessing para criar processos separados para cada sensor. No entanto, não está claro se a Central de Controle opera sobre várias unidades de processamento, como exigido.

- [] Fork-join: O código não implementa explicitamente o modelo fork-join. Para cada dado sensorial recebido, a Central de Controle define um atuador e um nível de atividade, mas não há divisão explícita de tarefas em subtarefas que são então reunidas.

- [] Falhas: O código não implementa a possibilidade de falhas na execução das subtarefas.

- [] Exclusão mútua: O código usa um multiprocessing.Lock para garantir a exclusão mútua ao acessar a tabela de atuadores, o que está de acordo com os requisitos.

- [-] Parametrização: O número de sensores e atuadores é parametrizável, mas está codificado diretamente no código. Seria melhor se esses valores pudessem ser passados como argumentos para o programa.

- [-] Impressão na tela: O código imprime as alterações no nível de atividade do atuador, mas não garante que nada seja impresso por 1 segundo após a mensagem.

# Requisitos

- [x] Python 3.6 ou superior.
- [x] Biblioteca `random`.
- [x] Biblioteca `time`.
- [x] Biblioteca `threading`.

# Execução

Para executar o código, basta rodar o arquivo `t1.py` no terminal.

```
python t.py
```

ou

```
python3 t1.py
```
