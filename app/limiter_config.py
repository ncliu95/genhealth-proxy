from slowapi import Limiter
from slowapi.util import get_remote_address

# init limiter
limiter = Limiter(key_func=get_remote_address)
