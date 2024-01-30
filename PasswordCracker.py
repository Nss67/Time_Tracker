# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet = [' ', '!', '"', '#', '$', '%', '&', "''", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

count = 0
alphabet_length = len(alphabet)

password = "FSFwFEw#5d4a65d4as654d 34#?#2$?@42hdjh ahd"
password_length = len(password)

guess = ""
password_length_count = 0
alphabet_length_count = 0
for i in range(password_length):
    x = password[i]
    for p in range(alphabet_length):
        y = alphabet[p]
        if x == y:
            guess += f"{y}"
        if guess == password:
            print(f"{guess} is WiFi password")
            break


