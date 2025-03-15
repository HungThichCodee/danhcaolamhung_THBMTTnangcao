class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():  # Nếu là ký tự chữ cái
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')  # Tính độ dịch của khóa
                if char.isupper():  # Nếu ký tự là chữ hoa
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:  # Nếu ký tự là chữ thường
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
                key_index += 1  # Chuyển sang ký tự tiếp theo trong khóa
            else:
                encrypted_text += char  # Nếu không phải chữ cái, thêm trực tiếp vào kết quả
        return encrypted_text

    def vigenere_decrypt(self, encrypt_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypt_text:
            if char.isalpha():  # Nếu là ký tự chữ cái
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')  # Tính độ dịch của khóa
                if char.isupper():  # Nếu ký tự là chữ hoa
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:  # Nếu ký tự là chữ thường
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                key_index += 1  # Chuyển sang ký tự tiếp theo trong khóa
            else:
                decrypted_text += char  # Nếu không phải chữ cái, thêm trực tiếp vào kết quả
        return decrypted_text
