from flask import Flask, jsonify, render_template, send_file
import psutil
import subprocess
import os

app = Flask(__name__)

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

@app.route('/generate_report', methods=['GET'])
def generate_report():
    try:
        # Run powercfg command to generate battery report
        report_path = os.path.join(os.getcwd(), "battery-report.html")
        subprocess.run(["powercfg", "/batteryreport", f"/output", report_path], check=True)

        return jsonify({
            "message": "Battery report generated successfully.",
            "report_path": "/view_report"
        })
    except subprocess.CalledProcessError as e:
        return jsonify({
            "error": "Failed to generate battery report",
            "message": str(e)
        })

@app.route('/view_report', methods=['GET'])
def view_report():
    report_path = os.path.join(os.getcwd(), "battery-report.html")
    if os.path.exists(report_path):
        return send_file(report_path)
    else:
        return jsonify({"error": "Report not found"})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
