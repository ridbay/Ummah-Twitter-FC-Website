<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Navbar from './components/Navbar.vue'

const route = useRoute()
const showNavbar = computed(() => {
  return route.path !== '/admin'
})
</script>

<template>
  <div class="app-layout">
    <Navbar v-if="showNavbar" class="no-print" />
    <RouterView />
  </div>
</template>

<style>
@media print {
  .no-print {
    display: none !important;
  }
}
</style>
