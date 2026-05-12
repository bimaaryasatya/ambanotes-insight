from flask import Flask, jsonify
from flask_cors import CORS
from services.analytics_service import generate_insight

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "Instagram Event Insight API"
    })

@app.route("/api/insights", methods=["GET"])
def insights():
    try:
        data = generate_insight()
        return jsonify(data), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )