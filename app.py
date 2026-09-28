from flask import Flask

app = Flask(__name__)

VERSION = "1.0.0"


@app.route("/")
def home():
    return {
        "message": "Hello from Flask!",
        "version": VERSION
    }


@app.route("/health")
def health():
    return {
        "status": "healthy"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5018)
