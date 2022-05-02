<template>
  <div>
    <Layout>
      <div class="flex items-center justify-center w-full">
        <div
          class="w-3/4 grid"
          style="
            grid-template-rows: auto auto;
            grid-template-columns: auto auto;
          "
        >
          <div
            class="rounded w-56 h-56 row-span-2 mr-24"
            :style="{
              backgroundImage:
                'url(\'' + store.state.profilePicturePath + '\')',
            }"
            style="background-size: cover"
          ></div>
          <h2 class="text-3xl font-bold uppercase self-end mb-6">
            {{ store.state.nickname }}
          </h2>
          <p class="width-1/2">
            {{ store.state.description }}
          </p>
        </div>
      </div>
    </Layout>
  </div>
</template>

<script>
import Layout from "../components/Layout.vue";
import { inject } from "vue";

export default {
  components: { Layout },
  setup() {
    const store = inject("store");

    store.state.socket.on("game:message", (data) => {
      store.state.message = data.message;
    });

    return { store };
  },
};
</script>

<style></style>
