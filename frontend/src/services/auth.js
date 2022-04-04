class AuthService {
  async register(nickname, password, description, profilePicture) {
    let formData = new FormData();

    formData.append("profile_picture", profilePicture);
    formData.append("nickname", nickname);
    formData.append("description", description);
    formData.append("password", password);

    const response = await fetch("http://localhost:5000/api/users", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log(data);

    if (response.status == 201) {
      return { success: true, message: "" };
    }

    return { success: false, message: data.message };
  }
  async login(nickname, password) {
    const response = await fetch("http://localhost:5000/api/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ nickname, password }),
    });

    const data = await response.json();

    if (response.status != 200) {
      return { success: false, message: data.message, data: {} };
    }

    const session = {
      token: data.token,
      nickname: data.nickname,
      description: data.description,
      profile_picture_path: "http://localhost:5000" + data.profile_picture_path,
    };

    localStorage.setItem("user", session);

    return {
      success: true,
      message: "Login successfully.",
      data: session,
    };
  }
}

export default new AuthService();
