from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

from handlers.routes import configure_routes

app = Flask(__name__)

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
