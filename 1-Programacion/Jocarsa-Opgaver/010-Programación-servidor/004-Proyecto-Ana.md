En este ejercicio, trabajo con Flask para gestionar sesiones de ejecución. Lo hago para simular cómo una aplicación web puede iniciar, controlar y leer desde un proceso en ejecución, lo cual es útil en proyectos reales, como ejecutores de código en línea, herramientas interactivas y muchas otras cosas. Esto me ayuda a comprender cómo los servidores gestionan las tareas de larga duración y las interacciones de los usuarios durante períodos de tiempo más largos.

Creo puntos finales REST que permiten iniciar una nueva sesión de ejecución, escribir líneas de código en una sesión existente y leer la salida acumulada. Cada sesión también se identifica con un ID único, lo que permite tener varias sesiones al mismo tiempo. Utilizo POST para enviar datos al servidor y solicitudes GET para recuperar los datos resultantes.


# Enunciado paso a paso:

# ---------- 1. Añade un nuevo endpoint para iniciar una nueva sesión ----------
- 012-iniciar_sesion.py
@app.route("/api/start", methods=["POST"])
def api_start():
    data = request.get_json(force=True)
    code = data.get("code", "")

    session_id = str(uuid.uuid4())
    sessions[session_id] = PythonSession(code)

    return jsonify({"session_id": session_id})


# ---------- 2. Añade un nuevo endpoint para escribir líneas de código en una sesión ----------
- 010-mejoras.py

@app.route("/api/write", methods=["POST"])
def api_write():
    data = request.get_json(force=True)
    session_id = data.get("session_id")
    line = data.get("line", "")

    sess = sessions.get(session_id)
    if not sess:
        return jsonify({"error": "Sesión no encontrada"}), 404

    sess.write(line)
    return jsonify({"ok": True})

# ---------- 3. Añade un nuevo endpoint para leer la salida de una sesión ----------
- 010-mejoras.py
@app.route("/api/read", methods=["GET"])
def api_read():
    session_id = request.args.get("session_id")
    sess = sessions.get(session_id)
    if not sess:
        return jsonify({"error": "Sesión no encontrada"}), 404

    output = sess.read_all()
    alive = sess.is_alive()

    # Si el proceso ha terminado y no queda nada que leer, limpiar la sesión
    if not alive and not output:
        sessions.pop(session_id, None)

    return jsonify({"output": output, "alive": alive})


Este ejercicio me ayudó a comprender mejor cómo funcionan las sesiones en el servidor y cómo se pueden controlar a través de diferentes puntos finales. Aprendí la importancia de los ID de sesión, el manejo de procesos y la comunicación estructurada entre el cliente y el servidor. Estos conceptos son muy importantes en el mundo real, donde los procesos de las aplicaciones web deben permanecer activos, recibir entradas y devolver salidas de forma controlada.