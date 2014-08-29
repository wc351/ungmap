from hashlib import sha1
from base64 import urlsafe_b64encode as b64encode
import random

random.seed()
pattern = "%%0%dX"
junk_len = 1024


def generate_key(max_length, seed_length, encoder=b64encode, digester=sha1):
    """
    Generate a Base64-encoded 'random' key by hashing the data.
    data is a tuple of seeding values. Pass arbitrary encoder and
    digester for specific hashing and formatting of keys

    https://gist.github.com/airtonix/6204802

    """
    junk = (pattern % (junk_len * 2)) % random.getrandbits(junk_len * seed_length)
    key = str(junk).encode()
    return b64encode(key)[:max_length]


def random_hash():
    return generate_key(96, 1024, digester=sha1)
