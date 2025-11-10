import load_dict

word_list = load_dict.load('words.txt')


def find_palingrams():
    palingrams = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    palingrams.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    palingrams.append((rev_word[:end-i], word))
    return palingrams


palingrams_sorted = sorted(find_palingrams())

print("Number of palingrams: {}".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
