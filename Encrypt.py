"""Write a code that will remove vowels from a string and run it for the sentence:

'Computer Science Makes the World go round but it doesn't make the world round itself!'

Print the save the result as the variable = NoVowels
"""
def Ciphertext(pie):
    Ciphertext = ""
    for i in pie:
        if i =='a':
            Ciphertext = Ciphertext + '%'
        elif i == 'e':
            Ciphertext = Ciphertext + '^'
        elif i == 'i':
            Ciphertext = Ciphertext + '$'
        elif i == 'o':
            Ciphertext = Ciphertext + '@'
        elif i == '*':
            Ciphertext = Ciphertext + '!'
        else:
            Ciphertext = Ciphertext + i
    return Ciphertext
print(Ciphertext('onomonopia'))











"""Write an encryption code that you make up and run it for the variable NoVowels"""
