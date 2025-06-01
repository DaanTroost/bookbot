def get_book_text(filepath: str) -> str: 
    content = ""
    with open(filepath) as f:
        content = f.read()

    return content

def main():
    print(get_book_text("books/frankenstein.txt"))

main()