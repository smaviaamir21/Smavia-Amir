# secret code program

def encode(message):
    secret = ""
    for char in message:
        # shift each character by 3 in ASCII
        secret += chr(ord(char) + 3)
    return secret

def decode(secret):
    message = ""
    for char in secret:
        # shift each character back by 3 in ASCII
        message += chr(ord(char) - 3)
    return message

# Main program
choice = input("Do you want to Encode (E) or Decode (D)? ").upper()

if choice == "E":
    msg = input("Enter your message: ")
    code = encode(msg)
    print("Encoded Message:", code)

elif choice == "D":
    code = input("Enter your secret code: ")
    msg = decode(code)
    print("Decoded Message:", msg)

else:
    print("Invalid choice! Please select E or D.")
