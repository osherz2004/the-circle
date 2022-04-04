<template>
  <div class="flex">
    <Navbar />
    <slot></slot>
  </div>
</template>

<script>
import Navbar from './Navbar.vue';

export default {
  components: { Navbar },
};
</script>

<style></style>
