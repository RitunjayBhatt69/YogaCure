import sqlite3
from sqlite3 import Error
import os

def create_connection():
         db_path = os.path.join(os.path.dirname(__file__), "yoga.db")
         conn = None
         try:
             conn = sqlite3.connect(db_path)
             return conn
         except Error as e:
             print(f"Error connecting to database: {e}")
         return conn

def create_tables():
         conn = create_connection()
         try:
             cursor = conn.cursor()
             # Table for yoga poses
             cursor.execute('''
                 CREATE TABLE IF NOT EXISTS yoga_poses (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     condition TEXT NOT NULL,
                     pose_name TEXT NOT NULL,
                     description TEXT,
                     duration_seconds INTEGER,
                     video_url TEXT
                 )
             ''')
             # Table for diet plans
             cursor.execute('''
                 CREATE TABLE IF NOT EXISTS diet_plans (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     condition TEXT NOT NULL,
                     day INTEGER NOT NULL,
                     meal_type TEXT NOT NULL,
                     meal_description TEXT
                 )
             ''')
             # Insert sample data for testing
             cursor.execute('''
                 INSERT OR IGNORE INTO yoga_poses (condition, pose_name, description, duration_seconds, video_url)
                 VALUES
                     ('back pain', 'Cat-Cow Pose', 'Gently stretches the spine, relieving back pain.', 30, 'https://example.com/cat-cow'),
                     ('stress', 'Child’s Pose', 'Calms the mind and reduces stress.', 60, 'https://example.com/childs-pose'),
                     ('diabetes', 'Seated Forward Bend', 'Improves circulation and digestion.', 45, 'https://example.com/seated-forward-bend')
             ''')
             cursor.execute('''
                 INSERT OR IGNORE INTO diet_plans (condition, day, meal_type, meal_description)
                 VALUES
                     ('diabetes', 1, 'Breakfast', 'Oatmeal with berries, no added sugar'),
                     ('back pain', 1, 'Lunch', 'Grilled vegetables with quinoa'),
                     ('stress', 1, 'Dinner', 'Dal with brown rice and steamed greens')
             ''')
             conn.commit()
         except Error as e:
             print(f"Error creating tables: {e}")
         finally:
             conn.close()