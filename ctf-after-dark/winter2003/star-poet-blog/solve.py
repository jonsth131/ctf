#!/usr/bin/env python3
import re
import requests

url = "https://star-poet-blog.acmcyber.com/"
password_file = "archive/password.txt"

poems = []


def get_poem_urls():
    r = requests.get(url)
    poem_regex = re.compile(r"(archive\/\w+\.txt)")
    return poem_regex.findall(r.text)


def get_poems():
    poem_urls = get_poem_urls()
    poems = []
    for poem_url in poem_urls:
        r = requests.get(url + poem_url)
        poems.append(r.text)
    return poems


def get_encoded_words():
    r = requests.get(url + password_file)
    word_regex = re.compile(r"(\d{4})")
    return [int(word) for word in word_regex.findall(r.text)]


def get_poem_stanza(poem, stanza):
    return poem.replace("\n \n", "\n\n").split("\n\n")[stanza]


def get_poem_line(stanza, line):
    return stanza.split("\n")[line-1]


def get_poem_word(line, word):
    return line.strip().split(" ")[word-1]


def clean_word(word):
    return "".join([c for c in word.lower() if c.isalpha()])


def get_word_from_book_cipher(code):
    book = code // 1000
    stanza = (code % 1000) // 100
    line = (code % 100) // 10
    word = code % 10
    poem = poems[book-1]
    stanza = get_poem_stanza(poem, stanza)
    line = get_poem_line(stanza, line)
    word = get_poem_word(line, word)
    return clean_word(word)


poems = get_poems()
encoded_words = get_encoded_words()
decoded_words = []

for encoded_word in encoded_words:
    decoded_words.append(get_word_from_book_cipher(encoded_word))

print("flag{" + "_".join(decoded_words) + "}")
