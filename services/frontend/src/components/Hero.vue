<template>
    <transition name="fade" mode="out-in">
      <section class="text-gray-600 relative bg-[url(/img/background.png)] bg-cover bg-top bg-no-repeat h-[100vh] w-full">
        <div class="container mx-auto flex h-full px-5 py-24 md:flex-row flex-col items-center">
          <div class="lg:flex-grow md:w-1/2 md:pr-8 flex flex-col md:items-end mb-16 md:mb-0 items-center pb-80">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-white italic border-4 border-red-700 rounded-2xl p-4">DONGFENG -
              <br class="hidden lg:inline-block">сервис, которому вы<br>можете доверять
            </h1>
          </div>
        </div>
      </section>
    </transition>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'heroMain',
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
a {
  cursor: pointer;
}
</style>