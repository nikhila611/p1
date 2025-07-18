# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Azure App Service with CI/CD!'

if __name__ == '__main__':
    app.run(debug=True)
