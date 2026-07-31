from fastapi import APIRouter,Request
from fastapi.responses import PlainTextResponse
from config import VERIFY_TOKEN
from fastapi.responses import  JSONResponse
from app.whatsapp.send_message import send_whatsapp_message

router = APIRouter(
    prefix="/webhook",
    tags=["Webhook"]
)


@router.get("/")
async def verify_webhook(request:Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)
    return PlainTextResponse("Verification Failed",status_code=403)


@router.post("/")
async def recieve_message(request: Request):

    body = await request.json()
    print(body)

    try:
        entry = body["entry"][0]
        changes =entry["changes"][0]
        value =changes["value"]


        if "messages" in value:

            message = value["message"][0]

            from_numbers = message["from"]
            text = message["text"]["body"]

            print(f"Message from :{from_numbers}")
            print(f"Message text:{text}")


            send_whatsapp_message(
                to_number=from_numbers,
                message="Welcome to Identity Clothes \n\n Thanks for contacting us."
            )

    except Exception as e:
        print("error:",e)

    return JSONResponse(content={"status","ok"})
