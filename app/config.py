import os
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig:
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEVELOPMENT_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig
}