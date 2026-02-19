import os
import random
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Memoria volátil para la bitácora (se limpia al reiniciar el servidor en Render)
bitacora_datos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activar_portal')
def activar_portal():
    dimensiones = [
        {"nombre": "FLUJO DE ORO LÍQUIDO", "frecuencia": 888, "color": "#FFD700", "mantra": "Abundancia infinita en Inevisual."},
        {"nombre": "ESCUDO DE SOBERANÍA", "frecuencia": 528, "color": "#00D4FF", "mantra": "Espacio libre de interferencias."},
        {"nombre": "DESVÍO DIMENSIONAL", "frecuencia": 417, "color": "#9B59B6", "mantra": "Las molestias se disuelven en el vacío."},
        {"nombre": "MAGNETISMO TOTAL", "frecuencia": 639, "color": "#FF69B4", "mantra": "Atracción y armonía divina."}
    ]
    return jsonify(random.choice(dimensiones))

@app.route('/guardar_log', methods=['POST'])
def guardar_log():
    data = request.json
    if data and 'texto' in data:
        bitacora_datos.insert(0, data)
    return jsonify({"status": "Éxito anclado"})

@app.route('/obtener_logs')
def obtener_logs():
    return jsonify(bitacora_datos[:10])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)