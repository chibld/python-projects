import load_dict

words = load_dict.load("words.txt")

anagrams = []

wordToCheck = input("Enter a word or name to find its anagrams: ").lower()

sortedWord = sorted(wordToCheck)

for word in words:
    word = word.lower()
    if word != wordToCheck:
        if sorted(word) == sortedWord:
            anagrams.append(word)

if len(anagrams) == 0:
    print("No anagrams found :(")
else:
    print("Anagrams are:", *anagrams, sep='\n')
