from argon2 import PasswordHasher, exceptions

ph = PasswordHasher()

def generate_hash(password: str) -> str:
    return ph.hash(password)

def verify_password(stored_hash: str, entered_password: str) -> bool:
    try:
        return ph.verify(stored_hash, entered_password)
    except exceptions.VerifyMismatchError:
        return False

