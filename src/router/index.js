import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import CheckIn from '../views/CheckIn.vue'
import Admin from '../views/Admin.vue'
import QR from '../views/QR.vue'
import Schedule from '../views/Schedule.vue'
import Certificate from '../views/Certificate.vue'

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/about', component: About },
    { path: '/register', component: CheckIn },
    { path: '/admin', component: Admin },
    { path: '/qr', component: QR },
    { path: '/schedule', component: Schedule },
    { path: '/certificate', component: Certificate },
  ],
})
