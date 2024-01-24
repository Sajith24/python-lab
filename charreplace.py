string=input("Enter the string:")
char=string[0]
string=string.replace(char,'$')
print(char+string[1:])
