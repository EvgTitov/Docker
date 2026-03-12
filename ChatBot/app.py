from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('message', '')

    # Простая логика ответа
    if 'привет' in user_message.lower():
        response = 'Привет! Чем могу помочь?'
    elif 'пока' in user_message.lower():
        response = 'До свидания! Было приятно пообщаться.'
    else:
        response = f'Вы сказали: "{user_message}". Я пока учусь отвечать на такие вопросы.'

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
