import binascii
import os
import sys

def hexstr(fn):
    # Lit un fichier binaire et le convertit en chaîne hexadécimale
    with open(fn, "rb") as f:
        content = f.read()
    return binascii.hexlify(content).decode("utf-8")

def dsem(h, n):
    # Découpe une chaîne hexadécimale en segments de taille n
    n = max(1, n)
    return [h[i: i + n] for i in range(0, len(h), n)]

def letiscover(letters, types, mode):
    Delay = 0
    String = 0
    Result = []
    
    Letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
        ",", ".", "/", ";", "'", "[", "]", "\\", "-", "=", " ", "\n", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "BSPACE", "`", "TAB", "UP", "DOWN", "RIGHT", "LEFT", "DEL"
    ]
    CapLetters = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "<", ">", "?", ":", "\"", "{", "}", "|", "_", "+", "SPACE", "ENTER", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "BSPACE", "~", "TAB", "UP", "DOWN", "RIGHT", "LEFT"
    ]
    HexLetters = [
        "04", "05", "06", "07", "08", "09", "0a", "0b", "0c", "0d", "0e", "0f", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1a", "1b", "1c", "1d", "36", "37", "38", "33", "34", "2f", "30", "31", "2d", "2e", "2c", "28", "1e", "1f", "20", "21", "22", "23", "24", "25", "26", "27", "2a", "35", "2b", "52", "51", "4f", "50", "4c"
    ]
    
    for i in range(len(letters)):
        if letters[i] in HexLetters:
            LetterPos = HexLetters.index(letters[i])
            Result.append(Letters[LetterPos])
    
    return Result

def usage(reason, ecode):
    print(f"Usage: {sys.argv[0]} <display|decode> inject.bin\n")
    print(f"Example: {sys.argv[0]} display ./inject.bin\n")
    if reason:
        print(f"Error: {reason}\n")
    sys.exit(ecode)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage("Insufficient arguments", 2)
    
    mode = sys.argv[1]
    filename = os.path.realpath(sys.argv[2])
    
    List = dsem(hexstr(filename), 2)
    chars = List[::2]
    types = List[1::2]
    
    if mode == "decode":
        Result = letiscover(chars, types, 1)
    elif mode == "display":
        Result = letiscover(chars, types, 0)
    else:
        usage("Invalid option", -1)
    
    print("".join(Result))
