import secrets
import string
def generate_password (length=15, use_uppercase=True, use_digits=True, use_special_chars=True):
     if length < 10:
        raise ValueError(f"Password length should be at least 10 characters.")
    
     character_pool = string.ascii_lowercase
     if use_uppercase:
        character_pool += string.ascii_uppercase
     if use_digits:
        character_pool += string.digits
     if use_special_chars:
        character_pool += string.punctuation
     if not character_pool:
        raise ValueError("At least one character type must be selected.")
     password = ''.join(secrets.choice(character_pool) for _ in range(length))
     return password
 
print(generate_password())
