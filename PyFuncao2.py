#Demonstração de funções em Python
import math

def numPrimo(num):
    '''verificando se um número
       é primo.
    '''
    if (num % 2) == 0 and (num > 2):
        return 'Este número não é primo'
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return 'Este número não é primo'
    return 'Este número é primo'

numPrimo(541)

numPrimo(int(input('Digite um número: ')))

# Fazendo split dos dados
def split_string(texto):
    return texto.split(" ")

frase = "Esta função é bastante útil para separar grandes volumes de dados."

# isso divide a string em uma lista
print(split_string(frase))

# Podemos atribuir o output de uma função, para uma variável
token = split_string(frase)

print(token)

caixa_baixa = "Este Texto Será Convertido TODO em LowerCase"

print(caixa_baixa)

def lowercase(text):
    return text.lower()

print(lowercase(caixa_baixa))

# Funções com número variável de argumentos
def printVarInfo( arg1, *vartuple ):
    # Imprimindo o valor do primeiro argumento
    print("O parâmetro passado foi: ", arg1)
    
    # Imprimindo o valor do segundo parâmetro
    for item in vartuple:
        print("O parâmetro passado foi: ", item)
    return;

printVarInfo(39)

printVarInfo('Chocolate', 'Café', 'Leite', 'Pão', 'Frutas')
