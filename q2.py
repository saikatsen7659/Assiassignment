word_count = {}
with open('sentences.txt', 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

for word, count in word_count.items():
    print({word: count})

