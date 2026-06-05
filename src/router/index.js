import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import CheckIn from '../views/CheckIn.vue'
import Admin from '../views/Admin.vue'
import QR from '../views/QR.vue'

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/register', component: CheckIn },
    { path: '/admin', component: Admin },
    { path: '/qr', component: QR },
  ],
})
