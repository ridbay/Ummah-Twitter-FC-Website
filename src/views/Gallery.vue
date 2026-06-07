<script setup>
import { ref, reactive } from 'vue'

const imageIds = ['1-Q70kD590ss-wpwLhpcD5oSBE__NvJVE', '1kVo_UDtCLkK5mPXg2-zFzifi7A7gPXVM', '1N3Y6j1l8JmBQ-aoizrOKmOoXy6z_G85q', '1HsqBA2bkLsGyPl9cE9YxzWXHQGf3a-FO', '1O8jiLypAeTbesvRkRS8-txhMrEKJdNgI', '12-XGRipgQvF-358mqPl6sRylFpkb8obS', '1yPvJ5MhSFSoWs8i6LWTkFwf0lDDMn2yO', '1jbQyr4JdWOAjuf9_LfX2VApdfqIURaRM', '1PZLqGm0O1DbUSyPGZi6UtsK7w1WeA7ic', '1NUyRSH9XYotGJfvkxax_3vU0k-6Vpss5', '1pTRxt7SM8LI3rVucMH5bHJIwu6hwgyWw', '13CV1y4kb8CYc3eM3QGNMdph4m1sHHH-q', '1L4GZUdwNvptSWabP9VVkQEpEnXDFs8ar', '1UNBsdReDzUnLbNLbowzA_Kycj-7yGwV5', '1qQ3fbGebEqKGabin71BnZjj8Rh5-yQN4', '1PHEqsh-L6kBBw6M8OawIQXy1QPlaowN3', '1JvgFGfvyjRVaIrRW7JxmKzpxZp2qWY9e', '1nNk0XqeswU9ooq_QZ_-sFr-wdaDhEAVs', '1U9Mpxnd_Hs8QO8NTzzNebl04HN-TlEox', '1wPL77G4hyi4qRtT8JMWHNlAgKk8idpWa', '1Pi6Op458sXwO2zx2XbeN7YoOu7aD7g1E', '1G3LkNtcjY1Sq7OolHaT5nmoWTEZZvdw7', '1EAk9wSsrDRECsJ95Pa9lPw82XHaBEPqm', '1AsQrZXU3cuQdw3Kj9cJrvzE5yc872QyN', '1XVw8FXpLesW9rSGKM575nrBVUIcPjty3', '1JDTqCtWY5mFqSoJqj9uM88ETWatgWhMN', '1urq3UruzcpQ1wAI2CiPGzLSx0rqi_r4K', '16AwKMCE3ZOve7qYBJthuMSv3Q1Tsw-Np', '1ltmKKhuaHLvk-pYwwoH6gkZqiGTXdBMl', '1KzmCO-zB-R3l5bWQ5icxnhlrNqvpPea3', '1mpsvzPMxhT6_hnMYPEnIa0vEjdyG1Raz', '1f7ZNBHtXE22TE6uWR2NNvJiN3rOqWXpC', '110mR1P5VtuRLM_poiE9-Syioo1jDubZS', '1utMeVIfIxAgbE2iYRpFi4sjs8q9flSj6', '1UomhsvdqGFSnJpYk3AkLiIQsKEfOqjP7', '1vsu6S14NPiCDUw6IghJDv58sEAneAa2q', '1MMHMnjoP9zUWeSJFdr_0L8dEVmzmRP0h', '1GPj-UOi_Qyyyw65xYlEGslKDg5YcRBTQ', '168bJWc4qvNh2M1ftf3BHMjz7tOtnHfDv', '1GBbBIgSV4A_SAC4oRWcO6mbJRkhEXtKy', '1VmfuHoAb9qM9MPYvkske3mjRhIV0X8Lf', '1OAe0GgRspsJpEqA07dTRMS7n8ZTSX039', '1UHxxozR3Mapszgl25czFUeEunDEQrC9i', '1BdfXm5atXScO9KHQSDRiZdHiK8Jt_Mr-', '1MiV8bnXr75run_SbBpflB2hXVcB_426F', '19fMQ5meYjriCfSnqIdpu3xoSVp-bXBf1', '1UkJs7LAUbX5gNzKIYImEi4vLAyZjkd7D', '1th_WGFVNAfNaxJeiU5ZbTAIadE8SMXcb', '1sFO3ew-qhPXbLGrYGDdNfNvGKqug5tH2', '1pmrt2SeRcoi18cZ8wfgf2GiDIWlkHAbA']

const selectedImage = ref(null)
const loadedImages = reactive({})

function onImageLoad(id) {
  loadedImages[id] = true
}

function getImageUrl(id) {
  return `https://lh3.googleusercontent.com/d/${id}`
}

function openLightbox(url) {
  selectedImage.value = url
}

function closeLightbox() {
  selectedImage.value = null
}
</script>

<template>
  <div class="page">
    <header class="gallery-header">
      <div class="container">
        <h1 class="gallery-title">Event Gallery</h1>
        <p class="gallery-subtitle">Relive the moments from the Ummah Twitter FC 2026 Match.</p>
      </div>
    </header>

    <main class="container gallery-main">
      <div class="gallery-grid">
        <div 
          v-for="id in imageIds" 
          :key="id" 
          class="gallery-item"
          @click="openLightbox(getImageUrl(id))"
        >
          <!-- Loader overlay -->
          <div v-if="!loadedImages[id]" class="image-loader">
            <svg class="spinner" width="32" height="32" viewBox="0 0 16 16" fill="none" style="animation: spin 1s linear infinite; color: #D4AF37;">
              <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2" opacity="0.25"/>
              <path d="M8 2a6 6 0 0 1 6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </div>

          <img 
            :src="getImageUrl(id)" 
            loading="lazy" 
            alt="Event moment" 
            class="gallery-img" 
            @load="onImageLoad(id)"
            :style="{ opacity: loadedImages[id] ? 1 : 0 }"
          />
          <div class="overlay">
            <svg class="zoom-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="11" cy="11" r="8"/>
              <line x1="21" y1="21" x2="16.65" y2="16.65"/>
              <line x1="11" y1="8" x2="11" y2="14"/>
              <line x1="8" y1="11" x2="14" y2="11"/>
            </svg>
          </div>
        </div>
      </div>
      
      <div style="text-align: center; margin-top: 3rem;">
        <a href="https://drive.google.com/drive/folders/1KMVb7lrMoKbD7w0u86yI0bwiwEYwTcF-?usp=sharing" target="_blank" rel="noopener noreferrer" class="btn-external">
          View all in Google Drive
          <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1rem; height: 1rem; margin-left: 0.5rem;">
            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
            <polyline points="15 3 21 3 21 9"/>
            <line x1="10" x2="21" y1="14" y2="3"/>
          </svg>
        </a>
      </div>
    </main>

    <!-- Lightbox Modal -->
    <transition name="fade">
      <div v-if="selectedImage" class="lightbox" @click="closeLightbox">
        <button class="lightbox-close" @click="closeLightbox" aria-label="Close image">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"/>
            <line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
        <img :src="selectedImage" alt="Expanded event moment" class="lightbox-img" @click.stop />
      </div>
    </transition>
  </div>
</template>

<style scoped>
.page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: #052014;
  color: #F8FAFC;
  padding-top: 90px;
}

.gallery-header {
  padding: 4rem 1.5rem;
  text-align: center;
  border-bottom: 1px solid #27523d;
  background: linear-gradient(to bottom, rgba(39, 82, 61, 0.1), transparent);
}

.gallery-title {
  font-size: 3rem;
  font-weight: 900;
  margin-bottom: 1rem;
  color: #FFFFFF;
}

.gallery-subtitle {
  font-size: 1.125rem;
  color: rgba(248, 250, 252, 0.8);
  max-width: 600px;
  margin: 0 auto;
}

.gallery-main {
  padding: 3rem 1.5rem 5rem;
  flex: 1;
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 1200px;
  margin: 0 auto;
}

.gallery-item {
  position: relative;
  aspect-ratio: 4 / 3;
  border-radius: 12px;
  overflow: hidden;
  cursor: pointer;
  background-color: rgba(39, 82, 61, 0.3);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
}

.gallery-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.gallery-item:hover .gallery-img {
  transform: scale(1.05);
}

.overlay {
  position: absolute;
  inset: 0;
  background: rgba(5, 32, 20, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.gallery-item:hover .overlay {
  opacity: 1;
}

.zoom-icon {
  width: 48px;
  height: 48px;
  color: #D4AF37;
  transform: scale(0.8);
  transition: transform 0.3s ease;
}

.gallery-item:hover .zoom-icon {
  transform: scale(1);
}

.image-loader {
  position: absolute;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(39, 82, 61, 0.1);
}

.btn-external {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  background-color: #27523d;
  color: #FFFFFF;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  text-decoration: none;
  font-weight: 600;
  transition: background-color 0.2s, color 0.2s;
}

.btn-external:hover {
  background-color: #D4AF37;
  color: #052014;
}

/* Lightbox styles */
.lightbox {
  position: fixed;
  inset: 0;
  z-index: 9999;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  backdrop-filter: blur(8px);
}

.lightbox-img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  border-radius: 8px;
  box-shadow: 0 0 40px rgba(0, 0, 0, 0.5);
}

.lightbox-close {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #fff;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: background 0.2s;
  z-index: 10000;
}

.lightbox-close:hover {
  background: rgba(255, 255, 255, 0.2);
}

.lightbox-close svg {
  width: 24px;
  height: 24px;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>
