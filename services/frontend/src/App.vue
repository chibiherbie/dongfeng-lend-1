
<script setup>
  import heroMain from "./components/Hero.vue";
  import NavBar from './components/NavBar.vue'
  import AdvantagesMain from "./components/Advantages.vue";
  import ChoiceCar from "./components/ChoiceCar.vue";
  import CalculationMain from "./components/Calculation.vue";
  import RequestForm from "./components/RequestForm.vue";
  import FooterMain from "./components/Footer.vue";
</script>


<template>
  <div id="app" >
<!--    <Hello />-->
    <NavBar/>
<!--    <div class="main container">-->
      <heroMain/>
      <AdvantagesMain/>
      <ChoiceCar
        @slide-change="handleDataUpdated"
        @cars_info="handleCarsUpdated"
      />
      <CalculationMain
      :data="receivedData"
      :cars_data="carsData"
      />
      <RequestForm/>
      <FooterMain/>
<!--    </div>-->
  </div>
</template>

<script>

export default {
  name: 'app',
  data() {
    return {
      receivedData: 0,
      carsData: {'cars':
        [
            {"img": "C80", "total": 0},
            {"img": "C100"},
            {"img": "C120"},
            {"img": "C180"},
            {"img": "Z55"},
            {"img": "Z80"},
        ]
    }
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
