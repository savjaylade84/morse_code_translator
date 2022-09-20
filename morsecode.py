import argparse as arg


_parser = arg.ArgumentParser(
                                description="Encrypt and Decrypt Message to Morse Code",
                                usage='''
python3 morsecode.py [option] file/string
-em encrypt and prompt message
-dm decrypt and prompt message
-ef encrypt file
-df decrypt file
-efp encrypt and prompt file
-dfp decrypt and prompt file
                                ''',
                                formatter_class=arg.RawDescriptionHelpFormatter,
                                epilog='''
Author: John Jayson B. De Leon
Email: savjaylade84@gmail.com
Github: savjaylade84'''

                             )
                             
_parser.add_argument(
                        '-e',
                        '--encrypt',
                        action='store_true',
                        help='encrypt a message to morse code'
                    )
                    
_parser.add_argument(
                        '-d',
                        '--decrypt',
                        action='store_true',
                        help='decrypt a morse code to  message'
                    )
                    
                    
_parser.add_argument(
                        '-v',
                        '--version',
                        action='version',
                        version='%(prog)s - 1.0v'
                    )
_parser.add_argument('-m','--message',help='direct input')
_parser.add_argument('-f','--filename',help='file input')
_parser.add_argument(
                        '-p',
                        '--printfile',
                        action='store_true',
                        help='print the process output file content'

                    )


# message to morse code
MORSE_CODE = { 'A':'.-', 'B':'-...',

                    'C':'-.-.', 'D':'-..', 'E':'.',

                    'F':'..-.', 'G':'--.', 'H':'....',

                    'I':'..', 'J':'.---', 'K':'-.-',

                    'L':'.-..', 'M':'--', 'N':'-.',

                    'O':'---', 'P':'.--.', 'Q':'--.-',

                    'R':'.-.', 'S':'...', 'T':'-',

                    'U':'..-', 'V':'...-', 'W':'.--',

                    'X':'-..-', 'Y':'-.--', 'Z':'--..',

                    '1':'.----', '2':'..---', '3':'...--',

                    '4':'....-', '5':'.....', '6':'-....',

                    '7':'--...', '8':'---..', '9':'----.',

                    '0':'-----', ', ':'--..--', '.':'.-.-.-',

                    '?':'..--..', '/':'-..-.', '-':'-....-',

                    '(':'-.--.', ')':'-.--.-',' ':'.......'}

# morse code to message
MORSE_CODE_REVERSE = {value:key for key,value in MORSE_CODE.items()}

''' 
    look for each letter in the string
    then converted it to morse code letter
'''
def encrypt(message:str=' ') -> str:
    return ' '.join(MORSE_CODE.get(char.upper()) for char in message)

''' 
    look for each morse code letter
    then converted it to string 
'''
def decrypt(message:str='') -> str:
    return ''.join(MORSE_CODE_REVERSE.get(char) for char in message.split())

''' 
    open a file then get the content then
    encrypt the content then write it
    to the file
'''
def encrypt_file(file_name:str=' ') -> None:
    _encrypt:list = str(open(file_name,'r').read())
    _encrypt:str = ''.join(_encrypt).replace('\n',' ').strip()
    _encrypt = encrypt(_encrypt)
    open(file_name,'w').write(_encrypt)

'''
     open a file then get the content then
     decrypt the content then write it
     to the file
'''
def decrypt_file(file_name:str=' ') -> None:
    _decrypt = str(open(file_name,'r').read())
    _decrypt = ''.join(_decrypt).replace('\n',' ')
    _decrypt = decrypt(_decrypt)
    open(file_name,'w').write(_decrypt)

#   prompt and encrypt the file 
def read_encrypt_file(file_name:str='') -> str:
    encrypt_file(file_name)
    return open(file_name,'r').read()

# prompt and decrypt the file
def read_decrypt_file(file_name:str='') ->str:
    decrypt_file(file_name)
    return open(file_name,'r').read()

_args = _parser.parse_args()


if _args.encrypt:
    if _args.message:
        print(f'[ Message Encrypted ]: => {encrypt(_args.message)}')
    if _args.filename:
        if _args.printfile:
            print(f'[ Encrypting File ]: => Success')
            print(f'[ Message Encrypted ]: => {read_encrypt_file(_args.filename)}')
        else:
            encrypt_file(_args.filename)
            print(f'[ Encrypting File ]: => Success')

if _args.decrypt:
     if _args.message:
         print(f'[ Message Decrypted ]: => {decrypt(_args.message)}')
     if _args.filename:
        if _args.printfile:
            print(f'[ Decrypting File ]: => Success')
            print(f'[ Message Decrypted ]: => {read_decrypt_file(_args.filename)}')
        else:
            print(f'[ Decrypting File ]: => Success')
            decrypt_file(_args.filename)

