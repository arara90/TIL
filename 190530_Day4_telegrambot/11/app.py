from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    token = '663899527:AAHyZWnizopIR45o5GXn06YZx2r63toAhT4'
    api_url = f'https://api.telegram.org/bot{token}'
    chat_id = '894138210'

    text = request.args.get('message')

    url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
    response = requests.get(url)
    return '전송완료'


if __name__ == '__main__' :
    app.run(debug=True)