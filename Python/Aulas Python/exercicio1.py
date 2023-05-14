# Crie um programa utilizando os conhecimentos apresentados nas aulas 1 e 2. 
# Programa - Criação de personagem
# O objetivo é criar um programa que simule a criação de personagem, o usuário deve inserir o nome do personagem, nível de força
# nível de magia e o nome da habilidade principal. O nível de força e magia deve ser transformado para inteiro.
# Ao final, escreva na tela o todos os dados coletados.

nome = input('Digite o nome do seu personagem: ')

forca = int(input('Digite o valor da força do personagem: '))
magia = int(input('Digite o valor da magia do personagem: '))

habilidade = input('Digite o nome da habilidade do personagem: ')

print(f'O personagem {nome} tem força igual a {forca} e tem magia igual a {magia}')
print(f'Sua habilidade principal é {habilidade}')