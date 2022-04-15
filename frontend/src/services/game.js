import { io } from 'socket.io-client';

class Game {
  connect(token) {
    return io('http://localhost:5000', {
      extraHeaders: { Authorization: `Bearer ${token}` },
    });
  }
}

export default new Game();
