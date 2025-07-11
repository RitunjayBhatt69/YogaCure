YogaCure is a REST API built with Flask and SQLite to recommend personalized yoga poses and diet plans for specific health issues (e.g., back pain, stress, diabetes). Designed for developers to integrate into custom apps, it offers a flexible, free, and lightweight backend, deployed on Render’s free tier.

 ## Why Choose YogaCure?
 Unlike consumer apps like Todoist or Alo Moves, YogaCure is a developer-focused API that enables custom task management solutions for health conditions. It provides:
 - **Health-Specific Plans**: Tailored yoga poses (e.g., Cat-Cow Pose for back pain) and diet plans (e.g., low-glycemic meals for diabetes).
 - **Free and Accessible**: No paywalls, hosted on Render’s free tier.
 - **Indian Context**: Includes Indian dietary preferences (e.g., dal, roti) and traditional yoga.
 - **Lightweight**: Uses SQLite for simplicity and scalability.

 ## Live Demo
 Test the API at: [https://yogsantra.onrender.com](https://yogsantra.onrender.com)

 ## API Endpoints
 - **GET /**: Welcome message for the API.
   - Example: `https://yogsantra.onrender.com/`
   - Response: `{"message": "Welcome to YogaCure API!..."}`
 - **GET /yoga-poses?condition=<condition>**: Fetch yoga poses for a health condition.
   - Example: `https://yogsantra.onrender.com/yoga-poses?condition=back pain`
   - Response: `[{"id": 1, "pose_name": "Cat-Cow Pose", ...}]`
 - **POST /health-plan**: Create a personalized plan with yoga poses and diet recommendations.
   - Example: `POST https://yogsantra.onrender.com/health-plan`
   - Body: `{"condition": "back pain"}`
   - Response: `{"condition": "back pain", "yoga_plan": [...], "diet_plan": [...]}`

 ## Setup (Local Development)
 1. Clone the repository:
    ```bash
    git clone https://github.com/RitunjayBhatt69/YogaCure.git
    cd yogacure
    ```
 2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
 3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
 4. Run the app:
    ```bash
    python main.py
    ```
 5. Test endpoints using Postman at `http://127.0.0.1:5000`.

 ## Technologies Used
 - **Backend**: Flask (Python), SQLite
 - **Deployment**: Render (free tier)
 - **Testing**: Postman

 ## Future Improvements
 - Add a React frontend for a user-friendly interface.
 - Implement AI-based personalization for yoga and diet plans.
 - Add offline mode with downloadable pose guides and diet PDFs.
 - Include a community forum and gamification (e.g., badges for consistency).

 ## Status
 - Backend API deployed on Render with core endpoints (`/yoga-poses`, `/health-plan`).
 - Next steps: Develop React frontend and add more health conditions.