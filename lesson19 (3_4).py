# Самостоятельная работа по уроку "Произвольное число параметров"

def single_root_words(root_word,*other_word):
    same_words = []
    for curr_word in other_word:
        if curr_word.lower() in root_word.lower() or root_word.lower() in curr_word.lower():
            same_words.append(curr_word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)