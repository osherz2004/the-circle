class User {
  async get(nickname) {
    const response = await fetch(`http://localhost:5000/api/users/${nickname}`);
    const data = await response.json();
    return data;
  }
  async getAll() {
    const response = await fetch('http://localhost:5000/api/users');
    const data = await response.json();
    return data;
  }
}

export default new User();
