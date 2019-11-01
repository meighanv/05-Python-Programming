alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

string_input = input("Enter a string to encrypt:")

shift = int(input('Provide th enumber of places to shift input:'))
input_length = len(string_input)
print(string_input)
#print(input_length)

string_output = ""

for i in range(input_length):
    character = string_input[i]
    charlocation = alphabet.find(character)
    newlocation = (charlocation + shift) % 52
    string_output += (alphabet[newlocation])
print(string_output)