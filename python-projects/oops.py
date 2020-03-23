#OOP -Encapsulation,abstraction,inheritance,polymorphism
#class
#private variable -no private var like java
class User():
    def __init__(self,email):
        self.email=email
        
    def signin(self):
        print('logged in')
        
    def attack(self):
            print('do nothing')

class Wizard(User):
    def __init__(self,name,power,email):
        User.__init__(self,email) #super().__init__(email)  -polymorphism
        self.name=name
        self.power=power
        
    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self,name,num_arrows):
        self.name=name
        self.num_arrows=num_arrows
        
    def attack(self):
        User.attack(self)
        print(f'Attacking with arrows of {self.num_arrows}')

wizard=Wizard('maha',21,'maha@gmail.com')
arc=Archer('devi',2)

wizard.attack()
arc.attack()

wizard.signin()
arc.signin()

print(isinstance(wizard,User))

def player_attack(char):
    char.attack()

player_attack(wizard)
player_attack(arc)

print(wizard.email)

#introsepction -determine the object type in run time

print(dir(wizard))

class Hybrid(Wizard,Archer): #multiple inheritance
    def __init__(self,name,power,arrows,email):
        Wizard.__init__(self,name,power,email)
        Archer.__init__(self,name,arrows)

hb=Hybrid('maha',21,13,'maha@gmail.com')
hb.attack()
hb.signin()

''''

class PlayerCharacter: #class
    membership = True #class object attribute - static
    def __init__(self,name='anonymous',age=0): #constructor,init method -whenever the class is called init initiantiate
       # if age>18: #access with PlayerCharacter.membership also
        self._name=name #attributes 
        self._age =age #private var if var name start with _
    
    
    def run(self):
        print(f'my name is {self._name}')
        print(self) # prints object memory 
        
    @classmethod   #method on actual class
    def adding_things(cls,num1,num2):
        return cls('mahabharathi',num1+num2)
        
    @staticmethod  #static method
    def adding_things2(num1,num2):
        return num1+num2
    
player1=PlayerCharacter('maha',21) #instantiating class to create object
player2=PlayerCharacter('devi',10) # objects are created in difference memory location

print(player1._name,player1._age)
print(player2._name,player2._age)
player1.run()
player2.run()
player1.attack=50
print(player1.adding_things(5,4))

player2=PlayerCharacter.adding_things(4,5)
print(player2._age)
print(player1.adding_things2(5,4))

      
#class  -blueprint (methods,action)
#object -instances 
#class initantiate a instance
# static and class method called without class instatiation


#abstarction : able to override and convert method to str
#if we see _ infront of var -think it like private var 

'''