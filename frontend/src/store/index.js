import { reactive } from 'vue';

const state = reactive({
  token: "",
  nickname: "",
  description: "",
  profilePicturePath: "",
});

const methods = {
  updateUser(token, nickname, description, profilePicturePath) {
    state.token = token;
    state.nickname = nickname;
    state.description = description;
    state.profilePicturePath = profilePicturePath;
  }
}

export default { state, methods }