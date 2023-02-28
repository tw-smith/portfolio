from flask import Flask
from config import Config
from flask_hcaptcha import hCaptcha

app = Flask(__name__)
hcaptcha = hCaptcha(app)
app.config.from_object(Config)

from app import routes
