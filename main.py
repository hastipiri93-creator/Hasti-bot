from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN =312779411:ghOFlBU4IQ1q_VCeKLbFItqZs5LaUQoluH0
API_URL = f'https://tapi.bale.ai/bot{TOKEN}/sendMessage'

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    text = "سلام! خوش اومدی به دنیای وردهای جادویی! 🌿✨"
    requests.post(API_URL, json={'chat_id': chat_id, 'text': text})
    return 'ok'

if __name__ == '__main__':
    app.run()
