import email.message
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import imaplib
import email
from typing import List
from fastapi.responses import JSONResponse

api = FastAPI()

IMAP_SERVER = 'imap.gmail.com'
EMAIL = 'seb.larag@duocuc.cl'
PASSWORD = 'Notebooksamsung2000'

class Correo(BaseModel):
    destinatario : str
    asunto : str


# Solicitud para obtener los correos electronicos
@api.get("/correos/")
async def obtener_correos():
    # Conexión al servidor 
    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL, PASSWORD)
        mail.select("inbox")

        # Busca los correos que no han sido leidos
        estadoResultado, tipo = mail.search(None, "UNSEEN")
        # Lista que almacena correos no leidos
        emails = []

        if estadoResultado == "OK":
            for estandarCorreo in tipo[0].split():
                estadoResultado, tipo = mail.fetch(estandarCorreo, "(RFC822)")
                contenido_correo = tipo[0][1]
                mensaje = email.message_from_bytes(contenido_correo)

                destinatario = mensaje["from"]
                asunto = mensaje["subject"]

                correo = Correo(destinatario=destinatario, asunto=asunto)
                emails.append(correo.model_dump())


                mail.store(estandarCorreo, '-FLAGS', '\SEEN')
            mail.close()
            mail.logout()

            return emails
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))


@api.post("/request/correos/")
async def postear_correos(correos: List[Correo]):
    datos_correos = []
    for correo in correos:
        datos_correos.append({"destinatario": correo.destinatario, "asunto": correo.asunto})
    return JSONResponse(content=datos_correos)


uvicorn.run(api)

