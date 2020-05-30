#Error handling

#1.Syntax error, name error, index out of range, key error, zerodivision error,type error

while True:
    try:
          age=int(input('what is your age? '))
          10/age
          print(age)
          raise Exception('hey cut it out')
    #      raise ValueError('hey cut it out')
   # except ValueError as err:
     #     print(err)
    
    except ZeroDivisionError as err:
        print(err)
        
    except TypeError as err:
        print(err)
    else:
         print('thank you')
         break;
    finally:
        print('ok am finalyy done')


#multiple error (TypeError,ZeroDivisionError) as err