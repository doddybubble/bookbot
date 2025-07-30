import sys
try:
    print(sys.argv[1])
except Exception:
    print("Usage: python3 main.py <path_to_book>") 
    sys.exit(1)
from stats import (count_number_of_words, get_characters, sort_dictionary)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    number_of_words = count_number_of_words(text)
    all_characters = get_characters(text)
    sorted_dict = sort_dictionary(all_characters)
    print_report(book_path, number_of_words, sorted_dict)
    

def get_book_text(book_path):
    with open(book_path) as f:
       return f.read()

def print_report(book_path, number_of_words, sorted_dict):
    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {book_path}
    ----------- Word Count ---------- 
    Found {number_of_words} total words
    --------- Character Count -------""")
    for i in sorted_dict:
        if i["character name"].isalpha():
            print(f"{i["character name"]}: {i["character number"]}")
    print("============= END ===============") 
    
main()