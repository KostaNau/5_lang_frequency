import collections
import re
import argparse


ENCODING = 'utf-8'
RE_PATTERN = r'[^\W|\d]+'

def load_input_file(filepath):
    # text_data = None
    with open(filepath, 'r', encoding=ENCODING) as input_file:
        text_data = input_file.readlines()
    return text_data


def find_all_words(text):
    all_words_list = []
    for line in text:
        word_stack = re.findall(RE_PATTERN, line)
        for word in word_stack:
            all_words_list.append(word.lower())
    return all_words_list


def get_most_frequent_word(word_list):
    amount_output_words = 10
    most_frequent = collections.Counter(word_list).most_common(amount_output_words)
    return most_frequent


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Most frequen word_stack')
    parser.add_argument('text_file', help="path to any text file or filename for current directory")
    args = parser.parse_args()
    input_file_path = args.text_file

    word_list = find_all_words(load_input_file(input_file_path))
    most_frequent_words = get_most_frequent_word(word_list)
    print('10 Most frequent words:', end='\n')
    for word in most_frequent_words:
        print('Word "{}" meets: {} times.'.format(word[0], word[1]))
