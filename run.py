from flask import Flask, jsonify
from modules.currency import Currency

app = Flask(__name__)

@app.route("/")
def index():
	currency = Currency()
	data = currency.get()
	return jsonify(**data)
