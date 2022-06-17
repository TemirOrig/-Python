words_input = input().split()
print(words_input)
i = 0
k = 1
for word in words_input:
    if len(words_input[i]) > 10:
        print(k, words_input[i][:10], sep=')')
        i += 1
        k += 1
    else:
        print(k, words_input[i], sep=')')
        i += 1
        k += 1
