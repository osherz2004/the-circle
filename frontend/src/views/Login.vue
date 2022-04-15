<template>
  <div class="h-screen w-1/2 mx-auto flex flex-col justify-center">
    <Notification />
    <h1 class="text-4xl font-bold uppercase">Login and Play!</h1>
    <hr class="border-2 border-indigo-500 bg-indigo-500 my-4" />
    <form @submit="handleLogin">
      <div class="border-b border-indigo-500 py-2 mt-8 mb-8">
        <label for="nickname" class="font-bold text-sm uppercase">
          Nickname
        </label>
        <input
          type="text"
          id="nickname"
          name="nickname"
          class="
            appearance-none
            bg-transparent
            border-none
            w-full
            text-gray-700
            mr-3
            mt-4
            py-1
            px-2
            leading-tight
            focus:outline-none
            text-sm
          "
          placeholder="Enter your nickname..."
          v-model="nickname"
        />
      </div>
      <div class="border-b border-indigo-500 py-2 mb-8">
        <label for="password" class="font-bold text-sm uppercase">
          Password
        </label>
        <input
          type="password"
          id="password"
          name="password"
          class="
            appearance-none
            bg-transparent
            border-none
            w-full
            text-gray-700
            mr-3
            mt-4
            py-1
            px-2
            leading-tight
            focus:outline-none
            text-sm
          "
          placeholder="Enter your password..."
          v-model="password"
        />
      </div>
      <button
        class="
          bg-indigo-500
          px-4
          py-3
          text-white text-sm
          uppercase
          font-medium
          hover:bg-indigo-400
          mt-4
        "
      >
        Submit
      </button>
    </form>
  </div>
</template>

<script>
import { ref, inject } from "vue";
import { useRouter } from "vue-router";
import AuthService from "../services/auth";
import Notification from "../components/Notification.vue";
import GameService from "../services/game";

export default {
  components: { Notification },
  setup() {
    const store = inject("store");

    const router = useRouter();

    const nickname = ref("");
    const password = ref("");

    const handleLogin = async (e) => {
      e.preventDefault();

      const result = await AuthService.login(nickname.value, password.value);

      if (!result.success) {
        store.state.message = result.message;
        return;
      }

      store.state.token = result.data.token;
      store.state.nickname = result.data.nickname;
      store.state.description = result.data.description;
      store.state.profilePicturePath = result.data.profile_picture_path;
      store.state.socket = GameService.connect(result.data.token);

      router.push("/waiting-screen");
    };

    return {
      store,
      nickname,
      password,
      handleLogin,
    };
  },
};
</script>

<style></style>
