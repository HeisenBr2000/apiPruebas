from fastapi import FastAPI
from google.oauth2.credentials import Credentials
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import uvicorn

api = FastAPI()


@api.get("/autorizacion/")
async def token_autorizacion():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/gmail.readonly']
    )
    authorization_url, _ = flow.authorization_url(prompt='consent')

    return RedirectResponse(authorization_url)

@api.get("/respuesta/")
async def respuesta(code: str):
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json',
        scopes=['https://www.googleapis.com/auth/gmail.readonly']
    )

    flow.fetch_token(code=code)

    credentials = flow.credentials

    with open('acceso.json', 'w') as token_file:
        token_file.write(credentials.to_json())

    return{'Autorizacion exitosa'}


#@api.get("/correos/")
#async def obtener_correos():
#    creds = Credentials.from_authorized_user_file('credentials.json')
#   service = build('gmail', 'v1', Credentials=creds)
#    results = service.users().messages().list(userId='me').execute()
#    messages = results.get('messages',[])
#    return {"messages": messages}

# Ingresa con puerto 8001
