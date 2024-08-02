"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime, date

from flask import Flask, Response, request, jsonify

from date_functions import (convert_to_datetime, get_day_of_week_on,
                            get_days_between, get_current_age)

app_history = []

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True


def add_to_history(current_request):
    """Adds a route to the app history."""
    app_history.append({
        "method": current_request.method,
        "at": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "route": current_request.endpoint
    })


@app.get("/")
def index():
    """Returns an API welcome messsage."""
    return jsonify({"message": "Welcome to the Days API."})

@app.route("/between", methods=["POST"])
def calculate_days_between():
    "Returns the number of days between two dates."
    pass

@app.route("/weekday", methods=["POST"])
def say_which_weekday():
    "Returns the day of the week a specific date is."
    pass

@app.route("/history", methods=["GET"])
def details_of_requests():
    "Returns details on the last number of requests to the API."
    pass

@app.route("/history", methods=["DELETE"])
def delete_request_history():
    "Deletes details of all previous requests to the API."
    pass

@app.route("/current_age", methods=["GET"])
def give_current_age_in_years():
    "Returns a current age in years based on a given birthdate."
    pass


if __name__ == "__main__":
    app.run(port=8080, debug=True)
