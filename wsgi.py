import os
from dotenv import load_dotenv
from app import create_app
from flask_cors import CORS

load_dotenv()

app = create_app()
CORS(app)