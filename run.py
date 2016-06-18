from flask import Flask, jsonify
from modules.currency import Currency
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
	currency = Currency()
	data = currency.get()
	return jsonify(**data)
