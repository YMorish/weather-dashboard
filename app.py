from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # ✅ Allow frontend (index.html) to access this API

API_KEY = "61ed5f7b560b9df208c140ad35821853"   # Replace with your OpenWeather API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/weather", methods=["GET"])
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Please provide a city"}), 400

    # Build request to OpenWeather
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "city": data.get("name", city),
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
            "description": data['weather'][0]['description']
        })
    else:
        return jsonify({"error": "City not found"}), 404

@app.route('/')
def serve_frontend():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)