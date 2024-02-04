from django.shortcuts import redirect

from dotenv import load_dotenv
import os
import requests

load_dotenv()

REST_API_KEY = os.environ.get("REST_API_KEY")
REDIRECT_URI = os.environ.get("REDIRECT_URI")
SECRET_API_KEY = os.environ.get("SECRET_API_KEY")

def kakaologin(request):
  URL = f"https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}"
  return redirect(URL)

def callback(request):
  TOKEN_HEADER = {
    "Content-type": "application/x-www-form-urlencoded;charset=utf-8"
  }
  TOKEN_DATA = {
    "grant_type": "authorization_code",
    "client_id": REST_API_KEY,
    "redirection_uri": REDIRECT_URI,
    "code": request.GET["code"],
    "client_secret": SECRET_API_KEY,
  }
  ACCESS_TOKEN = requests.post("https://kauth.kakao.com/oauth/token", headers=TOKEN_HEADER, data=TOKEN_DATA).json()["access_token"]
  
  USER_HEADER = {
    "Authorization": "Bearer $" + ACCESS_TOKEN
  }
  USER_DATA = requests.get("https://kapi.kakao.com/v2/user/me", headers=USER_HEADER).json()
  request.session["id"] = USER_DATA["id"]
  request.session["token"] = ACCESS_TOKEN
  return redirect("/")

def kakaologout(request):
  USER_HEADER = {
    "Authorization": "Bearer $" + request.session["token"]
  }
  requests.post("https://kapi.kakao.com/v1/user/unlink", headers=USER_HEADER)
  del request.session["id"]
  del request.session["token"]
  return redirect("/")
  