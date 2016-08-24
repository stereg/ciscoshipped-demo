from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "my life is simple, i create output thats it, hello to you all"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
