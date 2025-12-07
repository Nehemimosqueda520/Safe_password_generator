import math
from password_generator import generate_password

def calculate_entropy(data: str):
    if not data:
        return 0
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char, 0) + 1
    entropy = 0
    data_length = len(data)
    for freq in frequency.values():
        p_x = freq / data_length
        entropy -= p_x * math.log2(p_x)
    return entropy