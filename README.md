# 🏥 Next-Gen Digi-Health Platform

## 📌 Project Overview

Next-Gen Digi-Health is a full-stack digital healthcare prototype that integrates AI-powered health assistance, physiotherapy guidance, e-pharmacy services, and insurance claim management into a single unified platform. The project demonstrates how modern web technologies and AI can simplify healthcare access and workflows.

---

## 🎯 Prototype Objective

To design and demonstrate an integrated digital healthcare ecosystem that provides AI-based health guidance, supports patient recovery through physiotherapy demos, enables online medicine ordering, and streamlines insurance claim tracking.

---

## 💡 One-Line Value Proposition

A unified digital healthcare platform combining AI health guidance, physiotherapy support, e-pharmacy services, and insurance claims in one seamless experience.

---

## 🧩 Core Features

- User authentication (login & registration)
- AI health chatbot using local LLM
- E-pharmacy with cart and checkout flow
- Physiotherapy exercise demo videos
- Insurance claim submission and timeline tracking
- Dashboard-based navigation
- MongoDB-backed data storage

---

## 🛠️ Technology Stack

### Frontend
- HTML5
- CSS3 (Glassmorphism, responsive UI)
- JavaScript (Vanilla)

### Backend
- Python (Flask)
- Flask-Bcrypt
- Flask Sessions

### Database
- MongoDB Atlas

### AI
- Ollama (Phi model)
- Prompt-based response generation (RAG-style)

---

## 📁 Project Structure

Next_gen_digi_health/
│
├── backend/
│   ├── app.py
│   └── ai_chatbot/
│       ├── ollama_client.py
│       ├── rag_engine.py
│       └── prompts.py
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── welcome.html
│   ├── chatbot.html
│   ├── physio.html
│   └── insurance.html
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── videos/
│
└── README.md

---

## ✅ Success Criteria

Metric 1: Coverage (target: all core modules available, observed: all modules implemented)  
Metric 2: Usability (target: smooth end-to-end user flow, observed: flows completed successfully)  
Metric 3: Responsiveness (target: ≤15s chatbot response, observed: ~8–12s response time)

---

## 🧪 Real vs Simulated Components

### Real Components
- User authentication and session handling  
- Dashboard navigation  
- E-pharmacy cart and order storage  
- MongoDB data persistence  
- Local AI chatbot responses  
- Physiotherapy video playback  
- Insurance claim timeline UI  

### Simulated Components
- Medical diagnosis accuracy  
- Insurance claim approval logic  
- Payment gateway processing  
- Real hospital or insurer integrations  
- Advanced clinical decision-making  

---

## ⚠️ Disclaimer

This prototype provides general health guidance only and does not replace professional medical advice. Some components are intentionally simulated to demonstrate system behavior.

---

## 🚀 How to Run the Project

1. Install dependencies:
   pip install flask flask-bcrypt pymongo certifi requests

2. Start Ollama and load a model:
   ollama run phi

3. Run the Flask server:
   python app.py

4. Open in browser:
   http://127.0.0.1:5000

---

## 🔮 Future Enhancements

- Real insurance backend integration  
- Advanced medical RAG knowledge base  
- AI-generated physiotherapy videos  
- Role-based dashboards  
- Production deployment  

---

## 👨‍💻 Author

Next-Gen Digi-Health  
Prototype developed for academic and hackathon demonstration purposes.
