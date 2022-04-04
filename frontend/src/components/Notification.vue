<template>
  <div
    class="fixed top-0 left-0 w-full px-96"
    v-if="message1.length > 0 && isDisplayed"
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
      <p class="uppercase text-gray-700">{{ message1 }}</p>
      <i
        @click="handleClose"
        class="bi bi-x text-black text-3xl cursor-pointer"
      ></i>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";

export default {
  props: ["message"],
  setup(props) {
    const isDisplayed = ref(true);
    const message1 = computed(() => {
      console.log(props.message);
      return props.message;
    });

    const handleClose = () => {
      isDisplayed.value = false;
    };

    return { isDisplayed, handleClose, message1 };
  },
};
</script>

<style></style>
