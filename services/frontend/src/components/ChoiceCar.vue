<template>
  <section id="service" class="body-font bg-[#ECECEC] relative w-full pb-20 md:pb-40 text-black pt-4 md:pt-24">

    <div class="container px-5 mx-auto md:absolute top-0 right-4">
      <h1 class="mb-10 md:mb-0 text-right font-semibold text-5xl md:text-[64px] text-[#00000030] mr-20">СЕРВИСНЫЙ<br>КОНТРАКТ</h1>
    </div>

    <div class="flex relative h-[92px] md:h-[140px] w-full mb-20 md:mb-32">
      <div class="w-24 h-1 rounded-full bg-[#E60020] inline-flex absolute bottom-2"></div>

      <div class="absolute left-28 flex items-center">
        <p class="text-[#E60020] font-semibold text-[75px] md:text-[122px]">1</p>
        <h1 class="font-semibold text-3xl md:text-4xl ml-2">ВЫБОР<br>АВТОМОБИЛЯ</h1>
      </div>

      <div class="hidden md:visible w-[40%] xl:w-[75%] h-1 rounded-full bg-[#E60020] md:inline-flex absolute bottom-2 right-0"></div>

    </div>

    <div class="w-full relative">

        <Carousel ref="carousel" v-model="currentSlide" :items-to-show="itemsToShow" :wrap-around="true">
          <Slide v-for="slide in cars_data.cars" :key="slide">
            <div class="md:w-full xl:w-[90%]">

              <div class="md:w-full xl:w-[90%] px-5 py-10 mx-auto bg-white rounded-3xl md:rounded-[98px] relative">
              <img :src="'img/' + slide.img + '.png'" alt="Изображение" class="h-60 w-96 md:h-auto md:w-auto object-cover">
              <p class="text-center font-semibold text-xl">DONGFENG {{ slide.img }}</p>

            </div>

          </div>
          </Slide>

        <template #addons>
          <Navigation />
        </template>
      </Carousel>


      <button type="button" class="absolute right-1 sm:right-20 md:right-[28%] xl:right-[33%] bottom-32 xl:bottom-52 z-10" @click="next">
        <svg width="36" height="79" viewBox="0 0 36 79" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M1.25722 0.920326C2.76676 -0.453609 5.03946 -0.267934 6.33339 1.33495L35.1335 37.0122C36.2888 38.4439 36.2888 40.556 35.1335 41.9877L6.33339 77.665C5.03946 79.268 2.76676 79.4535 1.25722 78.0799C-0.252331 76.7058 -0.427196 74.2925 0.866735 72.6896L27.6585 39.4999L0.866735 6.31036C-0.427196 4.70743 -0.252331 2.29426 1.25722 0.920326Z" fill="black" fill-opacity="0.2"/>
        </svg>
      </button>

      <button type="button" class="absolute left-1 sm:left-20 md:left-[28%] xl:left-[33%] bottom-32 xl:bottom-52 z-10" @click="prev">
        <svg width="36" height="78" viewBox="0 0 36 78" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M34.7428 77.0913C33.2332 78.4479 30.9605 78.2645 29.6666 76.682L0.866516 41.4563C-0.288841 40.0427 -0.288841 37.9574 0.866516 36.5438L29.6666 1.31807C30.9605 -0.264572 33.2332 -0.447746 34.7428 0.90844C36.2523 2.26514 36.4272 4.64791 35.1333 6.23055L8.34153 39.0001L35.1333 71.7695C36.4272 73.3522 36.2523 75.7348 34.7428 77.0913Z" fill="black" fill-opacity="0.2"/>
        </svg>
      </button>

    </div>

  </section>
</template>

<script>
import {defineComponent} from 'vue';
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Navigation } from 'vue3-carousel'
import axios from "axios";



export default defineComponent({
  name: 'ChoiceCar',
    components: {
    Carousel,
    Slide,
    Navigation,
  },

  data() {
    return {
      cars_data: {},
      currentSlide: 0
    };
  },
  computed: {
    // Вычисляемое свойство, которое будет возвращать количество отображаемых элементов в зависимости от ширины окна браузера
    itemsToShow() {
      if (window.innerWidth < 768) {
        return 1; // Например, на мобильных устройствах отображаем 1 элемент
      } else if (window.innerWidth < 1024) {
        return 2; // На планшетах отображаем 2 элемента
      } else {
        return 2.5; // На больших экранах отображаем 2.5 элемента
      }
    }
  },
  methods: {
    next() {
      this.$refs.carousel.next()

      if (this.currentSlide + 1 === this.cars_data.cars.length) {
        this.$emit('slide-change', 0);
      }
      else {
        this.$emit('slide-change', this.currentSlide + 1);
      }

    },
    prev() {
      this.$refs.carousel.prev()

      if (this.currentSlide - 1 === -1) {
        this.$emit('slide-change', this.cars_data.cars.length - 1);
      }
      else {
        this.$emit('slide-change', this.currentSlide - 1);
      }

    },
    async getCars() {
      await axios.get('/cars')
        .then((res) => {
          this.cars_data = res.data
          this.$emit('cars_info', this.cars_data);
        })
        .catch((error) => {
          console.error(error);
          // this.cars_data = {}
          // this.$emit('cars_info', this.cars_data);
        });
    },
  },
  created() {
    this.getCars();
  },
});

</script>

<style scoped>

.carousel__viewport {
  perspective: 1000px;

}

.carousel__slide--sliding {
  transition: 0.5s;
}

.carousel__slide {
  padding: 20px;
  width: 100%;
  opacity: 0.9;
  transform: rotateY(-20deg) scale(0.9);
}

.carousel__next {
  opacity: 0;
}

.carousel__prev {
  opacity: 0;
}


.carousel__item {
  width: 90%;
}

@media (max-width: 768px) {
  .carousel__slide {
    padding: 0;
    transform: none;
  }
}

</style>