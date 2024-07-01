from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

class CustomAES:
    def __init__(self, key: bytes):
        self.key = pad(key, AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC)

    def _shift_ciphertext(self, data: bytes, shift_value: int) -> bytes:
        return bytes((byte + shift_value) % 256 for byte in data)

    def _unshift_ciphertext(self, data: bytes, shift_value: int) -> bytes:
        return bytes((byte - shift_value) % 256 for byte in data)

    def _calculate_shift_value(self, key):
        last_char_value = key[-1]
        shift_value = last_char_value + len(key)
        return shift_value
    
    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.key[:16])
        encrypted_data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        shift_value = self._calculate_shift_value(self.key)
        encrypted_data_modified = bytearray(encrypted_data)
        encrypted_data_modified[-1] += shift_value  # Example modification
        return bytes(encrypted_data_modified)

    def decrypt(self, encrypted_data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.key[:16])
        decrypted_data = cipher.decrypt(encrypted_data)
        shift_value = self._calculate_shift_value(self.key)
        decrypted_data_modified = bytearray(decrypted_data)
        decrypted_data_modified[-1] -= shift_value
        return decrypted_data_modified.decode('utf-8')
