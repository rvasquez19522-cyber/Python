# funcions/web.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola, bienvenidos a mi API de prueba."

if __name__ == '__main__':
    app.run(debug=True)
