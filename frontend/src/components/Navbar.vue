<template>
  <nav class="h-screen w-28 bg-indigo-500">
    <ul class="h-full flex flex-col justify-between items-center py-16">
      <li>
        <router-link to="/" class="text-white"
          ><i class="bi bi-house-door-fill text-3xl hover:text-gray-300"></i
        ></router-link>
      </li>
      <li>
        <router-link to="/players" class="text-white"
          ><i class="bi bi-people-fill text-3xl hover:text-gray-300"></i
        ></router-link>
      </li>
      <li>
        <router-link to="/chat" class="text-white"
          ><i class="bi bi-chat-left-text-fill text-3xl hover:text-gray-300"></i
        ></router-link>
      </li>
      <li>
        <router-link to="/" class="text-white"
          ><i class="bi bi-file-bar-graph-fill text-3xl hover:text-gray-300"></i
        ></router-link>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {};
</script>

<style></style>
