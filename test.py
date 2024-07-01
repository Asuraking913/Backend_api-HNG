from flask import Flask, request

app = Flask(__name__)

@app.route("/home", methods = ['GET'])
def home(): 
    name = request.args.get("visitor")
    return {"text": "sdfsfd", "visitor" : name}

if __name__ == "__main__":
    app.run(debug= True)