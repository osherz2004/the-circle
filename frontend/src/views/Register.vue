<template>
  <div class="h-screen w-1/2 mx-auto flex flex-col justify-center">
    <Notification :message="message" />
    <h1 class="text-4xl font-bold uppercase">Create Your Player!</h1>
    <hr class="border-2 border-indigo-500 bg-indigo-500 my-4" />
    <form @submit="handleSubmit">
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
      <div class="border-b border-indigo-500 py-2 mt-8 mb-8">
        <label for="description" class="font-bold text-sm uppercase">
          Description
        </label>
        <textarea
          id="description"
          name="description"
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
          placeholder="Enter your description..."
          v-model="description"
          rows="8"
        ></textarea>
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
      <div>
        <label for="profile_picture" class="font-bold text-sm uppercase"
          >Profile picture</label
        >
        <input
          class="
            form-control
            block
            w-full
            p-3
            text-base
            font-normal
            text-gray-700
            bg-white bg-clip-padding
            border border-solid border-gray-300
            focus:text-gray-700
            focus:bg-white
            focus:border-indigo-600
            focus:outline-none
            mt-4
          "
          type="file"
          id="profile_picture"
          name="profile_picture"
          @change="handleImageSelect"
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
import { ref } from "vue";
import AuthService from "../services/auth";
import { useRouter } from "vue-router";
import Notification from "@/components/Notification.vue";

export default {
  components: { Notification },
  setup() {
    const nickname = ref("");
    const description = ref("");
    const password = ref("");
    const profilePicture = ref(null);
    const message = ref("");

    const router = useRouter();

    const handleImageSelect = (e) => {
      if (e.target.files.length == 0) return;

      profilePicture.value = e.target.files[0];
    };

    const handleSubmit = async (e) => {
      e.preventDefault();

      const result = await AuthService.register(
        nickname.value,
        password.value,
        description.value,
        profilePicture.value
      );

      if (result.success) {
        router.push("/login");
        return;
      }

      message.value = result.message;
    };

    return {
      nickname,
      description,
      password,
      profilePicture,
      handleImageSelect,
      handleSubmit,
      message,
    };
  },
};
</script>

<style>
</style>