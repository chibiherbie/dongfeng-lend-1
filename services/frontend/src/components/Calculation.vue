<template>
  <section class="body-font bg-[#ECECEC] relative w-full pb-40">

    <div class="flex relative h-[140px] w-full">
      <div class="w-24 h-1 rounded-full bg-[#E60020] inline-flex absolute bottom-2"></div>

      <div class="absolute left-28 flex items-center">
        <p class="text-[#E60020] font-semibold text-[122px]">2</p>
        <h1 class="font-semibold text-4xl ml-2 text-black">ПОЛУЧЕНИЕ<br>РАСЧЕТА</h1>

      </div>

      <div class="w-[75%] h-1 rounded-full bg-[#E60020] inline-flex absolute bottom-2 right-0"></div>

    </div>
    <transition name="fade">
    <div class="bg-white mt-32" :class="{ 'w-[95%]': visible, 'w-[85%]': !visible }">
      <div class="container mx-auto py-20">

        <div class="flex justify-between items-center">
          <h1 class="font-semibold text-4xl ml-2 text-black">ТЕХНИЧЕСКОЕ ОБСЛУЖИВАНИЕ</h1>
          <svg width="61" height="61" viewBox="0 0 61 61" fill="none" xmlns="http://www.w3.org/2000/svg" :class='"transition-all ease-in-out cursor-pointer rotate-" + degree' @click="toggled">
            <path d="M24.9116 21.9023C24.0806 21.0713 22.7333 21.0713 21.9023 21.9023C21.0713 22.7333 21.0713 24.0806 21.9023 24.9116L27.4906 30.5L21.9024 36.0885C21.0714 36.9192 21.0714 38.2666 21.9024 39.0976C22.7333 39.9286 24.0807 39.9286 24.9116 39.0976L30.5001 33.5095L36.0882 39.0976C36.9192 39.9286 38.2666 39.9286 39.0977 39.0976C39.9287 38.2666 39.9287 36.9192 39.0977 36.0882L33.5092 30.5L39.0977 24.9116C39.9287 24.0807 39.9287 22.7334 39.0977 21.9024C38.2666 21.0714 36.9192 21.0714 36.0882 21.9024L30.5001 27.4906L24.9116 21.9023Z" fill="#E60020"/>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M30.5 0C13.6553 0 0 13.6553 0 30.5C0 47.3448 13.6553 61 30.5 61C47.3448 61 61 47.3448 61 30.5C61 13.6553 47.3448 0 30.5 0ZM4.25581 30.5C4.25581 16.0057 16.0057 4.25581 30.5 4.25581C44.9942 4.25581 56.7442 16.0057 56.7442 30.5C56.7442 44.9942 44.9942 56.7442 30.5 56.7442C16.0057 56.7442 4.25581 44.9942 4.25581 30.5Z" fill="#E60020"/>
          </svg>
        </div>

        <div class="transition-all ease-in-out" :style="{ display: visible ? 'block' : 'none' }">
          <table class="iksweb mt-16 mb-24">
            <tbody>
              <tr class="font-bold text-lg text-center h-14">
                <th class="!border-t-0 !border-l-0">Модель</th>
                <th class="text-left !border-t-0 !border-l-0">Наполнение</th>
                <th class="!border-t-0 !border-l-0"></th>
                <th class="!border-t-0 !border-r-0" colspan="7">Пробег, км</th>
              </tr>
              <tr v-for="(row, rowIndex) in cars_data.cars[data].data" :key="rowIndex">
                <td :rowspan="cars_data.cars[data].data.length + 1" class="font-bold text-lg text-center h-14" v-if="rowIndex === 0">
                  {{ cars_data.cars[data].img }}
                </td>
                <td v-for="(value, key) in row" :key="key" :class="{ 'red-row': rowIndex === 1 || Object.keys(row).length < 3}">
                  {{ value }}
                </td>
                <td :colspan="7" class="font-bold text-lg text-center h-14 red-row" v-if="Object.keys(row).length < 3">

                </td>
              </tr>
              <tr class="red-row h-14">
                <td colspan="9" class="!border-b-0 !border-r-0"></td>
              </tr>
            </tbody>
          </table>

          <form action="" class="w-4/6 ml-auto mr-[15%] flex flex-wrap justify-center text-black relative">

          <div class="p-2 mb-3 w-full">
            <div class="relative">
              <label for="VIN" class="leading-7 text-sm pl-2 font-bold">VIN номер ТС</label>
              <input type="text" id="VIN" name="VIN" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>

          <div class="p-2 mb-3 w-full">
            <div class="relative">
              <label for="email" class="leading-7 text-sm pl-2 font-bold">Наименование юридического лица</label>
              <input type="email" id="" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>

          <div class="p-2 mb-3 w-full">
            <div class="relative">
              <label for="email" class="leading-7 text-sm pl-2 font-bold">ФИО контактного лица</label>
              <input type="email" id="" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>

          <div class="p-2 mb-3 w-full">
            <div class="relative">
              <label for="email" class="leading-7 text-sm pl-2 font-bold">Должность</label>
              <input type="email" id="" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>

          <div class="p-2 mb-3 w-full">
            <div class="relative">
              <label for="email" class="leading-7 text-sm pl-2 font-bold">Телефон</label>
              <input type="phone" id="phone" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>

          <div class="p-2 mb-3 w-full">
            <div class="relative">
              <label for="email" class="leading-7 text-sm pl-2 font-bold">Email</label>
              <input type="email" id="email" name="email" class="w-full bg-white rounded-lg border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
            </div>
          </div>

          <div class="mt-10">
            <button class="text-white bg-[#E60020] hover:text-[#E60020] font-semibold uppercase border-0 py-3 px-6 focus:outline-none hover:bg-gray-100 rounded-[50px] text-sm transition duration-200 ease-in-out">СГЕНИРИРОВАТЬ КП</button>
          </div>

          <div class="absolute right-0 bottom-0 flex space-x-2">
            <svg class="cursor-pointer stroke-black hover:stroke-[#E60020] transition duration-200 ease-in-out" width="56" height="55" viewBox="0 0 56 55" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="28.2988" cy="27.5" r="27.5" fill="#D9D9D9" stroke="none"/>
              <path d="M14.3474 35.9359C12.2443 34.5222 10.8596 32.1145 10.8596 29.382C10.8596 25.2775 13.9838 21.906 17.9743 21.5348C18.7906 16.5483 23.1022 12.7441 28.2986 12.7441C33.4951 12.7441 37.8067 16.5483 38.6231 21.5348C42.6135 21.906 45.7377 25.2775 45.7377 29.382C45.7377 32.1145 44.353 34.5222 42.2499 35.9359M21.323 37.2631L28.2986 44.2685M28.2986 44.2685L35.2743 37.2631M28.2986 44.2685V28.5063" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <svg class="cursor-pointer stroke-black hover:stroke-[#E60020] transition duration-200 ease-in-out" width="56" height="55" viewBox="0 0 56 55" fill="none" xmlns="http://www.w3.org/2000/svg">
              <circle cx="27.7012" cy="27.5" r="27.5" fill="#D9D9D9" stroke="none"/>
              <path d="M35.5904 39.2212V33.3606H19.8117V39.2212M35.5904 39.2212V45.0819H19.8117V39.2212M35.5904 39.2212H43.4797V21.6393H35.5904M19.8117 39.2212H11.9224V21.6393H19.8117M35.5904 21.6393H19.8117M35.5904 21.6393V11.8715C35.5904 10.7926 34.7074 9.91797 33.6181 9.91797H21.784C20.6948 9.91797 19.8117 10.7926 19.8117 11.8715V21.6393" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>


          </div>
        </form>
        </div>


      </div>
    </div>
    </transition>
  </section>

</template>


<script setup>
import { defineComponent, ref } from 'vue'

const visible = ref(false);
const degree = ref('45');

function toggled () {
  visible.value = !visible.value
  degree.value = visible.value ? '0' : '45';

  // console.log(visible.value)
  // console.log(degree.value)
}

</script>


<script>


export default defineComponent({
  name: 'CalculationMain',
  props: ['data', 'cars_data'],
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
  methods: {
    async logout () {
      await this.$store.dispatch('logOut');
      // this.$router.push('/login');
    }
  },
});
</script>

<style scoped>
  table.iksweb{
    width: 97%;
    color: black;
    height: auto;
    position:relative;
  }
  table.iksweb td, table.iksweb th {
    border: 1px solid #eeeef5;
  }
  table.iksweb td,table.iksweb th {
    padding: 10px;
    width: 30px;
    height: 35px;
  }
  table.iksweb th {
  }
  table::after {
    content: " ";
    inset: 0;
    border: 1px solid #eeeef5;
    position: absolute;
    border-radius: 10px;
  }

  .red-row {
    background: #e60020;
    color: white;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s ease;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
</style>