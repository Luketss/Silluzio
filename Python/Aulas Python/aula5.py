# Funções


def ola_mundo(texto):
    print(texto)


def soma(a, b):
    return a + b


def saudacao(nome):
    print(f"Olá, {nome}!")


def calcular_media(aluno, numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    texto_aluno = f"O aluno {aluno} tem media {media}"
    return media, texto_aluno


notas = [7.5, 8.0, 6.5, 9.0]
media, texto_aluno = calcular_media("Lucas", notas)
print(texto_aluno)
