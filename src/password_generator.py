import secrets
import string
from validators import validate_entry
import config
def generate_password (length=config.DEFAULT_PASSWORD_LENGTH, use_uppercase=config.DEFAULT_USE_UPPERCASE, use_digits=config.DEFAULT_USE_DIGITS, use_special_chars=config.DEFAULT_USE_SPECIAL_CHARS):   
     character_pool = string.ascii_lowercase
     
     if use_uppercase:
        character_pool += string.ascii_uppercase
     if use_digits:
        character_pool += string.digits
     if use_special_chars:
        character_pool += string.punctuation
        character_pool = ''.join(char for char in character_pool if char not in ['$', '%', '#', '<', '>'])
     if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
     password = ''.join(secrets.choice(character_pool) for _ in range(length))
     if validate_entry(password):
        return password
     else:
        raise ValueError("Generated password did not pass validation.")
    
print(generate_password())


