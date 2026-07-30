import os

from dotenv import load_dotenv

load_dotenv()
WHATSAPP_ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
WHATSAPP_BUSINESS_ACCOUNT_ID = os.getenv("WHATSAPP_BUSINESS_ACCOUNT_ID")
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

#print("Token",WHATSAPP_ACCESS_TOKEN)
print("phone_number",PHONE_NUMBER_ID)
print("Token starts with:", WHATSAPP_ACCESS_TOKEN[:15])