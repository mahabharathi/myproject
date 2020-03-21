age=input('What is your age?: ')

def checkDriverAge(age=0):
    if int(age) <18:
        print('Sorry, you are too young to drive this car. powering off')
    elif int(age) > 18:
        print('Powering on.Enjoy the ride!')
    elif int(age) == 18:
        print('Congratulations on your first year of driving.Enjoy the ride!.')

checkDriverAge(age)
checkDriverAge()