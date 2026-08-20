# ANOTAÇÕES - PYTHON / JSON / CRUD

## O QUE É UMA BIBLIOTECA?
tenta explicar

--> biblioteca é um bagulho que se bota no código que meio que te dá as coisas
que você precisa pra programar, mano. Alguém já escreveu um monte de código
pronto e guardou tudo num pacote, aí você só importa e usa.

`IMPORT` --> chama a biblioteca pro seu código
= todas as ferramentas que ela te dá disponíveis pra usar


## E O QUE VOCÊ ENTENDEU DE JSON?

JSON é um jeito de guardar e transferir dados sem precisar de um banco de
dados de verdade, forma simples. Pra usar, funciona com key-item (tipo um
dicionário), meio como uma tabela do SQL (CSV --> tabela). É basicamente
o formato que se usa pra guardar os dados.

```python
import json
```

**Modos de abrir arquivo:**
- `"r"` --> READ (ler o que já tá no arquivo)
- `"w"` --> WRITE (cria o arquivo se ele não existir, OU APAGA TUDO e
  escreve por cima se ele já existir)
- `"a"` --> APPEND (adiciona lá no final do arquivo, não apaga nem
  reescreve nada que já tava lá)


## CRUD

**CREATE, READ, UPDATE, DELETE**

Isso é o conceito. Na prática (tipo numa API), cada verbo HTTP resolve
uma dessas ações:

| Verbo HTTP | Ação do CRUD | O que faz |
|---|---|---|
| POST | Create | cria um dado novo |
| GET | Read | busca/lê os dados |
| PUT | Update | atualiza TODOS os dados de um objeto |
| PATCH | Update | atualiza só 1 ou alguns campos do objeto |
| DELETE | Delete | apaga o dado |


## SINTAXE

**1. Importa a biblioteca**
```python
import json
```

**2. Abre o arquivo**
```python
with open(caminho, modo, encoding="utf-8") as arquivo:
```
- `caminho` = caminho do arquivo (ex: `"lanchonete_dados.json"`)
- `modo` = `"r"`, `"w"` ou `"a"` (sempre entre aspas, é string!)
- `encoding` = `"utf-8"` (evita bug com acento/ç)

```python
with open("lanchonete_dados.json", "r", encoding="utf-8") as arquivo:
```

**3. Lendo o arquivo (JSON --> Python)**
```python
json.load(arquivo)  # lê o arquivo e transforma em dict (ou list), NÃO em string
```

**4. Escrevendo no arquivo (Python --> JSON)**
```python
json.dump(objeto, arquivo, indent=4, ensure_ascii=False)
```
- `indent=4` --> deixa bonitinho/organizado pra um humano ler
- `ensure_ascii=False` --> deixa salvar acento normal, sem virar `\uXXXX`

```python
with open("lanchonete_dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)
```


## 5. TRATAMENTO DE ERRO (ERRO NÃO É BUG!)

Se no input você espera um número inteiro e a pessoa digita uma letra,
o que acontece? --> dá um **ValueError**

```python
while True:
    try:
        num = int(input(""))
        print("você digitou o número", num)
    except ValueError:
        print("escreve um número porra!!!!")
```


## 6. json.JSONDecodeError

É o erro que o Python solta quando tenta LER um JSON e o conteúdo do
arquivo tá malformado (vazio, corrompido, vírgula sobrando, etc). No
projeto, a gente pega esse erro pra o programa não travar se o arquivo
tiver vazio ou bugado.

```python
try:
    return json.load(arquivo)
except json.JSONDecodeError:
    # arquivo existe mas tá vazio/corrompido -> começa do zero
    return {"produtos": [], "pedidos": []}
```


## 7. BIBLIOTECA OS

```python
import os
import json
```

`os` é basicamente uma biblioteca que serve pra mexer com seu sistema
operacional, WOOOW. No projeto uso ela só pra isso aqui:

```python
os.path.exists("lanchonete_dados.json")  # checa se o arquivo já existe
```


## FUNÇÃO

Um algoritmo pré-projetado que pode ser chamado e reutilizado várias vezes.

- **parâmetro** --> a informação que você manda pra dentro da função
- **return** --> o valor que a função devolve pra quem chamou ela
- o **corpo** --> é a programação dentro dela mesmo
- **chamar ela** --> é só escrever o nome + `()` em algum lugar do código

```python
def somar(a, b):        # a e b são os parâmetros
    resultado = a + b    # isso aqui é o corpo da função
    return resultado     # devolve o valor calculado

somar(2, 3)  # chamando a função --> retorna 5
```
