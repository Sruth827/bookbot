import sys
from stats import word_count, character_count, char_sorted

def get_book_text(filepath):
    with open(filepath) as f:
        text_contents = f.read()
    return text_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)

    #count total words in book 
    total_words = word_count(text)
    
    #count then sort list of characters found in words of book
    char_list = char_sorted(character_count(text))
    char_list.sort(reverse=True, key=lambda x: x["count"])
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    # Assume `total_words` is calculated somewhere earlier in your code
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    
    for items in char_list:
        char = items["char"]
        count = items["count"]
        if char.isalpha(): 
            print(f"{char}: {count}")

    print("============= END ===============")


main()
