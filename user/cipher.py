# generates string for translation
initial = ""
for i in range(97, 97 + 26):
    initial += chr(i)
# generate mapped chars for string
translated= ''
for i in range(97, 97 + 26):
    translated += chr(i- 10)
# prints the letters and coordianted code
print('INITIAL   ', initial)
print('CODE', translated)
# creates a table 
table = str.maketrans(initial, translated)
# allows the user to enter a word to translate
value= input("eneter word to translate: ")
result= value.translate(table)
# print users message and then the message turned into the code
print("BEFORE", value)
print('AFTER', result)



