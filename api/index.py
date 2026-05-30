try:
    from .app import app
except ImportError:
    from app import app

# This is the WSGI application that Vercel will run



