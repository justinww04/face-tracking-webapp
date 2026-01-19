# Face Tracking Web App

This is a real-time **face tracking** web application built with **Flask** and **OpenCV**.  
It uses your webcam to detect faces, draws green bounding boxes around them, and shows a label explaining what's being tracked — all without storing any personal data.

> ✅ No recognition  
> ✅ No data storage  
> ✅ Just clean, ethical face detection

---

### 🔍 Features

- 📷 Real-time face detection via webcam
- 🟩 Green box highlights each detected face
- 🔒 No enrollment, no storage, no recognition — 100% safe to demo or showcase
- 💻 Built with Python, Flask, and OpenCV
- amin panel
- 2fa verification
- sms alerts
- User roles
- updated css- re did color scheme
-updated home page
- In non showcase version enrollment is completed.
- Admin Controls Panel is accesible in non showcase version.
- Real Time Facial Recognition is available in non showcase version.
- Real Time Facial Recognition learning is available in non showcase version.
- SMS Alert for faces shown in camera is available in non showcase versions.

- new update next week

---

### 📸 Demo

> _Want to see it in action?_  
> You can run it locally with your webcam.

_(Optional: Add screenshots or a YouTube demo link here later.)_

---

### 🚀 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/justinww04/face-tracking-webapp.git
cd face-tracking-webapp

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python backend/app.py
