n = int(input("Enter a number: "))
sp = (n - 2)*2+1
sp2 = 0

for i in range(n - 1):
    c = 0
    e = 0
    while c<sp2 :
        print(" ", end = '')
        c+=1
    sp2+= 1
    print("*", end = '')

    while e < sp:
        print(" ", end = '')
        e+=1
    print("*")
    sp-= 2

c = 0
while c<sp2 :
    print(" ", end = '')
    c+=1
print("*")

sp = 1
sp2 = n-2
for i in range (n-1):
    c = 0
    e = 0

    while c < sp2:
        print(" ", end = '')
        c+=1
    sp2-=1
    print("*", end = '')

    while e < sp:
        print(" ", end = '')
        e += 1
    print("*")
    sp+=2
