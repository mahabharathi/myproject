#implementation using list

def fib(number):
    list=[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(2,number):
        if i<number:
            fibNum=list[i-2]+list[i-1]
         #   print(fibNum)
            list[i]=fibNum
    
    print(list)
    
def fibLoop(number):
    a=0
    b=1
    result=[]
    for i in range(number):
        result.append(a)
        temp=a
        a=b
        b=temp+b
    return result
        
print(fibLoop(10000))
fib(21)