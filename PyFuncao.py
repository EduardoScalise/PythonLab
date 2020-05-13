# Definindo uma função
def primeiraFunc():
    print('Hello World!')
    
primeiraFunc()

# Definindo uma função com parâmetro
def primFunc(nome):
    print('Welcome %s' %(nome))

primFunc(input('What\'s your name: '))

def funcLeitura():
    for i in range(0, 5):
        print("Número " + str(i))
        
funcLeitura()

def addNum(firstNum, secondNum):
    print('Primeiro número: ' + str(firstNum))
    print('Segundo número: ' + str(secondNum))
    print('Soma: ' , firstNum + secondNum)

addNum(27, 8)
