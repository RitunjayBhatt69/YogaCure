from flask import Flask, jsonify, request
from flask_cors import CORS
from database import create_connection, create_tables
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

     # Initialize database
create_tables()

     # Root endpoint for welcome message
@app.route('/', methods=['GET'])
def home():
         return jsonify({"message": "Welcome to YogaCure API! Use /yoga-poses to get yoga poses or /health-plan to create a personalized health plan."}), 200

     # Get yoga poses for a health condition
@app.route('/yoga-poses', methods=['GET'])
def get_yoga_poses():
         condition = request.args.get('condition')
         if not condition:
             return jsonify({"error": "Health condition is required"}), 400

         conn = create_connection()
         try:
             cursor = conn.cursor()
             cursor.execute('SELECT id, pose_name, description, duration_seconds, video_url FROM yoga_poses WHERE condition = ?', (condition,))
             poses = cursor.fetchall()
             if not poses:
                 return jsonify({"error": f"No yoga poses found for condition: {condition}"}), 404
             return jsonify([{
                 "id": pose[0],
                 "pose_name": pose[1],
                 "description": pose[2],
                 "duration_seconds": pose[3],
                 "video_url": pose[4]
             } for pose in poses]), 200
         except Error as e:
             return jsonify({"error": str(e)}), 500
         finally:
             conn.close()

     # Generate personalized health plan (yoga poses and diet)
@app.route('/health-plan', methods=['POST'])
def create_health_plan():
         data = request.get_json()
         condition = data.get('condition')
         if not condition:
             return jsonify({"error": "Health condition is required"}), 400

         conn = create_connection()
         try:
             cursor = conn.cursor()
             # Fetch yoga poses
             cursor.execute('SELECT id, pose_name, description, duration_seconds, video_url FROM yoga_poses WHERE condition = ?', (condition,))
             poses = cursor.fetchall()
             if not poses:
                 return jsonify({"error": f"No yoga poses found for condition: {condition}"}), 404

             # Fetch diet plan
             cursor.execute('SELECT day, meal_type, meal_description FROM diet_plans WHERE condition = ?', (condition,))
             diet = cursor.fetchall()
             if not diet:
                 return jsonify({"error": f"No diet plan found for condition: {condition}"}), 404

             # Format response
             response = {
                 "condition": condition,
                 "yoga_plan": [{
                     "id": pose[0],
                     "pose_name": pose[1],
                     "description": pose[2],
                     "duration_seconds": pose[3],
                     "video_url": pose[4]
                 } for pose in poses],
                 "diet_plan": [{
                     "day": d[0],
                     "meal_type": d[1],
                     "meal_description": d[2]
                 } for d in diet]
             }
             return jsonify(response), 200
         except Error as e:
             return jsonify({"error": str(e)}), 500
         finally:
             conn.close()

if __name__ == '__main__':
         app.run(debug=True)