def IsAbbreviable(word):
    global maxLength, words, abbreviableWords, unabbreviableWords
    if len(word) > 1:
        for i in range(len(word)):
            abbrevedWord = word[:i] + word[i + 1:]
            if abbrevedWord in abbreviableWords or abbrevedWord in words and abbrevedWord not in unabbreviableWords and IsAbbreviable(abbrevedWord) is not None:
                abbreviableWords.add(word)
                maxLength = max(maxLength, len(word))
                return word
    unabbreviableWords.add(word)
    return None


def printLongestWord(word, *, root: bool = True):
    global words
    arrow = ' → '
    if len(word) > 1:
        for i in range(len(word)):
            abbrevedWord = word[:i] + word[i + 1:]
            if abbrevedWord in {'a', 'i'}:
                print(abbrevedWord, end=arrow)
                break
            elif abbrevedWord in words and printLongestWord(abbrevedWord, root=False) is not None:
                break
        else:
            return None
    print(word, end=' ({})\n'.format(len(word)) if root else arrow)
    return word


with open(r".\Python Computing\Experiment\words.txt") as wordsFile:
    words = [word.strip("\n") for word in wordsFile if "a" in word or "i" in word]
words = set(words)
abbreviableWords = {"a", "i"}
unabbreviableWords = set()
maxLength = 1
result = "a"
for word in words:
    if len(word) > maxLength:
        word = IsAbbreviable(word)
        if word is not None:
            result = word
printLongestWord(result)
