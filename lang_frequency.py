import collections
import re
import argparse
import time


BUFFER_SIZE = 0x1000
ENCODING = 'utf-8'
RE_PATTERN = r'[^\W|\d]+'


def read_file_buffer(file):
  flow = True
  while flow:
    flow = file.read(BUFFER_SIZE)
    yield flow


def load_all_words(input_filepath):
    all_words_list = []
    with open(input_filepath, 'r', encoding=ENCODING) as input_file:
        for line in read_file_buffer(input_file):
            word_stack = re.findall(RE_PATTERN, line)
            for word in word_stack:
                all_words_list.append(word)
    return all_words_list


def get_most_frequent_word(word_list):
    most_frequent = collections.Counter(word_list).most_common(10)
    return most_frequent


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Most frequen  word_stack')
    parser.add_argument('text_file', help="path to any text file or filename for current directory")
    args = parser.parse_args()
    input_file_path = args.text_file

    word_list = load_all_words(input_file_path)
    print(get_most_frequent_word(word_list))
