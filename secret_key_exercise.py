def rc4(key, text):
    """
    Encrypts or decrypts a given text using the RC4 stream cipher.

    The RC4 algorithm works in two phases:
    1. Key-Scheduling Algorithm (KSA): Initializes a state array 'S'.
    2. Pseudo-Random Generation Algorithm (PRGA): Generates a keystream.

    The keystream is then XORed with the input text (plaintext or ciphertext)
    to produce the output (ciphertext or plaintext).

    Args:
        key (bytes): The secret key for the cipher.
        text (bytes): The input text (plaintext or ciphertext).

    Returns:
        bytes: The resulting encrypted or decrypted text.
    """
    # 1. Key-Scheduling Algorithm (KSA)
    # Initialize the state array 'S' with values from 0 to 255.
    S = list(range(256))
    j = 0
    key_length = len(key)

    # Permute the state array 'S' based on the secret key.
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        # Swap S[i] and S[j]
        S[i], S[j] = S[j], S[i]

    # 2. Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    keystream = bytearray()

    # Generate a keystream byte for each byte of the input text.
    for _ in range(len(text)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        # Swap S[i] and S[j]
        S[i], S[j] = S[j], S[i]
        # Generate the keystream byte 'k'
        k = S[(S[i] + S[j]) % 256]
        keystream.append(k)

    # 3. XOR the input text with the generated keystream.
    # This performs both encryption and decryption.
    result = bytearray(b ^ k for b, k in zip(text, keystream))

    return bytes(result)

# --- Example Usage ---
if __name__ == "__main__":
    # The secret key (as a byte string).
    secret_key = b'mysecretkey'

    # The plaintext message to be encrypted (as a byte string).
    plaintext = b'This is a secret message.'

    # --- Encryption ---
    # Encrypt the plaintext using the secret key.
    ciphertext = rc4(secret_key, plaintext)
    print(f"Plaintext:  '{plaintext.decode()}'")
    print(f"Ciphertext (hex): {ciphertext.hex()}")

    # --- Decryption ---
    # To decrypt, apply the same RC4 function to the ciphertext with the same key.
    decrypted_plaintext = rc4(secret_key, ciphertext)
    print(f"Decrypted:  '{decrypted_plaintext.decode()}'")
