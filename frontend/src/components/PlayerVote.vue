<template>
  <div
    class="
      w-full
      flex
      justify-between
      items-center
      p-8
      border border-gray-400
      rounded
    "
  >
    <span class="text-xl font-bold">{{ name }}</span>
    <div class="w-24 gap-8 flex">
      <svg
        :fill="isFavorite ? '#6366f1' : 'black'"
        @click="selectStar"
        version="1.1"
        id="Capa_1"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        x="0px"
        y="0px"
        viewBox="0 0 473.486 473.486"
        style="enable-background: new 0 0 473.486 473.486"
        xml:space="preserve"
      >
        <polygon
          points="473.486,182.079 310.615,157.952 235.904,11.23 162.628,158.675 0,184.389 117.584,299.641 91.786,462.257 
	237.732,386.042 384.416,460.829 357.032,298.473 "
        />
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
        <g></g>
      </svg>
      <svg
        version="1.1"
        :fill="isCatfish ? '#6366f1' : 'black'"
        @click="selectCatfish"
        x="0px"
        y="0px"
        viewBox="0 0 1000 1000"
        enable-background="new 0 0 1000 1000"
        xml:space="preserve"
        :class="{ 'fill-indigo-500': true }"
      >
        <g>
          <path
            d="M893,111.3C885.2,107.2,700.1,10,507.2,10c-208.5,0-392.9,99.4-400.7,103.6l-23.1,12.6v454.3c0,88.4,69.3,183.3,206,282.1c95.8,69.3,190.2,115.6,194.2,117.5l20,9.8l19.8-10.3c87.4-45.3,162.1-93.2,222-142.3c49.1-40.3,88.7-81.8,117.7-123.2c50.7-72.6,53.4-122.4,53.4-132.8V123.8L893,111.3z M801.3,579.9c-0.6,4-5,28.9-32.6,68.4c-22.9,32.8-55.3,66.5-96.3,100.1c-46.3,38-103.3,75.6-169.7,111.9C469,842,412.8,809.7,357,769.3c-58.2-42.1-101.5-82.3-128.7-119.6c-13.5-18.5-29.6-45.5-29.6-69.2l0-383.6c18.2-8.1,42.5-18.1,71.1-28.1c37.3-12.9,74.6-23.1,110.9-30.4c44-8.8,86.5-13.3,126.5-13.3c117.5,0,235.6,44.4,294.1,70.1L801.3,579.9L801.3,579.9z"
          />
          <path d="M434.1,632.1V763h131.7V632.1L434.1,632.1L434.1,632.1z" />
          <path d="M434.1,196.6h131.7v383.1H434.1V196.6z" />
        </g>
      </svg>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  props: {
    nickname: String,
  },
  setup(props) {
    const isCatfish = ref(false);
    const isFavorite = ref(false);

    const selectStar = () => {
      isFavorite.value = !isFavorite.value;
    };
    const selectCatfish = () => {
      isCatfish.value = !isCatfish.value;
    };

    return {
      isCatfish,
      isFavorite,
      selectStar,
      selectCatfish,
      name: props.nickname,
    };
  },
};
</script>

<style>
</style>