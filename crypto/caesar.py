from helpers import alphabet_position, rotate_character 


def encrypt(text,rot):
    
    encryptedText = ""
    
    for aLetter in text:
        encryptedText += rotate_character (aLetter, rot)
        
    return encryptedText 
    

def main():
    userText = input("Type a message:")

    userRot = input("What integer value is your encryption key?")
    userRot = int(userRot)

    print(encrypt(userText, userRot))

if __name__ == "__main__":
    main()