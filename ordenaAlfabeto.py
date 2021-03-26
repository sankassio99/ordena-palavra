def bubbleSort(arrayWord):


    for j in range(len(arrayWord) - 1):
        for s in range(len(arrayWord) - 1):
            if (arrayWord[s] > arrayWord[s+1]):
                arrayWord[s], arrayWord[s+1] = arrayWord[s+1], arrayWord[s]

    return arrayWord


print("Ordena letras em ordem alfabeta")
word = input("Digite uma palavra")

arrayWord = []
for w in word:
    arrayWord.append(w)

print(bubbleSort(arrayWord))
