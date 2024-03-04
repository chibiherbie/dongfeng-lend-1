<template>
  <header class="text-gray-800 body-font fixed top-0 z-20 w-full transition-all duration-500" :class="{ 'bg-[#232323] ': isScrolled }">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a @click="scrollTo('hero')" class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0 cursor-pointer">
        <img src="../../public/img/logo-df-h360-color.png" class="max-w-[200px] max-h-[80px]" alt="">
      </a>
      <nav class="grid grid-cols-2 gap-y-2 md:ml-auto md:flex flex-wrap items-center text-base justify-center uppercase font-medium	transition duration-200 ease-in-out cursor-pointer">
        <a @click="scrollTo('advantages')" class="mr-5 hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Преимущества</a>
        <a @click="scrollTo('service')" class="mr-5 hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Сервисный контракт</a>
        <a @click="scrollTo('request')" class="mr-5 hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Заявка</a>
        <a @click="scrollTo('contact')" class="mr-5 hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Контакты</a>
      </nav>
      <button @click="toggled" class="inline-flex items-center bg-white border-0 py-1 px-2 focus:outline-none hover:bg-[#E60020] hover:stroke-white rounded-full text-base mt-4 md:mt-0 transition duration-200 ease-in-out cursor-pointer">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user hover:stroke-white">
          <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
        </svg>
      </button>

    </div>
  </header>

  <transition name="bounce" mode="out-in" v-if="visible">
    <the-modal-component @close="toggled"></the-modal-component>
  </transition>

</template>


<script setup>
import { ref } from "vue";
import TheModalComponent from "./Popup.vue";

const visible = ref(false);

function toggled () {
  visible.value = !visible.value
}

</script>


<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'NavBar',
  data() {
    return {
      isScrolled: false
    };
  },
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut');
      this.$router.push('/login');
    },
    scrollTo(targetId) {
      const targetBlock = document.getElementById(targetId);
      if (targetBlock) {
        const targetPosition = targetBlock.offsetTop - 150;
        window.scrollTo({ top: targetPosition, behavior: 'smooth' });
      }
    },
    handleScroll() {
      // Проверяем положение скролла
      this.isScrolled = window.scrollY > 250;
    }
  },
});

</script>

<style scoped>

</style>