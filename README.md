# Plataforma Inteligente de Customer Success 💡📈

Automação completa para prever churn, interpretar feedbacks com IA e acionar ações de retenção em tempo real — integrando Python, n8n, Google Sheets e Looker Studio.

---

## 🚀 Visão Geral

Este projeto é uma plataforma low-code para equipes de Customer Success monitorarem proativamente clientes com risco de churn, automatizando:

- Análise de risco com Python
- Interpretação de sentimento com HuggingFace
- Envio automático de alertas por e-mail
- Registro de eventos no Google Sheets
- Visualização via Dashboard (Looker Studio)

---

## 🧠 Tecnologias Utilizadas

- 🟨 n8n (automação low-code)
- 🐍 Python + Flask (microserviços)
- 🤗 HuggingFace Transformers (NLP - análise de sentimentos)
- 📊 Google Sheets (registro)
- 📈 Looker Studio (dashboard)
- ✉️ Gmail API (alerta por e-mail)
- ☁️ Replit (desenvolvimento rápido)
- 🐙 GitHub (versionamento e portfólio)

---

## ⚙️ Como Funciona

1. Evento do cliente é enviado para um Webhook (ex: via Postman ou sistema externo)
2. n8n envia os dados para dois microserviços:
   - `/customer-analyzer`: calcula o risco de churn
   - `/feedback-insights`: interpreta o sentimento do comentário
3. Se risco > 0.6 ou sentimento negativo:
   - Dispara alerta por e-mail
   - Registra no Google Sheets
4. Looker Studio atualiza automaticamente o dashboard

---

## 📬 Exemplo de Execução

Webhook (POST):

```json
POST /webhook/churn-check
{
  "uso_mensal": 2,
  "ticket_suporte_aberto": true,
  "comentario": "Estou insatisfeito com o atendimento"
}

## 🔁 Fluxo no n8n

Abaixo está o fluxo completo criado no n8n que orquestra os serviços de análise de churn e sentimento:

![Fluxo n8n](workflows/workflow.png)

📄 Arquivo do Workflow (n8n exportado):
➡️ [`workflow-churn-alert.json`](workflows/workflow-churn-alert.json)

Você pode importar este arquivo diretamente no seu n8n e começar com o fluxo já pronto!

## 🗃 Estrutura do Projeto
/customer-analyzer
│   └── app.py         → API que calcula risco de churn
/feedback-insights
│   └── app.py         → API de análise de sentimento
/workflows
│   └── workflow-churn-alert.json → fluxo n8n exportado
requirements.txt       → dependências Python
README.md              → você está aqui!

## 📊 Dashboard
Looker Studio mostrando todos os clientes em risco, sentimento, e comentários:

## https://lookerstudio.google.com/reporting/69c595a5-394d-4294-ab5b-e516293f5c7e

🧪 Como rodar localmente
Instale as dependências:

```bash
Copiar
Editar
pip install -r requirements.txt
```
Execute os microserviços:

```bash
Copiar
Editar
python customer-analyzer/app.py
python feedback-insights/app.py
```

Use Postman ou CURL para enviar requisições ao webhook do n8n.

## 🛠 Melhorias Futuras

Treinar modelo de churn com dados históricos
Integração com WhatsApp (Make ou Twilio)
Interface no Bubble para monitoramento em tempo real
Detecção de upsell automático com base no perfil de uso

## 👩‍💻 Desenvolvido por

<p>
    <img 
      align="left" 
      width="80" 
      src="https://github.com/Mirellawanessa/DIO-Trilha-Java-Basico/blob/main/GitHub/imagens/User.jpeg?raw=true"
    />
    <p>&nbsp;&nbsp;&nbsp;Mirella Wanessa<br>
    &nbsp;&nbsp;&nbsp;
    <a href="https://github.com/Mirellawanessa">GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/mirellawanessa/">LinkedIn</a>&nbsp;|&nbsp;
    <a href="https://www.instagram.com/itsmirella._/">Instagram</a>
    &nbsp;|&nbsp;</p>
</p>

---

⌨️ with 💜 by [Mirella Wanessa](https://github.com/Mirellawanessa)  
Sinta-se à vontade para deixar uma ⭐ se você curtir o conteúdo!
"# microservi-o-customer-analyzer" 
"# microservi-o-customer-analyzer" 
