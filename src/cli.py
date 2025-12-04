#create interface for a password generator
import argparse
from password_generator import generate_password
def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument('--length', type=int, default=None, help='Length of the password')
    parser.add_argument('--no-uppercase', action='store_true', help='Exclude uppercase letters')
    parser.add_argument('--no-digits', action='store_true', help='Exclude digits')
    parser.add_argument('--no-special-chars', action='store_true', help='Exclude special characters')
    
    args = parser.parse_args()
    
    length = args.length if args.length is not None else None
    use_uppercase = not args.no_uppercase
    use_digits = not args.no_digits
    use_special_chars = not args.no_special_chars
    
    password = generate_password(length=length, use_uppercase=use_uppercase, use_digits=use_digits, use_special_chars=use_special_chars)
    print("Generated Password:", password)