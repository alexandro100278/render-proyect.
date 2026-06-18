from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Modificado aqui por que me dijo cristal :v"

if __name__ == "__main__":
    app.run()
