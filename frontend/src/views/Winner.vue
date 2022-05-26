<template>
  <div class="h-screen w-full flex justify-center flex-col items-center">
    <h1 class="font-bold uppercase text-5xl">{{ text }}</h1>
    <hr class="border w-96 border-indigo-500 my-8" />
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  setup() {
    const text = ref("Waiting for results ⏳");
    setTimeout(() => {
      text.value = "The Winner is: carl 🏆";
    }, 15000);
    return { text };
  },
};
</script>

<style>
</style>