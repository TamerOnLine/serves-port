from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Flask API is running!"

if __name__ == "__main__":
    import sys
    port = 5001  # الافتراضي
    if "port" in sys.argv:
        idx = sys.argv.index("port")
        if idx + 1 < len(sys.argv):
            port = int(sys.argv[idx + 1])
    app.run(host="0.0.0.0", port=port)
