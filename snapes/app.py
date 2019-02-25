from flask import Flask, Blueprint
from controllers.snippet import snippet

app = Flask(__name__)

app.register_blueprint(snippet)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)