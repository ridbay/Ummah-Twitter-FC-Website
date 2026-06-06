<script setup>
import { ref, reactive } from 'vue'
import { supabase } from '../lib/supabase.js'
import { jsPDF } from 'jspdf'

const form = reactive({ name: '', twitter: '', email: '', role: 'Fan', supporting: 'Neutral' })
const state = ref('idle') // idle | loading | success | error
const errorMsg = ref('')
const isDuplicateEmail = ref(false)
const successName = ref('')

const ticketInfo = reactive({ name: '', role: '', ticketId: '', twitter: '', supporting: 'Neutral' })

async function handleSubmit() {
  if (!form.name.trim())  return setError('Please enter your full name.')
  if (!form.email.trim()) return setError('Please enter your email address.')

  state.value = 'loading'
  errorMsg.value = ''

  const twitter = form.twitter.trim().replace(/^@+/, '')

  const { data, error } = await supabase.from('checkins').insert({
    name:       form.name.trim(),
    twitter:    twitter ? `@${twitter}` : null,
    email:      form.email.trim().toLowerCase(),
    role:       form.role,
    supporting: form.supporting,
  }).select()

  if (error) {
    state.value = 'error'
    if (error.code === '23505') {
      errorMsg.value = 'This email address is already registered.'
      isDuplicateEmail.value = true
    } else {
      errorMsg.value = 'Something went wrong. Please try again.'
      isDuplicateEmail.value = false
    }
    return
  }
  isDuplicateEmail.value = false

  const insertedRow = data && data[0]
  const uniqueSuffix = insertedRow ? String(insertedRow.id).slice(-4).toUpperCase() : Math.floor(1000 + Math.random() * 9000)
  
  ticketInfo.name = form.name.trim()
  ticketInfo.role = form.role
  ticketInfo.twitter = twitter ? `@${twitter}` : ''
  ticketInfo.supporting = form.supporting
  ticketInfo.ticketId = `UM-${uniqueSuffix}`

  successName.value = form.name.trim().split(' ')[0]
  state.value = 'success'
}

function setError(msg) {
  errorMsg.value = msg
  state.value = 'error'
  isDuplicateEmail.value = false
}

function loadLogo() {
  return new Promise((resolve) => {
    const img = new Image()
    img.src = '/logo.jpg'
    img.onload = () => resolve(img)
    img.onerror = () => resolve(null)
  })
}

async function downloadTicket() {
  const logoImg = await loadLogo()
  const canvas = document.createElement('canvas')
  canvas.width = 1200
  canvas.height = 675
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  // 1. Forest Green Background
  ctx.fillStyle = '#052014'
  ctx.fillRect(0, 0, canvas.width, canvas.height)

  // 2. Soccer watermark/circles
  ctx.strokeStyle = 'rgba(212, 175, 55, 0.04)'
  ctx.lineWidth = 4
  ctx.beginPath()
  ctx.arc(canvas.width - 200, canvas.height / 2, 220, 0, Math.PI * 2)
  ctx.stroke()
  
  ctx.beginPath()
  ctx.arc(canvas.width - 200, canvas.height / 2, 150, 0, Math.PI * 2)
  ctx.stroke()

  ctx.beginPath()
  ctx.arc(canvas.width - 200, canvas.height / 2, 80, 0, Math.PI * 2)
  ctx.stroke()

  // 3. Gold border
  ctx.strokeStyle = '#e8b84b'
  ctx.lineWidth = 6
  ctx.strokeRect(30, 30, canvas.width - 60, canvas.height - 60)

  // 4. Inner green border
  ctx.strokeStyle = '#27523d'
  ctx.lineWidth = 2
  ctx.strokeRect(45, 45, canvas.width - 90, canvas.height - 90)

  // 5. Ticket Cutouts
  ctx.fillStyle = '#08080e' // Match background outside ticket
  ctx.beginPath()
  ctx.arc(45, canvas.height / 2, 40, 0, Math.PI * 2)
  ctx.fill()
  ctx.strokeStyle = '#e8b84b'
  ctx.lineWidth = 4
  ctx.beginPath()
  ctx.arc(45, canvas.height / 2, 40, -Math.PI/2, Math.PI/2)
  ctx.stroke()

  ctx.fillStyle = '#08080e'
  ctx.beginPath()
  ctx.arc(canvas.width - 45, canvas.height / 2, 40, 0, Math.PI * 2)
  ctx.fill()
  ctx.strokeStyle = '#e8b84b'
  ctx.lineWidth = 4
  ctx.beginPath()
  ctx.arc(canvas.width - 45, canvas.height / 2, 40, Math.PI/2, -Math.PI/2)
  ctx.stroke()

  // 6. Dashed separator
  ctx.strokeStyle = 'rgba(232, 184, 75, 0.3)'
  ctx.lineWidth = 4
  ctx.setLineDash([15, 10])
  ctx.beginPath()
  ctx.moveTo(canvas.width - 320, 60)
  ctx.lineTo(canvas.width - 320, canvas.height - 60)
  ctx.stroke()
  ctx.setLineDash([])

  // 7. Headers
  if (logoImg) {
    ctx.save()
    ctx.beginPath()
    ctx.arc(110, 90, 30, 0, Math.PI * 2)
    ctx.clip()
    ctx.drawImage(logoImg, 80, 60, 60, 60)
    ctx.restore()

    ctx.strokeStyle = '#e8b84b'
    ctx.lineWidth = 2
    ctx.beginPath()
    ctx.arc(110, 90, 30, 0, Math.PI * 2)
    ctx.stroke()
  }

  ctx.fillStyle = '#FFFFFF'
  ctx.font = 'bold 36px sans-serif'
  ctx.fillText('UMMAH TWITTER FC', logoImg ? 160 : 80, 102)

  ctx.fillStyle = '#e8b84b'
  ctx.font = 'bold 20px sans-serif'
  ctx.fillText('OFFICIAL SPECTATOR ENTRY PASS', 80, 140)

  // 8. Name with dynamic font scaling to fit the ticket area
  ctx.fillStyle = '#FFFFFF'
  let nameFontSize = 56
  ctx.font = `bold ${nameFontSize}px sans-serif`
  while (ctx.measureText(ticketInfo.name).width > 700 && nameFontSize > 24) {
    nameFontSize -= 4
    ctx.font = `bold ${nameFontSize}px sans-serif`
  }
  ctx.fillText(ticketInfo.name, 80, 260)

  // 9. Role Badge
  const roleText = ticketInfo.role.toUpperCase()
  ctx.fillStyle = '#0a2d1d'
  ctx.fillRect(80, 300, 160, 48)
  ctx.strokeStyle = '#27523d'
  ctx.lineWidth = 2
  ctx.strokeRect(80, 300, 160, 48)

  ctx.fillStyle = '#e8b84b'
  ctx.font = 'bold 22px sans-serif'
  ctx.textAlign = 'center'
  ctx.fillText(roleText, 160, 332)
  ctx.textAlign = 'left' // Reset

  // 9b. Supporting Team Badge
  const teamText = `SUPPORTING: ${ticketInfo.supporting.toUpperCase()}`
  ctx.fillStyle = '#0a2d1d' // Default green
  let teamTextColor = '#FFFFFF'
  
  if (ticketInfo.supporting.toLowerCase() === 'neutral') {
    ctx.fillStyle = '#1a1a26'
    teamTextColor = '#9898b0'
  } else if (ticketInfo.supporting.toLowerCase() === 'aliy') {
    ctx.fillStyle = '#2b220c'
    teamTextColor = '#e8b84b'
  } else if (ticketInfo.supporting.toLowerCase() === 'abubakar') {
    ctx.fillStyle = '#0c2236'
    teamTextColor = '#4ba8e8'
  } else if (ticketInfo.supporting.toLowerCase() === 'umar') {
    ctx.fillStyle = '#22222a'
    teamTextColor = '#9898b0'
  } else if (ticketInfo.supporting.toLowerCase() === 'uthman') {
    ctx.fillStyle = '#0a3220'
    teamTextColor = '#3dd68c'
  }
  
  ctx.fillRect(260, 300, 260, 48)
  ctx.strokeStyle = '#27523d'
  ctx.lineWidth = 2
  ctx.strokeRect(260, 300, 260, 48)
  
  ctx.fillStyle = teamTextColor
  ctx.font = 'bold 18px sans-serif'
  ctx.textAlign = 'center'
  ctx.fillText(teamText, 390, 330)
  ctx.textAlign = 'left' // Reset

  // 9c. Twitter Handle (shifted right to X = 540)
  if (ticketInfo.twitter) {
    // Draw small X (Twitter) logo
    const xLogo = new Path2D('M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z')
    
    ctx.save()
    ctx.translate(540, 310) // Position the logo vertically centered with baseline
    ctx.fillStyle = '#4ba8e8'
    ctx.fill(xLogo)
    ctx.restore()

    ctx.fillStyle = '#4ba8e8'
    ctx.font = 'bold 22px sans-serif'
    ctx.fillText(ticketInfo.twitter, 572, 332)
  }

  // 10. Info details
  ctx.fillStyle = 'rgba(248, 250, 252, 0.75)'
  ctx.font = '24px sans-serif'
  ctx.fillText('📅 Saturday, June 6, 2026', 80, 420)
  ctx.fillText('📍 Landmark College, Ikorodu', 80, 470)
  ctx.fillText('⏰ 8:00 AM Prompt', 80, 520)

  // 11. Stub details (Centered inside the right ticket stub, X=1025)
  ctx.textAlign = 'center'
  
  ctx.fillStyle = '#e8b84b'
  ctx.font = 'bold 20px sans-serif'
  ctx.fillText('TICKET CODE', 1025, 220)

  ctx.fillStyle = '#FFFFFF'
  ctx.font = 'bold 44px sans-serif'
  ctx.fillText(ticketInfo.ticketId, 1025, 280)

  ctx.fillStyle = 'rgba(248, 250, 252, 0.5)'
  ctx.font = '14px sans-serif'
  ctx.fillText('Scan at the gates for entry', 1025, 320)

  // Barcode graphics centered
  const barcodeWidth = 220
  const barcodeHeight = 80
  const barcodeX = 1025 - (barcodeWidth / 2)
  const barcodeY = 360
  
  ctx.fillStyle = 'rgba(232, 184, 75, 0.15)'
  ctx.fillRect(barcodeX, barcodeY, barcodeWidth, barcodeHeight)
  
  ctx.fillStyle = '#052014'
  let lineOffset = 10
  while (lineOffset < barcodeWidth - 10) {
    const lineWidth = Math.floor(Math.random() * 5) + 2
    ctx.fillRect(barcodeX + lineOffset, barcodeY + 5, lineWidth, barcodeHeight - 10)
    lineOffset += lineWidth + Math.floor(Math.random() * 6) + 3
  }

  ctx.fillStyle = '#e8b84b'
  ctx.font = 'bold 12px sans-serif'
  ctx.fillText('BROTHERHOOD BEYOND THE PITCH', 1025, 580)
  
  ctx.textAlign = 'left' // Reset

  // Download Action
  const image = canvas.toDataURL('image/png')
  const link = document.createElement('a')
  link.download = `ummah_fc_pass_${ticketInfo.ticketId.toLowerCase()}.png`
  link.href = image
  link.click()
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
        <!-- Left penalty box -->
        <rect x="8" y="190" width="158" height="270"/>
        <rect x="8" y="262" width="56" height="126"/>
        <circle cx="118" cy="325" r="3" fill="white" stroke="none"/>
        <circle cx="118" cy="325" r="90" stroke-dasharray="50 520"/>
        <!-- Right penalty box -->
        <rect x="834" y="190" width="158" height="270"/>
        <rect x="936" y="262" width="56" height="126"/>
        <circle cx="882" cy="325" r="3" fill="white" stroke="none"/>
        <circle cx="882" cy="325" r="90" stroke-dasharray="50 520" transform="rotate(180 500 325)"/>
        <!-- Corner arcs -->
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
      <div class="event-label">Biggest Ummah Football Gathering</div>
      <h1>UmmahTwitter<br>Match 2026</h1>
      <p class="event-meta">
        <strong>Saturday, June 6 · 8:00 AM</strong><br>
        Landmark International School, Ikorodu Lagos
      </p>
    </header>

    <!-- Teams -->
    <div class="teams-strip" role="list" aria-label="Teams">
      <div class="team-chip gold"   role="listitem"><span class="dot" style="background:var(--gold)"></span>Aliy</div>
      <div class="team-chip blue"   role="listitem"><span class="dot" style="background:var(--blue)"></span>Abubakar</div>
      <div class="team-chip silver" role="listitem"><span class="dot" style="background:var(--silver)"></span>Umar</div>
      <div class="team-chip green"  role="listitem"><span class="dot" style="background:var(--green)"></span>Uthman</div>
    </div>

    <!-- Card -->
    <main>
      <div class="card">
        <Transition name="fade" mode="out-in">

          <!-- Form -->
          <form v-if="state !== 'success'" key="form" @submit.prevent="handleSubmit" novalidate>
            <p class="card-title">Event Check-In</p>

            <div class="field">
              <label for="name">Full Name <span class="req" aria-hidden="true">*</span></label>
              <input
                v-model="form.name"
                type="text" id="name" name="name"
                placeholder="Your full name"
                required autocomplete="name" inputmode="text"
              />
            </div>

            <div class="field">
              <label for="twitter">Twitter / X Handle</label>
              <div class="input-wrap">
                <span class="prefix" aria-hidden="true">@</span>
                <input
                  v-model="form.twitter"
                  type="text" id="twitter" name="twitter"
                  placeholder="yourhandle"
                  autocomplete="off" autocorrect="off" autocapitalize="none" spellcheck="false"
                  class="has-prefix"
                />
              </div>
            </div>

            <div class="field">
              <label for="email">Email <span class="req" aria-hidden="true">*</span></label>
              <input
                v-model="form.email"
                type="email" id="email" name="email"
                placeholder="you@example.com"
                required autocomplete="email" inputmode="email"
              />
            </div>

            <div class="field">
              <label for="role">Attending As<span class="req" aria-hidden="true">*</span></label>
              <div class="select-wrap">
                <select v-model="form.role" id="role" name="role" required>
                  <option value="Fan">Fan</option>
                  <option value="Player">Player</option>
                </select>
                <span class="chevron" aria-hidden="true">
                  <svg width="12" height="7" viewBox="0 0 12 7" fill="none">
                    <path d="M1 1l5 5 5-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
              </div>
            </div>

            <div class="field last">
              <label for="supporting">Supporting Team <span class="req" aria-hidden="true">*</span></label>
              <div class="select-wrap">
                <select v-model="form.supporting" id="supporting" name="supporting" required>
                  <option value="Neutral">Neutral</option>
                  <option value="Aliy">Aliy</option>
                  <option value="Abubakar">Abubakar</option>
                  <option value="Umar">Umar</option>
                  <option value="Uthman">Uthman</option>
                </select>
                <span class="chevron" aria-hidden="true">
                  <svg width="12" height="7" viewBox="0 0 12 7" fill="none">
                    <path d="M1 1l5 5 5-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                  </svg>
                </span>
              </div>
            </div>

            <button type="submit" class="btn-submit" :class="{ loading: state === 'loading' }" :disabled="state === 'loading'">
              <span v-if="state !== 'loading'">Check In</span>
              <span v-else class="btn-loading">
                <svg class="spinner" width="16" height="16" viewBox="0 0 16 16" fill="none">
                  <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2" opacity="0.25"/>
                  <path d="M8 2a6 6 0 0 1 6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
                Checking in…
              </span>
            </button>

            <Transition name="slide-down">
              <div v-if="state === 'error'" class="error-msg" role="alert" aria-live="polite" style="flex-direction: column; align-items: flex-start; gap: 4px;">
                <div style="display: flex; align-items: center; gap: 8px;">
                  <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
                    <circle cx="7" cy="7" r="6" stroke="currentColor" stroke-width="1.5"/>
                    <path d="M7 4v3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                    <circle cx="7" cy="10" r="0.75" fill="currentColor"/>
                  </svg>
                  <span>{{ errorMsg }}</span>
                </div>
                <div v-if="isDuplicateEmail" style="margin-left: 22px; margin-top: 4px;">
                  <router-link to="/certificate" style="color: var(--gold); text-decoration: underline;">
                    Download your certificate or pass here.
                  </router-link>
                </div>
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
            <h2>You're registered!</h2>
            <p>Welcome, <span class="success-name">{{ ticketInfo.name }}</span>.</p>
            <p class="success-sub" style="margin-bottom: 24px;">Your spectator pass has been generated. Download it below and present it at the gate.</p>

            <!-- CSS Ticket Pass -->
            <div class="ticket-wrapper">
              <div class="ticket-card">
                <div class="ticket-main">
                  <div class="ticket-logo-row" style="display: flex; align-items: center; gap: 0.5rem;">
                    <img src="/logo.jpg" alt="Ummah Twitter FC Logo" style="width: 24px; height: 24px; border-radius: 50%; object-fit: cover; border: 1px solid var(--gold);" />
                    <span class="ticket-logo-text">UMMAH TWITTER FC PASS</span>
                  </div>
                  <h3 class="ticket-user-name">{{ ticketInfo.name }}</h3>
                  <div style="display: flex; gap: 0.75rem; align-items: center; flex-wrap: wrap;">
                    <span class="ticket-role-badge" :class="ticketInfo.role.toLowerCase()">
                      {{ ticketInfo.role }}
                    </span>
                    <span class="ticket-team-badge" :class="ticketInfo.supporting.toLowerCase()">
                      Supporting: {{ ticketInfo.supporting }}
                    </span>
                    <span v-if="ticketInfo.twitter" class="ticket-twitter">
                      <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" style="opacity: 0.85; flex-shrink: 0;">
                        <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                      </svg>
                      {{ ticketInfo.twitter }}
                    </span>
                  </div>
                  
                  <div class="ticket-details-row">
                    <div class="ticket-detail">
                      <span class="detail-label">Date</span>
                      <span class="detail-value">Saturday, June 6</span>
                    </div>
                    <div class="ticket-detail">
                      <span class="detail-label">Venue</span>
                      <span class="detail-value">Landmark College</span>
                    </div>
                    <div class="ticket-detail">
                      <span class="detail-label">Time</span>
                      <span class="detail-value">8:00 AM Prompt</span>
                    </div>
                  </div>
                </div>

                <div class="ticket-stub">
                  <div class="stub-divider"></div>
                  <span class="stub-label">Ticket ID</span>
                  <span class="stub-value">{{ ticketInfo.ticketId }}</span>
                  <div class="stub-barcode" aria-hidden="true">
                    <div class="barcode-line" style="width: 2px;"></div>
                    <div class="barcode-line" style="width: 4px;"></div>
                    <div class="barcode-line" style="width: 1px;"></div>
                    <div class="barcode-line" style="width: 3px;"></div>
                    <div class="barcode-line" style="width: 5px;"></div>
                    <div class="barcode-line" style="width: 2px;"></div>
                    <div class="barcode-line" style="width: 4px;"></div>
                    <div class="barcode-line" style="width: 1px;"></div>
                    <div class="barcode-line" style="width: 3px;"></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Download button -->
            <button @click="downloadTicket" class="btn-download-pass" style="margin-bottom: 0.75rem;">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 0.5rem; display: inline-block; vertical-align: middle;">
                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
                <polyline points="7 10 12 15 17 10"/>
                <line x1="12" x2="12" y1="15" y2="3"/>
              </svg>
              Download Pass (PNG)
            </button>


          </div>

        </Transition>
      </div>
    </main>

    <footer class="page-footer">
      <p>Football · Banter · Networking</p>
      <p>Ummah Twitter FC · 2026</p>
      <div style="display: flex; gap: 0.5rem; justify-content: center; margin-top: 10px; flex-wrap: wrap;">
        <router-link to="/qr" class="qr-link" title="Show QR code">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
            <rect x="1" y="1" width="5" height="5" rx="0.5" stroke="currentColor" stroke-width="1.2"/>
            <rect x="8" y="1" width="5" height="5" rx="0.5" stroke="currentColor" stroke-width="1.2"/>
            <rect x="1" y="8" width="5" height="5" rx="0.5" stroke="currentColor" stroke-width="1.2"/>
            <rect x="2.5" y="2.5" width="2" height="2" fill="currentColor"/>
            <rect x="9.5" y="2.5" width="2" height="2" fill="currentColor"/>
            <rect x="2.5" y="9.5" width="2" height="2" fill="currentColor"/>
            <path d="M8 8.5h1.5v1.5H8zM10.5 8.5H12V10h-1.5zM8 11h1.5v2H8zM10.5 10.5H12V12h-1.5z" fill="currentColor"/>
          </svg>
          Show QR code
        </router-link>
        <router-link to="/schedule" class="qr-link" title="View Game Schedule">
          ⚽ View Schedule
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

/* ── Pitch background ── */
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

/* ── Atmospheric glow at center ── */
.atmo-glow {
  position: fixed;
  top: 0; left: 50%; transform: translateX(-50%);
  width: 700px;
  height: 500px;
  background: radial-gradient(ellipse at 50% 30%, rgba(20, 38, 20, 0.55) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

/* All content above background */
.logo-wrap, .header, .teams-strip, main, .page-footer {
  position: relative;
  z-index: 1;
}

/* ── Logo ── */
.logo-wrap {
  margin-bottom: 22px;
}

.logo-svg {
  display: block;
  filter: drop-shadow(0 0 16px rgba(232, 184, 75, 0.28));
}

/* ── Header ── */
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

.event-meta {
  color: var(--muted);
  font-size: 13.5px;
  line-height: 1.75;
}

.event-meta strong {
  color: var(--text);
  font-weight: 600;
}

/* ── Teams strip ── */
.teams-strip {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  justify-content: center;
  margin-bottom: 28px;
}

.team-chip {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 5px 11px;
  border-radius: 999px;
  font-size: 11.5px;
  font-weight: 600;
  border: 1px solid;
  letter-spacing: 0.01em;
}

.team-chip .dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  flex-shrink: 0;
}

.team-chip.gold   { color: var(--gold);   border-color: rgba(232,184,75,0.3);  background: rgba(232,184,75,0.06);  }
.team-chip.blue   { color: var(--blue);   border-color: rgba(75,168,232,0.3);  background: rgba(75,168,232,0.06);  }
.team-chip.silver { color: var(--silver); border-color: rgba(152,152,176,0.3); background: rgba(152,152,176,0.06); }
.team-chip.green  { color: var(--green);  border-color: rgba(61,214,140,0.3);  background: rgba(61,214,140,0.06);  }

/* ── Card ── */
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

/* ── Fields ── */
.field {
  margin-bottom: 18px;
}

.field.last {
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

.input-wrap {
  position: relative;
}

.prefix {
  position: absolute;
  left: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--dim);
  font-size: 15px;
  font-weight: 500;
  pointer-events: none;
  user-select: none;
}

input, select {
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--border-mid);
  color: var(--text);
  padding: 13px 15px;
  border-radius: var(--radius-sm);
  font-size: 16px;
  font-family: inherit;
  outline: none;
  -webkit-appearance: none;
  appearance: none;
  transition: border-color 0.15s, box-shadow 0.15s;
}

input.has-prefix {
  padding-left: 30px;
}

input::placeholder {
  color: var(--dim);
  font-weight: 400;
}

input:focus, select:focus {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(232, 184, 75, 0.1);
}

.select-wrap {
  position: relative;
}

.select-wrap select {
  cursor: pointer;
  padding-right: 42px;
  color: v-bind("form.role ? 'var(--text)' : 'var(--dim)'");
}

.chevron {
  position: absolute;
  right: 14px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
  pointer-events: none;
  display: flex;
  align-items: center;
}

select option {
  background: #1a1a26;
  color: var(--text);
}

/* ── Submit button ── */
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

/* ── Error ── */
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

/* ── Success ── */
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

/* ── Footer ── */
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

/* ── Transitions ── */
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

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}

/* ── CSS Ticket ── */
.ticket-wrapper {
  margin: 1.5rem 0 2rem;
  perspective: 1000px;
}
.ticket-card {
  display: flex;
  background: #052014;
  border: 1.5px solid var(--gold);
  border-radius: var(--radius-md);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
  position: relative;
  overflow: hidden;
  text-align: left;
}
.ticket-card::before,
.ticket-card::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  background-color: var(--surface);
  border: 1.5px solid var(--gold);
  border-radius: 50%;
  z-index: 5;
}
.ticket-card::before {
  top: -11px;
  right: 110px;
}
.ticket-card::after {
  bottom: -11px;
  right: 110px;
}

.ticket-main {
  flex: 1;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}
.ticket-logo-row {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.ticket-logo-text {
  font-size: 11px;
  font-weight: 800;
  color: var(--gold);
  letter-spacing: 0.05em;
  text-transform: uppercase;
}
.ticket-user-name {
  font-size: 20px;
  font-weight: 900;
  color: #FFFFFF;
  margin: 0.25rem 0;
  line-height: 1.2;
}
.ticket-role-badge {
  align-self: flex-start;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 3px 10px;
  border-radius: 4px;
  background-color: rgba(232, 184, 75, 0.1);
  border: 1px solid rgba(232, 184, 75, 0.3);
  color: var(--gold);
}
.ticket-role-badge.player {
  background-color: rgba(75, 168, 232, 0.1);
  border-color: rgba(75, 168, 232, 0.3);
  color: var(--blue);
}

.ticket-details-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.5rem;
  border-top: 1px dashed rgba(39, 82, 61, 0.5);
  padding-top: 0.75rem;
  margin-top: 0.5rem;
}
.ticket-detail {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}
.detail-label {
  font-size: 8px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--muted);
  letter-spacing: 0.05em;
}
.detail-value {
  font-size: 11px;
  font-weight: 600;
  color: #FFFFFF;
}

.ticket-stub {
  width: 120px;
  padding: 1.5rem 1rem;
  background-color: rgba(10, 45, 29, 0.4);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  text-align: center;
}
.stub-divider {
  position: absolute;
  top: 10px;
  bottom: 10px;
  left: 0;
  border-left: 2px dashed rgba(232, 184, 75, 0.3);
}
.stub-label {
  font-size: 8px;
  font-weight: 700;
  text-transform: uppercase;
  color: var(--gold);
  letter-spacing: 0.05em;
}
.stub-value {
  font-size: 16px;
  font-weight: 900;
  color: #FFFFFF;
  margin-top: 0.25rem;
  letter-spacing: 0.05em;
}
.stub-barcode {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  gap: 2px;
  height: 36px;
  margin-top: 1rem;
  opacity: 0.6;
}
.barcode-line {
  background-color: var(--gold);
  height: 100%;
}

.btn-download-pass {
  background: linear-gradient(135deg, #F3C64F 0%, #D4AF37 50%, #B89020 100%);
  color: #052014;
  border: none;
  padding: 15px 20px;
  border-radius: var(--radius-sm);
  font-size: 15px;
  font-weight: 700;
  cursor: pointer;
  width: 100%;
  transition: background 0.15s, box-shadow 0.15s, transform 0.1s;
}
.btn-download-pass:hover {
  background: linear-gradient(135deg, #FFE082 0%, #E8C14A 50%, #CFA52D 100%);
  box-shadow: 0 4px 22px rgba(232, 184, 75, 0.35);
}
.btn-download-pass:active {
  transform: scale(0.985);
}

.ticket-twitter {
  font-size: 12px;
  font-weight: 600;
  color: var(--blue);
  display: inline-flex;
  align-items: center;
  gap: 4px;
}
.ticket-team-badge {
  align-self: flex-start;
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 3px 10px;
  border-radius: 4px;
  background-color: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #FFFFFF;
}
.ticket-team-badge.neutral {
  background-color: rgba(152, 152, 176, 0.1);
  border-color: rgba(152, 152, 176, 0.3);
  color: var(--silver);
}
.ticket-team-badge.aliy {
  background-color: rgba(232, 184, 75, 0.1);
  border-color: rgba(232, 184, 75, 0.3);
  color: var(--gold);
}
.ticket-team-badge.abubakar {
  background-color: rgba(75, 168, 232, 0.1);
  border-color: rgba(75, 168, 232, 0.3);
  color: var(--blue);
}
.ticket-team-badge.umar {
  background-color: rgba(152, 152, 176, 0.15);
  border-color: rgba(152, 152, 176, 0.4);
  color: var(--silver);
}
.ticket-team-badge.uthman {
  background-color: rgba(61, 214, 140, 0.1);
  border-color: rgba(61, 214, 140, 0.3);
  color: var(--green);
}
</style>

