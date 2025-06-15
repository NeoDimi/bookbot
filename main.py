from stats import count_words, count_characters

def get_book_text(file_path: str) -> str:
    #Reads the content of a book file and returns it as a string.
    with open(file_path, 'r', encoding='utf-8') as file:
        text_file = file.read()
        return text_file

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    words_count = count_words(book_text)
    print(f"{words_count} words found in the document.")
    character_dict = count_characters(book_text)
    print(f"{character_dict}")

main()