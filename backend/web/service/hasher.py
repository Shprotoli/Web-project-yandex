from bcrypt import gensalt, hashpw, checkpw


class BcryptPasswordHasher:
    def hash(self, password: str) -> str:
        salt = gensalt()
        hashed = hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')

    def verify(self, password: str, hashed_password: str) -> bool:
        return checkpw(
            password.encode('utf-8'),
            hashed_password.encode('utf-8')
        )