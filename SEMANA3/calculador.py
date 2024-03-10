def calculadora(a,operador,b):
    resultado = 0
    if operador=='soma':
        resultado = a+b
    elif operador=='multiplicacao':
        resultado = a*b
    elif operador =='divisao':
        resultado = a/b
    elif operador =='subtracao':
        resultado = a-b
    return resultado
print(calculadora(2,'multiplicacao',3))
