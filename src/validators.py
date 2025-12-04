import config   

def validate_entry(entry):
    if not isinstance(entry, str):
        raise ValueError("Entry must be a string.")
    if len(entry) < config.MIN_PASSWORD_LENGTH:
        raise ValueError("Entry must be at least 10 characters long.")
    if any(char in entry for char in config.INVALID_CHARACTERS):
        raise ValueError("Entry contains invalid characters.")
    return True
