from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import tradingeconomics as te
import mysql.connector
from datetime import datetime, timedelta

from flask import jsonify

from helpers import login_required, check_connection

# Connect to database
database = mysql.connector.connect(
    host ="eu-cdbr-west-03.cleardb.net",
    user ="bb989d462fa875",
    password="68278a16",
    database="heroku_9a92cf889ad5d2b"
)

# Set database cursor and let it return dict objects instead of tulpes
db = database.cursor(dictionary=True)

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Log into API
te.login('a1c5abfa1d174fc:oc90mhf4gbw0jtn')

# Declare empty list to cache JSON data
data = []


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/register", methods=["POST", "GET"])
def register():
    """Register for an account"""
    
    if request.method == "POST":

        # Assure connection to database
        check_connection(database)

        # Get user input
        username = request.form.get("username")
        password = request.form.get("password")

        # Load all usernames in database to check if requested username already exist
        db.execute("SELECT user_name FROM user_c")
        names = db.fetchall()

        # Iterate over each name and return apology if name exists already in database
        for name in names:
            if name["user_name"] == username:
                return render_template("/register.html", not_available=True)
                
        # Generate password hash
        password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # Insert new user in database
        query = "INSERT INTO user_c (user_name, hash_value) VALUES (%s, %s)"
        val = (username, password)
        db.execute(query, val)
        database.commit()

        # Redirect user to login
        return redirect("/login")

    return render_template("register.html")



@app.route("/login", methods=["POST", "GET"])
def login():
    """Log user in"""

    # Assure connection to database
    check_connection(database)

    # Forget any user ID
    session.clear()
    
    if request.method == "POST":

        # Assure connection to database
        check_connection(database)

        # Fetch user input
        username = request.form.get("username")

        # Query database for username
        query = "SELECT * FROM user_c WHERE user_name = %s"
        val = (username,)
        db.execute(query, val)
        rows = db.fetchall()

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash_value"], request.form.get("password")):
            return render_template("login.html", invalid=True)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user
        return redirect("/")

    else:
        return render_template("login.html")
        

@app.route("/logout", methods=["POST", "GET"])
@login_required
def logout():
    """"Log user out"""

    # Clear session
    session.clear()

    # Redirect user to login page
    return redirect("/login")

@app.route("/", methods=["POST", "GET"])
@login_required
def index():
    """Main Page"""

    # Declare list with countries available with Trading Economics free tier
    countries = ['Mexico', 'New Zealand', 'Sweden', 'Thailand']

    if len(data) == 0:
        for country in countries:
            # Fetch countries data
            currency = te.getIndicatorData(country=country, indicators='currency')[0]
            gdp = te.getIndicatorData(country=country, indicators='gdp')[0]
            unemployment = te.getIndicatorData(country=country, indicators='unemployment rate')[0]
            inflation_rate = te.getIndicatorData(country=country, indicators='inflation rate')[0]
            interest_rate = te.getIndicatorData(country=country, indicators='interest rate')[0]
            balance_of_trade = te.getIndicatorData(country=country, indicators='balance of trade')[0]
            consumer_confidence = te.getIndicatorData(country=country, indicators='consumer confidence')[0]

            # Declare keywords
            CRY = "Country"
            LV = "LatestValue"
            PV = "PreviousValue"

            # Declare dictionary with containing chosen data
            currency_data = {
                "Country": currency[CRY],
                "LV_currency": currency[LV],
                "PV_currency": currency[PV],
                "LV_gdp": gdp[LV],
                "PV_gdp": gdp[PV],
                "LV_unemployment": unemployment[LV],
                "PV_unemployment": unemployment[PV],
                "LV_inflationrate": inflation_rate[LV],
                "PV_inflationrate": inflation_rate[PV],
                "LV_interestrate": interest_rate[LV],
                "PV_interestrate": interest_rate[PV],
                "LV_bot": balance_of_trade[LV],
                "PV_bot": balance_of_trade[PV],
                "LV_conconf": consumer_confidence[LV],
                "PV_conconf": consumer_confidence[PV]
            }

            # Append dict objects to data list
            data.append(currency_data)
        else:
            pass

    return render_template("index.html", data=data)