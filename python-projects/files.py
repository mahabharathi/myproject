#compress image 
my_file=open("E:/test.txt")

'''print(my_file.read())
my_file.seek(0) #move the cursor to beggining

print(my_file.readlines())'''

my_file.close()

#r+ mode will override the content
with open("E:/test.txt",mode='w') as my_file: #r - read mode | w - write mode | r+ -read and write | a- append at end
    text=my_file.write('hey it\'s me!')
    #print(my_file.readlines())

try:
    with open("E:/test2.txt",mode='r') as my_file: # w- create new file if not exist and write
        #text=my_file.write('hey it\'s me!')
        print(my_file.readlines())

except FileNotFoundError as err:
    print('File not exits')
    raise err





