#same as range()
#used when we need index counter

for i,char in enumerate('hellooooo'): #unpacked i=index
    print(i,char)

print("                 ")
for i,char in enumerate([1,2,3,4]): #unpacked i=index
    print(i,char)

print("                 ")
for i,num in enumerate(range(100)): #unpacked i=index
    if num==50:
        print("index of 50 is : "+str(i))