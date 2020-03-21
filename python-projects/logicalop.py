print(4>5) #greater than
print(4==5) #equals to
print(4<5) #lesser than
print("hello"=='hello')
print('a'>'b') #ASCII values
print('a'>'A')
print('a'=='a')
print(1<2>3<4)
print(1<=0) #lesser than or equal to
print(1>=0) #greater than or equal to
print(1!=0) # not equal to
print(not (1==1)) # not equal same as 1!=1
print(not(1==0))

#wizard game
is_magician=True
is_expert=True


#check if magician and expert:"you are a master magician".
if is_magician and is_expert:
    print('You are a master magician!')
    
#check if magician but not expert:'at least you are getting there'.
elif is_magician and not is_expert:
    print('At least you are getting there!')

#if you are not a magician : 'you need magic powers'.
elif not is_magician:
    print('You need magic powers!')


#== equality of value
print(True==1) #0=false 1=True True==bool(1) =True (Truthy)
print("1"==1) #falshy
print([]==1) #falshy
print(10==10.0)
print([1,2,3]==[1,2,3]) #check two lists are same

print("               ")
#is =Loc of value in memory is same
print(True is 1)
print('1' is 1)
print([] is 1)
print(10 is 10.0)
print([1,2,3] is [1,2,3]) #two different lists reside in different loc
print(True is True)
print('1' is '1')
print([] is []) #two different lists reside in different loc
print(10 is 10)
