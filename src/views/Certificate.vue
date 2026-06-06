<script setup>
import { ref, reactive } from 'vue'
import { supabase } from '../lib/supabase.js'
import { jsPDF } from 'jspdf'

const form = reactive({ email: '' })
const state = ref('idle') // idle | loading | success | error
const errorMsg = ref('')

const ticketInfo = reactive({ name: '', role: '', ticketId: '', twitter: '', supporting: 'Neutral' })

async function handleSubmit() {
  if (!form.email.trim()) return setError('Please enter your email address.')

  state.value = 'loading'
  errorMsg.value = ''

  const { data, error } = await supabase
    .from('checkins')
    .select('*')
    .eq('email', form.email.trim().toLowerCase())

  if (error) {
    state.value = 'error'
    errorMsg.value = 'Something went wrong. Please try again.'
    return
  }

  if (!data || data.length === 0) {
    state.value = 'error'
    errorMsg.value = 'No check-in found for this email address.'
    return
  }

  const row = data[0]
  const uniqueSuffix = String(row.id).slice(-4).toUpperCase()
  
  ticketInfo.name = row.name
  ticketInfo.role = row.role
  ticketInfo.twitter = row.twitter || ''
  ticketInfo.supporting = row.supporting || 'Neutral'
  ticketInfo.ticketId = `UM-${uniqueSuffix}`

  state.value = 'success'
}

function setError(msg) {
  errorMsg.value = msg
  state.value = 'error'
}

function loadLogo() {
  return new Promise((resolve) => {
    const img = new Image()
    img.src = '/logo.jpg'
    img.onload = () => resolve(img)
    img.onerror = () => resolve(null)
  })
}

async function downloadCertificate() {
  const logoImg = await loadLogo()
  const canvas = document.createElement('canvas')
  canvas.width = 2000
  canvas.height = 1414
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  // 1. Deep Rich Forest Green Radial Gradient Background
  const grad = ctx.createRadialGradient(1000, 707, 100, 1000, 707, 1200)
  grad.addColorStop(0, '#0a321c')
  grad.addColorStop(1, '#03170e')
  ctx.fillStyle = grad
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  // 2. Soccer Field Watermark lines
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.02)'
  ctx.lineWidth = 4
  ctx.strokeRect(100, 100, 1800, 1214)
  
  ctx.beginPath()
  ctx.moveTo(1000, 100)
  ctx.lineTo(1000, 1314)
  ctx.stroke()
  
  ctx.beginPath()
  ctx.arc(1000, 707, 240, 0, Math.PI * 2)
  ctx.stroke()

  // 3. Double Gold Borders
  ctx.strokeStyle = '#e8b84b'
  ctx.lineWidth = 8
  ctx.strokeRect(60, 60, canvas.width - 120, canvas.height - 120)

  ctx.strokeStyle = 'rgba(232, 184, 75, 0.4)'
  ctx.lineWidth = 2
  ctx.strokeRect(85, 85, canvas.width - 170, canvas.height - 170)

  // 4. Ornamental Corner Brackets
  ctx.fillStyle = '#e8b84b'
  // Top-left
  ctx.fillRect(80, 80, 80, 8)
  ctx.fillRect(80, 80, 8, 80)
  // Top-right
  ctx.fillRect(1840, 80, 80, 8)
  ctx.fillRect(1912, 80, 8, 80)
  // Bottom-left
  ctx.fillRect(80, 1326, 80, 8)
  ctx.fillRect(80, 1254, 8, 80)
  // Bottom-right
  ctx.fillRect(1840, 1326, 80, 8)
  ctx.fillRect(1912, 1254, 8, 80)

  // 5. Header: Logo & Club Title
  if (logoImg) {
    ctx.save()
    ctx.beginPath()
    ctx.arc(1000, 150, 60, 0, Math.PI * 2)
    ctx.clip()
    ctx.drawImage(logoImg, 940, 90, 120, 120)
    ctx.restore()
    
    // Gold ring around logo
    ctx.strokeStyle = '#e8b84b'
    ctx.lineWidth = 3
    ctx.beginPath()
    ctx.arc(1000, 150, 60, 0, Math.PI * 2)
    ctx.stroke()
  }

  ctx.fillStyle = '#e8b84b'
  ctx.font = 'bold 28px sans-serif'
  ctx.textAlign = 'center'
  ctx.fillText('U M M A H   T W I T T E R   F O O T B A L L   C L U B', 1000, 265)

  // 6. Certificate Title in Gold Gradient
  const goldGrad = ctx.createLinearGradient(600, 0, 1400, 0)
  goldGrad.addColorStop(0, '#FFE082')
  goldGrad.addColorStop(0.5, '#E8C14A')
  goldGrad.addColorStop(1, '#B89020')
  ctx.fillStyle = goldGrad
  ctx.font = 'bold 84px Georgia, serif'
  ctx.fillText('CERTIFICATE OF ATTENDANCE', 1000, 370)

  // 7. Presentation statement
  ctx.fillStyle = '#FFFFFF'
  ctx.font = 'italic 28px Georgia, serif'
  ctx.fillText('This certificate is proudly presented to', 1000, 480)

  // 8. Name with dynamic scaling
  ctx.fillStyle = '#FFFFFF'
  let nameSize = 80
  ctx.font = `bold ${nameSize}px sans-serif`
  while (ctx.measureText(ticketInfo.name).width > 1400 && nameSize > 36) {
    nameSize -= 4
    ctx.font = `bold ${nameSize}px sans-serif`
  }
  ctx.fillText(ticketInfo.name, 1000, 590)

  // Underline decorative line
  ctx.strokeStyle = '#e8b84b'
  ctx.lineWidth = 3
  ctx.beginPath()
  ctx.moveTo(600, 630)
  ctx.lineTo(1400, 630)
  ctx.stroke()

  // Central diamond on underline
  ctx.fillStyle = '#e8b84b'
  ctx.beginPath()
  ctx.moveTo(1000, 620)
  ctx.lineTo(1012, 630)
  ctx.lineTo(1000, 640)
  ctx.lineTo(988, 630)
  ctx.closePath()
  ctx.fill()

  // 9. Event Description based on role
  ctx.fillStyle = 'rgba(255, 255, 255, 0.85)'
  ctx.font = '26px sans-serif'
  const isPlayer = ticketInfo.role.toLowerCase() === 'player'
  const supportText = ticketInfo.supporting.toLowerCase() === 'neutral'
    ? 'as a neutral observer'
    : `supporting ${ticketInfo.supporting} FC`
  const descLine1 = isPlayer
    ? 'for active participation as a player, demonstrating outstanding teamwork, discipline, and'
    : `for participating as a spectator and loyal community supporter (${supportText}), exhibiting`
  ctx.fillText(descLine1, 1000, 715)
  ctx.fillText('brotherhood, unity, and sportsmanship at the annual Ummah Twitter Match.', 1000, 765)

  // 10. Venue/Date details
  ctx.fillStyle = '#e8b84b'
  ctx.font = 'bold 24px sans-serif'
  ctx.fillText('Saturday, June 6, 2026  ·  Landmark College, Ikorodu', 1000, 850)

  // 11. Signature Block (Left side)
  const sigX = 550
  const sigY = 1070
  ctx.strokeStyle = 'rgba(232, 184, 75, 0.6)'
  ctx.lineWidth = 2
  ctx.beginPath()
  ctx.moveTo(sigX - 180, sigY)
  ctx.lineTo(sigX + 180, sigY)
  ctx.stroke()

  ctx.fillStyle = '#4ba8e8' // Brand cyan
  ctx.font = 'italic 44px cursive, "Brush Script MT", Georgia, serif'
  ctx.fillText('Ummah Twitter FC Committee', sigX, sigY - 20)

  ctx.fillStyle = 'rgba(255, 255, 255, 0.6)'
  ctx.font = '18px sans-serif'
  ctx.fillText('Organizing Committee', sigX, sigY + 30)
  ctx.fillText('Ummah Twitter FC 2026', sigX, sigY + 55)

  // 12. Official Stamp / Gold Seal (Right side)
  const sealX = 1450
  const sealY = 1070

  // Draw Ribbons
  ctx.fillStyle = '#b89020'
  ctx.beginPath()
  ctx.moveTo(sealX - 25, sealY)
  ctx.lineTo(sealX - 45, sealY + 110)
  ctx.lineTo(sealX - 15, sealY + 95)
  ctx.lineTo(sealX + 5, sealY + 110)
  ctx.lineTo(sealX - 5, sealY)
  ctx.closePath()
  ctx.fill()
  
  ctx.beginPath()
  ctx.moveTo(sealX + 5, sealY)
  ctx.lineTo(sealX + 25, sealY + 110)
  ctx.lineTo(sealX - 5, sealY + 95)
  ctx.lineTo(sealX - 25, sealY + 110)
  ctx.lineTo(sealX - 15, sealY)
  ctx.closePath()
  ctx.fill()
  
  // Seal Outer Circle
  ctx.fillStyle = '#FFE082'
  ctx.beginPath()
  ctx.arc(sealX, sealY, 75, 0, Math.PI * 2)
  ctx.fill()
  
  ctx.fillStyle = '#E8C14A'
  ctx.beginPath()
  ctx.arc(sealX, sealY, 68, 0, Math.PI * 2)
  ctx.fill()

  // Seal Rotated Text
  ctx.save()
  ctx.translate(sealX, sealY)
  ctx.fillStyle = '#052014'
  ctx.font = '900 13px sans-serif'
  const sealText = '  OFFICIAL PASS  ·  UMMAH TWITTER MATCH  ·'
  for (let i = 0; i < sealText.length; i++) {
    const angle = (i * 2 * Math.PI) / sealText.length
    ctx.save()
    ctx.rotate(angle)
    ctx.fillText(sealText[i], 0, -50)
    ctx.restore()
  }
  ctx.restore()
  
  if (logoImg) {
    ctx.save()
    ctx.beginPath()
    ctx.arc(sealX, sealY, 42, 0, Math.PI * 2)
    ctx.clip()
    ctx.drawImage(logoImg, sealX - 42, sealY - 42, 84, 84)
    ctx.restore()
  } else {
    ctx.fillStyle = '#052014'
    ctx.font = '36px sans-serif'
    ctx.fillText('⚽', sealX, sealY + 12)
  }

  // 13. Stamped Ticket ID (Center Bottom)
  ctx.fillStyle = 'rgba(232, 184, 75, 0.08)'
  ctx.fillRect(820, 1180, 360, 70)
  ctx.strokeStyle = '#e8b84b'
  ctx.lineWidth = 1.5
  ctx.strokeRect(820, 1180, 360, 70)
  
  ctx.fillStyle = '#e8b84b'
  ctx.font = '14px sans-serif'
  ctx.fillText('VERIFIED TICKET PASS CODE', 1000, 1205)
  
  ctx.fillStyle = '#FFFFFF'
  ctx.font = 'bold 24px sans-serif'
  ctx.fillText(ticketInfo.ticketId, 1000, 1238)

  ctx.textAlign = 'left' // Reset

  // 14. Convert to PDF using jsPDF
  const imgData = canvas.toDataURL('image/png')
  const pdf = new jsPDF({
    orientation: 'landscape',
    unit: 'px',
    format: [2000, 1414]
  })
  pdf.addImage(imgData, 'PNG', 0, 0, 2000, 1414)
  pdf.save(`ummah_fc_certificate_${ticketInfo.ticketId.toLowerCase()}.pdf`)
}
</script>

<template>
  <div class="page">
    <!-- Faint football pitch background -->
    <div class="pitch-bg" aria-hidden="true">
      <svg viewBox="0 0 1000 650" fill="none" stroke="white" stroke-width="1.5" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        <rect x="8" y="8" width="984" height="634"/>
        <line x1="500" y1="8" x2="500" y2="642"/>
        <circle cx="500" cy="325" r="90"/>
        <circle cx="500" cy="325" r="3.5" fill="white" stroke="none"/>
        <rect x="8" y="190" width="158" height="270"/>
        <rect x="8" y="262" width="56" height="126"/>
        <circle cx="118" cy="325" r="3" fill="white" stroke="none"/>
        <circle cx="118" cy="325" r="90" stroke-dasharray="50 520"/>
        <rect x="834" y="190" width="158" height="270"/>
        <rect x="936" y="262" width="56" height="126"/>
        <circle cx="882" cy="325" r="3" fill="white" stroke="none"/>
        <circle cx="882" cy="325" r="90" stroke-dasharray="50 520" transform="rotate(180 500 325)"/>
        <path d="M8,32 A24,24 0 0,1 32,8"/>
        <path d="M968,8 A24,24 0 0,1 992,32"/>
        <path d="M8,618 A24,24 0 0,0 32,642"/>
        <path d="M968,642 A24,24 0 0,0 992,618"/>
      </svg>
    </div>

    <!-- Atmospheric glow -->
    <div class="atmo-glow" aria-hidden="true"></div>

    <!-- Logo -->
    <div class="logo-wrap">
      <img src="/logo.jpg" alt="Ummah Twitter FC Logo" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 2px solid #D4AF37; box-shadow: 0 0 16px rgba(232, 184, 75, 0.28);" />
    </div>

    <!-- Header -->
    <header class="header">
      <div class="event-label">Download Certificate</div>
      <h1>UmmahTwitter<br>Match 2026</h1>
    </header>

    <main>
      <div class="card">
        <Transition name="fade" mode="out-in">
          <!-- Form -->
          <form v-if="state !== 'success'" key="form" @submit.prevent="handleSubmit" novalidate>
            <p class="card-title">Find Your Certificate</p>

            <div class="field">
              <label for="email">Email Used During Check-In <span class="req" aria-hidden="true">*</span></label>
              <input
                v-model="form.email"
                type="email" id="email" name="email"
                placeholder="you@example.com"
                required autocomplete="email" inputmode="email"
              />
            </div>

            <button type="submit" class="btn-submit" :class="{ loading: state === 'loading' }" :disabled="state === 'loading'">
              <span v-if="state !== 'loading'">Find Certificate</span>
              <span v-else class="btn-loading">
                <svg class="spinner" width="16" height="16" viewBox="0 0 16 16" fill="none">
                  <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2" opacity="0.25"/>
                  <path d="M8 2a6 6 0 0 1 6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
                Searching…
              </span>
            </button>

            <Transition name="slide-down">
              <div v-if="state === 'error'" class="error-msg" role="alert" aria-live="polite">
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
                  <circle cx="7" cy="7" r="6" stroke="currentColor" stroke-width="1.5"/>
                  <path d="M7 4v3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                  <circle cx="7" cy="10" r="0.75" fill="currentColor"/>
                </svg>
                {{ errorMsg }}
              </div>
            </Transition>
          </form>

          <!-- Success -->
          <div v-else key="success" class="success-state" aria-live="polite">
            <div class="success-icon" aria-hidden="true">
              <svg width="30" height="30" viewBox="0 0 30 30" fill="none">
                <path d="M6 15.5l7.5 7.5 10.5-13" stroke="#3dd68c" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </div>
            <h2>Record Found!</h2>
            <p>Welcome back, <span class="success-name">{{ ticketInfo.name }}</span>.</p>
            <p class="success-sub" style="margin-bottom: 24px;">Your certificate of attendance is ready to be downloaded.</p>

            <!-- Download Certificate button -->
            <button @click="downloadCertificate" class="btn-download-cert" style="margin-bottom: 1rem;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 0.5rem; display: inline-block; vertical-align: middle;">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                <polyline points="14 2 14 8 20 8"/>
                <line x1="16" x2="8" y1="13" y2="13"/>
                <line x1="16" x2="8" y1="17" y2="17"/>
                <polyline points="10 9 9 9 8 9"/>
              </svg>
              Download Certificate of Participation (PDF)
            </button>
            
            <button @click="state = 'idle'; form.email = ''" class="btn-back" style="margin-bottom: 1rem;">
              Search Another Email
            </button>
          </div>
        </Transition>
      </div>
    </main>

    <footer class="page-footer">
      <p>Football · Banter · Networking</p>
      <p>Ummah Twitter FC · 2026</p>
      <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 10px; flex-wrap: wrap;">
        <router-link to="/" class="qr-link" title="Go home">
          🏠 Home
        </router-link>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.page {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 90px 16px 56px;
  position: relative;
  overflow: hidden;
}

.pitch-bg {
  position: fixed;
  inset: 0;
  opacity: 0.038;
  pointer-events: none;
  z-index: 0;
}
.pitch-bg svg {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.atmo-glow {
  position: fixed;
  top: 0; left: 50%; transform: translateX(-50%);
  width: 700px;
  height: 500px;
  background: radial-gradient(ellipse at 50% 30%, rgba(20, 38, 20, 0.55) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.logo-wrap, .header, main, .page-footer {
  position: relative;
  z-index: 1;
}

.logo-wrap {
  margin-bottom: 22px;
}

.header {
  text-align: center;
  margin-bottom: 24px;
}
.event-label {
  display: inline-block;
  font-size: 10px;
  font-weight: 700;
  letter-spacing: 0.11em;
  text-transform: uppercase;
  color: var(--gold);
  background: rgba(232, 184, 75, 0.08);
  border: 1px solid rgba(232, 184, 75, 0.2);
  padding: 4px 12px;
  border-radius: 999px;
  margin-bottom: 14px;
}
h1 {
  font-size: clamp(28px, 7vw, 40px);
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1.05;
  margin-bottom: 12px;
}

main {
  width: 100%;
  max-width: 520px;
}
.card {
  background: var(--surface);
  border: 1px solid var(--border-mid);
  border-radius: var(--radius-xl);
  padding: 32px 28px 36px;
  position: relative;
  overflow: hidden;
  box-shadow: 0 32px 80px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(255,255,255,0.03);
}
.card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(232,184,75,0.55) 40%, rgba(232,184,75,0.7) 50%, rgba(232,184,75,0.55) 60%, transparent);
}
.card-title {
  font-size: 13px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 24px;
}

.field {
  margin-bottom: 26px;
}
label {
  display: block;
  font-size: 11.5px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  color: var(--muted);
  margin-bottom: 8px;
}
.req {
  color: var(--gold);
  margin-left: 1px;
}
input {
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--border-mid);
  color: var(--text);
  padding: 13px 15px;
  border-radius: var(--radius-sm);
  font-size: 16px;
  font-family: inherit;
  outline: none;
  transition: border-color 0.15s, box-shadow 0.15s;
}
input::placeholder {
  color: var(--dim);
  font-weight: 400;
}
input:focus {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(232, 184, 75, 0.1);
}

.btn-submit {
  width: 100%;
  background: var(--gold);
  color: #0c0900;
  border: none;
  padding: 15px 20px;
  border-radius: var(--radius-sm);
  font-size: 15px;
  font-weight: 700;
  font-family: inherit;
  cursor: pointer;
  letter-spacing: 0.01em;
  transition: background 0.15s, box-shadow 0.15s, transform 0.1s;
}
.btn-submit:hover:not(:disabled) {
  background: #f0c456;
  box-shadow: 0 4px 22px rgba(232, 184, 75, 0.35);
}
.btn-submit:active:not(:disabled) {
  transform: scale(0.985);
}
.btn-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
.btn-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}
.spinner {
  animation: spin 0.7s linear infinite;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}

.error-msg {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 14px;
  padding: 11px 14px;
  background: rgba(240, 68, 68, 0.08);
  border: 1px solid rgba(240, 68, 68, 0.2);
  border-radius: var(--radius-sm);
  color: #f87171;
  font-size: 13px;
  line-height: 1.4;
}

.success-state {
  text-align: center;
  padding: 16px 0 12px;
}
.success-icon {
  width: 66px;
  height: 66px;
  border-radius: 50%;
  background: rgba(61, 214, 140, 0.08);
  border: 1.5px solid rgba(61, 214, 140, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 20px;
  animation: pop 0.35s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}
@keyframes pop {
  from { transform: scale(0.6); opacity: 0; }
  to   { transform: scale(1);   opacity: 1; }
}
.success-state h2 {
  font-size: 26px;
  font-weight: 900;
  letter-spacing: -0.025em;
  margin-bottom: 8px;
}
.success-state p {
  color: var(--muted);
  font-size: 15px;
}
.success-name {
  color: var(--gold);
  font-weight: 700;
}
.success-sub {
  margin-top: 4px;
  font-size: 14px;
}

.btn-download-cert {
  background: transparent;
  color: var(--gold);
  border: 1.5px solid var(--gold);
  padding: 15px 20px;
  border-radius: var(--radius-sm);
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  width: 100%;
  transition: background 0.15s, box-shadow 0.15s, transform 0.1s;
}
.btn-download-cert:hover {
  background: rgba(232, 184, 75, 0.08);
  box-shadow: 0 4px 22px rgba(232, 184, 75, 0.15);
}
.btn-download-cert:active {
  transform: scale(0.985);
}

.btn-back {
  background: transparent;
  color: var(--muted);
  border: none;
  padding: 10px 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  width: 100%;
  text-decoration: underline;
}

.page-footer {
  margin-top: 28px;
  text-align: center;
  color: var(--dim);
  font-size: 12px;
  line-height: 1.8;
  letter-spacing: 0.02em;
}
.qr-link {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  margin-top: 10px;
  color: var(--dim);
  text-decoration: none;
  font-size: 11.5px;
  font-weight: 500;
  padding: 5px 10px;
  border: 1px solid var(--border);
  border-radius: 999px;
  transition: color 0.15s, border-color 0.15s;
}
.qr-link:hover {
  color: var(--muted);
  border-color: var(--border-mid);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-down-enter-active {
  transition: all 0.2s ease;
}
.slide-down-enter-from {
  opacity: 0;
  transform: translateY(-6px);
}
</style>
