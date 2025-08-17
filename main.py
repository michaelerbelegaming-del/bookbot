import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        book = get_book_text(file_path)
        num_words = count_words(book)
        num_chars = count_characters(book)
        sorted = sort_dict(num_chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for entry in sorted:
            if entry["name"].isalpha():
                print(f"{entry["name"]}: {entry["num"]}")
        print("============ END ============")

main()