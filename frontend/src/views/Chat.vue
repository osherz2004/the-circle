<template>
  <Layout>
    <div class="flex-1 p:2 sm:p-6 justify-between flex flex-col h-screen">
      <div
        id="messages"
        class="
          flex flex-col
          space-y-4
          p-3
          overflow-y-auto
          scrollbar-thumb-blue
          scrollbar-thumb-rounded
          scrollbar-track-blue-lighter
          scrollbar-w-2
          scrolling-touch
        "
      >
        <ChatMessage
          v-for="msg in chatMessages"
          :key="msg.id"
          :message="msg.message"
          :self="msg.self"
          :picture="msg.picture"
        />
      </div>
      <div class="border-t-2 border-gray-200 px-4 pt-4 mb-2 sm:mb-0">
        <div class="relative flex">
          <span class="absolute inset-y-0 flex items-center"></span>
          <input
            type="text"
            placeholder="Write your message!"
            class="
              w-full
              focus:outline-none focus:placeholder-gray-400
              text-gray-600
              placeholder-gray-600
              pl-8
              bg-gray-200
              rounded-md
              py-3
            "
            v-model="newMessage"
          />
          <div class="absolute right-0 items-center inset-y-0 hidden sm:flex">
            <button
              type="button"
              class="
                inline-flex
                items-center
                justify-center
                rounded-lg
                px-4
                py-3
                transition
                duration-500
                ease-in-out
                text-white
                bg-indigo-500
                hover:bg-indigo-400
                focus:outline-none
              "
              @click="sendMessage"
            >
              <span class="font-bold">Send</span>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                class="h-6 w-6 ml-2 transform rotate-90"
              >
                <path
                  d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"
                ></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </Layout>
</template>

<script>
import Layout from "../components/Layout.vue";
import ChatMessage from "../components/ChatMessage.vue";
import { inject, onMounted, ref } from "vue";
export default {
  components: { Layout, ChatMessage },
  setup() {
    const store = inject("store");
    const chatMessages = ref([]);
    const newMessage = ref("");

    onMounted(() => {
      store.state.socket.emit("chat:get");
      store.state.socket.on("chat:recive", (messages) => {
        chatMessages.value = messages.map((msg) => ({
          id: msg.id,
          message: msg.message,
          self: msg.player == store.state.nickname,
          picture: msg.profile_picture_path,
        }));
        console.log(messages);
      });
    });

    const sendMessage = () => {
      store.state.socket.emit("chat:send", {
        message: newMessage.value,
        player: store.state.nickname,
        profile_picture_path: store.state.profilePicturePath,
      });
    };

    return { chatMessages, newMessage, sendMessage };
  },
};
</script>

<style>
</style>