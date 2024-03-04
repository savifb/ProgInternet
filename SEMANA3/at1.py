dados_alunos = {}
disciplinas = []
print('Bem-vindo(x) ao sistema de cadastramento de aluno e disciplinas! ')
while True:
    nome = input("Qual o nome do aluno: ")
    qtd_disciplina = int(input('Digite a quantidade de disciplinas para cadastrar: '))
    for i in range(qtd_disciplina):
        disciplina= input('Qual a disciplina? ')
        disciplinas.append(disciplina)
    dados_alunos[nome] = disciplinas
    continuar = input('Digite s se quiser sair: ')
    if continuar == 's':
        break


print(dados_alunos)
