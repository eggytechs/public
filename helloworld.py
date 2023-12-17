from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello, World from Python Flask App!'

if __name__ == "__main__": 
    # Run Flask Application 
    app.run(host="0.0.0.0", port=8080)
