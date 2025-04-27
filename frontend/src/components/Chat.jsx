import React, { useState } from 'react';
import axios from 'axios';

const Chat = () => {
 const [message, setMessage] = useState('');
 const [chatHistory, setChatHistory] = useState([]);

 const handleSendMessage = async () => {
 if (message.trim() !== '') {
 try {
 const response = await axios.post('http://localhost:8000/chat', { message });
 setChatHistory([...chatHistory, { user: message, bot: response.data.response }]);
 setMessage('');
 } catch (error) {
 console.error('Erro ao enviar mensagem:', error);
 }
 }
 };

 return (
 <div>
 <h2>Chat</h2>
 <div>
 {chatHistory.map((chat, index) => (
 <div key={index}>
 <p><strong>Usuário:</strong> {chat.user}</p>
 <p><strong>Bot:</strong> {chat.bot}</p>
 </div>
 ))}
 </div>
 <input
 type="text"
 value={message}
 onChange={(e) => setMessage(e.target.value)}
 placeholder="Digite sua mensagem"
 />
 <button onClick={handleSendMessage}>Enviar</button>
 </div>
 );
};

export default Chat;
