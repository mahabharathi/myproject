is_old=False
is_licenced=True

if not is_old: #not 
    print('not eligible')

if is_old & is_licenced: #you can use 'and' instead of & also
    print('you are old enough to drive!')
elif is_old==False & is_licenced:
    print('you are not eligible!')
else:
    print('you are not of age')
    
print('checkcheck')

#Truthy and falsey
is_old='hello'
is_licenced=5

print(bool(is_old),bool(is_licenced))
print(bool(''),bool(0))


password= '123'
username='johny'

if password and username:
    print('yes')

#Ternary operator -conditional expression
#evalute something based on condition

#condition_if_true if condition else condition_if_else

is_friend=True
can_msg='message allowed' if is_friend else 'not allowed to message'

print(can_msg)
