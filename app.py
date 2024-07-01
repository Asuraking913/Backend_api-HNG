from flask import Flask
from root_route import root_routes

app = Flask(__name__)

root_routes(app)

if __name__ == "__main__":
    app.run(debug = True)