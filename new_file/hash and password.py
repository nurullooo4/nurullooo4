from typing import Tuple
import os
import hashlib
import hmac


def hash_password(password: str) ->Tuple[bytes, bytes]:
    salt = os.urandom(16)
    p_hash = hashlib.pbkdf2_hmac('123', password.encode(), salt, 100000)
    return salt, p_hash

def correct_password(salt: bytes, p_hash: bytes, password: str) -> bool:
    return hmac.compare_digest(
        p_hash,
        hashlib.pbkdf2_hmac('123', password.encode(), salt, 100000)
    )


salt, p_hash = hash_password('--\\--\\--')
assert correct_password(salt, p_hash, '--\\--\\--')
assert not correct_password(salt, p_hash, '---\\\---')
assert not correct_password(salt, p_hash, '--\\\---\\\---')

