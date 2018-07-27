import os

"Configurations for development"
class DevelopmentConfig():
    DEBUG = True

"Configurations for testing"
class TestConfig():
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    TESTING = True
    DEBUG = True

"Configurations for production"
class ProductConfig():
    DEBUG = False
    TESTING = False

config_environment = {}
