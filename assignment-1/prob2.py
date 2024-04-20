import hashlib

# 要計算的字串
message = "I love cryptography."

# 計算 SHA-3-512 message digest
sha3_512_digest = hashlib.sha3_512(message.encode()).hexdigest()

print("SHA-3-512 message digest:", sha3_512_digest)
