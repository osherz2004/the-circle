<template>
  <Layout>
    <div
      class="
        flex flex-col
        h-screen
        w-full
        justify-center
        items-center
        px-8
        gap-4
      "
    >
      <PlayerVote nickname="carl" />
      <PlayerVote nickname="john" />
      <button
        @click="handleSubmit"
        class="w-full bg-indigo-500 text-white uppercase rounded mt-4 py-2"
      >
        Submit Results
      </button>
    </div>
  </Layout>
</template>

<script>
import Layout from "../components/Layout.vue";
import PlayerVote from "../components/PlayerVote.vue";
import { useRouter } from "vue-router";
import { inject } from "vue";

export default {
  components: { Layout, PlayerVote },
  setup() {
    const store = inject("store");
    const router = useRouter();

    const handleSubmit = () => {
      store.state.socket.emit("vote", {
        carl: { catfish: false, favorite: false },
      });
      router.push("/winner");
    };

    return { handleSubmit };
  },
};
</script>

<style>
</style>