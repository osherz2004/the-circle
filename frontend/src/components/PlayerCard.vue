<template>
  <div class="border shadow rounded w-72 p-8">
    <div class="w-full h-56 overflow-hidden">
      <img :src="profilePicturePath" alt="x" class="w-full" />
    </div>
    <h5 class="font-bold text-2xl mt-2">{{ name }}</h5>
    <hr class="my-2" />
    <p class="text-md">
      {{ description }}
    </p>
  </div>
</template>

<script>
export default {
  props: { name: String, description: String, profilePicturePath: String },
  setup(props) {
    return { ...props };
  },
};
</script>

<style>
</style>