import { createApp } from 'vue'
import PrimeVue from 'primevue/config';
import "primevue/resources/themes/saga-blue/theme.css"; //theme
import "primevue/resources/primevue.min.css"; //core CSS
// import "primeicons/primeicons.css"; //icons
import './style.css'
import axios from 'axios';



import App from './App.vue'
// import store from './store'; // New

const app = createApp(App);

// app.use(PrimeVue, {
//     unstyled: true
// });

axios.defaults.withCredentials = false;
axios.defaults.baseURL = 'http://127.0.0.1:5000/';  // the FastAPI backend

app.mount('#app')
