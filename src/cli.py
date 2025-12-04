import argparse
from password_generator import generate_password
from config import (
    DEFAULT_PASSWORD_LENGTH,
    DEFAULT_USE_DIGITS,
    DEFAULT_USE_SPECIAL_CHARS,
    DEFAULT_USE_UPPERCASE,
)


def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument(
        "--length",
        "-l",
        type=int,
        default=DEFAULT_PASSWORD_LENGTH,
        help=f"Length of the password (default: {DEFAULT_PASSWORD_LENGTH})",
    )
    parser.add_argument(
        "--uppercase",
        dest="use_uppercase",
        action=argparse.BooleanOptionalAction,
        default=DEFAULT_USE_UPPERCASE,
        help="Include uppercase letters.",
    )
    parser.add_argument(
        "--digits",
        dest="use_digits",
        action=argparse.BooleanOptionalAction,
        default=DEFAULT_USE_DIGITS,
        help="Include digits.",
    )
    parser.add_argument(
        "--special-chars",
        dest="use_special_chars",
        action=argparse.BooleanOptionalAction,
        default=DEFAULT_USE_SPECIAL_CHARS,
        help="Include special characters.",
    )

    args = parser.parse_args()

    password = generate_password(
        length=args.length,
        use_uppercase=args.use_uppercase,
        use_digits=args.use_digits,
        use_special_chars=args.use_special_chars,
    )
    print("Generated Password:", password)
