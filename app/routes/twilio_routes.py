from fastapi import APIRouter, Request
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
from app.services.chatbot_service import get_bot_response
import traceback

router = APIRouter(prefix="/twilio", tags=["Twilio"])


@router.post("/webhook")
async def twilio_webhook(request: Request):

    try:

        form = await request.form()

        print("FORM =", dict(form))

        incoming_message = form.get("Body", "")

        print("BODY =", repr(incoming_message))

        bot_reply = get_bot_response(incoming_message)

        response = MessagingResponse()
        response.message(bot_reply)

        print("REPLY =", bot_reply)

        return PlainTextResponse(
            str(response),
            media_type="application/xml"
        )

    except Exception:

        traceback.print_exc()

        return PlainTextResponse(
            "ERROR",
            status_code=500
        )