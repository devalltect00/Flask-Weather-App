from flask import Flask, render_template, request, make_response, session
import requests
import json
from datetime import datetime

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.secret_key = app.config['SECRET_KEY']

@app.route("/", methods=["GET"])
def index():
    location = None
    if "location" in session:
        location = session["location"]
    return render_template("index.html", location=location)

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form["city"]
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={app.config['API_KEY']}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode())
        temperature = data["main"]["temp"]
        icon = data["weather"][0]["icon"]
        location = f"{data['name']}, {data['sys']['country']}"
        session["location"] = location
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return render_template(
            "weather.html",
            temperature=temperature,
            icon=icon,
            location=location,
            time=current_time,
        )
    else:
        return render_template("error.html", error="City not found!")


if __name__ == "__main__":
    # app.run()
    app.run(host="0.0.0.0", port=5000)
