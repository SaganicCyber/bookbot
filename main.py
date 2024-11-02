def read_contents(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1

    return counter

def character_count(text):
    char_dict = {
                'a': 0, 'b': 0, 'c': 0, 'd': 0,
                'e': 0, 'f': 0, 'g': 0, 'h': 0,
                'i': 0, 'j': 0, 'k': 0, 'l': 0,
                'm': 0, 'n': 0, 'o': 0, 'p': 0,
                'q': 0, 'r': 0, 's': 0, 't': 0,
                'u': 0, 'v': 0, 'w': 0, 'x': 0,
                'y': 0, 'z': 0
                }
    words = text.split()
    for word in words:
        word_lowered = word.lower()
        for letter in word_lowered:
            if letter in char_dict:
                char_dict[letter] += 1
    return char_dict

def dict_to_list(char_dict):
    letters=[]
    for key in char_dict:
        letters.append({"letter":key, "num":char_dict[key]})
    return letters
# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries credit: boot.dev
def sort_on(dict):
    return dict["num"]

def print_report(path, count_word, char_dict_list):
    print(f'--- Begin report of {path} ---\n',
        f'{count_word} words found in the document\n')
    for char_dict in char_dict_list:
        print(f"The '{char_dict['letter']}' character was found '{char_dict['num']}' times")
    print('--- End report ---')

def main():
    path = 'books/frankenstein.txt'
    text = read_contents(path)
    count_word = word_count(text)
    char_dict = character_count(text)
    char_dict_list = dict_to_list(char_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    print_report(path, count_word, char_dict_list)

if __name__ == '__main__':
    main()