from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, firestore
import os
from google.cloud import dialogflowcx_v3 as dialogflowcx
from google.oauth2 import service_account
import uuid
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = FastAPI()

# Configurar CORS
origins = ["*"]  # Adjust this in production to specific allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar variáveis de ambiente
DIALOGFLOW_CX_PROJECT_ID = os.getenv("DIALOGFLOW_CX_PROJECT_ID")
DIALOGFLOW_CX_AGENT_ID = os.getenv("DIALOGFLOW_CX_AGENT_ID")
DIALOGFLOW_CX_LOCATION = os.getenv("DIALOGFLOW_CX_LOCATION", "us-central1")

# Verificar variáveis de ambiente obrigatórias
if not all([DIALOGFLOW_CX_PROJECT_ID, DIALOGFLOW_CX_AGENT_ID]):
    raise ValueError("As variáveis de ambiente DIALOGFLOW_CX_PROJECT_ID e DIALOGFLOW_CX_AGENT_ID são obrigatórias")

# Caminho do arquivo de credenciais
credentials_path = "serviceAccountKey.json"

try:
    # Inicializar Firebase
    cred = credentials.Certificate(credentials_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Configurar credenciais para Dialogflow CX
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=["https://www.googleapis.com/auth/cloud-platform"],
    )

    # Criar cliente Dialogflow CX
    client = dialogflowcx.SessionsClient(credentials=credentials)
except Exception as e:
    raise ValueError(f"Erro ao inicializar serviços: {str(e)}")

class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
async def chat(message: ChatMessage):
    if not message.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # Gerar um ID de sessão único
    session_id = str(uuid.uuid4())
    session_path = f"projects/{DIALOGFLOW_CX_PROJECT_ID}/locations/{DIALOGFLOW_CX_LOCATION}/agents/{DIALOGFLOW_CX_AGENT_ID}/sessions/{session_id}"
    
    try:
        text_input = dialogflowcx.TextInput(text=message.message)
        query_input = dialogflowcx.QueryInput(text=text_input)

        # Enviar a mensagem para o Dialogflow CX
        response = await client.detect_intent(request={"session": session_path, "query_input": query_input})

        # Processar a resposta do Dialogflow CX
        bot_response = response.query_result.response_messages[0].text.text[0]

        # Salvar a conversa no Firestore
        conversation_ref = db.collection("conversations").document()
        conversation_ref.set({
            "conversation_id": conversation_ref.id,
            "message": message.message,
            "response": bot_response,
            "timestamp": firestore.SERVER_TIMESTAMP
        })

        return {"response": bot_response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"status": "ok", "message": "FURIA Chat API is running"}
