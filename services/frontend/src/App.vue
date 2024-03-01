
<script setup>
  import Hero from "./components/Hero.vue";
  import NavBar from './components/NavBar.vue'
  import Advantages from "./components/Advantages.vue";
  import ChoiceCar from "./components/ChoiceCar.vue";
  import Calculation from "./components/Calculation.vue";
  import RequestForm from "./components/RequestForm.vue";
  import Footer from "./components/Footer.vue";
  import Hello from "./components/HelloWorld.vue";
</script>


<template>
  <div id="app" >
<!--    <Hello />-->
    <NavBar/>
<!--    <div class="main container">-->
      <Hero/>
      <Advantages/>
      <ChoiceCar
        @slide-change="handleDataUpdated"
        @cars_info="handleCarsUpdated"
      />
      <Calculation
      :data="receivedData"
      :cars_data="carsData"
      />
      <RequestForm/>
      <Footer/>
<!--    </div>-->
  </div>
</template>

<script>

export default {
  name: 'app',
  data() {
    return {
      receivedData: 0,
      carsData: {}
    };
  },
  methods: {
    handleDataUpdated(data) {
      this.receivedData = data; // получаем данные от ChildComponent1
    },
    handleCarsUpdated(data) {
      this.carsData = data; // получаем данные от ChildComponent1
    },
  },
}
</script>


<style scoped>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.vue:hover {
    filter: drop-shadow(0 0 2em #42b883aa);
  }
</style>
