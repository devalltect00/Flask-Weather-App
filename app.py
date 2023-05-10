from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    location = request.form['location']
    api_key = '927277edbe8f004719fab24f02a108fd'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    # return render_template('weather.html', temperature=temperature, description=description)
    return render_template('weather.html', temperature=temperature, description=description, location=location)

if __name__ == '__main__':
    app.run(debug=True)
