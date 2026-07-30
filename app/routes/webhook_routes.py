from fastapi import APIRouter,Request
from fastapi.responses import PlainTextResponse
from config import VERIFY_TOKEN

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
