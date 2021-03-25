
print("Ordena letras em ordem alfabeta")
word = input("Digite uma palavra")

vetor = []
palavraOrdenada = ''

for w in word:
    vetor.append(w)

palavraOrdenada = sorted(vetor)
print(palavraOrdenada)
