def break_words(stuff):
    print(">>> break_words", stuff)
    """This function will break up words for us."""
    words = stuff.split(' ')
    print("<<< exit break_words")
    return words

def sort_words(words):
    print(">>> sort_words", words)
    """Sots the words."""
    return sorted(words)
    print("<<< exit sort_words")

def print_first_word(words):
    print(">>> print_first_word", words)
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
    print("<<< exit print_first_word")

def print_last_word(words):
    print(">>> print_last_word", words)
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
    print("<<< exit print_last_word")

def sort_sentence(sentence):
    print(">>> sort_sentence", sentence)
    """Takes in a full sentence and returns the sorted words>"""
    words = break_words(sentence)
    return sort_words(words)
    print("<<< exit sort_sentence")

def print_first_and_last(sentence):
    print(">>> print_first_and_last", sentence)
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    print("<<< print_first_and_last")

def print_first_and_last_sorted(sentence):
    print(">>> print_first_and_last_sorted", sentence)
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    print("<<< print_first_and_last_sorted")
