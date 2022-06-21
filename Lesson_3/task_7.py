def int_func(words_list_lower):
    words_list_cap = [word.capitalize() for word in words_list_lower]
    i = 0
    while i <= len(words_list_cap) - 1:
        print(words_list_cap[i], end="| ")
        i += 1


int_func(input().split())


