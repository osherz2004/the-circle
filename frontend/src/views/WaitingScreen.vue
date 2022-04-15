<template>
  <div class="h-screen w-full flex justify-center flex-col items-center">
    <h1 class="font-bold uppercase text-5xl">Waiting for players to join</h1>
    <hr class="border w-96 border-indigo-500 my-8" />
    <h2 class="font-bold text-2xl">{{ current }} / {{ max }}</h2>
  </div>
</template>

<script>
import { inject, ref } from "vue";
import { useRouter } from "vue-router";

export default {
  setup() {
    const store = inject("store");

    const router = useRouter();

    const max = ref(0);
    const current = ref(0);

    store.state.socket.emit("status:get");

    store.state.socket.on("status:recive", (data) => {
      current.value = data.current;
      max.value = data.max;
    });

    store.state.socket.on("game:start", () => {
      router.push("/");
    });

    return { max, current };
  },
};
</script>

<style>
</style>