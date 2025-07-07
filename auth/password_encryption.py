from secrets import choice
from string import ascii_letters, digits
from bcrypt import gensalt, hashpw


def generate_secure_password(length=8):
    return "".join(choice(ascii_letters + digits + "!#$@%&*") for _ in range(length))


def hash_password(password: str) -> str:
    return hashpw(password.encode(), gensalt()).decode("utf-8")
