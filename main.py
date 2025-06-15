from stats import count_words, count_characters, list_dict_characters, sort_list
import sys

def get_book_text(file_path: str) -> str:
    #Reads the content of a book file and returns it as a string.
    with open(file_path, 'r', encoding='utf-8') as file:
        text_file = file.read()
        return text_file

def main():
    #print(sys.argv)
    #book_path = "books/frankenstein.txt"
    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python3 main.py <path_to_book>")
    except ValueError as e:
        print(e)
        sys.exit(1)
    #The try-except block checks if the user did not forget to give a second argument in the CLI (the path)
    #There is no data validation however and if the second argument is there but not a valid path to a txt file, the program will crash

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words_count = count_words(book_text)
    character_dict = count_characters(book_text)
    #print(f"{character_dict}")
    list_dict_unsorted = list_dict_characters(character_dict)
    list_dict_sorted = sort_list(list_dict_unsorted)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {words_count} total words")
    print("--------- Character Count -------")
    for d in list_dict_sorted:
        if d["name"].isalpha():
            print(f"{d["name"]}: {d["count"]}")
    #print(list_dict_sorted)
    print("============= END ===============")


main()