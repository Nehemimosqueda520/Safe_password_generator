import secrets
import string
from validators import validate_entry
import config

def generate_password(length : int, use_uppercase: bool, use_digits: bool, use_special_chars: bool):
    character_pool = string.ascii_lowercase

    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_digits:
        character_pool += string.digits
    if use_special_chars:
        character_pool += string.punctuation
        character_pool = "".join(
            char for char in character_pool if char not in config.INVALID_CHARACTERS
        )
    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    password = "".join(secrets.choice(character_pool) for _ in range(length))
    if validate_entry(password):
        return password
    else:
        raise ValueError("Generated password did not pass validation.")