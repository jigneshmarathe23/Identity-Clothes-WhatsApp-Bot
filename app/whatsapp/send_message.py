import requests
from config import WHATSAPP_ACCESS_TOKEN, PHONE_NUMBER_ID

def send_whatsapp_message(to_number: str,message: str):

    url = f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages"
    headers ={
        "Authorization": f"Bearer {WHATSAPP_ACCESS_TOKEN}",
        "Content-Type" : "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "template",
        "template": {
            "name": "jaspers_market_plain_text_v1",
            "language": {
                "code": "en_US"
            }
        }
    }



    response = requests.post(
        url=url,
        headers=headers,
        json=payload
    )
    print ("Status_code:",response.status_code)
    print("Response:", response.text)
    return {
        "Status_code":response.status_code,
        "response":response.json()
    }



