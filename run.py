from flask import Flask, jsonify
import modules.currency

app = Flask(__name__)

@app.route("/")
def index():
    d = modules.currency.get_currency()
    return jsonify(**d)

if __name__ == "__main__":
    app.run()
