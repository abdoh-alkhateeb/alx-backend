#!/usr/bin/env python3
"""
Sets up a basic Flask app.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Flask configuration.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines locale.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index() -> str:
    """
    Renders a basic template.
    """
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
