from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Jenkins! This is a From GORIZM."

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)