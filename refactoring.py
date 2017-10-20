import json
import time

# 1: Naming -------------------------------------------------------------------
# What can be fixed here with naming of functions and variables?
# Why is good naming important?

def cube_of(i):
    return i ** 3

val1 = cube_of(3)
print('. cube of 3 =', val1)


# 2: DocStrings and Comments --------------------------------------------------
# How should we rewrite the DocString and Comment here? Why?
# What makes a good DocString / Comment?

def read_file_contents(file_path):
    '''Reads file content of the file located at file_path, and returns its contents'''
    with open(file_path, 'r', encoding='utf-8') as f:
        # setting encoding to utf-8 while opening the file to ensure that it works on windows
        return f.read()

lyrics = read_file_contents('paradise.txt')
if 'para-para-paradise' in lyrics:
    print('. lyrics loaded')


# 3: Efficiency / Performance -------------------------------------------------
# What is in the for loop, that shouldn't be in the loop, but out of it?
# Is that particular code even necessary?

def write_file_contents(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def count_words():
    word_count = {}

    for word in lyrics.lower().split():
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1

    # write_file_contents('paradise_word_count.json', json.dumps(word_count, indent=2, sort_keys=True))

    most_repeated_word = max(word_count, key=lambda k: word_count[k])
    print('. most repeated word in Paradise is', most_repeated_word)

start = time.time()
count_words()
end = time.time()
print('  execution time =', end - start)


# 4: Functions ----------------------------------------------------------------
# You see that the code is getting repeated.
# When you copy/paste the same code, and if there is a change,
# you will need to change every copy/pasted code in your code base.
# How can you avoid repeating similar code? How will you rewrite this?

def print_lines_with_40_chars(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        lyrics_lines = f.readlines()
        for line in lyrics_lines:
            if len(line.strip()) > 40:
                print(' ', line.strip())

print('. Paradise')
print_lines_with_40_chars('paradise.txt')

print('. Yellow')
print_lines_with_40_chars('yellow.txt')
