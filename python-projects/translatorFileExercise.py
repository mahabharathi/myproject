from translate import Translator

translator= Translator(to_lang="ko")
try:
    with open('E:/test.txt',mode='r') as my_file:
        translation = translator.translate(my_file.read())
        print(translation)
        with  open('E:/test_ko.txt',mode='w',encoding="utf-8") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('File not found error')