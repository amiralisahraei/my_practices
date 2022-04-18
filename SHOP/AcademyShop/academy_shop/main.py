import string
from random import choices
import sys
import argparse

def create_password(length=8, upper=False, lower=False, digit=False, pun=False):
    
    pool = ''

    if upper:
        pool += string.ascii_uppercase
        
    if lower:
        pool += string.ascii_lowercase
    
    if digit:
        pool += string.digits
    
    if pun:
        pool += string.punctuation
    
    if pool == '':
        pool = string.ascii_letters

    return ''.join(choices(pool, k=length))


if __name__ == "__main__":
    # try:
    #     length = int(sys.argv[1])
    # except ValueError:
    #     print("please enter int")
    # else:
    #     print(create_password(length))
    
    parser = argparse.ArgumentParser()
    parser.add_argument('length', type=int, help="length of password")
    parser.add_argument('-u', '--upper', help="User Upper case", action='store_true')
    parser.add_argument('-l', '--lower', help="User lower case", action='store_true')
    parser.add_argument('-d', '--digit', help="User digit case", action='store_true')
    parser.add_argument('-p', '--pun', help="User punc case", action='store_true')

    args = parser.parse_args()
    print(create_password(args.length, args.upper, args.lower, args.digit, args.pun))

    

