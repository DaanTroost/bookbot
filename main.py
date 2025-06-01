def get_book_text(filepath: str) -> str: 
    content = ""
    with open(filepath) as f:
        content = f.read()

    return content

def count_words(content: str) -> int:
    return len(content.split(None))

def main():
    book_content = get_book_text("books/frankenstein.txt")
    num_words = count_words(book_content)
    print(f"{num_words} words found in the document")

main()