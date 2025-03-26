def get_num_words(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def build_letter_count_dict(book_text):
    letter_count_dict = {}
    words = book_text.split()
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in letter_count_dict:
                letter_count_dict[letter] += 1
            else: 
                letter_count_dict[letter] = 1
    return letter_count_dict

def sort_on(dict):
    return dict["count"]

def create_sorted_letter_list(letter_count_dict):
    list_of_dicts = []
    for k, v in letter_count_dict.items():
        single_letter_dict = dict(letter = k, count = v)
        list_of_dicts.append(single_letter_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
