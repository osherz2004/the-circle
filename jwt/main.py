from base64 import urlsafe_b64encode, urlsafe_b64decode
import json
import rsa


class b64:
    @staticmethod
    def encode(string):
        return urlsafe_b64encode(string.encode()).rstrip(b"=").decode()

    @staticmethod
    def encode_bytes(bytes):
        return urlsafe_b64encode(bytes).rstrip(b"=").decode()

    @staticmethod
    def decode(string):
        padding = b"=" * (4 - (len(string) % 4))
        return urlsafe_b64decode(string.encode() + padding).decode()

    @staticmethod
    def decode_bytes(bytes):
        padding = b"=" * (4 - (len(bytes) % 4))
        return urlsafe_b64decode(bytes + padding)


class jwt:
    """
    Sign the token.
    """

    @staticmethod
    def sign_token(token, private_key):
        return rsa.encrypt(token, private_key)

    """
    Validate token.
    """

    @staticmethod
    def validate_token(token, public_key):
        signiture = b64.decode_bytes(token.split(".")[2].encode())
        try:
            if b64.decode(token.split(".")[1]) == rsa.decrypt(signiture, public_key):
                return True
        except Exception:
            return False

    """
    Encode a JWT with a private key.
    """

    @staticmethod
    def encode(claim, private_key, algorithm="RSA"):
        if algorithm != "RSA":
            raise Exception("Algorithm is not supported.")

        header = json.dumps({"alg": algorithm, "typ": "JWT"})
        payload = json.dumps(claim)

        token = b64.encode(header) + "." + b64.encode(payload)

        signature = b64.encode_bytes(jwt.sign_token(token.encode(), private_key))

        token += "." + signature

        return token

    """
    Decode a JWT with public key.
    """

    @staticmethod
    def decode(claim, public_key, algorithm="RSA"):
        if algorithm != "RSA":
            raise Exception("Algorithm is not supported.")

        if jwt.validate_token(claim, public_key):
            return b64.decode(claim.split(".")[1])
        else:
            raise Exception("Invalid signiture.")


k2, k1 = rsa.newkeys(1024)
print(k2)
token = jwt.encode({"test": "test"}, k2)
print(token)
t = jwt.decode(token, k1)
print(t)
