import { reactive } from 'vue';

let state;
const user = localStorage.getItem('user');

if (!user) {
  state = reactive({
    token: '',
    nickname: '',
    description: '',
    profilePicturePath: '',
    message: '',
  });
} else {
  const session = JSON.parse(user);
  state = reactive({
    token: session.token,
    nickname: session.nickname,
    description: session.description,
    profilePicturePath: session.profile_picture_path,
    message: '',
  });
}

const methods = {
  updateUser(token, nickname, description, profilePicturePath) {
    state.token = token;
    state.nickname = nickname;
    state.description = description;
    state.profilePicturePath = profilePicturePath;
  },
};

export default { state, methods };
