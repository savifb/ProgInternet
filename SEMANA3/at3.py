usuario = {}
perg_respostas = {}

while True:
    nome = input('Digite o nome do usuário: ')
    dengue = input('Ja teve dengue? ')
    covid = input('Já teve covid? ')
    comorbidade = input('Tem alguma comorbidade? ')
    risco = input('Pertence a algum grupo de risco? ')
    perg_respostas['Dengue'] = dengue
    perg_respostas['Covid'] = covid
    perg_respostas['Comorbidade'] = comorbidade
    perg_respostas['Risco'] = risco
    usuario[nome] = perg_respostas
    consulta = input('Deseja continuar com o preenchimento de dados?\nCaso queira sair digite "s".')
    if consulta == 's':
        break

print(usuario)