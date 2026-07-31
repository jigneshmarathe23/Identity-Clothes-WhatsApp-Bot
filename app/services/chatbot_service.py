def get_bot_response(message :str) ->str:
    message = message.strip().lower()

    if message in ["hi","hello"]:
        return """Welcome to Identity Clothes
        
We currently have the following T-shirt collections 

1️⃣ Regular Fit T-Shirts
2️⃣ Oversized T-Shirts
3️⃣ Polo T-Shirts

Please reply with 1, 2 or 3."""
    elif message == "1":
        return """Regular Fit T-Shirts
Our Regular Fit collection will be available soon.
please vist www.identityclothes.com"""
    elif message == "2":
        return """Oversized T-Shirts
Our Oversized collection will be available soon.
please vist www.identityclothes.com"""
    elif message == "3":
        return """Polo T-Shirts
Our Polo collection will be available soon.
please vist www.identityclothes.com"""
    else:
        return """X Invalid 
Type Hi to start again."""


