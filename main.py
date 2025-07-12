from flask import Flask, jsonify, request
from database import create_connection
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

@app.route('/')
def home():
    return jsonify({"message": "Welcome to YogaCure API! Use /yoga-poses to get yoga poses or /health-plan to create a personalized health plan."})

@app.route('/yoga-poses', methods=['GET'])
def get_yoga_poses():
    condition = request.args.get('condition')
    if not condition:
        return jsonify({"error": "Condition parameter is required"}), 400
    condition = condition.lower()  # Normalize to lowercase
    conn = create_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM yoga_poses WHERE condition = ?", (condition,))
    poses = cursor.fetchall()
    conn.close()
    if not poses:
        return jsonify({"error": f"No yoga poses found for condition: {condition}"}), 404
    return jsonify([{"id": p[0], "pose_name": p[2], "description": p[3], "duration_seconds": p[4], "video_url": p[5]} for p in poses])

@app.route('/health-plan', methods=['POST'])
def create_health_plan():
    data = request.get_json()
    condition = data.get('condition') if data else None
    if not condition:
        return jsonify({"error": "Condition is required in request body"}), 400
    condition = condition.lower()  # Normalize to lowercase
    conn = create_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM yoga_poses WHERE condition = ?", (condition,))
    yoga_plan = cursor.fetchall()
    cursor.execute("SELECT * FROM diet_plans WHERE condition = ?", (condition,))
    diet_plan = cursor.fetchall()
    conn.close()
    if not yoga_plan:
        return jsonify({"error": f"No yoga poses found for condition: {condition}"}), 404
    return jsonify({
        "condition": condition,
        "yoga_plan": [{"id": p[0], "pose_name": p[2], "description": p[3], "duration_seconds": p[4], "video_url": p[5]} for p in yoga_plan],
        "diet_plan": [{"id": d[0], "day": d[2], "meal_type": d[3], "meal_description": d[4]} for d in diet_plan]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)