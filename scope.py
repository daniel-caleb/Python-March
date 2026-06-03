secret_key = 'my_secret_key' # Global variable

def encrypt_message():
    algorithm = 'AES' # Local variable
    print(f"Encrypting message using {algorithm} algorithm and secret key: {secret_key}")

def decrypt_message():
    print(secret_key)
    print(algorithm)  # This will raise an error because 'algorithm' is not defined in this scope

encrypt_message()
decrypt_message()
print(secret_key)  # This will work because 'secret_key' is defined in the global scope 
print(algorithm)  # This will raise an error because 'algorithm' is not defined in the global scope 
