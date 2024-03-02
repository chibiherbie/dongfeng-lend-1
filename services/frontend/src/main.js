import { createApp } from 'vue'
import './style.css'
import axios from 'axios';
import App from './App.vue'
// import store from './store'; // New

const app = createApp(App);

axios.defaults.withCredentials = false;
axios.defaults.baseURL = 'http://127.0.0.1:5000/';  // the FastAPI backend

app.mount('#app')
