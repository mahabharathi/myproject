class Toy():
    def __init__(self,color,age):
        self.color=color
        self.age=age
        
    def __str__(self):    #dunder method override
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    '''
    def __del__(self):
        print('deleted!')
    
    '''
    def __call__(self):
        print('called!') 
               
action_figure=Toy('blue',4)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
#del action_figure  #delete some thing in class
print(action_figure()) #call all method