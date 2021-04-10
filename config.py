from data.User import User
#global variables

# display
WINDOW_WIDTH = 80              #in character

#working
ALLOWED_LOGIN_ATTEMPTS = 3

#hashing
SALT_SIZE = 32
HASH_ALGORITHM = 'SHA512'
ITERATIONS = 1000000


# runtime user
CURRENT_USER = None