#Duplicates in List

some_List = ['a','b','c','b','d','m','n','n','o','p']

#my answer
for i in range(0,len(some_List)):
    for j in range(i+1,len(some_List)):
        if some_List[i] == some_List [j]:
            print(some_List[i],True)

#answer by instructor

duplicate=[]

for value in some_List:
    if some_List.count(value)>1: #count values numb of times in list
        if value not in duplicate:
            duplicate.append(value)

print(duplicate)
