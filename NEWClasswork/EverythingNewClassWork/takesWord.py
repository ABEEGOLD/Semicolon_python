def fundction_that_takes_a_word(word,str_word):
        if len(word)% 2 == 1:
            return word + str_word
        else:
            middle = len(word) // 2
            return word[:middle] + str_word + word[middle:]


print(fundction_that_takes_a_word("ABY","ce"))




