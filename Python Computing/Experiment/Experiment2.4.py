file = open("D:\Visual Studio Code\Visual-Studio-Code-Python\Python Computing\Experiment\CountingWords.txt")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
reversedwords = []
counts = []
for line in lines:
    if line not in reversedwords:
        reversedwords.append(line)
        counts.append(1)
    else:
        counts[reversedwords.index(line)] = counts[reversedwords.index(line)] + 1
for i in range(len(reversedwords)):
    print(reversedwords[i] + ": " + str(counts[i]))
