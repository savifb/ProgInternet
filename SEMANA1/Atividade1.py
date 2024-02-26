def remove_espaco(dado):
    dado = dado.lstrip()
    return dado
def preenche_formulario():
    nome = input('Digite seu nome: ')
    nome = remove_espaco(nome)
    idade = int(input("Digite sua idade: "))
    altura = float(input('Digite sua altura: '))
    dados['nome'] = nome
    dados['idade'] = idade
    dados['altura'] = altura
def retorna_caracteres(nome):
    nome = nome[:5]
    return nome
def imprimi_formulario():
    print(f"Nome: {dados['nome']}")
    print(f'Idade: {dados['idade']}')
    print(f'Altura: {dados['altura']}')
dados = {}
preenche_formulario()
imprimi_formulario()
print(retorna_caracteres(dados['nome']))