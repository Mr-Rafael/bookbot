import sys
from stats import *

def read_user_input():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return(sys.argv[1])

def get_book_text(file_path):
    file_contents = ""
    try:
        with open(file_path) as file_object:
            file_contents = file_object.read()
    except Exception as e:
        print(f"Encountered an error while opening the book: {e}")
    return file_contents

def main():
    file_path = read_user_input()
    content_string = get_book_text(file_path)
    word_count = get_word_count_from_string(content_string)
    sorted_count_list = get_character_frequency_report(content_string)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(sorted_count_list)
    print("============= END ===============")

main()