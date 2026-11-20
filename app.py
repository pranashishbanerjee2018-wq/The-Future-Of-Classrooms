"""
THE FUTURE OF CLASSROOMS
Reimagining Education Through Innovation, Intelligence and Technology
File: app.py

Flask Web Application & Scientific Computing API Server.
Hosts the interactive academic presentation and provides real-time API endpoints
for MATLAB simulation data and execution.
"""

import os
import json
from flask import Flask, render_template, jsonify, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory(DATA_DIR, filename)

@app.route('/results/<path:filename>')
def serve_results(filename):
    return send_from_directory(RESULTS_DIR, filename)

@app.route('/api/results')
def api_results():
    json_path = os.path.join(DATA_DIR, "analysis_results.json")
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({"error": "Results not yet generated"}), 404

@app.route('/api/run_matlab', methods=['POST', 'GET'])
def api_run_matlab():
    import matlab_runner
    res = matlab_runner.run_simulation()
    return jsonify(res)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"[FUTURE OF CLASSROOMS] Launching Flask server on http://127.0.0.1:{port}")
    app.run(host='127.0.0.1', port=port, debug=False)
