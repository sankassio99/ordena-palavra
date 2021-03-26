
def bubbleSort(arrayWord):

    newWordArray = []

    for i in range(len(arrayWord)):
        beforeLetter = arrayWord[i]
        print("before " + beforeLetter)
        for s in range(len(arrayWord) - 1):
            afterLetter = arrayWord[s + 1]
            print("After " + afterLetter)
            if (beforeLetter < afterLetter):
                newWordArray.append(beforeLetter)
                newWordArray.append(afterLetter)
                break
            else:
                newWordArray.append(arrayWord[s + 1])
                newWordArray.append(arrayWord[i])
                break

    return newWordArray


print("Ordena letras em ordem alfabeta")
word = input("Digite uma palavra")

arrayWord = []
for w in word:
    arrayWord.append(w)

print(bubbleSort(arrayWord))





