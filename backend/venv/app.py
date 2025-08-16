from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins

@app.route('/api/message')
def get_message():
    return jsonify({"message": "Hello from Flask backend with Axios!"})

if __name__ == '__main__':
    app.run(debug=True)
