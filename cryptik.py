key = [
    "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj",
    "ak", "al", "am", "an", "ao", "ap", "aq", "ar", "as", "at",
    "au", "av", "aw", "ax", "ay", "az",

    "ba", "bb", "bc", "bd", "be", "bf", "bg", "bh", "bi", "bj",
    "bk", "bl", "bm", "bn", "bo", "bp", "bq", "br", "bs", "bt",
    "bu", "bv", "bw", "bx", "by", "bz",

    "ca", "cb", "cc", "cd", "ce", "cf", "cg", "ch", "ci", "cj",
    "ck", "cl", "cm", "cn", "co", "cp", "cq", "cr", "cs", "ct",
    "cu", "cv", "cw", "cx", "cy", "cz",

    "da", "db", "dc", "dd", "de", "df", "dg", "dh", "di", "dj",
    "dk", "dl", "dm", "dn", "do", "dp", "dq"
]
characters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z",

    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z",

    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",

    " ", "!", '"', "#", "$", "%", "&", "'", "(", ")",
    "*", "+", ",", "-", ".", "/", ":", ";", "<", "=",
    ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{",
    "|", "}", "~"
]

alphabets = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

import random as rdm

def encrypt(inputText):
    selected = 0
    output = ""
    for i in range (0, len(inputText), 1):
        j = 0
        selected = inputText[i]
        for j in range (0 , len(characters), 1):
            if(selected == characters[j]):
                print(selected, "is the", j, "th letter, so", key[j])
                break
        output = output + key[j]
    print("Encrypted text: ", output)

def decrypt(inputText):
    output = ""
    for i in range (0, len(inputText), 2):
        j = 0
        selected = inputText[i] + (inputText[i+1])
        for j in range(0, len(key), 1):
            if selected == key[j]:
                print(selected, "is the", j, "th key index, so", characters[j])
                break
        output = output + characters[j]
    print("\nDecrypted text: ", output)

def keyFunction():
    task = input("\nKey function menu\n-----------------\n1. Output current key \n2. Enter new key \n3. Generate new key \n(1,2,3): ")
    output = ""
    if task == "1" or task == "o":
        for i in range (0, len(key), 1):
            output = output + key[i]
        print("\nEncryption key:", output)

    elif task == "2" or task == "e":
        key.clear()
        newKey = input("New key: ")
        selected = 0
        for i in range (0, (len(newKey)),2):
            selected = newKey[i] + newKey[i+1]
            key.append(selected)

    elif task == "3" or task == "g":
        genList = []
        newKey = ""
        while len(genList) < 95:
            charGenTemp = alphabets[rdm.randint(0, 25)] + alphabets[rdm.randint(0, 25)]
            if not(charGenTemp in genList):
                genList.append(charGenTemp)
        for i in range (0, len(genList), 1):
            newKey = newKey + genList[i]
        print("\nNew encryption key:", newKey)

        setKey = input("\nSet this as your key?\n1. Yes\n2. No\n(1,2): ").lower()
        if setKey == "y" or setKey == "1":
            key.clear()
            selected = 0
            for i in range (0, (len(newKey)),2):
                selected = newKey[i] + newKey[i+1]
                key.append(selected)

notZero = 0
while notZero == 0:
    task = input("\nHome menu\n---------\n1. Encrypt\n2. Decrypt\n3. Key functions\n(1,2,3): ").lower()

    if task == "1" or task == "e":
        encrypt(input("Enter text: "))
    elif task == "2" or task == "d":
        decrypt(input("Enter text: "))
    elif task == "3" or task == "k":
        keyFunction()
    else:
        print("Invalid input")