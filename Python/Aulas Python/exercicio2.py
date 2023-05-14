# Programa - Criação de personagem
# Com o programa criado na aula 1 de exercícios, utilize uma estrutura de condição para checar qual o maior atributo do personagem

nome = input('Digite o nome do seu personagem: ')

forca = int(input('Digite o valor da força do personagem: '))
magia = int(input('Digite o valor da magia do personagem: '))

habilidade = input('Digite o nome da habilidade do personagem: ')

if forca > magia:
    print(f'O personagem {nome} é um gerreiro')
elif magia > forca:
    print(f'O personagem {nome} é um mago')
else:
    print(f'O personagem {nome} ainda precisa definir pra onde ir')

print(f'O personagem {nome} tem força igual a {forca} e tem magia igual a {magia}')
print(f'Sua habilidade principal é {habilidade}')