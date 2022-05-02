<template>
  <div>
    <div class="chat-message" v-if="self">
      <div class="flex items-center justify-end">
        <div
          class="
            flex flex-col
            space-y-2
            text-xs
            max-w-xs
            mx-2
            order-1
            items-end
          "
        >
          <div>
            <span
              class="
                px-4
                py-2
                rounded-lg
                inline-block
                rounded-br-none
                bg-indigo-500
                text-white
              "
              >{{ message }}</span
            >
          </div>
        </div>
        <img
          :src="picture"
          alt="My profile"
          class="w-16 h-16 rounded-full order-2"
        />
      </div>
    </div>
    <div class="flex items-center" v-else>
      <div
        class="
          flex flex-col
          space-y-2
          text-xs
          max-w-xs
          mx-2
          order-2
          items-start
        "
      >
        <div>
          <span
            class="
              px-4
              py-2
              rounded-lg
              inline-block
              rounded-bl-none
              bg-gray-300
              text-gray-600
            "
            >{{ message }}</span
          >
        </div>
      </div>
      <img
        :src="picture"
        alt="My profile"
        class="w-16 h-16 rounded-full order-1"
      />
    </div>
  </div>
</template>

<script>
export default {
  props: { message: String, self: Boolean, picture: String },
  setup() {
    return;
  },
};
</script>

<style>
</style>