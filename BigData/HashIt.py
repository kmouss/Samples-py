import uuid
import hashlib
 
def hash_it(input_str):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    hash_output = hashlib.sha256(salt.encode() + input_str.encode()).hexdigest() + ':' + salt
    print (hash_output)
    return hash_output
    
def check_input(hashed_input, user_input):
    input_str, salt = hashed_input.split(':')
    return input_str == hashlib.sha256(salt.encode() + user_input.encode()).hexdigest()
 
new_input = input('Please enter a new string: ')
hashed_input = hash_it(new_input)
print('The string to store in the db is: ' + hashed_input)
old_input = input('Now please enter the string again to check for match: ')

if check_input(hashed_input, old_input):
    print('You entered the right string')
else:
    print('I am sorry but the string does not match')