<template>
  <Layout>
    <div class="h-screen w-full flex flex-col items-center justify-center">
      <div class="grid grid-cols-4 gap-12 mt-8">
        <PlayerCard
          v-for="user in users"
          :key="user.id"
          :name="user.nickname"
          :description="user.description"
          :profilePicturePath="
            'http://localhost:5000' + user.profile_picture_path
          "
        />
      </div>
    </div>
  </Layout>
</template>

<script>
import { onMounted, ref } from "vue";
import Layout from "../components/Layout.vue";
import PlayerCard from "../components/PlayerCard.vue";
import UserService from "../services/user";
export default {
  components: { Layout, PlayerCard },
  setup() {
    const users = ref([]);

    onMounted(async () => {
      users.value = await UserService.getAll();
    });

    return { users };
  },
};
</script>

<style>
</style>