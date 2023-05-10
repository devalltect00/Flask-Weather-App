from flask import Flask, render_template, request, make_response
import requests
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/')
def index():
    location = request.cookies.get('location')
    return render_template('index.html', location=location)

@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    api_key = app.config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    resp = make_response(render_template('weather.html', temperature=temperature, description=description))
    resp.set_cookie('location', location)
    return resp

if __name__ == '__main__':
    app.run()
