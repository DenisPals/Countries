import os
import requests
import urllib.parse
import mysql.connector

from flask import redirect, render_template, request, session
from functools import wraps



def login_required(f):

    #Decorate routes to require login.

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def check_connection(database):
    database.ping(reconnect=True, attempts=2, delay=1)
    if not database.is_connected():
        return print("We have a problem with our server, please try again later!")

def error(message, code):
    return render_template("error.html", message=message, code=code)
