import json
import random
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import binascii
import requests
class AddisPay:
  def __init__(self,publickey,privatekey,Auth):
    self.publickey=publickey
    self.privatekey=privatekey
    self.Auth=Auth
    self.checkout_url="https://uat-checkoutapi.addispay.et/api/v1/encrypted/receive-data/"
  def parse_public_key(self,public_key):
      decoded_public_key = base64.b64decode(public_key)
      rsa_key = RSA.import_key(decoded_public_key)
      return rsa_key

  def parse_private_key(self,private_key):
      decoded_private_key = base64.b64decode(private_key)
      rsa_key = RSA.import_key(decoded_private_key)
      return rsa_key

  def encrypt_data(self,data):
      rsa_key = self.parse_public_key(self.publickey)
      cipher = PKCS1_v1_5.new(rsa_key)
      encrypted_bytes = cipher.encrypt(data.encode())
      return base64.b64encode(encrypted_bytes).decode()

  def decrypt_data(self,encrypted_data):
      rsa_key = self.parse_private_key(self.privatekey)
      cipher = PKCS1_v1_5.new(rsa_key)
      decoded_encrypted_data = base64.b64decode(encrypted_data)
      decrypted_bytes = cipher.decrypt(decoded_encrypted_data, None)
      return decrypted_bytes.decode()

  def send_request(self,total_amount,tx_ref,currency,first_name,email,phone_number,last_name,session_expiration_minute,nonce,notify_url,return_url,message,order_detail={}):
      json_data={
           "data": {
                "total_amount": self.encrypt_data(str(total_amount)),
                "tx_ref": self.encrypt_data(str(tx_ref)),
                "currency": self.encrypt_data(str(currency)),
                "first_name": self.encrypt_data(str(first_name)),
                "email": self.encrypt_data(str(email)),
                "phone_number":self.encrypt_data(str(phone_number)),
                "last_name": self.encrypt_data(str(last_name)),
                "session_expired":self.encrypt_data(str(session_expiration_minute)),
                "nonce":self.encrypt_data(str(nonce)),
                "order_detail":{
                    "items": "rfid",
                    "description": "I am testing this"
                },
                "notify_url":self.encrypt_data(notify_url),
                "success_url":self.encrypt_data(return_url),
                "cancel_url":self.encrypt_data(return_url),
                "error_url":self.encrypt_data(return_url)
                },
                "message": self.encrypt_data(str(message))
              }
      headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            "Auth": self.Auth
            }
      response = requests.post(self.checkout_url, json=json_data, headers=headers)
      return response
