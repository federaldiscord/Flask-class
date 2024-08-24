from flask import Flask
from controller import ciclista  # Import the Blueprint
from controller_maillot import maillot  # Import the Blueprint


app = Flask(__name__)

app.register_blueprint(ciclista)
app.register_blueprint(maillot)

if __name__ == '__main__':
    app.run(debug=True)
