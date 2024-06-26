from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)