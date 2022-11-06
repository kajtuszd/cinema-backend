from django.utils.crypto import get_random_string
    

def generate_slug():
    return get_random_string(10)
