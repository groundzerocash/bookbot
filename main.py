path_to_file = 'books/frankenstein.txt'

def count_words(text):
    words = text.split()
    num_of_words = len(words)

    return num_of_words

def count_characters(text):
    text_adj = text.lower()
    char_count = {}

    for char in text_adj:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1


    
    return char_count

def sort_on(dict):
    return dict['char']

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    
    #print(file_contents)
    #print(count_words(file_contents))
    #print(count_characters(file_contents))

    char_count_results_sorted = dict(sorted(count_characters(file_contents).items(), key=lambda item: item[1],reverse=True))

    print(f'--- Begin report of {path_to_file} ---')

    print(f'{count_words(file_contents)} words found in the doucment\n')

    for char in char_count_results_sorted.keys():
        print(f"The '{char}' character was found {char_count_results_sorted[char]} times")

    print('--- End report ---')

main()