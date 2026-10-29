"""
Package initializer
"""
import logging
from flask import Flask
from flask_talisman import Talisman

# Initialize Flask App
app = Flask(__name__)

# Initialize Flask-Talisman with security headers configuration
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': '\'self\'',
        'object-src': '\'none\''
    },
    force_https=True
)

# Set up logging
app.logger.setLevel(logging.INFO)
app.logger.info("Service initialized with Talisman security headers.")
