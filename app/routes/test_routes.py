from fastapi import APIRouter

from app.whatsapp.send_message import send_whatsapp_message

router = APIRouter(
    prefix="/test",
    tags=["Testing"]
)

@router.get("/send")
def send():

    response = send_whatsapp_message(
        to_number="917878529477",
        message="\n\n Welcome to Identity Clothes"
    )
    return response

