// URL da API WebSocket
var socketUrl = 'wss://chat.pragmaticplaylive.net/chat';

// Estabelece a conexão WebSocket
var socket = new WebSocket(socketUrl);

// Manipulador de eventos para quando a conexão é estabelecida
socket.onopen = function(event) {
  console.log('Conexão WebSocket estabelecida.');

  // Cria uma mensagem para enviar
  var mensagem = {
    timestamp: new Date().getTime(),
    userId: '2023082498926',
    tableId: 'spacemanyxeabn03', // Exemplo de ID de tabela
    action: 'COMMAND',
    role: 'GAME_USER',
    userScreenName: 'MandinhaStuart', // Seu nome de usuário
    casinoId: 'ppcdk00000004129', // Exemplo de ID de cassino
    tagMessage: 'GAME_USER',
    showHide: true,
    status: 'SUCCESS',
    messageId: '2023082498926',
    tableName: 'SPACEMAN',
    autoReply: false,
    content: '✅✅✅testeteste✅✅✅teste teste teste testetest✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅.' // Conteúdo da sua mensagem
  };

  // Envia a mensagem para o servidor
  socket.send(JSON.stringify(mensagem));
};

// Manipulador de eventos para mensagens recebidas
socket.onmessage = function(event) {
  var mensagemRecebida = JSON.parse(event.data);
  console.log('Mensagem recebida:', mensagemRecebida);
};

// Manipulador de eventos para erros
socket.onerror = function(event) {
  console.error('Erro na conexão WebSocket:', event);
};