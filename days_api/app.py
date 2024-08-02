"""This file defines the API routes."""

# pylint: disable = no-name-in-module

from datetime import datetime, date

from flask import Flask, request, jsonify

from date_functions import (convert_to_datetime, get_day_of_week_on,
                            get_days_between, get_current_age)

app_history = []

app = Flask(__name__)


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
    """Returns the number of days between two dates."""
    add_to_history(request)
    data = request.get_json()

    if "first" not in data or "last" not in data:
        return {"error": "Missing required data."}, 400

    if not isinstance(data["first"], str) or not isinstance(data["last"], str):
        return {"error": "Unable to convert value to datetime."}, 400

    try:
        first_date = convert_to_datetime(data["first"])
        last_date = convert_to_datetime(data["last"])
    except ValueError:
        return {"error": "Unable to convert value to datetime."}, 400

    days = get_days_between(first_date, last_date)
    return {"days": days}, 200

@app.route("/weekday", methods=["POST"])
def say_which_weekday():
    "Returns the day of the week a specific date is."
    add_to_history(request)
    data = request.get_json()

    if "date" not in data.keys():
        return {"error": "Missing required data."}, 400
    
    try:
        week = convert_to_datetime(data["date"])
    except ValueError:
        return {"error": "Unable to convert value to datetime."}, 400
    
    return {"weekday": get_day_of_week_on(week)}, 200


@app.route("/history", methods=["GET", "DELETE"])
def history():
    """Handles GET and DELETE requests for request history."""
    if request.method == "DELETE":
        add_to_history(request)
        app_history.clear()
        return {"status": "History cleared"}, 200

    add_to_history(request)
    args = request.args.to_dict()

    number = args.get("number", "5")  # Default value is 5

    try:
        number = int(number)
    except ValueError:
        return {"error": "Number must be an integer between 1 and 20."}, 400

    if not 1 <= number <= 20:
        return {"error": "Number must be an integer between 1 and 20."}, 400

    return app_history[-number:][::-1]


@app.route("/current_age", methods=["GET"])
def give_current_age_in_years():
    "Returns a current age in years based on a given birthdate."
    add_to_history(request)

    args = request.args.to_dict()
    birthdate = args.get("date")

    if not birthdate and not isinstance(birthdate, date):
        return {"error": "Date parameter is required."}, 400

    try:
        return {"current_age": get_current_age(birthdate)}
    except TypeError:
        return {"error": "Value for data parameter is invalid."}, 400

if __name__ == "__main__":
    app.run(port=8080, debug=True)
