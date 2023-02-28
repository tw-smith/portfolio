import os
from os import path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    HCAPTCHA_ENABLED = True
    HCAPTCHA_SITE_KEY = os.environ.get('HCAPTCHA_SITE_KEY')
    HCAPTCHA_SECRET_KEY = os.environ.get('HCAPTCHA_SECRET_KEY')
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')

