from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola! Este es mi chatbot funcionando en Render."

if __name__ == '__main__':
    app.run()
