from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <!DOCTYPE html>
        <html lang="uk">
        <head>
            <meta charset="UTF-8">
            <title>Проста сторінка</title>
        </head>
        <body>
            <h1>Вітаємо на простому HTTP-сервері!</h1>
            <p>Це приклад статичної сторінки.</p>
        </body>
        </html>
        """

@app.route('/user/<username>')
def user_profile(username):
    return f"""
        <!DOCTYPE html>
        <html lang="uk">
        <head>
            <meta charset="UTF-8">ц
            <title>Проста сторінка</title>
        </head>
        <body>
            <h1>Вітаємо {username} на простому HTTP-сервері!</h1>
            <p>Це приклад статичної сторінки.</p>
        </body>
        </html>
        """

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    return {'status': 'received', 'data': data}, 201

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)