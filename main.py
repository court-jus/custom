from flask import Flask
from flask import render_template
from flask import request
import datetime
from dateutil.parser import parse
import humanize
import os
import requests
from babel.dates import format_date, format_time
from utils import add_bold
from helpers import extra_context
import traceback


app = Flask(__name__)


@app.route("/health")
def health_check():
    return "Up and running"


@app.route("/message/")
def message_form():
    return render_template(f"message/form/main.html")


@app.route("/message/<title>/<path:messages>/")
def render_message(title, messages):
    messages = messages.split("/")
    kwargs = request.args
    template = kwargs.get("template", "default")
    try:
        context = extra_context()
        context.update(kwargs)
        context.update({"title": title, "messages": messages})
        return render_template(f"message/{template}.html", **context)
    except Exception:
        return render_template(
            "error.html",
            message="Can't find or render message template",
            details=traceback.format_exc(),
            template=template,
            **context,
        )
