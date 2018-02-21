initial = ""
for i in range(97, 97 + 26):
    initial += chr(i)

translated= ''
for i in range(97, 97 + 26):
    translated += chr(i- 10)

print('INITIAL   ', initial)
print('TRANSLATED', translated)

table = str.maketrans(initial, translated)

value= 'chelsea'
result= value.translate(table)

print("BEFORE", value)
print('AFTER', result)



