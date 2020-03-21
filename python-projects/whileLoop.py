#for loop =looped over number of times,simpler

my_List=[1,2,3]

for x in my_List:
    print(x)

print("          ")
#while =flexible,powerful,infinite times
x=0
while x < len(my_List):
    print(my_List[x])
    x+=1

print("          ")

while True:
    response = input('say something : ') #infinite loop -use condition op
    if(response == 'bye'):
        break

print("          ")


i=0
while i<50:
    if i==35:
        print("Reached")
        break
    i+=1
else: #execute only if there is no break statement in while loop
    print("Done with while loop") 

print("          ")

i=0
while i<50:
    i+=1
else:
    print("Done with while loop")


#break,continue,pass

for x in [1,2,3]:
    continue #not print anything
   # print(x)
    
for x in [1,2,3]:
    #thinking about it
    pass 