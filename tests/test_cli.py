#write tests for cli
import unittest
import subprocess
import sys
import os
from pathlib import Path
from src.config import DEFAULT_PASSWORD_LENGTH, MIN_PASSWORD_LENGTH, INVALID_CHARACTERS
class TestCLI(unittest.TestCase):
    CLI_PATH = Path(__file__).parent.parent / 'src' / 'cli.py'

    def run_cli(self, args):
        result = subprocess.run([sys.executable, str(self.CLI_PATH)] + args,
                                capture_output=True, text=True)
        return result

    def test_default_password_generation(self):
        result = self.run_cli([])
        self.assertEqual(result.returncode, 0)
        password = result.stdout.strip()
        self.assertEqual(len(password), DEFAULT_PASSWORD_LENGTH)

    def test_custom_length(self):
        custom_length = 20
        result = self.run_cli(['--length', str(custom_length)])
        self.assertEqual(result.returncode, 0)
        password = result.stdout.strip()
        self.assertEqual(len(password), custom_length)

    def test_invalid_length_below_minimum(self):
        invalid_length = MIN_PASSWORD_LENGTH - 1
        result = self.run_cli(['--length', str(invalid_length)])
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Entry must be at least", result.stderr)

    def test_exclude_special_characters(self):
        result = self.run_cli(['--no-special-chars'])
        self.assertEqual(result.returncode, 0)
        password = result.stdout.strip()
        for char in INVALID_CHARACTERS:
            self.assertNotIn(char, password)

    def test_include_all_character_types(self):
        result = self.run_cli(['--length', '25', '--use-uppercase', '--use-digits', '--use-special-chars'])
        self.assertEqual(result.returncode, 0)
        password = result.stdout.strip()
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in ''.join(INVALID_CHARACTERS) for c in password) == False)  # Ensure no invalid chars