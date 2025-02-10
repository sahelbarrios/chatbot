from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    mensaje = data.get('mensaje', '')  # Mensaje recibido
    respuesta = procesar_mensaje(mensaje)  # Procesar el mensaje
    return jsonify({"respuesta": respuesta})

def procesar_mensaje(mensaje):
    if "hola" in mensaje.lower():
        return "¡Hola! ¿En qué puedo ayudarte?"
    else:
        return "Lo siento, no entendí tu mensaje."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)