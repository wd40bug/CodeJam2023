
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def to_num(c: str) -> int:
    return ALPHABET.index(c)


def to_char(i: int) -> str:
    return ALPHABET[i]


def casesar_attempt(input: str, off: int) -> str:
    result = ""
    for char in input:
        if not char.isalnum():
            result += char
            continue
        upper = char.isupper()
        num = to_num(char.lower())
        new_char = to_char((num - off) % 26)
        new_char = new_char.upper() if upper else new_char
        result += new_char
    return result


def caesar(input: str) -> str:
    for i in range(0, 25):
        answer = casesar_attempt(input, i)
        if answer[0:2] == "We":
            return answer


f = open("level 3.txt")
case = f.read()
print("Cipher:\n", case, sep="")
print("\n\nTranslation:\n", caesar(case), sep="")
