import os, binascii, random
from django.core.urlresolvers import reverse
from django.conf import settings


def generate_hex_token(token_chars=32):
    """
    Generates a cryptographically random token containing a specified number of
    hexadecimal characters.
    
    :param token_chars: The number of characters in the returned token.
    """
    # One byte becomes two hex chars. The +1 accounts for odd number lengths.
    num_bytes = (token_chars + 1) / 2
    # Get the target number of bytes as a hex string.
    # Note: os.urandom is defined to be cryptographically pseudo-random.
    random_bytes = os.urandom(num_bytes)
    random_hex = binascii.hexlify(random_bytes)
    # Truncate the string at the target length.
    return random_hex[:token_chars]


def generate_tracking_link(url_name, token):
    root_url = random.choice(settings.PUBLIC_SITE_URLS) or u''
    root_url = root_url.rstrip('/')
    return root_url + reverse(url_name, kwargs={'token': token})
