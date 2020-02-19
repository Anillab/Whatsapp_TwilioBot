from flask import Flask,request
import requests

from twilio.twiml.messaging_response import MessagingResponse

app=Flask(__name__)

@app.route('/bot',methods=['POST'])
def bot():
    incoming_msg=request.values.get('Body','').lower()
    resp=MessagingResponse()
    msg=resp.message()
    responded=False
    if 'quote' in incoming_msg:
        r=requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data=r.json()
            quote=f'{data["content"]}({data["author"]})'
        else:
            quote='I coould rretrieve a quote'
        msg.body(quote)
        responded=True
    if 'cat' in incoming_msg:
        msg.media('https://cataas.com/cat')
        responded=True
    if not responded:
        msg.body('Sorry')
    return str(resp)
