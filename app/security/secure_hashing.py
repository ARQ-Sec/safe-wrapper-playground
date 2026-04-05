import hashlib

def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()
