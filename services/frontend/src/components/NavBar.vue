<template>
  <header class="text-gray-800 body-font fixed top-0 z-20 w-full transition-all duration-500 bg-[#232323]" :class="{ 'bg-[#232323] ': isScrolled }">
    <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
      <a @click="scrollTo('hero')" class="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0 cursor-pointer">
        <img src="../../public/img/logo-df-h360-color.png" class="max-w-[200px] max-h-[80px]" alt="">
      </a>

      <!--  HUMBURGER   -->
      <div class="md:hidden cursor-pointer" v-on:click="navOpen=!navOpen" v-bind:class="{active:navOpen}">
        <svg class="min-[320px]:hidden" xmlns="http://www.w3.org/2000/svg" width="50" height="12" viewBox="0 0 50 12" fill="none">
            <line x1="8.74228e-08" y1="1" x2="50" y2="1" stroke="white" stroke-width="2"/>
            <line x1="13" y1="11" x2="50" y2="11" stroke="white" stroke-width="2"/>
        </svg>
        <svg class="hidden min-[320px]:block" xmlns="http://www.w3.org/2000/svg" width="111" height="20" viewBox="0 0 112 24" fill="none">
          <line x1="0.910156" y1="2" x2="111.91" y2="2" stroke="white" stroke-width="4"/>
          <line x1="38" y1="22" x2="111" y2="22" stroke="white" stroke-width="4"/>
        </svg>
      </div>

      <transition name="translateX">
        <nav v-show="navOpen">
          <div class="mt-4">
            <ul class="space-y-2 items-center flex flex-col">
              <li @click="scrollTo('advantages')" class="hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Преимущества</li>
              <li @click="scrollTo('service')" class="hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Сервисный контракт</li>
              <li @click="scrollTo('request')" class="hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Заявка</li>
              <li @click="scrollTo('contact')" class="hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Контакты</li>
              <button @click="toggled" class="mx-auto items-center bg-white border-0 py-1 px-2 focus:outline-none hover:bg-[#E60020] hover:stroke-white rounded-full text-base mt-4 md:mt-0 transition duration-200 ease-in-out cursor-pointer">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user hover:stroke-white">
                  <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>
                </svg>
              </button>
            </ul>
          </div>
        </nav>
      </transition>

      <nav class="hidden md:visible md:ml-auto md:flex flex-wrap items-center text-base justify-center uppercase font-medium	transition duration-200 ease-in-out cursor-pointer">
        <a @click="scrollTo('advantages')" class="mr-5 hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Преимущества</a>
        <a @click="scrollTo('service')" class="mr-5 hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Сервисный контракт</a>
        <a @click="scrollTo('request')" class="mr-5 hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Заявка</a>
        <a @click="scrollTo('contact')" class="mr-5 hover:text-white bg-white hover:bg-[#E60020] py-1 px-4 rounded-full transition duration-200 ease-in-out cursor-pointer">Контакты</a>
      </nav>
      <button @click="toggled" class="hidden md:visible md:inline-flex items-center bg-white border-0 py-1 px-2 focus:outline-none hover:bg-[#E60020] hover:stroke-white rounded-full text-base mt-4 md:mt-0 transition duration-200 ease-in-out cursor-pointer">
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
      isScrolled: false,
      navOpen: false,
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

.translateX-enter{
	transform:translateX(-200px);
	opacity: 0;
}

.translateX-enter-active,.translateX-leave-active{
	transform-origin: top left 0;
	transition:.2s ease;
}

.translateX-leave-to{
	transform: translateX(-200px);
	opacity: 0;
}

@media (max-width: 768px) {
  header {
    background-color: #232323; /* Замените на нужный вам цвет */
  }
}

</style>