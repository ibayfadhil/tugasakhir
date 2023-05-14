from Crypto.Cipher import AES
import os

# Fungsi untuk menambahkan padding pada plaintext
def add_padding(plaintext):
    block_size = 16
    padding = block_size - len(plaintext) % block_size
    return plaintext + padding * bytes([padding])

# Fungsi untuk menghapus padding dari ciphertext
def remove_padding(ciphertext):
    padding = ord(bytes([ciphertext[-1]]))
    return ciphertext[:-padding]

# Fungsi untuk enkripsi file XLSX
def encrypt_file(key, input_file_path, output_file_path):
    # Baca isi file
    with open(input_file_path, 'rb') as f:
        plaintext = f.read()

    # Tambahkan padding pada plaintext
    plaintext = add_padding(plaintext)

    # Buat objek AES dengan kunci yang diberikan
    cipher = AES.new(key, AES.MODE_ECB)

    # Enkripsi plaintext
    ciphertext = cipher.encrypt(plaintext)

    # Tulis ciphertext ke file
    with open(output_file_path, 'wb') as f:
        f.write(ciphertext)

    print('File berhasil dienkripsi')

# Fungsi untuk dekripsi file XLSX
def decrypt_file(key, input_file_path, output_file_path):
    # Baca isi file
    with open(input_file_path, 'rb') as f:
        ciphertext = f.read()

    # Buat objek AES dengan kunci yang diberikan
    cipher = AES.new(key, AES.MODE_ECB)

    # Dekripsi ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Hapus padding dari plaintext
    plaintext = remove_padding(plaintext)

    # Tulis plaintext ke file
    with open(output_file_path, 'wb') as f:
        f.write(plaintext)

    print('File berhasil didekripsi')

# Contoh penggunaan
key = os.urandom(32) # Buat kunci acak dengan panjang 16 byte
input_file_path = 'file.xlsx'
encrypted_file_path = 'file_encrypted.xlsx'
decrypted_file_path = 'file_decrypted.xlsx'

# Enkripsi file
encrypt_file(key, input_file_path, encrypted_file_path)

# Dekripsi file
decrypt_file(key, encrypted_file_path, decrypted_file_path)
