import os
from dotenv import load_dotenv
from addispay import AddisPay
from utils import generate_unique

load_dotenv()

publickey = os.environ.get("publickey")
privatekey = os.environ.get("privatekey")
Auth = os.environ.get("Auth")
addispay = AddisPay(publickey, privatekey, Auth)
total_amount=12
tx_ref="TX-bcd"
currency="ETB"
first_name="Annis"
email="annis@gmail.com"
phone_number="0988888888"
last_name="Nelson",
session_expiration_minute=12
nonce=generate_unique([], 32)
notify_url="https://example.com/"
return_url="https://example.com/"
message="from customer to ..."
order_detail={}
response = addispay.send_request(total_amount=total_amount, tx_ref=tx_ref, currency=currency, first_name=first_name,email=email,phone_number=phone_number,last_name=last_name,session_expiration_minute=session_expiration_minute,nonce=nonce,notify_url=notify_url,return_url=return_url,message=message,order_detail=order_detail)
print(response.json)