from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configuración de Hugging Face
HUGGING_FACE_API_URL = "https://api-inference.huggingface.co/models/gpt2"
HUGGING_FACE_API_TOKEN = "TU_TOKEN_DE_API"

headers = {"Authorization": f"Bearer {HUGGING_FACE_API_TOKEN}"}

@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.json
    user_message = data.get("message", "")

    # Llamada a la API de Hugging Face
    payload = {"inputs": user_message}
    response = requests.post(HUGGING_FACE_API_URL, headers=headers, json=payload)
    generated_text = response.json().get("generated_text", "Lo siento, no puedo responder en este momento.")

    return jsonify({"response": generated_text})

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/bienvenida", methods=["POST"])
def bienvenida():
    data = request.json
    usuario = data.get("usuario", "nuevo")
    if usuario == "nuevo":
        return jsonify({"response": "¡Hola! Bienvenido a Fitnessmania 💪. ¿En qué puedo ayudarte hoy?"})
    else:
        return jsonify({"response": f"¡Qué bueno verte de nuevo, {usuario}! ¿Listo para entrenar?"})
    responses = {
    "planes": "Nuestros planes son: Mensual: $X, Trimestral: $Y, Anual: $Z. ¿Cuál te interesa?",
    "horarios": "Estamos abiertos de Lunes a Domingo de 5:00 AM a 10:00 PM. ¿Quieres ubicación?",
    "clases": "Clases disponibles: XtremeBike, TRX, Boxeo. ¿Quieres reservar?",
}

@app.route("/informacion", methods=["POST"])
def informacion():
    data = request.json
    pregunta = data.get("pregunta", "").lower()

    if "plan" in pregunta or "precio" in pregunta:
        return jsonify({"response": responses["planes"]})
    elif "horario" in pregunta or "hora" in pregunta:
        return jsonify({"response": responses["horarios"]})
    elif "clase" in pregunta:
        return jsonify({"response": responses["clases"]})
    else:
        return jsonify({"response": "No entendí bien tu consulta. ¿Puedes reformularla? 😊"})

    @app.route("/reservar", methods=["POST"])
def reservar():
    data = request.json
    clase = data.get("clase", "")
    horario = data.get("horario", "")

    if clase and horario:
        return jsonify({"response": f"¡Tu clase de {clase} está confirmada para el {horario}! Nos vemos en Fitnessmania 💪."})
    else:
        return jsonify({"response": "Por favor, indícame la clase y el horario que prefieres."})
