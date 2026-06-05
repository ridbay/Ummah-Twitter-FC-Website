<script setup>
import { ref, reactive } from 'vue'
import { supabase } from '../lib/supabase.js'

const form = reactive({ name: '', twitter: '', email: '', role: '' })
const state = ref('idle') // idle | loading | success | error
const errorMsg = ref('')
const successName = ref('')

async function handleSubmit() {
  if (!form.name.trim())  return setError('Please enter your full name.')
  if (!form.email.trim()) return setError('Please enter your email address.')
  if (!form.role)         return setError('Please select your role.')

  state.value = 'loading'
  errorMsg.value = ''

  const twitter = form.twitter.trim().replace(/^@+/, '')

  const { error } = await supabase.from('checkins').insert({
    name:    form.name.trim(),
    twitter: twitter ? `@${twitter}` : null,
    email:   form.email.trim().toLowerCase(),
    role:    form.role,
  })

  if (error) {
    state.value = 'error'
    errorMsg.value = error.code === '23505'
      ? 'This email address is already registered.'
      : 'Something went wrong. Please try again.'
    return
  }

  successName.value = form.name.trim().split(' ')[0]
  state.value = 'success'
}

function setError(msg) {
  errorMsg.value = msg
  state.value = 'error'
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
      <svg width="66" height="66" viewBox="0 0 52 52" fill="none" aria-label="Ummah FC" class="logo-svg">
        <circle cx="26" cy="26" r="25" stroke="#e8b84b" stroke-width="1.5" fill="none" opacity="0.45"/>
        <circle cx="26" cy="26" r="19" stroke="#e8b84b" stroke-width="1" fill="none" opacity="0.25"/>
        <path d="M26 14a12 12 0 1 0 0 24 10 10 0 1 1 0-24z" fill="#e8b84b" opacity="0.88"/>
        <polygon points="30,20 31,23.5 34.5,23.5 31.8,25.5 32.8,29 30,27 27.2,29 28.2,25.5 25.5,23.5 29,23.5" fill="#e8b84b"/>
      </svg>
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

            <div class="field last">
              <label for="role">Attending as <span class="req" aria-hidden="true">*</span></label>
              <div class="select-wrap">
                <select v-model="form.role" id="role" name="role" required>
                  <option value="" disabled>Select role</option>
                  <option value="Player">Player</option>
                  <option value="Fan">Fan</option>
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
            <h2>You're in!</h2>
            <p>Welcome, <span class="success-name">{{ successName }}</span>.</p>
            <p class="success-sub">See you on the pitch ⚽</p>
          </div>

        </Transition>
      </div>
    </main>

    <footer class="page-footer">
      <p>Football · Banter · Networking</p>
      <p>Ummah FC · 2026</p>
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
    </footer>

  </div>
</template>

<style scoped>
.page {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 36px 16px 56px;
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
</style>
