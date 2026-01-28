from flask import Flask, request, jsonify, render_template, redirect, url_for
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from urllib.parse import quote_plus
from datetime import datetime
import certifi

from ai_chatbot.rag_engine import retrieve_context
from ai_chatbot.ollama_client import call_ollama
from ai_chatbot.prompts import SYSTEM_PROMPT, build_user_prompt


app = Flask(__name__)
bcrypt = Bcrypt(app)

# ---------------- MONGODB ----------------
username = "nextgen_admin"
password = quote_plus("nextgen123")

MONGO_URI = (
    f"mongodb+srv://{username}:{password}"
    "@cluster0.grbxsig.mongodb.net/next_gen_digi_health"
    "?retryWrites=true&w=majority"
)

client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["next_gen_digi_health"]
users = db["users"]
orders = db["orders"]

# ---------------- PAGES ----------------
@app.route("/")
def login_page():
    return render_template("index.html")

@app.route("/register-page")
def register_page():
    return render_template("register.html")

@app.route("/welcome")
def welcome_page():
    return render_template("welcome.html")

# ---------------- API ----------------
@app.route("/register", methods=["POST"])
def register():
    data = request.json

    if not data:
        return jsonify({"error": "Invalid request"}), 400

    if users.find_one({"email": data["email"]}):
        return jsonify({"error": "User already exists"}), 400

    users.insert_one({
        "name": data["name"],
        "email": data["email"],
        "password": bcrypt.generate_password_hash(
            data["password"]
        ).decode("utf-8"),
        "role": data["role"]
    })

    return jsonify({"redirect": "/"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user = users.find_one({"email": data["email"]})
    if not user:
        return jsonify({"error": "User not found"}), 401

    if not bcrypt.check_password_hash(user["password"], data["password"]):
        return jsonify({"error": "Wrong password"}), 401

    return jsonify({"redirect": "/welcome"})

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

@app.route("/pharmacy")
def pharmacy():
    return render_template("pharmacy.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/prescription")
def prescription():
    return render_template("prescription.html")

@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if request.method == "POST":
        data = request.json

        if not data:
            return jsonify({"error": "Invalid order data"}), 400

        order = {
            "customer": {
                "name": data.get("name"),
                "phone": data.get("phone"),
                "address": data.get("address"),
                "city": data.get("city"),
                "pincode": data.get("pincode"),
            },
            "items": data.get("items"),
            "total_amount": data.get("total"),
            "payment_method": data.get("payment"),
            "status": "Order Placed",
            "created_at": datetime.utcnow()
        }

        orders.insert_one(order)   # ✅ SAVED TO MONGODB

        return jsonify({"redirect": "/order-success"})

    return render_template("checkout.html")


@app.route("/order_success")
@app.route("/order-success")
def order_success():
    return render_template("order_success.html")

@app.route("/order_status")
def order_status():
    return render_template("order_status.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


@app.route("/api/chat", methods=["POST"])
def chat_api():
    user_message = request.json["message"]

    context = retrieve_context(user_message)
    prompt = SYSTEM_PROMPT + build_user_prompt(context, user_message)

    reply = call_ollama(prompt)

    return jsonify({"reply": reply})

@app.route("/physio")
def physio():
    return render_template("physio.html")

@app.route("/insurance")
def insurance():
    return render_template("insurance.html")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
