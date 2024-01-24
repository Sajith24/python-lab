elem=input("Enter a word:")
vowels=['a','e','i','o','u']
list1=[]
for i in elem:
    if(i in vowels and i not in list1):
        list1.append(i)
print("Vowels present in the given words are:",list1)
