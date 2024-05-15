from fastapi import FastAPI, Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build 
import base64
import email




api = FastAPI()

# Definir los permisos de la interacción
SCOPES = ['https://www.googleapis.com/auth/gmail.addons.current.message.readonly','https://www.googleapis.com/auth/gmail.modify','https://www.googleapis.com/auth/gmail.labels']

# Función para obtener credenciales 
# def obtener_credencial():
#     flow = InstalledAppFlow.from_client_secrets_file(
#         'credentials.json', SCOPES
#     )
#     flow.redirect_uri = 'http://localhost:8080/'
#     credencial = flow.run_local_server()
#     flow.authorization_url(
#         access_type='offline'
#     )
# 
#     return credencial
# 
# credencial = obtener_credencial()

# Función que crea un servicio de gmail para trabajar con correo autenticado
# async def servicio_gmail(credencial):
#     service = build('gmail','v1',credentials=credencial)
#     return service


# @api.post("/")
# async def notificacionesUser():
#         service = await servicio_gmail(credencial)
#         request = {
#             'labelIds' : ['INBOX','UNREAD'],
#             'topicName' : 'projects/parseo-de-correos-fastapi/topics/PruebasAPI',
#             'labelFilterBehavior' : 'INCLUDE'
#         }
#         response = service.users().watch(userId='me', body=request).execute()
#         print(response)

@api.post("/")
async def notificacionesUser(request : Request):
    data = await request.json()
    print(data)
    return {}

