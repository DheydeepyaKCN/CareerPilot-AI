from flask import Flask, request, jsonify
from agents.career.router_agent import route_query

app = Flask(__name__)


# =========================
# HOME CHECK
# =========================
@app.route("/")
def home():
    return "CareerPilot AI is running 🚀"


# =========================
# MAIN CHAT / QUERY ENDPOINT
# =========================
@app.route("/query", methods=["POST"])
def query():

    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    response = route_query(user_input)

    return jsonify({
        "input": user_input,
        "response": response
    })


# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)