with open('mytxt.txt') as f:
    lines=[line for line in f]
print(lines)

with open('mytxt.txt') as f:
    lines=[line.rstrip() for line in f]
print(lines)
