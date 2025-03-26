from stats import get_num_words
from stats import build_letter_count_dict
from stats import create_sorted_letter_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        word_count = get_num_words(get_book_text(book_path))
        letter_count_dict = build_letter_count_dict(get_book_text(book_path))
        sorted_list = create_sorted_letter_list(letter_count_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for dict in sorted_list:
            if dict['letter'].isalpha():
                print(f"{dict['letter']}: {dict['count']}")


main()