import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router"
import '@fortawesome/fontawesome-free/js/all'


createApp(App).use(router).mount('#app')
