from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    # Exemplo de dados esperados:
    # {
    #   "uso_mensal": 3,
    #   "ticket_suporte_aberto": true,
    #   "feedback_negativo": true
    # }

    uso = data.get("uso_mensal", 0)
    suporte = data.get("ticket_suporte_aberto", False)
    feedback = data.get("feedback_negativo", False)

    # Regra simples pra simular churn
    risco = 0
    if uso < 5:
        risco += 0.4
    if suporte:
        risco += 0.3
    if feedback:
        risco += 0.3

    risco = min(risco, 1)

    return jsonify({"risco_churn": risco})

if __name__ == "__main__":
    print("Arquivo app.py executado até aqui")
    app.run(debug=True, port=5000)
