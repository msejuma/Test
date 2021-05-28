import sys
import os
import math
import requests

from django.http import request

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


print(greet('Isaac'))

r = requests.get('https://coreyms.com')
print(r.status_code)
