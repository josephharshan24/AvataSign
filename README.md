# ✍️ AvataSign — AI-Powered Gesture-Based Signature and Avatar System

AvataSign is an AI-based system that allows users to generate personalized digital signatures and avatars using real-time hand gesture recognition. It combines computer vision, deep learning, and web technologies to provide a seamless, interactive user experience.

---

## 🚀 Features

- ✋ Real-time hand gesture detection using webcam
- 🧠 Deep learning models (`gesture_model.pkl`, `gesture_map.pkl`) to interpret gestures
- 🖼️ Avatar and signature generation modules
- 🌐 Flask-based web interface with `static/` and `templates/`
- 🗃️ MySQL/SQLite-based user data storage (via WAMP or local DB)
- 🗂️ Organized modular structure (`camera`, `sign`, `avatar`, etc.)

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (via `templates/` and `static/`)
- **Backend:** Python, Flask
- **AI/ML:** Trained gesture classification model (using CNN or similar)
- **Database:** MySQL (via WAMP) or SQLite
- **Others:** OpenCV, NumPy, Pickle

---

## 📂 Project Structure

```
sign_tone_new/
├── camera/              # Webcam interaction & capture logic
├── avatar/              # Avatar generation logic
├── sign/                # Signature generation logic
├── static/              # CSS, JS, images
├── templates/           # HTML templates for Flask
├── gesture_model.pkl    # Trained model for gesture recognition
├── gesture_map.pkl      # Mapping of gestures to actions
├── main.py              # Entry point (Flask app)
├── database/            # MySQL/SQLite dump or config
├── requirements.txt     # Python dependencies
└── README.md            # Project overview
```

---

## 🖥️ Setup Instructions (Local)

### 🔧 Prerequisites
- Python 3.8+
- Git
- WAMP/XAMPP (if using MySQL DB)

### 📦 Install dependencies

```bash
git clone https://github.com/josephharshan24/AvataSign.git
cd AvataSign
python -m venv venv
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
```

### 🧠 Run the App

```bash
python main.py
```

Then open `http://localhost:5000` in your browser.

> ⚠️ Ensure your webcam is connected.

---

## 🛢️ Database Setup

- If using **WAMP**:
  - Import the `.sql` file from `/database` via **phpMyAdmin**
  - Update DB credentials in `main.py` or your DB config

---

## 📸 Screenshots (Optional)

_Add UI/gesture screenshots here if available._

---

## 🧠 AI Model Details

- Model trained on hand gesture data using OpenCV and a CNN classifier
- Outputs mapped to avatar/signature selection logic
- Stored using `pickle` in `.pkl` files

---

## 📜 License

MIT License — feel free to modify and use for learning and research purposes.

---

## 👨‍💻 Author

- **Joseph Harshan**  
  [GitHub](https://github.com/josephharshan24)  
  [LinkedIn]([https://linkedin.com/in/josephharshan24](https://www.linkedin.com/in/joseph-harshan-88b763248/))

---

## 🙏 Acknowledgements

- OpenCV & Flask communities
- GitHub Copilot / ChatGPT for guidance
