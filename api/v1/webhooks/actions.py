import ujson

import requests

from slack_movie_suggest.settings import FACEBOOK_WEBHOOK_TOKEN


def send_typing(user_id):
    url = "https://graph.facebook.com/v2.6/me/messages?access_token=%s" % FACEBOOK_WEBHOOK_TOKEN
    response = {
        "recipient": {
            "id": user_id
        },
        "sender_action": "typing_on"
    }
    headers = {'Content-Type': 'application/json'}
    print(response)
    requests.post(url, ujson.dumps(response), headers=headers)
