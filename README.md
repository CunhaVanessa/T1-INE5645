# T1-INE5645

Esse projeto é parte da avaliação da disciplina INE5645 - da UFSC, que implementa em código Python o algoritmo conforme os requisitos do PDF `INE5645_trabalho1.pdf`.

## Acadêmicos

- Gabriel Terra
- Pedro
- Vanessa Cunha - 17100926

## Requisitos

- [x] Python 3.6 ou superior.
- [x] Biblioteca `random` (incluída na biblioteca padrão).
- [x] Biblioteca `time` (incluída na biblioteca padrão).
- [x] Biblioteca `multiprocessing` (incluída na biblioteca padrão).
- [x] Biblioteca `concurrent.futures` (incluída na biblioteca padrão).
- [x] Biblioteca `argparse` (incluída na biblioteca padrão).
- [x] Biblioteca `unittest` (incluída na biblioteca padrão).
- [x] Biblioteca `psutil` (não incluída na biblioteca padrão).

## Execução

Para executar t1.py e test_t1.py, é necessário ter Python 3.6 ou superior instalado. As bibliotecas necessárias já estão incluídas na biblioteca padrão do Python, exceto psutil, que deve ser instalada separadamente.

### Instalação de Dependências

Instale a biblioteca psutil com o seguinte comando:

```sh
pip install psutil
```

### Execução do t1.py

Para rodar o programa t1.py, utilize os seguintes comandos, informando apenas o número de sensores e atuadores:

```sh
python t1.py --sensores 10 --atuadores 5
```

Também é possível informar o número de sensores, atuadores e o número máximo de eventos para execução em testes rápidos:

```sh
python t1.py --sensores 10 --atuadores 5 --eventos 10
```

Além disso também é possível adicionar um nível maior de debug com a seguinte flag:

```sh
python t1.py --sensores 10 --atuadores 5 --eventos 10 --debug
```

### Execução do test_t1.py

Para executar os testes automatizados definidos em test_t1.py, utilize o seguinte comando, especificando o teste desejado:

```sh
python test_t1.py --teste <nome_do_teste>
```

Os nomes dos testes disponíveis são: longa_duracao, tempo_resposta, escalabilidade_vertical, escalabilidade_horizontal, e eficiencia. Exemplo:

```sh
python test_t1.py --teste longa_duracao
```