from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Criar pipeline de análise de sentimento
sentiment_analyzer = pipeline("sentiment-analysis")

@app.route("/analyze-sentiment", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = sentiment_analyzer(text)[0]  # pega o primeiro resultado

    return jsonify({
        "label": result['label'],
        "score": result['score']
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
