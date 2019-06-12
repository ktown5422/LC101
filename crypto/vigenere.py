from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    
    encryptedText = ""
    rotKey = []
    index = 0

    for i in rot:
        key = alphabet_position(i)
        rotKey.append(key)   


    for letter in text:
        if not letter.isalpha():
            encryptedText += letter
        else:
            if index == (len(rotKey) - 1):
                encryptedText += rotate_character(letter, rotKey[index])
                index = 0
            else:
                encryptedText += rotate_character(letter, rotKey[index])
                index += 1

    return encryptedText
     

def main():
    userText = input("Type a message:")

    userRot = input("What is the key word?")
     

    print(encrypt(userText, userRot))

if __name__ == "__main__":
    main()