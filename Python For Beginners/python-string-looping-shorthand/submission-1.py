def print_string_characters_one_word(word: str) -> None:
    for i in range(len(word)):
        print(word[i])

def print_string_characters(word1: str, word2: str) -> None:
    print_string_characters_one_word(word1)
    print_string_characters_one_word(word2)




# do not modify below this line
print_string_characters("Hello, World!", "Good Job!")
