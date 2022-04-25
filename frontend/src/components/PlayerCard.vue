<template>
  <div class="border shadow rounded w-72 h-96 p-8">
    <img :src="profilePicturePath" alt="x" class="w-full" />
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