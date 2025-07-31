import sys
from stats import count_words, count_characters, sort_char_count

def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_counts = count_characters(text)
    char_stats = sort_char_count(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_stats:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()