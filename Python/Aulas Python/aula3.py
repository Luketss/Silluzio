# operadores -> == != > < >= <=
# is not and

idade = 17

if idade >= 18:
    print('Maior de idade')
elif idade >= 16 and idade < 18:
    print("Quase maior de idade")
else:
    print("Menor de idade")

for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero)
