def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_characters(file_contents)

def count_words(content):
    words = content.split()
    print(len(words))

def count_characters(content):
    character_count = {}
    content = content.lower()
    for char in content:
        if (char not in character_count):
            character_count[char] = 0
        character_count[char] += 1
    print(character_count)

main()