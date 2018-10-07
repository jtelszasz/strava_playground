from flask import Flask, request, current_app
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
