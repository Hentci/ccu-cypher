from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.backends import default_backend
import os
import time

'''
該程式包含了AES-CTR和ChaCha20加密演算法的加密和解密功能。而AES-CCM在AES-CCM.py中實現。
'''

def encrypt_decrypt(algorithm, mode, key, nonce, filename, encrypted_filename, decrypted_filename):
    if algorithm == 'AES' and mode == 'CTR':
        cipher = Cipher(algorithms.AES(key), modes.CTR(nonce), backend=default_backend())
        encryptor = cipher.encryptor().update
        decryptor = cipher.decryptor().update
    elif algorithm == 'ChaCha20':
        cipher = ChaCha20Poly1305(key)
        encryptor = lambda data: cipher.encrypt(nonce, data, None)
        decryptor = lambda data: cipher.decrypt(nonce, data, None)
    
    with open(filename, 'rb') as f:
        plaintext = f.read()

    
    start_time = time.time()
    ciphertext = encryptor(plaintext)
    end_time = time.time()
    encryption_speed = len(plaintext) / (end_time - start_time)

    with open(encrypted_filename, 'wb') as f:
        f.write(ciphertext)
    
    start_time = time.time()
    decrypted_data = decryptor(ciphertext)
    end_time = time.time()
    decryption_speed = len(ciphertext) / (end_time - start_time)

    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)
    
    assert plaintext == decrypted_data, "Decrypted data does not match original!"

    if plaintext == decrypted_data:
        print(f"{algorithm} - Encryption and decryption successful! Data integrity maintained.")
    
    return encryption_speed, decryption_speed

# 檔案名稱
filename = 'data.txt'

# 檢測所有加密模式
results = {}
for alg_info in [('AES', 'CTR', 16, 16), ('ChaCha20', None, 32, 12)]:
    algorithm, mode, key_size, nonce_size = alg_info
    key = os.urandom(key_size)
    nonce = os.urandom(nonce_size)

    if algorithm == 'AES':
        encrypted_filename = f'{filename}.aes.ctr.encrypted'
        decrypted_filename = f'{filename}.aes.ctr.decrypted'
    else:
        encrypted_filename = f'{filename}.chacha20.encrypted'
        decrypted_filename = f'{filename}.chacha20.decrypted'
        
    results[(algorithm, mode)] = encrypt_decrypt(algorithm, mode, key, nonce, filename, encrypted_filename, decrypted_filename)

# 輸出結果
for key, speeds in results.items():
    print(f"{key} - Encryption speed: {speeds[0]:.2f} bytes/sec, Decryption speed: {speeds[1]:.2f} bytes/sec")
