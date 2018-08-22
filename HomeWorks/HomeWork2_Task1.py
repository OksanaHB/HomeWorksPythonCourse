import this
def print_count_of_word(word,words_list):
    print("Count of word \"{}\" is ".format(word.lower()), words_list.count(word.upper()))
text_phylosofhy="".join([this.d.get(c, c) for c in this.s])
text_phylosofhy_upper=text_phylosofhy.upper()
words_list = text_phylosofhy_upper.split()
print("\nA:")
print_count_of_word("better",words_list)
print_count_of_word("never",words_list)
print_count_of_word("is",words_list)
print("\nB:")
print(text_phylosofhy_upper)
print("\nC:")
print(text_phylosofhy.replace("i","&"))