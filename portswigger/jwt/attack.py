import jwt
import json

def create_jwt(header, payload, secret):
    """
    Create a signed JWT using the HS256 algorithm.
    
    Args:
    header (dict): The JWT header.
    payload (dict): The JWT payload.
    secret (str): The secret key to sign the JWT.

    Returns:
    str: The signed JWT.
    """
    token = jwt.encode(payload, secret, headers=header)
    return token

# Example usage:
header = {
    "kid": "20552490-6361-4129-8ab9-c1cdde0bd74a",
    "alg": "HS256"
}

payload = {
    "iss": "portswigger",
    "exp": 1731621089,
    "sub": "administrator"
}

secret = "secret1"

signed_jwt = create_jwt(header, payload, secret)
print("Signed JWT:", signed_jwt)
