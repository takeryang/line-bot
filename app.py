from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('RIImXqB1aXhskGmYXSpcuv/hnuRjnfNakb4XaJOtY1uU9224wgswlAb8JGx5089mL/t5gIQd5L9lmoRD8kKhFGbijwqoX7K2/e7mnso2vODvMfhBk1q/bnBLxPWmv929mU710IUy6M3akgQNLUOQjQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('878639521d3546e6fc8c9faa3e00dc7f')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('請問想知道哪個停車場的資訊?')
    msg = event.message.text
    
    if msg == '雙十':
        r = '雙十停車場的費率為平日半小時六十元\n 假日半小時八十元'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()