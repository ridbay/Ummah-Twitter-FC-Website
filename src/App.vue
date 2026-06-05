<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

const route = useRoute()
const showChrome = computed(() => route.path !== '/admin')
</script>

<template>
  <div class="app-layout">
    <Navbar v-if="showChrome" class="no-print" />
    <RouterView />
    <Footer v-if="showChrome" />
  </div>
</template>

<style>
@media print {
  .no-print {
    display: none !important;
  }
}
</style>
