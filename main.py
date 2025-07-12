from flask import Flask, jsonify, request
from database import create_connection
from flask_cors import CORS
import logging
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins
logging.basicConfig(level=logging.DEBUG)  # Enable debug logging

@app.route('/')
def home():
    app.logger.debug("Handling GET / request")
    return jsonify({"message": "Welcome to YogaCure API! Use /yoga-poses to get yoga poses or /health-plan to create a personalized health plan."})

@app.route('/yoga-poses', methods=['GET'])
def get_yoga_poses():
    condition = request.args.get('condition')
    if not condition:
        app.logger.error("No condition provided in GET /yoga-poses")
        return jsonify({"error": "Condition parameter is required"}), 400
    condition = condition.strip().lower()  # Trim and lowercase
    app.logger.debug(f"Querying poses for condition: '{condition}'")
    conn = create_connection()
    if not conn:
        app.logger.error("Database connection failed")
        return jsonify({"error": "Database connection failed"}), 500
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM yoga_poses WHERE condition = ?", (condition,))
    poses = cursor.fetchall()
    app.logger.debug(f"Found {len(poses)} poses for '{condition}': {poses}")
    conn.close()
    if not poses:
        app.logger.warning(f"No yoga poses found for condition: '{condition}'")
        return jsonify({"error": f"No yoga poses found for condition: {condition}"}), 404
    return jsonify([{"id": p[0], "pose_name": p[2], "description": p[3], "duration_seconds": p[4], "video_url": p[5]} for p in poses])

@app.route('/health-plan', methods=['POST'])
def create_health_plan():
    data = request.get_json()
    app.logger.debug(f"Received POST /health-plan with data: {data}")
    condition = data.get('condition') if data else None
    if not condition:
        app.logger.error("No condition provided in POST /health-plan")
        return jsonify({"error": "Condition is required in request body"}), 400
    condition = condition.strip().lower()  # Trim and lowercase
    app.logger.debug(f"Querying health plan for condition: '{condition}'")
    conn = create_connection()
    if not conn:
        app.logger.error("Database connection failed")
        return jsonify({"error": "Database connection failed"}), 500
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM yoga_poses WHERE condition = ?", (condition,))
    yoga_plan = cursor.fetchall()
    cursor.execute("SELECT * FROM diet_plans WHERE condition = ?", (condition,))
    diet_plan = cursor.fetchall()
    app.logger.debug(f"Found {len(yoga_plan)} poses and {len(diet_plan)} diet plans for '{condition}'")
    conn.close()
    if not yoga_plan:
        app.logger.warning(f"No yoga poses found for condition: '{condition}'")
        return jsonify({"error": f"No yoga poses found for condition: {condition}"}), 404
    return jsonify({
        "condition": condition,
        "yoga_plan": [{"id": p[0], "pose_name": p[2], "description": p[3], "duration_seconds": p[4], "video_url": p[5]} for p in yoga_plan],
        "diet_plan": [{"id": d[0], "day": d[2], "meal_type": d[3], "meal_description": d[4]} for d in diet_plan]
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT
    app.logger.debug(f"Starting app on port {port}")
    app.run(host='0.0.0.0', port=port)