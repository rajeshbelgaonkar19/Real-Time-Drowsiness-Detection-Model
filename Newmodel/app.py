from flask import Flask, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# API endpoint to start drowsiness detection
@app.route('/start', methods=['POST'])
def start_detection():
    subprocess.Popen(["python", "alarm2.py"])  # Runs detection
    return jsonify({"message": "Drowsiness detection started!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # Backend runs on port 5000
