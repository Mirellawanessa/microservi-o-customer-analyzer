# Plataforma Inteligente de Customer Success 💡📈

Automação completa para prever churn, interpretar feedbacks com IA e acionar ações de retenção em tempo real — integrando Python, n8n, Google Sheets e Looker Studio.

---

## 🚀 Visão Geral

Este projeto é uma plataforma low-code para equipes de Customer Success monitorarem proativamente clientes com risco de churn, automatizando:

- 📉 Análise de risco com Python
- 💬 Interpretação de sentimento com HuggingFace
- ✉️ Envio automático de alertas por e-mail
- 📄 Registro de eventos no Google Sheets
- 📊 Visualização via Dashboard (Looker Studio)

---

## 🧠 Tecnologias Utilizadas

- 🟨 n8n (orquestração de automações low-code)
- 🐍 Python + Flask (microserviços)
- 🤗 HuggingFace Transformers (análise de sentimentos NLP)
- 📊 Google Sheets (base de dados leve e integrável)
- 📈 Looker Studio (dashboard interativo)
- ✉️ Gmail API (envio automático de e-mails)
- ☁️ Replit (ambiente de desenvolvimento e testes rápidos)
- 🐙 GitHub (versionamento e portfólio público)

---

## ⚙️ Como Funciona

1. Evento de cliente (ex: queda de uso ou reclamação) é enviado ao Webhook do n8n
2. O fluxo no n8n envia os dados para dois microserviços:
   - /customer-analyzer → calcula risco de churn
   - /feedback-insights → interpreta o sentimento do comentário
3. Se o risco > 0.6 ou o sentimento for negativo:
   - Um e-mail é disparado automaticamente para o time de CS
   - O alerta é registrado no Google Sheets
4. O dashboard no Looker Studio exibe os dados atualizados

---

## 📬 Exemplo de Requisição

Webhook para análise via POST:

```json
POST /webhook/churn-check
{
  "uso_mensal": 2,
  "ticket_suporte_aberto": true,
  "comentario": "Estou insatisfeito com o atendimento"
}
```

## 🔁 Fluxo no n8n

Fluxo completo criado no n8n que orquestra os serviços de análise de churn e sentimento:

![Fluxo no n8n](https://github.com/Mirellawanessa/microservi-o-customer-analyzer/blob/main/workflows/Screenshot%202025-05-20%20173822.png)

📄 Arquivo do Workflow (pronto para importar no n8n):  
➡️ [workflow-churn-alert.json](https://github.com/Mirellawanessa/microservi-o-customer-analyzer/blob/main/workflows/workflow-churn-alert.json.json)

---

## 🗃 Estrutura do Projeto

```bash
.
├── customer-analyzer/
│   └── app.py               # API que calcula risco de churn
├── feedback-insights/
│   └── app.py               # API de análise de sentimento via HuggingFace
├── workflows/
│   └── workflow-churn-alert.json  # Fluxo n8n exportado
├── requirements.txt         # Dependências dos microserviços Python
└── README.md                # Documentação do projeto
```

## 📊 Dashboard em Tempo Real

Dashboard no Looker Studio mostrando todos os clientes em risco, sentimentos e comentários registrados:

🔗 [Acessar Dashboard](https://lookerstudio.google.com/reporting/69c595a5-394d-4294-ab5b-e516293f5c7e)

---

## 🧪 Como Rodar Localmente

Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🧪 Como Rodar Localmente

Execute os microserviços:

```bash
python customer-analyzer/app.py
python feedback-insights/app.py
```
Use Postman ou CURL para enviar requisições ao webhook configurado no n8n.

---

## 💡 Melhorias Futuras

- Treinar um modelo de churn com base em dados históricos reais
- Integração com WhatsApp (via Make ou Twilio)
- Interface visual no Bubble para o time de CS
- Regras de upsell automatizadas com base no perfil de uso

## 👩‍💻 Desenvolvedora

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
