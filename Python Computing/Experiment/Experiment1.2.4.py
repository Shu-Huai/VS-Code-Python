file = open("D:\Visual Studio Code\Visual-Studio-Code-Python\Python Computing\Experiment\CountingWords.txt")
words = file.readlines()
for i in range(len(words)):
    words[i] = words[i].replace('\n', '')
savedWords = []
wordsCount = []
for word in words:
    if word not in savedWords:
        savedWords.append(word)
        wordsCount.append(1)
    else:
        wordsCount[savedWords.index(word)] = wordsCount[savedWords.index(word)] + 1
print('Frequency of occurrence of the words in "CountingWords.txt":')
for i in range(len(savedWords)):
    print(savedWords[i] + ": " + str(wordsCount[i]))
file.close()
file = open("D:\Visual Studio Code\Visual-Studio-Code-Python\Python Computing\Experiment\CountingWords.txt")
words = file.readlines()
for i in range(len(words)):
    words[i] = words[i].replace('\n', '')
keyWords = input("Please input the keywords: ")
keyWords = keyWords.split()
wordsCount = []
for i in range(len(keyWords)):
    wordsCount.append(0)
for word in words:
    if word in keyWords:
        wordsCount[keyWords.index(word)] = wordsCount[keyWords.index(word)] + 1
sum = 0
for i in range(len(keyWords)):
    sum += wordsCount[i]
wordsFrequency = []
for i in range(len(keyWords)):
    wordsFrequency.append(wordsCount[i] / sum)
print('Frequency of occurrence of the words in "CountingWords.txt" which is in the keywords list:')
for i in range(len(keyWords)):
    print(keyWords[i] + ": " + "%.3f" % wordsFrequency[i])
file.close()