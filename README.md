# FURIA Chat - Assistente Virtual para Fãs

Um chatbot interativo para fãs do time de CS:GO da FURIA, desenvolvido como parte do Challenge 1 do processo seletivo da FURIA Tech.

## 🚀 Tecnologias Utilizadas

### Backend
- Python 3.12
- FastAPI
- Firebase Firestore
- Dialogflow CX
- Uvicorn

### Frontend
- ReactJS
- Vite
- Axios
- CSS Modules

## 📋 Pré-requisitos

- Python 3.12+
- Node.js 18+
- Conta no Firebase
- Conta no Dialogflow CX
- Conta no Render.com (para deploy do backend)
- Conta no Netlify (para deploy do frontend)

## 🔧 Instalação

### Backend

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd FURIA/backend
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
- Copie o arquivo `.env.example` para `.env`
- Preencha as variáveis com suas credenciais:
  - DIALOGFLOW_CX_PROJECT_ID
  - DIALOGFLOW_CX_AGENT_ID
  - DIALOGFLOW_CX_LOCATION

5. Inicie o servidor:
```bash
uvicorn main:app --reload
```

### Frontend

1. Navegue até a pasta do frontend:
```bash
cd ../frontend
```

2. Instale as dependências:
```bash
npm install
```

3. Inicie o servidor de desenvolvimento:
```bash
npm run dev
```

## 🔄 Deploy

### Backend (Render.com)

1. Crie uma nova aplicação Web Service no Render
2. Conecte com seu repositório GitHub
3. Configure as variáveis de ambiente
4. Deploy automático será realizado

### Frontend (Netlify)

1. Crie uma nova aplicação no Netlify
2. Conecte com seu repositório GitHub
3. Configure o build command: `npm run build`
4. Configure o publish directory: `dist`
5. Deploy automático será realizado

## 📝 Funcionalidades

- Chat interativo com bot da FURIA
- Respostas personalizadas sobre o time
- Histórico de conversas salvo no Firebase
- Interface responsiva e moderna
- Integração com Dialogflow CX para respostas inteligentes

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Agradecimentos

- Equipe FURIA
- Google Cloud (Dialogflow CX)
- Firebase
- Render.com
- Netlify
