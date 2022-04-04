class AuthService {
  async register(nickname, password, description, profilePicture) {
    let formData = new FormData();

    formData.append('profile_picture', profilePicture);
    formData.append('nickname', nickname);
    formData.append('description', description);
    formData.append('password', password);

    const response = await fetch('http://localhost:5000/api/users', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    console.log(data);

    if (response.status == 201) {
      return { success: true, message: '' };
    }

    return { success: false, message: data.message };
  }
  login() {
    return;
  }
}

export default new AuthService();
