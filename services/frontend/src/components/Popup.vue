<template>
    <div>
      <div class="h-full w-full fixed top-0 left-0 z-20 bg-[#23232380]" v-on:click="hide"></div>
      <div class="bg-white rounded-[40px] text-lg pt-12 shadow-lg w-[454px] fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-30">
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg" class="cursor-pointer absolute right-6 top-6 z-40" v-on:click="hide">
          <path d="M1 1L13 13" stroke="#A7A7A7" stroke-opacity="0.65" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M1 13L13 1" stroke="#A7A7A7" stroke-opacity="0.65" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        <svg width="100%" height="135" viewBox="0 0 462 135" fill="none" xmlns="http://www.w3.org/2000/svg" class="absolute top-4">
          <g style="mix-blend-mode:multiply">
          <path d="M465.635 19.5993L464.192 53.8159C300.636 163.452 19.3777 107.549 -3.7188 108.394L-3.37014 100.126C30.5922 102.493 303.022 160.771 465.635 19.5993Z" fill="url(#paint0_linear_145_1010)"/>
          </g>
          <g style="mix-blend-mode:multiply">
          <path d="M458.547 68.5486C291.793 174.282 5.5001 90.468 -2.97226 90.6975L-1.96178 66.7348C56.8348 84.3283 293.852 154.428 458.547 68.5486Z" fill="#E40522"/>
          </g>
          <defs>
          <linearGradient id="paint0_linear_145_1010" x1="-1.57407" y1="57.5336" x2="463.209" y2="77.1329" gradientUnits="userSpaceOnUse">
          <stop stop-color="#E8E8E7"/>
          <stop offset="1" stop-color="#C1C0C0"/>
          </linearGradient>
          </defs>
        </svg>
        <div class="px-6 pb-6 text-center">
            <h3 class="text-2xl mb-2 font-semibold text-black">ЛИЧНЫЙ КАБИНЕТ</h3>
        </div>

        <div v-if="!register & !login">
          <ul class="cursor-pointer text-center mt-10 px-24">
            <li class="w-full px-6 py-4">
              <button v-on:click="registerPopup" class="w-full text-white bg-[#A7A7A7] hover:text-[#E60020] font-semibold uppercase border-0 py-3 px-6 focus:outline-none hover:bg-gray-100 rounded-[50px] text-sm transition duration-200 ease-in-out">Зарегистрироваться</button>
            </li>
            <li class="w-full px-6 pb-3">
              <button v-on:click="loginPopup" class="w-full text-white bg-[#E60020] hover:text-[#E60020] font-semibold uppercase border-0 py-3 px-6 focus:outline-none hover:bg-gray-100 rounded-[50px] text-sm transition duration-200 ease-in-out">Войти</button>
            </li>
          </ul>
        </div>

        <div v-if="register">
          <ul class="mt-10 px-24">
            <li class="p-2 w-full">
              <div class="relative">
                <label for="email" class="text-black leading-7 text-sm pl-2 font-semibold">ФИО</label>
                <input id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
              </div>
            </li>
            <li class="p-2 w-full">
              <div class="relative">
                <label for="email" class="text-black leading-7 text-sm pl-2 font-semibold">Должность</label>
                <input id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
              </div>
            </li>
            <li class="p-2 w-full">
              <div class="relative">
                <label for="email" class="text-black leading-7 text-sm pl-2 font-semibold">Телефон</label>
                <input id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
              </div>
            </li>
            <li class="p-2 w-full">
              <div class="relative">
                <label for="email" class="text-black leading-7 text-sm pl-2 font-semibold">email</label>
                <input type="email" id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
              </div>
            </li>
            <li class="p-2 w-full">
              <div class="relative">
                <label for="email" class="text-black leading-7 text-sm pl-2 font-semibold">Пароль</label>
                <input type="email" id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
              </div>
            </li>
            <li class="w-full px-6 py-4">
              <button class="w-full text-white bg-[#A7A7A7] hover:text-[#E60020] font-semibold uppercase border-0 py-3 px-6 focus:outline-none hover:bg-gray-100 rounded-[50px] text-sm transition duration-200 ease-in-out">Зарегистрироваться</button>
            </li>
          </ul>
        </div>

        <div v-if="login">
          <ul class="mt-10 px-24">
            <li class="p-2 w-full">
              <div class="relative">
                <label for="email" class="text-black leading-7 text-sm pl-2 font-semibold">Email</label>
                <input type="email" id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
              </div>
            </li>
            <li class="p-2 mb-3 w-full">
              <div class="relative">
                <label for="email" class="text-black leading-7 text-sm pl-2 font-semibold">Пароль</label>
                <input type="password" id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
              </div>
            </li>
            <li class="w-full px-6 pb-3">
              <button class="cursor-pointer w-full text-white bg-[#E60020] hover:text-[#E60020] font-semibold uppercase border-0 py-3 px-6 focus:outline-none hover:bg-gray-100 rounded-[50px] text-sm transition duration-200 ease-in-out">Войти</button>
            </li>
          </ul>
        </div>

      </div>
    </div>
</template>

<script setup>
import {ref} from "vue";

const register = ref(false);
const login = ref(false);

function registerPopup() {
      register.value = !register.value
}
function loginPopup() {
      login.value = !login.value
}

</script>

<script>
export default {
    name: "TheModalComponent",
    methods: {
        hide() {
            console.log('close popup');
            this.$emit('close')
        }
    }
}
</script>

<style scoped>
.bounce-enter-active {
    animation: bounce-in .5s ease-out both;
}

.bounce-leave-active {
    animation: bounce-in .5s reverse ease-in both;
}

@keyframes bounce-in {
    0% {
        transform: scale(0);
    }
    50% {
        transform: scale(1.10);
    }
    100% {
        transform: scale(1);
    }
}
</style>
