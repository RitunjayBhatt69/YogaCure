# 🧘‍♂️ YogaCure: Health-Specific Yoga and Diet REST API

**YogaCure** is a RESTful API built with Flask and SQLite to recommend personalized yoga poses and Indian diet plans based on various health conditions such as back pain, asthma, diabetes, arthritis, and more. It’s designed specifically for **developers** who want to integrate yoga and wellness suggestions into their apps.

---

## 🚀 Why Use YogaCure?

- 🧘‍♀️ **Comprehensive**: Yoga poses and diet plans for 30+ health conditions.
- 💸 **Free & Open**: Hosted on Render’s free tier, no cost to access or deploy.
- 🇮🇳 **Indian Context**: Emphasizes Indian dietary options (e.g., dal, roti) and traditional yoga.
- 🪶 **Lightweight**: Uses SQLite for easy setup and deployment.
- 👨‍💻 **Developer Friendly**: Clean JSON responses, easy to integrate.

---

## 🔗 Live Demo

➡️ **Test the API**: [https://yogsantra.onrender.com](https://yogsantra.onrender.com)

---

## 🩺 Supported Health Conditions

YogaCure provides plans for:

- Cold, Cough, Coryza
- Asthma, Acidity, Diabetes
- Mental Tension, Nervous Tension, Insomnia
- Back Pain, Spinal Disorders, Sciatica
- Kidney Problems, Liver Disorders
- Obesity, Constipation, Piles and Fistula
- Fatigue, Sour Eructations
- Rheumatism, Arthritis, Gout
- Weak Sexual Power, Frigidity and Sterility
- Menstrual Disorders, Hypertension, Throat Infections
- Stomach Disorders, Nervous Debility

Each plan includes yoga poses (asanas) and soon, a full diet chart (ongoing).

---

## 📡 API Endpoints

### `GET /`

Returns a welcome message.

**Example:**

###```json
{
  "message": "Welcome to YogaCure API! Use /yoga-poses to get yoga poses or /health-plan to create a personalized health plan."
}

**Response:**

