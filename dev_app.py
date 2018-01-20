from flask import Flask
from bot.hello import handler 
app = Flask(__name__)

@app.route("/")
def hello():
    print(handler({'body': ''}, {}))
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
