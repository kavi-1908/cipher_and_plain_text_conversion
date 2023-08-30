print("Enter choice ")
print("1. cipher text to plain text ")
print("2. plaint text to cipher text ")
pl1 =""
a =""
b =""
z =""
cip2=" "
a = int(input())
if a == 1 :
    print("Enter u r cipher text ")
    cip=input()
    key1=int(input("key "))
    for i in cip:
        pl1 += chr(ord(i)-key1)
    for i in pl1:
        if ord(i)<ord("a"):
            b +=chr(ord(i)+26)
        else:
            b += i
    print("plain text is ",b)
else:
    print("Enter u r plaintext ")
    pln2 = input()
    key2 = int(input(" Key "))
    for i in pln2:
         cip2 +=chr(ord(i)+key2)
    for i in cip2:
        if ord(i)>ord("z"):
            z += chr(ord(i)-26)
        else:
            z += str(i)
    print("ciper text =",z)
