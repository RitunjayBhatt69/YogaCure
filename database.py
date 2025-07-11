import sqlite3
from sqlite3 import Error
import os

import sqlite3
import os

def create_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'yoga.db')
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_tables():
         conn = create_connection()
         try:
             cursor = conn.cursor()
             # Drop existing tables to clear data
             cursor.execute('DROP TABLE IF EXISTS yoga_poses')
             cursor.execute('DROP TABLE IF EXISTS diet_plans')
             # Create yoga_poses table with unique constraint
             cursor.execute('''
                 CREATE TABLE IF NOT EXISTS yoga_poses (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     condition TEXT NOT NULL,
                     pose_name TEXT NOT NULL,
                     description TEXT,
                     duration_seconds INTEGER,
                     video_url TEXT,
                     UNIQUE(condition, pose_name)
                 )
             ''')
             # Create diet_plans table with unique constraint
             cursor.execute('''
                 CREATE TABLE IF NOT EXISTS diet_plans (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     condition TEXT NOT NULL,
                     day INTEGER NOT NULL,
                     meal_type TEXT NOT NULL,
                     meal_description TEXT,
                     UNIQUE(condition, day, meal_type)
                 )
             ''')
             # Insert new yoga poses
             yoga_data = [
                 ('cold', 'Sarvangasana', 'Shoulder stand to boost immunity.', 60, 'https://example.com/sarvangasana'),
                 ('cold', 'Halasana', 'Plow pose to improve sinus drainage.', 45, 'https://example.com/halasana'),
                 ('cold', 'Shirshasana', 'Headstand to enhance circulation.', 30, 'https://example.com/shirshasana'),
                 ('cough', 'Matsyaasana', 'Fish pose to open chest.', 45, 'https://example.com/matsyaasana'),
                 ('cough', 'Janushirasana', 'Head-to-knee pose for respiratory relief.', 60, 'https://example.com/janushirasana'),
                 ('cough', 'Supta Vajrasana', 'Reclining thunderbolt pose for lung health.', 45, 'https://example.com/supta-vajrasana'),
                 ('cough', 'Urdhva Vajrasana', 'Upward thunderbolt pose for breathing.', 30, 'https://example.com/urdhva-vajrasana'),
                 ('asthma', 'Shirshasana', 'Headstand to improve lung capacity.', 30, 'https://example.com/shirshasana'),
                 ('asthma', 'Shavasana', 'Corpse pose to relax breathing.', 120, 'https://example.com/shavasana'),
                 ('asthma', 'Sarvangasana', 'Shoulder stand for respiratory health.', 60, 'https://example.com/sarvangasana'),
                 ('asthma', 'Matsyaasana', 'Fish pose to open chest.', 45, 'https://example.com/matsyaasana'),
                 ('asthma', 'Supta Vajrasana', 'Reclining thunderbolt for asthma relief.', 45, 'https://example.com/supta-vajrasana'),
                 ('asthma', 'Shalabhasana', 'Locust pose to strengthen lungs.', 30, 'https://example.com/shalabhasana'),
                 ('asthma', 'Ushtrasana', 'Camel pose to expand chest.', 30, 'https://example.com/ushtrasana'),
                 ('asthma', 'Ujjayi Pranayam', 'Ocean breath to calm respiratory system.', 60, 'https://example.com/ujjayi-pranayam'),
                 ('diabetes', 'Dhanurasana', 'Bow pose to stimulate pancreas.', 30, 'https://example.com/dhanurasana'),
                 ('diabetes', 'Matsyendrasana', 'Spinal twist for digestion.', 45, 'https://example.com/matsyendrasana'),
                 ('diabetes', 'Naukasana', 'Boat pose for metabolic health.', 30, 'https://example.com/naukasana'),
                 ('diabetes', 'Surya Namaskarasana', 'Sun salutation for overall health.', 120, 'https://example.com/surya-namaskarasana'),
                 ('diabetes', 'Sarpaasana', 'Cobra pose to improve circulation.', 45, 'https://example.com/sarpaasana'),
                 ('stomach disorders', 'Sukhasana', 'Easy pose for digestion.', 60, 'https://example.com/sukhasana'),
                 ('stomach disorders', 'Padmaasana', 'Lotus pose for gut health.', 60, 'https://example.com/padmaasana'),
                 ('stomach disorders', 'Bhujangasana', 'Cobra pose for abdominal strength.', 30, 'https://example.com/bhujangasana'),
                 ('stomach disorders', 'Ardhachakrasana', 'Half-wheel pose for digestion.', 30, 'https://example.com/ardhachakrasana'),
                 ('stomach disorders', 'Uttanpadasana', 'Raised leg pose for gut motility.', 45, 'https://example.com/uttanpadasana'),
                 ('stomach disorders', 'Shalabhasana', 'Locust pose for digestive health.', 30, 'https://example.com/shalabhasana'),
                 ('liver disorders', 'Mayurasana', 'Peacock pose for liver detox.', 30, 'https://example.com/mayurasana'),
                 ('liver disorders', 'Bhujangasana', 'Cobra pose for liver health.', 30, 'https://example.com/bhujangasana'),
                 ('liver disorders', 'Shalabhasana', 'Locust pose for organ stimulation.', 30, 'https://example.com/shalabhasana'),
                 ('liver disorders', 'Shirshasana', 'Headstand for circulation.', 30, 'https://example.com/shirshasana'),
                 ('liver disorders', 'Shashankasana', 'Moon pose for relaxation.', 45, 'https://example.com/shashankasana'),
                 ('liver disorders', 'Halasana', 'Plow pose for liver health.', 45, 'https://example.com/halasana'),
                 ('liver disorders', 'Ushtrasana', 'Camel pose for organ stimulation.', 30, 'https://example.com/ushtrasana'),
                 ('mental tension', 'Trikonasana', 'Triangle pose for stress relief.', 30, 'https://example.com/trikonasana'),
                 ('mental tension', 'Halasana', 'Plow pose for calming mind.', 45, 'https://example.com/halasana'),
                 ('mental tension', 'Vajrasana', 'Thunderbolt pose for relaxation.', 60, 'https://example.com/vajrasana'),
                 ('mental tension', 'Shavasana', 'Corpse pose for mental calm.', 120, 'https://example.com/shavasana'),
                 ('mental tension', 'Garbhasana', 'Fetal pose for stress relief.', 60, 'https://example.com/garbhasana'),
                 ('mental tension', 'Shashankasana', 'Moon pose for relaxation.', 45, 'https://example.com/shashankasana'),
                 ('mental tension', 'Sarvangasana', 'Shoulder stand for mental clarity.', 60, 'https://example.com/sarvangasana'),
                 ('nervous debility', 'Halasana', 'Plow pose for nervous system.', 45, 'https://example.com/halasana'),
                 ('nervous debility', 'Chakrasana', 'Wheel pose for energy.', 30, 'https://example.com/chakrasana'),
                 ('nervous debility', 'Dhanurasana', 'Bow pose for vitality.', 30, 'https://example.com/dhanurasana'),
                 ('nervous debility', 'Garbhasana', 'Fetal pose for calm.', 60, 'https://example.com/garbhasana'),
                 ('nervous debility', 'Vajrasana', 'Thunderbolt pose for stability.', 60, 'https://example.com/vajrasana'),
                 ('nervous debility', 'Shirshasana', 'Headstand for nerve health.', 30, 'https://example.com/shirshasana'),
                 ('nervous debility', 'Sarvangasana', 'Shoulder stand for circulation.', 60, 'https://example.com/sarvangasana'),
                 ('nervous debility', 'Shalabhasana', 'Locust pose for strength.', 30, 'https://example.com/shalabhasana'),
                 ('nervous debility', 'Paschimottanasana', 'Seated forward bend for calm.', 45, 'https://example.com/paschimottanasana'),
                 ('nervous debility', 'Shashankasana', 'Moon pose for relaxation.', 45, 'https://example.com/shashankasana'),
                 ('nervous tension', 'Shavasana', 'Corpse pose for deep relaxation.', 120, 'https://example.com/shavasana'),
                 ('nervous tension', 'Kurmasana', 'Tortoise pose for mental calm.', 60, 'https://example.com/kurmasana'),
                 ('insomnia', 'Halasana', 'Plow pose for sleep.', 45, 'https://example.com/halasana'),
                 ('insomnia', 'Shirshasana', 'Headstand for relaxation.', 30, 'https://example.com/shirshasana'),
                 ('insomnia', 'Sarvangasana', 'Shoulder stand for calming.', 60, 'https://example.com/sarvangasana'),
                 ('insomnia', 'Sheetali Pranayam', 'Cooling breath for sleep.', 60, 'https://example.com/sheetali-pranayam'),
                 ('insomnia', 'Sheetkari Pranayam', 'Hissing breath for relaxation.', 60, 'https://example.com/sheetkari-pranayam'),
                 ('hypertension', 'Shashankasana', 'Moon pose for blood pressure.', 45, 'https://example.com/shashankasana'),
                 ('hypertension', 'Vajrasana', 'Thunderbolt pose for calm.', 60, 'https://example.com/vajrasana'),
                 ('hypertension', 'Pawanmuktasana', 'Wind-relieving pose for stress.', 45, 'https://example.com/pawanmuktasana'),
                 ('kidney problems', 'Ardha Matsyendrasana', 'Half spinal twist for kidney health.', 45, 'https://example.com/ardha-matsyendrasana'),
                 ('kidney problems', 'Ushtrasana', 'Camel pose for organ stimulation.', 30, 'https://example.com/ushtrasana'),
                 ('kidney problems', 'Bhujangasana', 'Cobra pose for kidney function.', 30, 'https://example.com/bhujangasana'),
                 ('kidney problems', 'Gomukhasana', 'Cow face pose for relaxation.', 45, 'https://example.com/gomukhasana'),
                 ('kidney problems', 'Shashankasana', 'Moon pose for calm.', 45, 'https://example.com/shashankasana'),
                 ('kidney problems', 'Halasana', 'Plow pose for kidney health.', 45, 'https://example.com/halasana'),
                 ('kidney problems', 'Dhanurasana', 'Bow pose for organ stimulation.', 30, 'https://example.com/dhanurasana'),
                 ('obesity', 'Trikonasana', 'Triangle pose for weight management.', 30, 'https://example.com/trikonasana'),
                 ('obesity', 'Paschimottanasana', 'Seated forward bend for metabolism.', 45, 'https://example.com/paschimottanasana'),
                 ('obesity', 'Dhanurasana', 'Bow pose for fat reduction.', 30, 'https://example.com/dhanurasana'),
                 ('obesity', 'Halasana', 'Plow pose for weight control.', 45, 'https://example.com/halasana'),
                 ('obesity', 'Shalabhasana', 'Locust pose for metabolism.', 30, 'https://example.com/shalabhasana'),
                 ('obesity', 'Sarvangasana', 'Shoulder stand for thyroid health.', 60, 'https://example.com/sarvangasana'),
                 ('obesity', 'Pada Hastasana', 'Hand-to-foot pose for flexibility.', 30, 'https://example.com/pada-hastasana'),
                 ('obesity', 'Nadi Shodhana', 'Alternate nostril breathing for balance.', 60, 'https://example.com/nadi-shodhana'),
                 ('obesity', 'Uddiyana Bandha', 'Abdominal lock for digestion.', 30, 'https://example.com/uddiyana-bandha'),
                 ('arthritis', 'Trikonasana', 'Triangle pose for joint mobility.', 30, 'https://example.com/trikonasana'),
                 ('arthritis', 'Santulanasana', 'Balancing pose for joint strength.', 30, 'https://example.com/santulanasana'),
                 ('arthritis', 'Gomukhasana', 'Cow face pose for joint flexibility.', 45, 'https://example.com/gomukhasana'),
                 ('arthritis', 'Siddhasana', 'Accomplished pose for joint health.', 60, 'https://example.com/siddhasana'),
                 ('arthritis', 'Natarajasana', 'Dancer pose for balance.', 30, 'https://example.com/natarajasana'),
                 ('arthritis', 'Veerasana', 'Warrior pose for joint strength.', 30, 'https://example.com/veerasana'),
                 ('arthritis', 'Vrikshasana', 'Tree pose for balance.', 30, 'https://example.com/vrikshasana'),
                 ('arthritis', 'Setu Bandhasana', 'Bridge pose for joint relief.', 30, 'https://example.com/setu-bandhasana'),
                 ('back pain', 'Chakrasana', 'Wheel pose for spine flexibility.', 30, 'https://example.com/chakrasana'),
                 ('back pain', 'Dhanurasana', 'Bow pose for back strength.', 30, 'https://example.com/dhanurasana'),
                 ('back pain', 'Bhujangasana', 'Cobra pose for spine health.', 30, 'https://example.com/bhujangasana'),
                 ('back pain', 'Mayurasana', 'Peacock pose for core strength.', 30, 'https://example.com/mayurasana'),
                 ('back pain', 'Shashankasana', 'Moon pose for back relief.', 45, 'https://example.com/shashankasana'),
                 ('back pain', 'Supta Vajrasana', 'Reclining thunderbolt for spine.', 45, 'https://example.com/supta-vajrasana'),
                 ('back pain', 'Padmasana', 'Lotus pose for posture.', 60, 'https://example.com/padmasana'),
                 ('back pain', 'Trikonasana', 'Triangle pose for spinal alignment.', 30, 'https://example.com/trikonasana'),
                 ('back pain', 'Utkatasana', 'Chair pose for back strength.', 30, 'https://example.com/utkatasana'),
                 ('back pain', 'Naukasana', 'Boat pose for core stability.', 30, 'https://example.com/naukasana'),
                 ('back pain', 'Pada Shalabhasana', 'Leg locust pose for back.', 30, 'https://example.com/pada-shalabhasana'),
                 ('rheumatism', 'Dhanurasana', 'Bow pose for joint mobility.', 30, 'https://example.com/dhanurasana'),
                 ('rheumatism', 'Padmasana', 'Lotus pose for joint health.', 60, 'https://example.com/padmasana'),
                 ('rheumatism', 'Vajrasana', 'Thunderbolt pose for joint relief.', 60, 'https://example.com/vajrasana'),
                 ('spinal disorders', 'Halasana', 'Plow pose for spinal health.', 45, 'https://example.com/halasana'),
                 ('spinal disorders', 'Dhanurasana', 'Bow pose for spine strength.', 30, 'https://example.com/dhanurasana'),
                 ('spinal disorders', 'Chakrasana', 'Wheel pose for flexibility.', 30, 'https://example.com/chakrasana'),
                 ('spinal disorders', 'Bhujangasana', 'Cobra pose for spine alignment.', 30, 'https://example.com/bhujangasana'),
                 ('spinal disorders', 'Shirshasana', 'Headstand for spinal health.', 30, 'https://example.com/shirshasana'),
                 ('spinal disorders', 'Vrishchikasana', 'Scorpion pose for advanced spine work.', 30, 'https://example.com/vrishchikasana'),
                 ('spinal disorders', 'Shashankasana', 'Moon pose for spinal relief.', 45, 'https://example.com/shashankasana'),
                 ('spinal disorders', 'Ushtrasana', 'Camel pose for spine mobility.', 30, 'https://example.com/ushtrasana'),
                 ('spinal disorders', 'Paschimottanasana', 'Seated forward bend for spine.', 45, 'https://example.com/paschimottanasana'),
                 ('gout', 'Dhanurasana', 'Bow pose for joint health.', 30, 'https://example.com/dhanurasana'),
                 ('gout', 'Paschimottanasana', 'Seated forward bend for joints.', 45, 'https://example.com/paschimottanasana'),
                 ('gout', 'Pawanmuktasana', 'Wind-relieving pose for joint relief.', 45, 'https://example.com/pawanmuktasana'),
                 ('gout', 'Trikonasana', 'Triangle pose for mobility.', 30, 'https://example.com/trikonasana'),
                 ('gout', 'Parvatasana', 'Mountain pose for joint health.', 30, 'https://example.com/parvatasana'),
                 ('gout', 'Gomukhasana', 'Cow face pose for flexibility.', 45, 'https://example.com/gomukhasana'),
                 ('gout', 'Ardha Matsyendrasana', 'Half spinal twist for joints.', 45, 'https://example.com/ardha-matsyendrasana'),
                 ('gout', 'Janusirasana', 'Head-to-knee pose for joint relief.', 60, 'https://example.com/janusirasana'),
                 ('sciatica', 'Vajrasana', 'Thunderbolt pose for nerve relief.', 60, 'https://example.com/vajrasana'),
                 ('sciatica', 'Gomukhasana', 'Cow face pose for sciatic relief.', 45, 'https://example.com/gomukhasana'),
                 ('sciatica', 'Hanumanasana', 'Monkey pose for nerve stretch.', 30, 'https://example.com/hanumanasana'),
                 ('constipation', 'Tadasana', 'Mountain pose for digestion.', 30, 'https://example.com/tadasana'),
                 ('constipation', 'Chakrasana', 'Wheel pose for gut motility.', 30, 'https://example.com/chakrasana'),
                 ('constipation', 'Janusirasana', 'Head-to-knee pose for digestion.', 60, 'https://example.com/janusirasana'),
                 ('constipation', 'Mayurasana', 'Peacock pose for digestive health.', 30, 'https://example.com/mayurasana'),
                 ('constipation', 'Bhujangasana', 'Cobra pose for gut health.', 30, 'https://example.com/bhujangasana'),
                 ('constipation', 'Dhanurasana', 'Bow pose for digestion.', 30, 'https://example.com/dhanurasana'),
                 ('constipation', 'Bhoomi Pada Mastakasana', 'Earth-head pose for digestion.', 45, 'https://example.com/bhoomi-pada-mastakasana'),
                 ('constipation', 'Supta Vajrasana', 'Reclining thunderbolt for digestion.', 45, 'https://example.com/supta-vajrasana'),
                 ('constipation', 'Karna Peedasana', 'Ear-pressure pose for gut health.', 30, 'https://example.com/karna-peedasana'),
                 ('constipation', 'Pada Hastasana', 'Hand-to-foot pose for digestion.', 30, 'https://example.com/pada-hastasana'),
                 ('constipation', 'Matsyasana', 'Fish pose for digestive relief.', 45, 'https://example.com/matsyasana'),
                 ('acidity', 'Shalabhasana', 'Locust pose for acid reflux relief.', 30, 'https://example.com/shalabhasana'),
                 ('sour eructations', 'Bhujangasana', 'Cobra pose for acid relief.', 30, 'https://example.com/bhujangasana'),
                 ('sour eructations', 'Janusirasana', 'Head-to-knee pose for digestion.', 60, 'https://example.com/janusirasana'),
                 ('sour eructations', 'Chakrasana', 'Wheel pose for gut health.', 30, 'https://example.com/chakrasana'),
                 ('sour eructations', 'Ushtrasana', 'Camel pose for acid relief.', 30, 'https://example.com/ushtrasana'),
                 ('sour eructations', 'Hasta Pada Angushthasana', 'Hand-to-toe pose for digestion.', 30, 'https://example.com/hasta-pada-angushthasana'),
                 ('sour eructations', 'Paschimottanasana', 'Seated forward bend for acid relief.', 45, 'https://example.com/paschimottanasana'),
                 ('frigidity and sterility', 'Bhujangasana', 'Cobra pose for reproductive health.', 30, 'https://example.com/bhujangasana'),
                 ('frigidity and sterility', 'Shirshasana', 'Headstand for hormonal balance.', 30, 'https://example.com/shirshasana'),
                 ('frigidity and sterility', 'Paschimottanasana', 'Seated forward bend for pelvic health.', 45, 'https://example.com/paschimottanasana'),
                 ('frigidity and sterility', 'Sarvangasana', 'Shoulder stand for hormonal health.', 60, 'https://example.com/sarvangasana'),
                 ('frigidity and sterility', 'Matsyasana', 'Fish pose for reproductive health.', 45, 'https://example.com/matsyasana'),
                 ('frigidity and sterility', 'Supta Vajrasana', 'Reclining thunderbolt for pelvic health.', 45, 'https://example.com/supta-vajrasana'),
                 ('weak sexual power', 'Chakrasana', 'Wheel pose for vitality.', 30, 'https://example.com/chakrasana'),
                 ('weak sexual power', 'Sarvangasana', 'Shoulder stand for hormonal balance.', 60, 'https://example.com/sarvangasana'),
                 ('weak sexual power', 'Garudasana', 'Eagle pose for energy.', 30, 'https://example.com/garudasana'),
                 ('weak sexual power', 'Vatayanasana', 'Horse pose for pelvic health.', 30, 'https://example.com/vatayanasana'),
                 ('weak sexual power', 'Bhujangasana', 'Cobra pose for vitality.', 30, 'https://example.com/bhujangasana'),
                 ('weak sexual power', 'Paschimottanasana', 'Seated forward bend for energy.', 45, 'https://example.com/paschimottanasana'),
                 ('weak sexual power', 'Shirshasana', 'Headstand for hormonal health.', 30, 'https://example.com/shirshasana'),
                 ('coryza', 'Shirshasana', 'Headstand for sinus relief.', 30, 'https://example.com/shirshasana'),
                 ('coryza', 'Halasana', 'Plow pose for sinus health.', 45, 'https://example.com/halasana'),
                 ('coryza', 'Sarvangasana', 'Shoulder stand for immunity.', 60, 'https://example.com/sarvangasana'),
                 ('throat infections', 'Simhasana', 'Lion pose for throat health.', 30, 'https://example.com/simhasana'),
                 ('throat infections', 'Sarvangasana', 'Shoulder stand for immunity.', 60, 'https://example.com/sarvangasana'),
                 ('throat infections', 'Shirshasana', 'Headstand for circulation.', 30, 'https://example.com/shirshasana'),
                 ('throat infections', 'Halasana', 'Plow pose for throat relief.', 45, 'https://example.com/halasana'),
                 ('throat infections', 'Chakrasana', 'Wheel pose for chest opening.', 30, 'https://example.com/chakrasana'),
                 ('throat infections', 'Bhujangasana', 'Cobra pose for throat health.', 30, 'https://example.com/bhujangasana'),
                 ('throat infections', 'Supta Vajrasana', 'Reclining thunderbolt for throat.', 45, 'https://example.com/supta-vajrasana'),
                 ('throat infections', 'Matsyasana', 'Fish pose for throat relief.', 45, 'https://example.com/matsyasana'),
                 ('menstrual disorders', 'Halasana', 'Plow pose for hormonal balance.', 45, 'https://example.com/halasana'),
                 ('menstrual disorders', 'Dhanurasana', 'Bow pose for pelvic health.', 30, 'https://example.com/dhanurasana'),
                 ('menstrual disorders', 'Shavasana', 'Corpse pose for relaxation.', 120, 'https://example.com/shavasana'),
                 ('menstrual disorders', 'Vajrasana', 'Thunderbolt pose for pelvic health.', 60, 'https://example.com/vajrasana'),
                 ('menstrual disorders', 'Sarvangasana', 'Shoulder stand for hormonal balance.', 60, 'https://example.com/sarvangasana'),
                 ('menstrual disorders', 'Bhujangasana', 'Cobra pose for pelvic health.', 30, 'https://example.com/bhujangasana'),
                 ('menstrual disorders', 'Matsyasana', 'Fish pose for hormonal health.', 45, 'https://example.com/matsyasana'),
                 ('menstrual disorders', 'Parvatasana', 'Mountain pose for relaxation.', 30, 'https://example.com/parvatasana'),
                 ('menstrual disorders', 'Shalabhasana', 'Locust pose for pelvic health.', 30, 'https://example.com/shalabhasana'),
                 ('menstrual disorders', 'Shirshasana', 'Headstand for hormonal balance.', 30, 'https://example.com/shirshasana'),
                 ('piles and fistula', 'Siddhasana', 'Accomplished pose for pelvic health.', 60, 'https://example.com/siddhasana'),
                 ('piles and fistula', 'Gomukhasana', 'Cow face pose for pelvic relief.', 45, 'https://example.com/gomukhasana'),
                 ('piles and fistula', 'Bhadrasana', 'Gracious pose for pelvic health.', 60, 'https://example.com/bhadrasana'),
                 ('piles and fistula', 'Chandra Namaskarasana', 'Moon salutation for calm.', 120, 'https://example.com/chandra-namaskarasana'),
                 ('piles and fistula', 'Janusirasana', 'Head-to-knee pose for digestion.', 60, 'https://example.com/janusirasana'),
                 ('piles and fistula', 'Sukhasana', 'Easy pose for pelvic health.', 60, 'https://example.com/sukhasana'),
                 ('piles and fistula', 'Sarvangasana', 'Shoulder stand for circulation.', 60, 'https://example.com/sarvangasana'),
                 ('piles and fistula', 'Uttanpadasana', 'Raised leg pose for pelvic health.', 45, 'https://example.com/uttanpadasana'),
                 ('fatigue', 'Pretasana', 'Corpse-like pose for deep rest.', 120, 'https://example.com/pretasana'),
                 ('fatigue', 'Shavasana', 'Corpse pose for relaxation.', 120, 'https://example.com/shavasana'),
                 ('fatigue', 'Matsyasana', 'Fish pose for energy.', 45, 'https://example.com/matsyasana'),
                 ('fatigue', 'Dandasana', 'Staff pose for strength.', 30, 'https://example.com/dandasana')
             ]
             cursor.executemany('INSERT OR IGNORE INTO yoga_poses (condition, pose_name, description, duration_seconds, video_url) VALUES (?, ?, ?, ?, ?)', yoga_data)
             # Insert sample diet plans
             diet_data = [
                 ('diabetes', 1, 'Breakfast', 'Oatmeal with berries, no added sugar'),
                 ('back pain', 1, 'Lunch', 'Grilled vegetables with quinoa'),
                 ('stress', 1, 'Dinner', 'Dal with brown rice and steamed greens')
             ]
             cursor.executemany('INSERT OR IGNORE INTO diet_plans (condition, day, meal_type, meal_description) VALUES (?, ?, ?, ?)', diet_data)
             conn.commit()
         except Error as e:
             print(f"Error creating tables: {e}")
         finally:
             conn.close()