from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey
)

# 1. 개인키 생성
private_key = Ed25519PrivateKey.generate()

# 2. 공개키 추출
public_key = private_key.public_key()

# 3. 서명할 메시지
message = b"Hello, this is a message."

# 4. 개인키로 서명
signature = private_key.sign(message)

print("Message   :", message)
print("Signature :", signature.hex())

# 5. 공개키로 서명 검증
try:
    public_key.verify(signature, message)
    print("Signature is valid!")
except Exception:
    print("Signature is invalid!")