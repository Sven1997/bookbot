import sys
from stats import get_word_count
from stats import get_count_per_character
from stats import get_sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    contents = get_book_text(path_to_file)
    num_words = get_word_count(contents)
    charcter_dict = get_count_per_character(contents)
    sorted_list = get_sorted_list(charcter_dict)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()