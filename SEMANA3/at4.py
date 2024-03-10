
num = int(input("Digite um número para ver sua tabuada: "))

def fazTabuada(numero):    
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    
fazTabuada(num)