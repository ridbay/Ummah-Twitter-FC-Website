<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { supabase } from '../lib/supabase.js'
import { calculateStandings } from '../lib/standings.js'
import html2canvas from 'html2canvas'

const teams = [
  { name: "Umar", color: "#cbd5e1" },
  { name: "Abubakar", color: "#22d3ee" },
  { name: "Uthman", color: "#34d399" },
  { name: "Aliy", color: "#fbbf24" }
]

const topScorers = [
  { name: "Azeez Mujeeb Ayinde", nickname: "Gustavo", goals: 2 },
  { name: "Olowoseunre Gbenga Qazeem", nickname: "Olowo", goals: 2 },
  { name: "Olorunjuwon Alimi", nickname: "Marcus", goals: 2 },
  { name: "Galeeb Al Ameen", nickname: "Al Amin", goals: 2 }
]

const matches = ref([])
const loading = ref(true)

async function loadMatches() {
  const { data, error } = await supabase
    .from('matches')
    .select('*')
    .order('created_at', { ascending: false })
    
  if (!error && data) {
    matches.value = data
  }
  loading.value = false
}

let channel
onMounted(() => {
  loadMatches()
  channel = supabase
    .channel('public:matches_standings')
    .on('postgres_changes', { event: '*', schema: 'public', table: 'matches' }, () => {
      loadMatches()
    })
    .subscribe()
})

onUnmounted(() => {
  if (channel) channel.unsubscribe()
})

const displayTeams = computed(() => {
  const teamNames = teams.map(t => t.name)
  const standings = calculateStandings(matches.value, teamNames)
  
  return standings.map(stat => {
    const t = teams.find(x => x.name === stat.name)
    return {
      ...stat,
      dotColor: t ? t.color : '#ffffff'
    }
  })
})

const recentMatches = computed(() => {
  return matches.value.filter(m => m.is_played).slice(0, 5)
})

const tableCardRef = ref(null)
const recentCardRef = ref(null)
const scorersCardRef = ref(null)
const downloading = ref(false)

async function downloadForIG(elementRef, filename) {
  if (!elementRef || downloading.value) return
  
  downloading.value = true
  const el = elementRef
  
  // Temporarily add export class
  el.classList.add('ig-export-mode')
  
  try {
    // Small delay to ensure styles apply
    await new Promise(r => setTimeout(r, 100))
    
    const canvas = await html2canvas(el, {
      backgroundColor: '#052014',
      scale: 2, // High res for IG
      useCORS: true,
      logging: false
    })
    
    const link = document.createElement('a')
    link.download = `${filename}.png`
    link.href = canvas.toDataURL('image/png')
    link.click()
  } catch (err) {
    console.error('Failed to capture image', err)
    alert('Failed to capture image.')
  } finally {
    el.classList.remove('ig-export-mode')
    downloading.value = false
  }
}
</script>

<template>
  <div class="page">
    <header class="standings-header">
      <div class="container">
        <h1 class="standings-title">League Standings</h1>
        <p class="standings-subtitle">Track the journey to glory. Points are awarded as 3 for a win, 2 for a draw, and 1 for a loss.</p>
      </div>
    </header>

    <main class="container standings-main">
      <div v-if="loading" style="text-align: center; padding: 4rem;">
        <svg class="spinner" width="32" height="32" viewBox="0 0 16 16" fill="none" style="animation: spin 1s linear infinite; margin: 0 auto; color: #D4AF37;">
          <circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="2" opacity="0.25"/>
          <path d="M8 2a6 6 0 0 1 6 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </div>

      <div v-else class="standings-content">
        <!-- Table Section -->
        <div class="table-card" ref="tableCardRef">
          <div class="ig-watermark">
            <div class="ig-logo">UMMAH TWITTER FC 2026</div>
            <div class="ig-title">LEAGUE STANDINGS</div>
          </div>
          
          <div class="card-header-flex">
            <h3 class="sr-only">League Standings</h3>
            <button @click="downloadForIG(tableCardRef, 'Ummah_FC_Standings')" class="btn-download" :disabled="downloading">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              IG Post
            </button>
          </div>
          <div class="table-wrapper">
            <table class="standings-table">
              <thead>
                <tr>
                  <th class="rank-col">#</th>
                  <th>Club</th>
                  <th>MP</th>
                  <th>W</th>
                  <th>D</th>
                  <th>L</th>
                  <th>GF</th>
                  <th>GA</th>
                  <th>GD</th>
                  <th class="pts-col">Pts</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(team, index) in displayTeams" :key="team.name" :class="{'first-place': index === 0}">
                  <td class="rank-col">{{ index + 1 }}</td>
                  <td class="team-col">
                    <span class="team-dot" :style="{ backgroundColor: team.dotColor }"></span>
                    <strong>{{ team.name }} FC</strong>
                  </td>
                  <td>{{ team.p }}</td>
                  <td>{{ team.w }}</td>
                  <td>{{ team.d }}</td>
                  <td>{{ team.l }}</td>
                  <td>{{ team.gf }}</td>
                  <td>{{ team.ga }}</td>
                  <td>{{ team.gd > 0 ? '+' + team.gd : team.gd }}</td>
                  <td class="pts-col">{{ team.pts }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="table-legend">
            <div class="legend-item"><span class="dot win"></span> 3 PTS (Win)</div>
            <div class="legend-item"><span class="dot draw"></span> 2 PTS (Draw)</div>
            <div class="legend-item"><span class="dot loss"></span> 1 PT (Loss)</div>
          </div>
          <div class="ig-footer">@MuslimUmmahFC</div>
        </div>

        <!-- Recent Matches Sidebar -->
        <div class="sidebar">
          <div class="sidebar-card" ref="recentCardRef">
            <div class="ig-watermark">
              <div class="ig-logo">UMMAH TWITTER FC 2026</div>
              <div class="ig-title">RECENT RESULTS</div>
            </div>
            
            <div class="card-header-flex">
              <h3>Recent Results</h3>
              <button @click="downloadForIG(recentCardRef, 'Ummah_FC_Results')" class="btn-download" :disabled="downloading">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </button>
            </div>
            <div v-if="recentMatches.length === 0" class="empty-state">
              No matches played yet.
            </div>
            <div class="match-list" v-else>
              <div v-for="match in recentMatches" :key="match.id" class="match-row">
                <div class="match-team text-right" :class="{ 'font-bold text-gold': match.score1 > match.score2 }">{{ match.team1 }}</div>
                <div class="match-score">
                  <span>{{ match.score1 }}</span>
                  <span class="score-dash">-</span>
                  <span>{{ match.score2 }}</span>
                </div>
                <div class="match-team text-left" :class="{ 'font-bold text-gold': match.score2 > match.score1 }">{{ match.team2 }}</div>
              </div>
            </div>
            <div class="ig-footer">@MuslimUmmahFC</div>
          </div>
          <!-- Top Scorers Sidebar -->
          <div class="sidebar-card" style="margin-top: 2rem;" ref="scorersCardRef">
            <div class="ig-watermark">
              <div class="ig-logo">UMMAH TWITTER FC 2026</div>
              <div class="ig-title">TOP GOAL SCORERS</div>
            </div>
            
            <div class="card-header-flex">
              <h3>Top Goal Scorers</h3>
              <button @click="downloadForIG(scorersCardRef, 'Ummah_FC_Scorers')" class="btn-download" :disabled="downloading">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              </button>
            </div>
            <div class="match-list">
              <div v-for="(scorer, idx) in topScorers" :key="idx" class="scorer-row">
                <div class="scorer-info">
                  <div class="scorer-name">{{ scorer.name }}</div>
                  <div class="scorer-nickname">"{{ scorer.nickname }}"</div>
                </div>
                <div class="scorer-goals">
                  <span class="goals-count">{{ scorer.goals }}</span>
                  <span class="goals-label">Goals</span>
                </div>
              </div>
            </div>
            <div class="ig-footer">@MuslimUmmahFC</div>
          </div>
        </div>
      </div>
    </main>
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

.standings-header {
  padding: 3rem 1rem;
  text-align: center;
  border-bottom: 1px solid #27523d;
  background: linear-gradient(to bottom, rgba(39, 82, 61, 0.1), transparent);
}

@media (min-width: 768px) {
  .standings-header {
    padding: 4rem 1.5rem;
  }
}

.standings-title {
  font-size: 2rem;
  font-weight: 900;
  margin-bottom: 1rem;
  color: #FFFFFF;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

@media (min-width: 768px) {
  .standings-title {
    font-size: 3rem;
  }
}

.standings-subtitle {
  font-size: 1.125rem;
  color: rgba(248, 250, 252, 0.8);
  max-width: 600px;
  margin: 0 auto;
}

.standings-main {
  padding: 2rem 1rem 4rem;
  flex: 1;
}

@media (min-width: 768px) {
  .standings-main {
    padding: 3rem 1.5rem 5rem;
  }
}

.standings-content {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

@media (min-width: 992px) {
  .standings-content {
    grid-template-columns: 2fr 1fr;
  }
}

.table-card, .sidebar-card {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  border-radius: 16px;
  padding: 1rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

@media (min-width: 768px) {
  .table-card, .sidebar-card {
    padding: 2rem;
  }
}

.table-wrapper {
  overflow-x: auto;
}

.standings-table {
  width: 100%;
  border-collapse: collapse;
  text-align: center;
  min-width: 600px;
}

.standings-table th {
  font-size: 0.75rem;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: rgba(248, 250, 252, 0.6);
  padding: 0.75rem 0.5rem;
  border-bottom: 2px solid rgba(39, 82, 61, 0.8);
}

@media (min-width: 768px) {
  .standings-table th {
    font-size: 0.875rem;
    padding: 1rem;
  }
}

.standings-table th:nth-child(2),
.standings-table td.team-col {
  text-align: left;
}

.standings-table td {
  padding: 1rem 0.5rem;
  border-bottom: 1px solid rgba(39, 82, 61, 0.4);
  font-weight: 600;
  font-size: 1rem;
}

@media (min-width: 768px) {
  .standings-table td {
    padding: 1.25rem 1rem;
    font-size: 1.125rem;
  }
}

.team-col {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #FFFFFF;
}

.team-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  flex-shrink: 0;
  box-shadow: 0 0 10px currentColor;
}

.rank-col {
  color: rgba(248, 250, 252, 0.5);
  font-weight: 700;
}

.pts-col {
  color: #D4AF37;
  font-weight: 800 !important;
  font-size: 1.125rem !important;
  background: rgba(212, 175, 55, 0.05);
}

@media (min-width: 768px) {
  .pts-col {
    font-size: 1.25rem !important;
  }
}

.first-place td {
  background: linear-gradient(to right, rgba(212, 175, 55, 0.1), transparent);
}

.table-legend {
  margin-top: 1.5rem;
  display: flex;
  gap: 1.5rem;
  justify-content: center;
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.6);
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.legend-item .dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.dot.win { background: #34d399; }
.dot.draw { background: #cbd5e1; }
.dot.loss { background: #f87171; }

.sidebar-card h3 {
  font-size: 1.5rem;
  color: #FFFFFF;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid rgba(39, 82, 61, 0.4);
  padding-bottom: 1rem;
}

.empty-state {
  color: rgba(248, 250, 252, 0.6);
  font-style: italic;
  text-align: center;
  padding: 2rem 0;
}

.match-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.match-row {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(39, 82, 61, 0.2);
  border-radius: 8px;
  border: 1px solid rgba(39, 82, 61, 0.4);
}

.match-team {
  font-size: 1.125rem;
  color: rgba(248, 250, 252, 0.9);
}

.text-right { text-align: right; }
.text-left { text-align: left; }
.font-bold { font-weight: 700; }
.text-gold { color: #D4AF37; }

.match-score {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  background: #052014;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-weight: 800;
  font-size: 1.25rem;
  color: #FFFFFF;
  min-width: 80px;
}

.score-dash {
  color: rgba(248, 250, 252, 0.4);
  font-weight: 400;
}

.scorer-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background: rgba(39, 82, 61, 0.2);
  border-radius: 8px;
  border: 1px solid rgba(39, 82, 61, 0.4);
}

.scorer-info {
  display: flex;
  flex-direction: column;
}

.scorer-name {
  font-weight: 700;
  color: #FFFFFF;
  font-size: 1.05rem;
}

.scorer-nickname {
  color: #D4AF37;
  font-size: 0.875rem;
  font-style: italic;
  margin-top: 0.25rem;
}

.scorer-goals {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: #052014;
  padding: 0.5rem;
  border-radius: 4px;
  min-width: 60px;
}

.goals-count {
  font-size: 1.25rem;
  font-weight: 800;
  color: #FFFFFF;
  line-height: 1;
}

.goals-label {
  font-size: 0.7rem;
  color: rgba(248, 250, 252, 0.6);
  text-transform: uppercase;
  margin-top: 0.25rem;
  letter-spacing: 0.05em;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

/* Download Button Styles */
.card-header-flex {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid rgba(39, 82, 61, 0.4);
  padding-bottom: 1rem;
}

.card-header-flex h3 {
  font-size: 1.5rem;
  color: #FFFFFF;
  margin: 0;
  border: none;
  padding: 0;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.btn-download {
  background: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.3);
  color: #D4AF37;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.btn-download svg {
  width: 16px;
  height: 16px;
}

.btn-download:hover:not(:disabled) {
  background: rgba(212, 175, 55, 0.2);
  border-color: rgba(212, 175, 55, 0.5);
  transform: translateY(-1px);
}

.btn-download:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Instagram Export Mode Styles */
.ig-watermark {
  display: none;
}
.ig-footer {
  display: none;
}

.ig-export-mode {
  padding: 3rem !important;
  background: linear-gradient(135deg, #052014 0%, #0a2d1d 100%) !important;
  border: none !important;
  border-radius: 0 !important;
  box-shadow: none !important;
  position: relative;
  /* Make sure it scales nicely, we enforce a semi-square aspect ratio if possible, 
     but html2canvas captures whatever the layout is. The padding helps. */
}

.ig-export-mode .btn-download {
  display: none !important;
}

.ig-export-mode .card-header-flex {
  border-bottom: none !important;
  margin-bottom: 0 !important;
  padding-bottom: 0 !important;
}

.ig-export-mode .card-header-flex h3 {
  display: none !important; /* Hide original titles in export, rely on watermark */
}

.ig-export-mode .ig-watermark {
  display: block;
  text-align: center;
  margin-bottom: 2.5rem;
}

.ig-export-mode .ig-logo {
  color: #D4AF37;
  font-weight: 900;
  font-size: 1.25rem;
  letter-spacing: 0.1em;
  margin-bottom: 0.5rem;
}

.ig-export-mode .ig-title {
  color: #FFFFFF;
  font-size: 2.5rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: -0.02em;
}

.ig-export-mode .ig-footer {
  display: block;
  text-align: center;
  margin-top: 3rem;
  color: rgba(248, 250, 252, 0.6);
  font-size: 1rem;
  font-weight: 600;
  letter-spacing: 0.05em;
}

.ig-export-mode .standings-table td, 
.ig-export-mode .standings-table th {
  padding: 1.5rem 1rem !important;
  font-size: 1.25rem !important;
}
</style>
