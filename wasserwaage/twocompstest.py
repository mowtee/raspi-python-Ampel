def fromtwos(value, wordsize):
    if(value & (1 << wordsize - 1)):
        value = value - (1<<wordsize)
    return value

def totwos(value, wordsize):
    if(value<0):
        value = bin((1<<wordsize)+value)
    return value


value = int(input("Input: "))
wordsize = int(input("Wordsize: "))
op = input("Fromtwos: type 'f' / Totwos: type 't': ")
if op == "f":
    value=int(str(value),2)
    value=fromtwos(value, wordsize)
elif op == "t":
    value=totwos(value,wordsize)
else:
    exit()
print(value)
    