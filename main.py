from stats import get_num_words, get_chars_dict, sort_chars
import sys
import glob

def get_book_text(path):
    with open(path) as f:
        return f.read()

def analyze_book(path):
    text = get_book_text(path)
    num_words = get_num_words(text)
    char_dict = get_chars_dict(text)
    sorted_list = sort_chars(char_dict)

    print("=========== SUPERCOUNT ===========")
    print(f"Analyzing: {path}")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count --------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============== END ===============\n")

def main():
    if len(sys.argv) < 2:
        print("=========== SUPERCOUNT ===========")
        print("No file provided. Enter a file path or glob pattern.")
        print("Examples: books/frankenstein.txt  |  books/*.txt")
        path = input("Path: ").strip()
        if not path:
            print("No path entered. Exiting.")
            sys.exit(1)
        args = [path]
    else:
        args = sys.argv[1:]

    files = []
    for pattern in args:
        expanded = glob.glob(pattern, recursive=True)
        if expanded:
            files.extend(sorted(expanded))
        else:
            files.append(pattern)

    for path in files:
        analyze_book(path)

main()
