#!/usr/bin/env python3

charmap = {
    "n": "!",
    ";": "@",
    "p": "#",
    "x": "$",
    "I": "%",
    "s": "^",
    "d": "&",
    "/": "*",
    "$": "(",
    "C": ")",
    "e": "-",
    "Q": "=",
    "c": "+",
    "g": "[",
    "Z": "]",
    "]": "'",
    "S": ";",
    "K": '"',
    "J": ":",
    "H": "/",
    "?": "?",
    "X": ".",
    "^": ">",
    "0": ",",
    "'": "<",
    "`": "`",
    "~": "~",
    "\\": "a",
    "_": "b",
    "l": "c",
    "u": "d",
    "P": "e",
    '"': "f",
    "f": "g",
    "{": "h",
    "A": "i",
    "q": "j",
    "i": "k",
    "3": "l",
    "@": "m",
    "V": "n",
    ">": "o",
    "k": "p",
    "v": "q",
    "8": "r",
    "D": "s",
    "G": "t",
    "*": "u",
    "(": "v",
    "=": "w",
    "6": "x",
    "j": "y",
    "r": "z",
    "w": "A",
    "R": "B",
    "o": "C",
    "E": "D",
    "m": "E",
    "+": "F",
    "}": "G",
    "5": "H",
    "T": "I",
    "U": "J",
    "&": "K",
    "<": "L",
    "N": "M",
    "b": "N",
    "h": "O",
    "9": "P",
    "F": "Q",
    ",": "R",
    "#": "S",
    "t": "T",
    "a": "U",
    "%": "V",
    "1": "W",
    "[": "X",
    "B": "Y",
    ".": "Z",
    "L": "0",
    "Y": "1",
    "W": "2",
    "!": "3",
    ")": "4",
    "4": "5",
    ":": "6",
    "y": "7",
    "2": "8",
    "M": "9",
    "z": "_",
    "7": "{",
    "|": "}",
}

encrypted_flag = "oTt74i!21/0;xLbk_Z3yPNdp|"
flag = "".join(charmap[c] for c in encrypted_flag)

print(flag)
