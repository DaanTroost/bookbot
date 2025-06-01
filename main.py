import stats
import sys

def get_book_text(filepath: str) -> str: 
    content = ""
    with open(filepath) as f:
        content = f.read()

    return content

def main(args):
    if len(args) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = stats.get_num_words(book_content)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_count = stats.get_char_count(book_content)
    charlist = stats.get_sorted_char_count(char_count)
    for entry in charlist:
        if entry["char"].isalpha():
            print(f'{entry["char"]}: {entry["num"]}')
    print("============= END ===============")

main(sys.argv)