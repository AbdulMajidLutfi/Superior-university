from flask import Flask, request, render_template
from weather import OpenWeatherAPI
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    location = ""
    if request.method == "POST":
        location = request.form["location"]
        weather_api = OpenWeatherAPI(api_key="8f85c24bd5674261b50236721d2842c9")
        weather, error = weather_api.fetch_weather(location)
        if weather:
            weather.save_to_csv(location)
    return render_template("index.html", weather=weather, error=error, location=location)

if __name__ == "__main__":
    app.run(debug=True)





