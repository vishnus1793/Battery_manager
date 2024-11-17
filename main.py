from flask import Flask, jsonify, render_template
import psutil

app = Flask(__name__)

# Route to get the battery status
@app.route('/battery', methods=['GET'])
def battery_status():
    try:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = battery.power_plugged
            return jsonify({
                "battery": percent,
                "plugged": plugged,
                "message": "Battery status fetched successfully"
            })
        else:
            return jsonify({
                "error": "Battery info unavailable",
                "message": "Could not fetch battery information. Ensure you're on a battery-powered device."
            })
    except Exception as e:
        return jsonify({
            "error": "Failed to fetch battery status",
            "message": str(e)
        })

# Route for the home page (HTML page)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
