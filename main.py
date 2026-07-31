from fastapi import FastAPI
from app.database.init_db import init_db
from app.routes.product_routes import router as product_router
from app.routes.test_routes import router as test_router
from app.routes.webhook_routes import router as webhook_router
from app.routes.twilio_routes import router as twilio_router

app=FastAPI(
    title="Identity clothes chat bot",
    version ="1.0.0"
)
init_db()
app.include_router(product_router)
app.include_router(test_router)
app.include_router(webhook_router)
app.include_router(twilio_router)
@app.get("/")

def home():
    return{
        "message": "Identity clothes WhatsApp Bot is running Successfully"
    }

