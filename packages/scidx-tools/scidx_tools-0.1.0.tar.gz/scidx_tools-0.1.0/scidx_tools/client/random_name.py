import asyncio
import random
import string

def generate_unique_name(self):
    return ''.join(random.choices(string.ascii_lowercase + string.digits + '-_', k=10))