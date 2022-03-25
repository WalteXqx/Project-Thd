
import random

# random characters
chtrs = 'abcdefghijklmnoprstuyvzwxABCDEFGHIJKLMNOPRSTUYZWX.,/#@!$%><?'
password = ''
print('password generator')


# deciding password long
lon = int(input('how long you want your password to be? :'))

for i in range(lon):
    exte = random.randint(0, len(chtrs)-1)
    password += chtrs[exte]

# showing the password
print('your password:', password)
