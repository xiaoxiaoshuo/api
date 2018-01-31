from flask import Flask

from flask_cors import CORS


app = Flask(api)
CORS(app)

app.run(host='0.0.0.0',debug=True)