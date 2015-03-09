import os, binascii

def generate_hex_token(token_chars=32):
    '''
    Generates a cryptographically random token containing a specified number of
    hexadecimal characters.
    
    :param token_chars: The number of characters in the returned token.
    '''
    #One byte becomes two hex chars. The +1 accounts for odd number lengths.
    num_bytes = (token_chars + 1) / 2
    #Get the target number of bytes as a hex string.
    #Note: os.urandom is defined to be cryptographically pseudo-random.
    random_bytes = os.urandom(num_bytes)
    random_hex = binascii.hexlify(random_bytes)
    #Truncate the string at the target length.
    return random_hex[:token_chars]
