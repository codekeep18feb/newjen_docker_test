# app.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hellu, World!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8090))  # Default to 8090 if PORT not set
    app.run(host='0.0.0.0', port=port)