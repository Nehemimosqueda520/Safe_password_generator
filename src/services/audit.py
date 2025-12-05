#make audit service to log password generation events
import logging
logger = logging.getLogger("audit_logger")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("audit.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
def log_password_generation(length, use_uppercase, use_digits, use_special_chars):
    logger.info(
        f"Generated password with length={length}, "
        f"use_uppercase={use_uppercase}, "
        f"use_digits={use_digits}, "
        f"use_special_chars={use_special_chars}"
    )
    