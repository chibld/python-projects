import load_dict

word_list = load_dict.load('words.txt')

palindromes = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        palindromes.append(word)

print("Number of palindromes found: {}".format(len(palindromes)))
print(palindromes, sep="\n")
