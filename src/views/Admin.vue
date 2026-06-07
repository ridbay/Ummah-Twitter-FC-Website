<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { supabase } from '../lib/supabase.js'

const ADMIN_PIN = import.meta.env.VITE_ADMIN_PIN ?? '1234'

// ── Auth ──────────────────────────────────────────────────────
const authed    = ref(sessionStorage.getItem('admin_authed') === '1')
const pinInput  = ref('')
const pinError  = ref('')
const pinLoading = ref(false)

function checkPin() {
  pinLoading.value = true
  setTimeout(() => {
    if (pinInput.value === ADMIN_PIN) {
      sessionStorage.setItem('admin_authed', '1')
      authed.value = true
      loadData()
    } else {
      pinError.value = 'Incorrect PIN. Try again.'
      pinInput.value = ''
    }
    pinLoading.value = false
  }, 400)
}

function signOut() {
  sessionStorage.removeItem('admin_authed')
  authed.value = false
  registrations.value = []
}

// ── Data ──────────────────────────────────────────────────────
const registrations = ref([])
const dataLoading   = ref(false)
const lastRefreshed = ref(null)

const currentTab = ref('checkins') // 'checkins' | 'teams'

const teams = ref([])
const matches = ref([])
const teamStatsLoading = ref(false)

async function loadData() {
  dataLoading.value = true
  
  if (currentTab.value === 'checkins') {
    const { data, error } = await supabase
      .from('checkins')
      .select('*')
      .order('created_at', { ascending: false })

    if (!error) {
      registrations.value = data ?? []
      lastRefreshed.value = new Date()
    }
  } else if (currentTab.value === 'teams') {
    teamStatsLoading.value = true
    const { data: teamsData } = await supabase.from('team_stats').select('name').order('name')
    const { data: matchesData } = await supabase.from('matches').select('*').order('created_at', { ascending: false })
    
    if (teamsData) teams.value = teamsData.map(t => t.name)
    if (matchesData) matches.value = matchesData
    
    lastRefreshed.value = new Date()
    teamStatsLoading.value = false
  }
  
  dataLoading.value = false
}

async function addMatch() {
  const { error } = await supabase
    .from('matches')
    .insert([{ team1: teams.value[0], team2: teams.value[1], score1: 0, score2: 0, is_played: false }])
  if (!error) loadData()
}

async function saveMatch(match) {
  const { error } = await supabase
    .from('matches')
    .update({
      team1: match.team1,
      team2: match.team2,
      score1: match.score1,
      score2: match.score2,
      is_played: match.is_played
    })
    .eq('id', match.id)
    
  if (!error) {
    loadData()
  } else {
    alert('Failed to save match.')
  }
}

async function deleteMatch(id) {
  if (!confirm('Delete this match?')) return
  const { error } = await supabase.from('matches').delete().eq('id', id)
  if (!error) loadData()
}

// Standings computed from matches not needed here since we only manage matches. 
// But we could show them if we import the helper. We'll just manage matches here.

async function toggleArrived(reg) {
  const next = !reg.arrived
  reg.arrived    = next
  reg.arrived_at = next ? new Date().toISOString() : null

  const { error } = await supabase
    .from('checkins')
    .update({ arrived: next, arrived_at: reg.arrived_at })
    .eq('id', reg.id)

  if (error) {
    reg.arrived    = !next
    reg.arrived_at = null
  }
}

// ── Filters ───────────────────────────────────────────────────
const search       = ref('')
const roleFilter   = ref('all')
const statusFilter = ref('all')

const filtered = computed(() => {
  const q = search.value.toLowerCase().trim()
  return registrations.value.filter(r => {
    const matchSearch =
      !q ||
      r.name.toLowerCase().includes(q) ||
      (r.twitter ?? '').toLowerCase().includes(q) ||
      r.email.toLowerCase().includes(q) ||
      (r.supporting ?? '').toLowerCase().includes(q)
    const matchRole   = roleFilter.value   === 'all' || r.role.toLowerCase() === roleFilter.value
    const matchStatus = statusFilter.value === 'all' ||
      (statusFilter.value === 'arrived' ? r.arrived : !r.arrived)
    return matchSearch && matchRole && matchStatus
  })
})

const stats = computed(() => ({
  total:   registrations.value.length,
  players: registrations.value.filter(r => r.role === 'Player').length,
  fans:    registrations.value.filter(r => r.role === 'Fan').length,
  arrived: registrations.value.filter(r => r.arrived).length,
}))

// ── Real-time ─────────────────────────────────────────────────
let channel

function setupRealtime() {
  channel = supabase
    .channel('checkins_rt')
    .on('postgres_changes', { event: 'INSERT', schema: 'public', table: 'checkins' }, ({ new: row }) => {
      if (!registrations.value.find(r => r.id === row.id)) {
        registrations.value.unshift(row)
      }
    })
    .on('postgres_changes', { event: 'UPDATE', schema: 'public', table: 'checkins' }, ({ new: row }) => {
      const idx = registrations.value.findIndex(r => r.id === row.id)
      if (idx !== -1) registrations.value[idx] = { ...registrations.value[idx], ...row }
    })
    .on('postgres_changes', { event: '*', schema: 'public', table: 'matches' }, () => {
      if (currentTab.value === 'teams') loadData()
    })
    .subscribe()
}

// ── Utilities ─────────────────────────────────────────────────
function timeAgo(iso) {
  const secs = Math.floor((Date.now() - new Date(iso)) / 1000)
  if (secs < 60)   return 'just now'
  if (secs < 3600) return `${Math.floor(secs / 60)}m ago`
  if (secs < 86400) return `${Math.floor(secs / 3600)}h ago`
  return new Date(iso).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' })
}

function formatTime(iso) {
  if (!iso) return '—'
  return new Date(iso).toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' })
}

// ── Lifecycle ─────────────────────────────────────────────────
onMounted(() => {
  if (authed.value) {
    loadData()
    setupRealtime()
  }
})

onUnmounted(() => {
  channel?.unsubscribe()
})
</script>

<template>
  <div class="admin-root">

    <!-- ── PIN Gate ───────────────────────────────── -->
    <Transition name="fade">
      <div v-if="!authed" class="pin-gate">
        <div class="pin-card">
          <div class="pin-logo" aria-hidden="true">
            <svg width="52" height="52" viewBox="0 0 52 52" fill="none">
              <circle cx="26" cy="26" r="25" stroke="#e8b84b" stroke-width="1.5" fill="none" opacity="0.45"/>
              <path d="M26 14a12 12 0 1 0 0 24 10 10 0 1 1 0-24z" fill="#e8b84b" opacity="0.88"/>
              <polygon points="30,20 31,23.5 34.5,23.5 31.8,25.5 32.8,29 30,27 27.2,29 28.2,25.5 25.5,23.5 29,23.5" fill="#e8b84b"/>
            </svg>
          </div>
          <h2>Admin Access</h2>
          <p class="pin-sub">UmmahTwitter Match 2026</p>
          <form @submit.prevent="checkPin" novalidate>
            <input
              v-model="pinInput"
              type="password"
              placeholder="Enter PIN"
              inputmode="numeric"
              maxlength="6"
              autocomplete="current-password"
              :disabled="pinLoading"
            />
            <Transition name="slide-down">
              <p v-if="pinError" class="pin-error" role="alert">{{ pinError }}</p>
            </Transition>
            <button type="submit" :disabled="!pinInput || pinLoading" class="pin-btn">
              <span v-if="!pinLoading">Enter</span>
              <span v-else class="btn-loading">
                <svg class="spinner" width="14" height="14" viewBox="0 0 16 16" fill="none">
                  <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2" opacity="0.25"/>
                  <path d="M8 2a6 6 0 0 1 6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
              </span>
            </button>
          </form>
        </div>
      </div>
    </Transition>

    <!-- ── Dashboard ─────────────────────────────── -->
    <Transition name="fade">
      <div v-if="authed" class="dashboard">

        <!-- Top bar -->
        <header class="top-bar">
          <div class="top-bar-left">
            <svg width="28" height="28" viewBox="0 0 52 52" fill="none" aria-hidden="true">
              <circle cx="26" cy="26" r="25" stroke="#e8b84b" stroke-width="2" fill="none" opacity="0.5"/>
              <path d="M26 14a12 12 0 1 0 0 24 10 10 0 1 1 0-24z" fill="#e8b84b" opacity="0.9"/>
              <polygon points="30,20 31,23.5 34.5,23.5 31.8,25.5 32.8,29 30,27 27.2,29 28.2,25.5 25.5,23.5 29,23.5" fill="#e8b84b"/>
            </svg>
            <div>
              <div class="top-bar-title">Admin Dashboard</div>
              <div class="top-bar-sub">UmmahTwitter Match 2026</div>
            </div>
          </div>
          <div class="top-bar-right">
            <button @click="loadData" class="btn-refresh" :class="{ spinning: dataLoading }" title="Refresh">
              <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
                <path d="M13 7.5A5.5 5.5 0 0 1 2 9.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                <path d="M2 7.5A5.5 5.5 0 0 1 13 5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                <path d="M11.5 4.5l1.5 1-1.5 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M3.5 10.5L2 9.5l1.5-1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </button>
            <router-link to="/qr" target="_blank" class="btn-signout" title="Show QR code">QR Code</router-link>
            <button @click="signOut" class="btn-signout">Sign Out</button>
          </div>
        </header>

        <!-- Tabs -->
        <div class="tabs-container">
          <button 
            class="tab-btn" 
            :class="{ active: currentTab === 'checkins' }"
            @click="currentTab = 'checkins'; loadData()"
          >
            Check-Ins
          </button>
          <button 
            class="tab-btn" 
            :class="{ active: currentTab === 'teams' }"
            @click="currentTab = 'teams'; loadData()"
          >
            Matches
          </button>
        </div>

        <div class="content">

          <!-- ── Check-Ins Tab ── -->
          <template v-if="currentTab === 'checkins'">

          <!-- Stats -->
          <div class="stats-grid">
            <div class="stat-card">
              <span class="stat-value">{{ stats.total }}</span>
              <span class="stat-label">Registered</span>
            </div>
            <div class="stat-card player">
              <span class="stat-value">{{ stats.players }}</span>
              <span class="stat-label">Players</span>
            </div>
            <div class="stat-card fan">
              <span class="stat-value">{{ stats.fans }}</span>
              <span class="stat-label">Fans</span>
            </div>
            <div class="stat-card arrived">
              <span class="stat-value">{{ stats.arrived }}</span>
              <span class="stat-label">Arrived</span>
            </div>
          </div>

          <!-- Filters -->
          <div class="filter-block">
            <div class="search-wrap">
              <svg class="search-icon" width="15" height="15" viewBox="0 0 15 15" fill="none" aria-hidden="true">
                <circle cx="6.5" cy="6.5" r="5" stroke="currentColor" stroke-width="1.5"/>
                <path d="M10.5 10.5l3 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
              </svg>
              <input
                v-model="search"
                type="search"
                placeholder="Search name, handle or email…"
                class="search-input"
              />
            </div>
            <div class="filter-row">
              <select v-model="roleFilter">
                <option value="all">All Roles</option>
                <option value="player">Players only</option>
                <option value="fan">Fans only</option>
              </select>
              <select v-model="statusFilter">
                <option value="all">All Status</option>
                <option value="arrived">Arrived</option>
                <option value="pending">Not yet</option>
              </select>
            </div>
          </div>

          <!-- Results info -->
          <div class="results-info">
            <span>{{ filtered.length }} {{ filtered.length === 1 ? 'person' : 'people' }}</span>
            <span v-if="lastRefreshed" class="last-updated">
              Updated {{ formatTime(lastRefreshed.toISOString()) }}
            </span>
          </div>

          <!-- Loading skeleton -->
          <div v-if="dataLoading && registrations.length === 0" class="skeleton-list">
            <div v-for="i in 5" :key="i" class="skeleton-card"></div>
          </div>

          <!-- Empty state -->
          <div v-else-if="!dataLoading && filtered.length === 0" class="empty-state">
            <svg width="40" height="40" viewBox="0 0 40 40" fill="none" aria-hidden="true">
              <circle cx="20" cy="20" r="18" stroke="currentColor" stroke-width="1.5" opacity="0.3"/>
              <path d="M13 20h14M20 13v14" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" opacity="0.3"/>
            </svg>
            <p>{{ search || roleFilter !== 'all' || statusFilter !== 'all' ? 'No results match your filters.' : 'No one has registered yet.' }}</p>
          </div>

          <!-- Registration list -->
          <div v-else class="reg-list">
            <TransitionGroup name="list" tag="div">
              <div
                v-for="reg in filtered"
                :key="reg.id"
                class="reg-card"
                :class="{ 'is-arrived': reg.arrived }"
              >
                <div class="reg-header">
                  <div class="reg-name-row" style="flex-wrap: wrap;">
                    <span class="reg-name">{{ reg.name }}</span>
                    <span class="role-badge" :class="reg.role.toLowerCase()">{{ reg.role }}</span>
                    <span class="support-badge" :class="(reg.supporting || 'neutral').toLowerCase()">
                      Supports: {{ reg.supporting || 'Neutral' }}
                    </span>
                  </div>
                  <div class="reg-time">{{ timeAgo(reg.created_at) }}</div>
                </div>

                <div class="reg-details">
                  <span v-if="reg.twitter" class="reg-handle">{{ reg.twitter }}</span>
                  <span class="reg-email">{{ reg.email }}</span>
                </div>

                <div class="reg-footer">
                  <template v-if="reg.arrived">
                    <div class="arrived-info">
                      <span class="arrived-badge">
                        <svg width="11" height="11" viewBox="0 0 11 11" fill="none" aria-hidden="true">
                          <path d="M1.5 5.5l3 3 5-5.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                        Arrived
                      </span>
                      <span v-if="reg.arrived_at" class="arrived-time">at {{ formatTime(reg.arrived_at) }}</span>
                    </div>
                    <button @click="toggleArrived(reg)" class="btn-undo">Undo</button>
                  </template>
                  <template v-else>
                    <button @click="toggleArrived(reg)" class="btn-arrive">
                      <svg width="13" height="13" viewBox="0 0 13 13" fill="none" aria-hidden="true">
                        <path d="M1.5 7l4 4 6-7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                      </svg>
                      Mark Arrived
                    </button>
                  </template>
                </div>
              </div>
            </TransitionGroup>
          </div>
          </template>

          <!-- ── Teams Tab ── -->
          <template v-if="currentTab === 'teams'">
            <div class="results-info" style="justify-content: space-between;">
              <span>Manage Matches</span>
              <button @click="addMatch" class="btn-arrive" style="background: var(--gold); color: #000; font-weight: bold; border-radius: 4px; padding: 4px 12px; height: auto;">
                + Add Match
              </button>
            </div>
            
            <div v-if="teamStatsLoading && matches.length === 0" class="skeleton-list">
              <div v-for="i in 4" :key="i" class="skeleton-card" style="height: 140px;"></div>
            </div>
            
            <div v-else-if="!teamStatsLoading && matches.length === 0" class="empty-state">
              <p>No matches found. Click Add Match to create one.</p>
            </div>
            
            <div v-else class="reg-list">
              <div v-for="match in matches" :key="match.id" class="reg-card">
                
                <div class="stats-form-grid" style="grid-template-columns: 1fr auto 1fr; align-items: center; gap: 8px;">
                  <div class="stat-input-group">
                    <label>Team 1</label>
                    <select v-model="match.team1" style="width: 100%; padding: 8px; border-radius: 4px; background: rgba(255,255,255,0.05); border: 1px solid var(--border-mid); color: white;">
                      <option v-for="t in teams" :key="t" :value="t">{{ t }}</option>
                    </select>
                  </div>
                  <div style="font-weight: bold; padding-top: 20px;">VS</div>
                  <div class="stat-input-group">
                    <label>Team 2</label>
                    <select v-model="match.team2" style="width: 100%; padding: 8px; border-radius: 4px; background: rgba(255,255,255,0.05); border: 1px solid var(--border-mid); color: white;">
                      <option v-for="t in teams" :key="t" :value="t">{{ t }}</option>
                    </select>
                  </div>
                </div>

                <div class="stats-form-grid" style="grid-template-columns: 1fr 1fr auto; align-items: center; gap: 8px; margin-top: 10px;">
                  <div class="stat-input-group">
                    <label>Score 1</label>
                    <input type="number" v-model.number="match.score1" min="0" style="padding: 8px;"/>
                  </div>
                  <div class="stat-input-group">
                    <label>Score 2</label>
                    <input type="number" v-model.number="match.score2" min="0" style="padding: 8px;"/>
                  </div>
                  <div class="stat-input-group" style="display: flex; align-items: center; gap: 8px; flex-direction: row; margin-top: 24px;">
                    <input type="checkbox" v-model="match.is_played" :id="'played-'+match.id" style="width: auto;"/>
                    <label :for="'played-'+match.id" style="margin: 0;">Match Played</label>
                  </div>
                </div>
                
                <div class="reg-footer" style="justify-content: flex-end; margin-top: 14px; gap: 10px;">
                  <button @click="deleteMatch(match.id)" class="btn-arrive" style="background: rgba(248, 113, 113, 0.1); color: #f87171; border-color: rgba(248, 113, 113, 0.3);">
                    Delete
                  </button>
                  <button @click="saveMatch(match)" class="btn-arrive" style="background: rgba(232, 184, 75, 0.1); color: var(--gold); border-color: rgba(232, 184, 75, 0.3);">
                    Save Match
                  </button>
                </div>
              </div>
            </div>
          </template>

        </div>
      </div>
    </Transition>

  </div>
</template>

<style scoped>
.admin-root {
  min-height: 100svh;
  background: var(--bg);
}

/* ── PIN Gate ── */
.pin-gate {
  min-height: 100svh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px 16px;
}

.pin-card {
  width: 100%;
  max-width: 360px;
  background: var(--surface);
  border: 1px solid var(--border-mid);
  border-radius: var(--radius-xl);
  padding: 36px 28px;
  text-align: center;
  box-shadow: 0 32px 80px rgba(0,0,0,0.5);
  position: relative;
}

.pin-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(232,184,75,0.5) 50%, transparent);
  border-radius: var(--radius-xl) var(--radius-xl) 0 0;
}

.pin-logo {
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
}

.pin-logo svg {
  filter: drop-shadow(0 0 14px rgba(232, 184, 75, 0.3));
}

.pin-card h2 {
  font-size: 22px;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 4px;
}

.pin-sub {
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 28px;
}

.pin-card input {
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--border-mid);
  color: var(--text);
  padding: 13px 16px;
  border-radius: var(--radius-sm);
  font-size: 18px;
  font-family: inherit;
  text-align: center;
  letter-spacing: 0.2em;
  outline: none;
  -webkit-appearance: none;
  transition: border-color 0.15s, box-shadow 0.15s;
  margin-bottom: 14px;
}

.pin-card input:focus {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(232,184,75,0.1);
}

.pin-error {
  color: #f87171;
  font-size: 13px;
  margin-bottom: 14px;
  text-align: center;
}

.pin-btn {
  width: 100%;
  background: var(--gold);
  color: #0c0900;
  border: none;
  padding: 14px;
  border-radius: var(--radius-sm);
  font-size: 15px;
  font-weight: 700;
  font-family: inherit;
  cursor: pointer;
  transition: background 0.15s, box-shadow 0.15s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pin-btn:hover:not(:disabled) {
  background: #f0c456;
  box-shadow: 0 4px 20px rgba(232,184,75,0.3);
}

.pin-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* ── Dashboard ── */
.dashboard {
  min-height: 100svh;
  display: flex;
  flex-direction: column;
}

/* Top bar */
.top-bar {
  position: sticky;
  top: 0;
  z-index: 10;
  background: rgba(8, 8, 14, 0.9);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border);
  padding: 14px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
}

.top-bar-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.top-bar-title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text);
  line-height: 1.2;
}

.top-bar-sub {
  font-size: 11px;
  color: var(--muted);
  margin-top: 1px;
}

.top-bar-right {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn-refresh {
  background: transparent;
  border: 1px solid var(--border-mid);
  color: var(--muted);
  width: 34px;
  height: 34px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: color 0.15s, border-color 0.15s;
}

.btn-refresh:hover {
  color: var(--text);
  border-color: var(--muted);
}

.btn-refresh.spinning svg {
  animation: spin 0.8s linear infinite;
}

.btn-signout {
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
  white-space: nowrap;
}

.btn-signout:hover {
  color: var(--text);
  border-color: var(--muted);
}

/* Content */
.tabs-container {
  display: flex;
  justify-content: center;
  gap: 1rem;
  padding: 16px 20px 0;
  max-width: 680px;
  margin: 0 auto;
  width: 100%;
}

.tab-btn {
  flex: 1;
  background: transparent;
  color: var(--muted);
  border: none;
  border-bottom: 2px solid transparent;
  padding: 10px 0;
  font-size: 14px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
}

.tab-btn:hover {
  color: var(--text);
}

.tab-btn.active {
  color: var(--gold);
  border-bottom-color: var(--gold);
}

.content {
  padding: 20px 16px 48px;
  max-width: 680px;
  margin: 0 auto;
  width: 100%;
}

/* Team Stats Form */
.stats-form-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.stat-input-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.stat-input-group label {
  font-size: 11px;
  font-weight: 700;
  color: var(--muted);
  text-transform: uppercase;
}

.stat-input-group input {
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--border-mid);
  color: var(--text);
  padding: 8px 10px;
  border-radius: var(--radius-sm);
  font-size: 16px;
  font-family: inherit;
  font-weight: 600;
  text-align: center;
  outline: none;
  transition: border-color 0.15s;
}

.stat-input-group input:focus {
  border-color: var(--gold);
}

/* Stats */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
  margin-bottom: 20px;
}

.stat-card {
  background: var(--surface);
  border: 1px solid var(--border-mid);
  border-radius: var(--radius-md);
  padding: 14px 12px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stat-value {
  font-size: 26px;
  font-weight: 900;
  letter-spacing: -0.03em;
  line-height: 1;
  color: var(--text);
}

.stat-label {
  font-size: 10.5px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--muted);
}

.stat-card.player .stat-value { color: var(--blue); }
.stat-card.fan    .stat-value { color: var(--gold); }
.stat-card.arrived .stat-value { color: var(--green); }

/* Filters */
.filter-block {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 14px;
}

.search-wrap {
  position: relative;
}

.search-icon {
  position: absolute;
  left: 13px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--muted);
  pointer-events: none;
}

.search-input {
  width: 100%;
  background: var(--surface);
  border: 1px solid var(--border-mid);
  color: var(--text);
  padding: 11px 14px 11px 38px;
  border-radius: var(--radius-sm);
  font-size: 14px;
  font-family: inherit;
  outline: none;
  -webkit-appearance: none;
  transition: border-color 0.15s, box-shadow 0.15s;
}

.search-input::placeholder { color: var(--dim); }
.search-input:focus {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(232,184,75,0.08);
}

.filter-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

.filter-row select {
  width: 100%;
  background: var(--surface);
  border: 1px solid var(--border-mid);
  color: var(--text);
  padding: 10px 34px 10px 12px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-family: inherit;
  outline: none;
  -webkit-appearance: none;
  appearance: none;
  cursor: pointer;
  background-image: url("data:image/svg+xml,%3Csvg width='10' height='6' viewBox='0 0 10 6' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M1 1l4 4 4-4' stroke='%2377768a' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  transition: border-color 0.15s;
}

.filter-row select:focus { border-color: var(--gold); outline: none; }

select option { background: #1a1a26; color: var(--text); }

/* Results row */
.results-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
  font-size: 12.5px;
  color: var(--muted);
  font-weight: 500;
}

.last-updated {
  font-size: 11.5px;
  color: var(--dim);
}

/* Skeleton */
.skeleton-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.skeleton-card {
  height: 110px;
  border-radius: var(--radius-md);
  background: var(--surface);
  border: 1px solid var(--border);
  animation: pulse 1.4s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; }
  50%       { opacity: 1; }
}

/* Empty */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding: 56px 20px;
  color: var(--dim);
  text-align: center;
  font-size: 14px;
}

/* Reg list */
.reg-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.reg-card {
  background: var(--surface);
  border: 1px solid var(--border-mid);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  transition: border-color 0.2s;
}

.reg-card.is-arrived {
  border-color: rgba(61, 214, 140, 0.25);
  background: rgba(61, 214, 140, 0.03);
}

.reg-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 8px;
  margin-bottom: 8px;
}

.reg-name-row {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.reg-name {
  font-size: 15px;
  font-weight: 700;
  color: var(--text);
  letter-spacing: -0.01em;
}

.role-badge {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  padding: 2px 8px;
  border-radius: 999px;
  border: 1px solid;
  flex-shrink: 0;
}

.role-badge.player {
  color: var(--blue);
  background: rgba(75,168,232,0.1);
  border-color: rgba(75,168,232,0.3);
}

.role-badge.fan {
  color: var(--gold);
  background: rgba(232,184,75,0.1);
  border-color: rgba(232,184,75,0.3);
}

.support-badge {
  font-size: 10px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.07em;
  padding: 2px 8px;
  border-radius: 999px;
  border: 1px solid;
  flex-shrink: 0;
}

.support-badge.neutral {
  color: var(--silver);
  background: rgba(152,152,176,0.1);
  border-color: rgba(152,152,176,0.3);
}

.support-badge.aliy {
  color: var(--gold);
  background: rgba(232,184,75,0.1);
  border-color: rgba(232,184,75,0.3);
}

.support-badge.abubakar {
  color: var(--blue);
  background: rgba(75,168,232,0.1);
  border-color: rgba(75,168,232,0.3);
}

.support-badge.umar {
  color: var(--silver);
  background: rgba(152,152,176,0.15);
  border-color: rgba(152,152,176,0.4);
}

.support-badge.uthman {
  color: var(--green);
  background: rgba(61,214,140,0.1);
  border-color: rgba(61,214,140,0.3);
}

.reg-time {
  font-size: 11.5px;
  color: var(--dim);
  white-space: nowrap;
  flex-shrink: 0;
}

.reg-details {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 14px;
  margin-bottom: 14px;
}

.reg-handle,
.reg-email {
  font-size: 12.5px;
  color: var(--muted);
}

.reg-handle { color: var(--blue); opacity: 0.8; }

/* Reg footer */
.reg-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  padding-top: 12px;
  border-top: 1px solid var(--border);
}

.btn-arrive {
  display: flex;
  align-items: center;
  gap: 6px;
  background: rgba(61, 214, 140, 0.1);
  border: 1px solid rgba(61, 214, 140, 0.3);
  color: var(--green);
  padding: 8px 16px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  font-weight: 600;
  font-family: inherit;
  cursor: pointer;
  transition: background 0.15s, box-shadow 0.15s;
  width: 100%;
  justify-content: center;
}

.btn-arrive:hover {
  background: rgba(61, 214, 140, 0.18);
  box-shadow: 0 2px 12px rgba(61, 214, 140, 0.15);
}

.arrived-info {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.arrived-badge {
  display: flex;
  align-items: center;
  gap: 5px;
  color: var(--green);
  font-size: 13px;
  font-weight: 600;
}

.arrived-time {
  font-size: 12px;
  color: var(--muted);
}

.btn-undo {
  background: transparent;
  border: 1px solid var(--border-mid);
  color: var(--muted);
  padding: 6px 12px;
  border-radius: var(--radius-sm);
  font-size: 12px;
  font-family: inherit;
  cursor: pointer;
  white-space: nowrap;
  transition: color 0.15s, border-color 0.15s;
  flex-shrink: 0;
}

.btn-undo:hover {
  color: var(--text);
  border-color: var(--muted);
}

/* Shared */
.btn-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.spinner {
  animation: spin 0.7s linear infinite;
}

@keyframes spin { to { transform: rotate(360deg); } }

/* Transitions */
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

.slide-down-enter-active { transition: all 0.18s ease; }
.slide-down-enter-from { opacity: 0; transform: translateY(-5px); }

.list-enter-active { transition: all 0.25s ease; }
.list-enter-from { opacity: 0; transform: translateY(-8px); }

/* Responsive */
@media (max-width: 480px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .stat-value { font-size: 22px; }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}
</style>
