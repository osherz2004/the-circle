<template>
  <div
    class="fixed top-0 left-0 w-full px-96"
    v-if="store.state.message.length > 0"
  >
    <div
      class="
        bg-gray-100
        border-2 border-indigo-500
        mt-8
        p-4
        flex
        justify-between
        items-center
      "
    >
      <p class="uppercase text-gray-700">{{ store.state.message }}</p>
      <i
        @click="handleClose"
        class="bi bi-x text-black text-3xl cursor-pointer"
      ></i>
    </div>
  </div>
</template>

<script>
import { inject } from "vue";

export default {
  setup() {
    const store = inject("store");

    const handleClose = () => {
      store.state.message = "";
    };

    return { handleClose, store };
  },
};
</script>

<style></style>
