<script setup>
import { ref, onMounted } from 'vue'
import QRCode from 'qrcode'

const qrDataUrl = ref('')
const checkinUrl = window.location.origin + '/'

onMounted(async () => {
  qrDataUrl.value = await QRCode.toDataURL(checkinUrl, {
    width: 320,
    margin: 2,
    color: { dark: '#0d0d14', light: '#ffffff' },
  })
})

function print() {
  window.print()
}
</script>

<template>
  <div class="qr-page">

    <div class="no-print top-nav">
      <router-link to="/" class="back-link">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true">
          <path d="M10 3L5 8l5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Check-in form
      </router-link>
      <button @click="print" class="btn-print">
        <svg width="15" height="15" viewBox="0 0 15 15" fill="none" aria-hidden="true">
          <rect x="3" y="1" width="9" height="7" rx="1" stroke="currentColor" stroke-width="1.5"/>
          <path d="M3 10H1.5A.5.5 0 0 1 1 9.5v-4A.5.5 0 0 1 1.5 5h12a.5.5 0 0 1 .5.5v4a.5.5 0 0 1-.5.5H12" stroke="currentColor" stroke-width="1.5"/>
          <rect x="3" y="9" width="9" height="5" rx="1" stroke="currentColor" stroke-width="1.5"/>
        </svg>
        Print / Save
      </button>
    </div>

    <div class="card">
      <div class="logo-row" aria-hidden="true">
        <svg width="40" height="40" viewBox="0 0 52 52" fill="none">
          <circle cx="26" cy="26" r="25" stroke="#e8b84b" stroke-width="1.5" fill="none" opacity="0.45"/>
          <circle cx="26" cy="26" r="19" stroke="#e8b84b" stroke-width="1" fill="none" opacity="0.25"/>
          <path d="M26 14a12 12 0 1 0 0 24 10 10 0 1 1 0-24z" fill="#e8b84b" opacity="0.88"/>
          <polygon points="30,20 31,23.5 34.5,23.5 31.8,25.5 32.8,29 30,27 27.2,29 28.2,25.5 25.5,23.5 29,23.5" fill="#e8b84b"/>
        </svg>
      </div>

      <h1>UmmahTwitter Match 2026</h1>
      <p class="subtitle">Scan to register for the event</p>

      <div class="qr-wrap">
        <img v-if="qrDataUrl" :src="qrDataUrl" alt="Check-in QR code" class="qr-img" width="320" height="320"/>
        <div v-else class="qr-placeholder" aria-hidden="true"></div>
      </div>

      <p class="url-label">{{ checkinUrl }}</p>

      <div class="event-meta">
        <span>Saturday, June 6 · 8:00 AM</span>
        <span class="sep">·</span>
        <span>Landmark International School, Ikorodu Lagos</span>
      </div>
    </div>

  </div>
</template>

<style scoped>
.qr-page {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 24px 16px 48px;
  background: var(--bg);
}

/* ── Top nav ── */
.top-nav {
  position: fixed;
  top: 0; left: 0; right: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 20px;
  background: rgba(8, 8, 14, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  z-index: 10;
}

.back-link {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--muted);
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  transition: color 0.15s;
}

.back-link:hover { color: var(--text); }

.btn-print {
  display: flex;
  align-items: center;
  gap: 7px;
  background: transparent;
  border: 1px solid var(--border-mid);
  color: var(--muted);
  padding: 7px 14px;
  border-radius: var(--radius-sm);
  font-size: 12.5px;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: color 0.15s, border-color 0.15s;
}

.btn-print:hover {
  color: var(--text);
  border-color: var(--muted);
}

/* ── Card ── */
.card {
  margin-top: 60px;
  width: 100%;
  max-width: 440px;
  background: var(--surface);
  border: 1px solid var(--border-mid);
  border-radius: var(--radius-xl);
  padding: 40px 32px 36px;
  text-align: center;
  box-shadow: 0 32px 80px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(255,255,255,0.03);
  position: relative;
}

.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(232,184,75,0.55) 40%, rgba(232,184,75,0.7) 50%, rgba(232,184,75,0.55) 60%, transparent);
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
}

.logo-row {
  display: flex;
  justify-content: center;
  margin-bottom: 16px;
  filter: drop-shadow(0 0 14px rgba(232, 184, 75, 0.28));
}

h1 {
  font-size: 20px;
  font-weight: 900;
  letter-spacing: -0.025em;
  margin-bottom: 6px;
}

.subtitle {
  color: var(--muted);
  font-size: 13.5px;
  margin-bottom: 28px;
}

/* ── QR ── */
.qr-wrap {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.qr-img {
  border-radius: 12px;
  display: block;
  width: 260px;
  height: 260px;
}

.qr-placeholder {
  width: 260px;
  height: 260px;
  border-radius: 12px;
  background: var(--surface);
  border: 1px solid var(--border-mid);
  animation: pulse 1.4s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.5; }
  50%       { opacity: 1; }
}

.url-label {
  font-size: 12px;
  color: var(--dim);
  font-family: monospace;
  letter-spacing: 0.02em;
  margin-bottom: 20px;
  word-break: break-all;
}

.event-meta {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 4px 8px;
  font-size: 12px;
  color: var(--muted);
  line-height: 1.6;
}

.sep { color: var(--border-mid); }

/* ── Print styles ── */
@media print {
  .no-print { display: none !important; }

  .qr-page {
    background: #fff;
    padding: 0;
    justify-content: flex-start;
  }

  .card {
    margin-top: 0;
    max-width: 100%;
    border: none;
    box-shadow: none;
    background: #fff;
    color: #000;
    padding: 40px 20px;
  }

  .card::before { display: none; }

  h1, .subtitle, .url-label, .event-meta { color: #000 !important; }

  .qr-img {
    width: 300px;
    height: 300px;
  }
}
</style>
