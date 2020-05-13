# Definindo uma função
def primeiraFunc():
    print('Hello World!')
    
primeiraFunc()

# Definindo uma função com parâmetro
def primFunc(nome):
    print('Welcome %s' %(nome))

# Chamando a função e passando parãmetro (Neste caso solicitando o nome - entrada
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

addNum(int(input('Entre com o primeiro número: ')), int(input('Entre com o segundo número: ')))

array = ['a', 'b', 'c', 'd', 'e']
print(array)
print(max(array))
print(min(array))

array2 = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']
print(array2)
print(max(array2))
print(min(array2))

list1 = [17, 9, 22, 35, 46]
print(sum(list1))
