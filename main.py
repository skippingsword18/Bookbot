import re

def lettercount(words):
    d = {}
    for word in re.sub(r'[^a-zA-Z]', '', words.lower()):
        for letter in word:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
    return d


def wordcount(words):
    print(len(words.split()))

def main():
    with open("/home/austin/workspace/github.com/skippingsword18/Bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        output = lettercount(file_contents)
        for key in output:
            print(f"The '{key}' character was found {output[key]} times")

if __name__ == '__main__':
    main()