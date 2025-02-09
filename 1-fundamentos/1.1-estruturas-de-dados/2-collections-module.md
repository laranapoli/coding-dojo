# Collections

O módulo `collections`do Python fornece estruturas de dados especializadas que estendem as funcionalidades built-in. É útil para melhorar a eficiência e legibilidade do código ao lidar com coleções de dados mais complexas.

## Principais estruturas
- `Counter`: Conta a frequência de elementos em uma sequência
- `defaultdict`: `dict`que define um valor padrão para chaves ausentes
- `OrderedDict`: `dict` que mantém a ordem de inserção dos elementos (< Python 3.7)
- `deque`: Lista otimizada para inserções e remoções rápidas nas extremidades
- `namedtuple`: Semelhante a `tuple`, mas com nomes para os campos.

## Exemplos 

```python
from collections import Counter, defaultdict, deque, namedtuple

# Contar elementos em uma lista
contagem = Counter("banana")  
print(contagem)  # Saída: Counter({'a': 3, 'n': 2, 'b': 1})

# Criar um dicionário com valor padrão
d = defaultdict(int)
d["x"] += 1  
print(d)  # Saída: defaultdict(<class 'int'>, {'x': 1})

# Criar e acessar um namedtuple
Pessoa = namedtuple("Pessoa", "nome idade")
p = Pessoa("Lara", 27)
print(p.nome)  # Saída: Lara

# Usar deque para operações eficientes
fila = deque([1, 2, 3])
fila.appendleft(0)
fila.pop()
print(fila)  # Saída: deque([0, 1, 2])

```


# Counter
- Subclasse do dicionário
- Usado para contar elementos de maneira iterábel de um dicionário não ordenado 
- As chaves representam os elementos do iterável e os valores, a contagem do elemento no iterável

```python
from collections import Counter
  
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
  
# with dictionary
count = Counter({'A':3, 'B':5, 'C':2})
print(count)

count.update(['A', 1])
print(count)

```

# OrderedDict
- Subclasse de dicionário, mas retém a ordem em que as chaves foram inseridas.

# DefaultDict
- Usado para prove default values para chaves que ainda não existem
- Nunca levanta um `KeyError`
- Objetos inicializados usando o método `DefaultDict`e passando um tipo de dados como argumento

# ChainMap
- Encapsula vários dicionários em um e retorna a lista de dicionários
- Quando uma chave precisa ser achada, todos os dicionários são percorridos um por um até que a chave seja encontrada

```python
from collections import ChainMap
    
    
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
    
# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)       # ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

print(c['a'])  # Output: 1
print(c['g'])  # Output: KeyError: 'g'

```