import sys
from stats import count_words,count_character,sort_list


def get_book_text(book_path):
    with open(book_path, "r", encoding="utf-8") as f:
        return f.read()



def main(book_path):
    # book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    character_count = sort_list(count_character(book_text))
    print(f'Found {word_count} total words')
    for item in character_count:
        print(f"{item['character']}: {item['count']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 mainpy <path_to_book>')
        sys.exit(1)
    else:
        main(sys.argv[1])
