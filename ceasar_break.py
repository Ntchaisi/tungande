clear_text = input("Enter secret message: ").lower()
validLetters = "abcdefghijklmnopqrstuvwxyz "
shift = int(input("Enter shift value: "))

newString = ""
cipher_text = []

for char in clear_text:
    if char in validLetters:
        newString += char

for char in newString:
    x = ord(char)
    x =x+shift
    cipher_text.append(chr(x if 97 <= x <= 122 else 96+x%122))

print(clear_text)
print(" super secure encrypted message:")
print("".join(cipher_text))
  