import requests
import hashlib
import sys


#print(res) #<Response [400]> -unauthorized 
def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/'+query_char[0:5]
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Error fetching: {res.status_code} check the api and try again')
    return res

def get_password_leaks_count(hashes,hash_to_check):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        if h==hash_to_check:
            return count
    return 0
    
def pwned_api_check(password):
    #check password if it exists in API response
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char,tail_char=sha1_password[:5],sha1_password[5:]
    response=request_api_data(first5_char)
    print(first5_char,tail_char)
    return get_password_leaks_count(response,tail_char)

def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you should change your password')
        else:
            print(f'{password} was not found. Carry on!')
    return 'done!'

if __name__=='__main__':
    sys.exit(main(sys.argv[1:]))

#python passChecker.py password123 ghfghkgghkftygjk hello