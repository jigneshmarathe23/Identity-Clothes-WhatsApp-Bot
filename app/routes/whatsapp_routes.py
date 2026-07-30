from fastapi import APIRouter

router = APIRouter(
    prefix="/webhook",
    tags=["WhatsApp"]
)

@router.get("/")

def verify_webhook():
    return{
        "message" : "Whatsapp webhook working Successfully !!!"

    }