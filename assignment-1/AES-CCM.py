from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
from cryptography.hazmat.backends import default_backend
import os
import time

def encrypt_decrypt_aes_ccm(key, nonce, filename, encrypted_filename, decrypted_filename):
    # 初始化 AESCCM 對象
    cipher = AESCCM(key)

    with open(filename, 'rb') as f:
        plaintext = f.read()

    # 加密
    start_time = time.time()
    ciphertext = cipher.encrypt(nonce, plaintext, None)
    end_time = time.time()
    encryption_speed = len(plaintext) / (end_time - start_time)

    with open(encrypted_filename, 'wb') as f:
        f.write(ciphertext)

    # 解密
    start_time = time.time()
    decrypted_data = cipher.decrypt(nonce, ciphertext, None)
    end_time = time.time()
    decryption_speed = len(ciphertext) / (end_time - start_time)

    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

    assert plaintext == decrypted_data, "Decrypted data does not match original!"

    if plaintext == decrypted_data:
        print("AES-CCM - Encryption and decryption successful! Data integrity maintained.")
    
    return encryption_speed, decryption_speed

# 檔案名稱
filename = 'data.txt'
encrypted_filename = f'{filename}.aes.ccm.encrypted'
decrypted_filename = f'{filename}.aes.ccm.decrypted'

# nonce_size 12不行 13也不行 = =
# 但11以下就可以
key_size = 16  
nonce_size = 10  
key = os.urandom(key_size)
nonce = os.urandom(nonce_size)

# 執行加密和解密
encryption_speed, decryption_speed = encrypt_decrypt_aes_ccm(key, nonce, filename, encrypted_filename, decrypted_filename)

# 輸出結果
print(f"AES-CCM - Encryption speed: {encryption_speed:.2f} bytes/sec, Decryption speed: {decryption_speed:.2f} bytes/sec")
