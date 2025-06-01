import stats

def get_book_text(filepath: str) -> str: 
    content = ""
    with open(filepath) as f:
        content = f.read()

    return content

def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = stats.get_num_words(book_content)
    print(f"{num_words} words found in the document")

    char_count = stats.get_char_count(book_content)
    print(f"charcount: {char_count}")

main()