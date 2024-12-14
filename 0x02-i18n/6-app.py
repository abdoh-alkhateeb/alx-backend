#!/usr/bin/env python3
"""
Sets up a basic Flask app.
"""

from typing import Dict, Union

from flask import Flask, g, render_template, request
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    if g.user:
        locale = g.user.get("locale")

        if locale in app.config["LANGUAGES"]:
            return locale

    locale = request.headers.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user(user_id: Union[int, None]) -> Dict:
    """
    Gets user dictionary if existent.
    """
    return users.get(user_id, {}) if user_id is not None else {}


@app.before_request
def before_request():
    """
    Preprocesses requests.
    """
    user_id = request.args.get("login_as", None)
    user_id = int(user_id) if user_id is not None else None
    g.user = get_user(user_id)


@app.route("/")
def index() -> str:
    """
    Renders a basic template.
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run()
