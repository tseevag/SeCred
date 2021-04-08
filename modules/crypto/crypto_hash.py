import os
import hashlib

import config

def gen_salt():
    """Generate random bytes of size SALT_SIZE"""

    salt_size = config.SALT_SIZE
    return os.urandom(32)



def gen_hash(plain_pass, salt=gen_salt()):
    """Generate hash of given plain text password\n
    Arguments: plain password,  b'salt\n
    Return: (b'salt,  b'hash)
    """

    algorith = config.HASH_ALGORITHM
    passwd = plain_pass.encode('utf-8')
    iteration = config.ITERATIONS

    dk = hashlib.pbkdf2_hmac(algorith, passwd, salt, iteration)

    return (salt, dk)