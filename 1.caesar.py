text = input("Enter the messsage: ")
shift = int(input("Enter the key: "))
case = int(input("Enter 0 for encryption and 1 for decryption: "))

def caesar(message, offset, case):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in message.lower():
        if char == ' ':
            result += char
        else:
            if case == 0: #encryption case
                index = alphabet.find(char)
                new_index = (index + offset) % len(alphabet)
                result += alphabet[new_index]
            elif case == 1: #decryption case
                index = alphabet.find(char)
                new_index = (index +len(alphabet)) % (len(alphabet)+offset)
                result += alphabet[new_index]
    
    if case == 0: #encryption case
        print('plain text:', message)
        print('encrypted text:', result)
    elif case == 1:
        print('cypher text:', message)
        print('decrypted text:', result)

caesar(text, shift, case)