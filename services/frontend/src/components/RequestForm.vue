<template>

<section id="request" class="body-font bg-[#ECECEC] relative w-full">
    <div class="container px-5 py-24 mx-auto bg-white rounded-t-[480px] md:rounded-t-[780px] lg:w-4/5">

      <div class="flex flex-col text-center w-full mb-12">
        <h1 class="sm:text-4xl text-3xl text-[#00000030] font-semibold">ЗАЯВКА НА<br>ПОДГОТОВКУ ДОГОВОРА</h1>
      </div>

      <form @submit.prevent="submitForm" class="w-4/5 md:w-3/5 mx-auto flex flex-wrap justify-center text-black">

        <div class="p-2 mb-3 w-full">
          <div class="relative">
            <label for="VIN" class="leading-7 text-sm pl-2 font-semibold">VIN номер ТС</label>
            <input required type="text" id="VIN" name="VIN" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>

        <div class="p-2 mb-3 w-full">
          <div class="relative">
            <label for="name-company" class="leading-7 text-sm pl-2 font-semibold">Наименование юридического лица</label>
            <input required type="text" id="name-company" name="name-company" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>

        <div class="p-2 mb-3 w-full">
          <div class="relative">
            <label for="name" class="leading-7 text-sm pl-2 font-semibold">ФИО контактного лица</label>
            <input required type="text" id="name" name="name" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>

        <div class="p-2 mb-3 w-full">
          <div class="relative">
            <label for="position" class="leading-7 text-sm pl-2 font-semibold">Должность</label>
            <input required type="text" id="position" name="position" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>

        <div class="p-2 mb-3 w-full">
          <div class="relative">
            <label for="phone" class="leading-7 text-sm pl-2 font-semibold">Телефон</label>
            <input required type="phone" id="phone" name="phone" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>

        <div class="p-2 mb-3 w-full">
          <div class="relative">
            <label for="email" class="leading-7 text-sm pl-2 font-semibold">Email</label>
            <input required type="email" id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>

        <div class="mt-4">
          <button class="text-white bg-[#E60020] hover:text-[#E60020] font-semibold uppercase border-0 py-3 px-6 focus:outline-none hover:bg-gray-100 rounded-[50px] text-sm transition duration-200 ease-in-out">Отправить</button>
        </div>
      </form>
      <div v-if="responseMessage">{{ responseMessage }}</div>


    </div>
  </section>

</template>

<script>
import { defineComponent } from 'vue';
import axios from "axios";

export default defineComponent({
  name: 'RequestForm',
  data() {
    return {
      formData: {
        email: '',
      },
      responseMessage: ''
    };
  },
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut');
      // this.$router.push('/login');
    },
    async submitForm() {
      try {
        const response = await axios.post('http://localhost:5000/send_email', this.formData, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
        this.responseMessage = response.data.message;
      } catch (error) {
        console.error('Error:', error);
      }
    }
  },
});
</script>

<style scoped>

</style>