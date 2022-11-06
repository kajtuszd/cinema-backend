from django.utils.crypto import get_random_string
from django.utils.text import slugify
    

def append_slug(text):
    return slugify(text) + '-' + get_random_string(7)
