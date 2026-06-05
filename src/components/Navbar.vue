<script setup>
import { ref } from 'vue'

const isMobileMenuOpen = ref(false)

function toggleMobileMenu() {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}

function closeMobileMenu() {
  isMobileMenuOpen.value = false
}
</script>

<template>
  <nav class="navbar">
    <div class="container navbar-container">
      <!-- Brand Logo -->
      <router-link to="/" class="brand" @click="closeMobileMenu">
        <img src="/logo.jpg" alt="Ummah Twitter FC Logo" style="width: 32px; height: 32px; border-radius: 50%; object-fit: cover; border: 1px solid #D4AF37; flex-shrink: 0;" />
        <div>
          <span class="brand-title">UMMAH TWITTER FC</span>
          <span class="brand-subtitle">Brotherhood Beyond the Pitch</span>
        </div>
      </router-link>
      
      <!-- Desktop Navigation Links -->
      <div class="nav-links">
        <router-link to="/" class="nav-link-a">Home</router-link>
        <router-link to="/about" class="nav-link-a">About</router-link>
        <router-link to="/schedule" class="nav-link-a">Schedule</router-link>
        <router-link to="/register" class="nav-link-a">Check In</router-link>
        <router-link to="/qr" class="nav-link-a">QR Code</router-link>
        <a href="https://www.google.com/maps/place/Landmark+College,+Ikorodu/data=!4m2!3m1!1s0x0:0x5f683c00ec0c6aeb?sa=X&ved=1t:2428&ictx=111" target="_blank" rel="noopener noreferrer" class="nav-link-a">
          Directions ↗
        </a>
      </div>

      <!-- Action Button (Desktop Only) -->
      <div class="nav-actions">
        <router-link to="/register" class="gold-button">
          Get Spectator Pass
        </router-link>
      </div>

      <!-- Mobile Hamburger Button -->
      <button class="hamburger-btn" @click="toggleMobileMenu" aria-label="Toggle Navigation Menu">
        <svg v-if="!isMobileMenuOpen" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="4" x2="20" y1="12" y2="12"/>
          <line x1="4" x2="20" y1="6" y2="6"/>
          <line x1="4" x2="20" y1="18" y2="18"/>
        </svg>
        <svg v-else width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" x2="6" y1="6" y2="18"/>
          <line x1="6" x2="18" y1="6" y2="18"/>
        </svg>
      </button>
    </div>

    <!-- Mobile Navigation Dropdown Menu -->
    <transition name="slide-down">
      <div v-if="isMobileMenuOpen" class="mobile-menu">
        <router-link to="/" class="mobile-menu-item" @click="closeMobileMenu">Home</router-link>
        <router-link to="/about" class="mobile-menu-item" @click="closeMobileMenu">About</router-link>
        <router-link to="/schedule" class="mobile-menu-item" @click="closeMobileMenu">Game Schedule</router-link>
        <router-link to="/register" class="mobile-menu-item" @click="closeMobileMenu">Spectator Check In</router-link>
        <router-link to="/qr" class="mobile-menu-item" @click="closeMobileMenu">Event QR Code</router-link>
        <a href="https://www.google.com/maps/place/Landmark+College,+Ikorodu/data=!4m2!3m1!1s0x0:0x5f683c00ec0c6aeb?sa=X&ved=1t:2428&ictx=111" target="_blank" rel="noopener noreferrer" class="mobile-menu-item" @click="closeMobileMenu">
          Directions ↗
        </a>
        <div style="padding: 1.5rem 1rem;">
          <router-link to="/register" class="gold-button" style="width: 100%; padding: 0.875rem;" @click="closeMobileMenu">
            Get Spectator Pass
          </router-link>
        </div>
      </div>
    </transition>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background-color: rgba(5, 32, 20, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid #27523d;
}

.navbar-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  text-decoration: none;
}

.brand-title {
  font-weight: 900;
  font-size: 1.25rem;
  letter-spacing: 0.05em;
  background: linear-gradient(to right, #F3C64F, #A07817);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: block;
  line-height: 1;
}

.brand-subtitle {
  font-size: 9px;
  letter-spacing: 0.15em;
  color: rgba(212, 175, 55, 0.8);
  font-weight: 700;
  display: block;
  text-transform: uppercase;
  margin-top: 0.125rem;
}

/* Nav Links */
.nav-links {
  display: none;
}

@media (min-width: 1024px) {
  .nav-links {
    display: flex;
    align-items: center;
    gap: 2rem;
    font-size: 0.875rem;
    font-weight: 600;
    letter-spacing: 0.025em;
  }
}

.nav-link-a {
  color: #F8FAFC;
  text-decoration: none;
  font-weight: 500;
  transition: color 0.2s;
}

.nav-link-a:hover,
.router-link-active.nav-link-a {
  color: #D4AF37;
}

.nav-actions {
  display: none;
}

@media (min-width: 1024px) {
  .nav-actions {
    display: block;
  }
}

/* Hamburger Button */
.hamburger-btn {
  background: none;
  border: none;
  color: #F8FAFC;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem;
  transition: color 0.2s;
}

.hamburger-btn:hover {
  color: #D4AF37;
}

@media (min-width: 1024px) {
  .hamburger-btn {
    display: none;
  }
}

/* Gold Button */
.gold-button {
  background: linear-gradient(135deg, #F3C64F 0%, #D4AF37 50%, #B89020 100%);
  color: #052014;
  border: none;
  border-radius: 999px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.25);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  padding: 0.625rem 1.25rem;
}

.gold-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
  background: linear-gradient(135deg, #FFE082 0%, #E8C14A 50%, #CFA52D 100%);
}

.gold-button:active {
  transform: translateY(1px);
}

/* Mobile Menu Dropdown */
.mobile-menu {
  background-color: #052014;
  border-bottom: 1px solid #27523d;
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 90;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
  padding: 1rem 0;
}

.mobile-menu-item {
  color: #F8FAFC;
  text-decoration: none;
  font-size: 1rem;
  font-weight: 600;
  padding: 1rem 2rem;
  border-bottom: 1px solid rgba(39, 82, 61, 0.3);
  transition: background-color 0.2s, color 0.2s;
}

.mobile-menu-item:hover,
.router-link-active.mobile-menu-item {
  background-color: rgba(39, 82, 61, 0.3);
  color: #D4AF37;
}

/* Transition */
.slide-down-enter-active,
.slide-down-leave-active {
  transition: transform 0.3s ease, opacity 0.3s ease;
}

.slide-down-enter-from,
.slide-down-leave-to {
  transform: translateY(-20px);
  opacity: 0;
}

.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  max-width: 1280px;
}
</style>
