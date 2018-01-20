from bot.hello import handler 
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["POST"])
def sms():
    print(request.get_data(as_text=True))
    ret = handler({
        'body': request.get_data(as_text=True),
    }, {})
    return ret.get('body') 

if __name__ == "__main__":
    app.run(debug=True)
