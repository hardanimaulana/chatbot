from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'kata' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'gambar' in incoming_msg:
        # return a cat pic
        msg.media('https://source.unsplash.com/featured/?birthday')
        responded = True
    if 'tanggal' in incoming_msg:
        msg.body('13 Juli 2020')
        responded = True
    if not responded:
        msg.body('Kata kunci tidak dikenali, mohon maaf. Silahkan gunakan: kata, gambar, tanggal')
    return str(resp)


if __name__ == '__main__':
    app.run()