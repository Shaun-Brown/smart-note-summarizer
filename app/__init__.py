from flask import Flask

app = Flask(__name__)

from app import controller  # Import routes after app is defined