<script setup>
import { ref } from 'vue'

const pointsKey = [
  { label: 'WIN', points: 3, class: 'win' },
  { label: 'DRAW', points: 2, class: 'draw' },
  { label: 'LOSE', points: 1, class: 'lose' }
]

const teams = [
  { name: 'Abubakar', color: 'border-cyan-400 text-cyan-400 bg-cyan-950/40', dotColor: '#22d3ee' },
  { name: 'Aliy', color: 'border-amber-400 text-amber-400 bg-amber-950/40', dotColor: '#fbbf24' },
  { name: 'Umar', color: 'border-slate-300 text-slate-300 bg-slate-950/40', dotColor: '#cbd5e1' },
  { name: 'Uthman', color: 'border-emerald-500 text-emerald-400 bg-emerald-950/40', dotColor: '#34d399' }
]

const schedule = [
  { home: 'Aliy', away: 'Uthman', homeColor: '#fbbf24', awayColor: '#34d399', fh: '20 mins', rest: '5 mins', sh: '20 mins', total: '45 mins' },
  { home: 'Umar', away: 'Abubakar', homeColor: '#cbd5e1', awayColor: '#22d3ee', fh: '20 mins', rest: '5 mins', sh: '20 mins', total: '45 mins' },
  { home: 'Aliy', away: 'Umar', homeColor: '#fbbf24', awayColor: '#cbd5e1', fh: '20 mins', rest: '5 mins', sh: '20 mins', total: '45 mins' },
  { home: 'Abubakar', away: 'Aliy', homeColor: '#22d3ee', awayColor: '#fbbf24', fh: '20 mins', rest: '5 mins', sh: '20 mins', total: '45 mins' },
  { home: 'Uthman', away: 'Abubakar', homeColor: '#34d399', awayColor: '#22d3ee', fh: '20 mins', rest: '5 mins', sh: '20 mins', total: '45 mins' },
  { home: 'Umar', away: 'Uthman', homeColor: '#cbd5e1', awayColor: '#34d399', fh: '20 mins', rest: '5 mins', sh: '20 mins', total: '45 mins' }
]
</script>

<template>
  <div class="schedule-page">
    <!-- Shared header rendered globally via App.vue -->

    <!-- Main Content -->
    <main class="container content-wrapper">
      <header class="schedule-header animate-fade-in-up">
        <div class="event-tag">Football League Schedule</div>
        <h1 class="main-title">MUSLIM TWITTER FOOTBALL EXHIBITION MATCH</h1>
        <p class="subtitle">SATURDAY 6TH JUNE 2026 • 10:00 AM - 4:00 PM</p>
      </header>

      <!-- Key Info Bar -->
      <section class="info-row">
        <div class="info-metric">
          <span class="metric-value">6 Hours</span>
          <span class="metric-label">Exhibition Event</span>
        </div>
        <div class="info-metric highlight">
          <span class="metric-value">4.3 Hours</span>
          <span class="metric-label">Game Time Total</span>
        </div>
        <div class="info-metric">
          <span class="metric-value">5 Hours</span>
          <span class="metric-label">Networking & Trade</span>
        </div>
      </section>

      <div class="grid-layout">
        <!-- Left Column: Table & Rules -->
        <div class="left-col">
          <!-- Standings Table -->
          <div class="card">
            <h3 class="card-title">League Standings</h3>
            <div class="table-container">
              <table class="standings-table">
                <thead>
                  <tr>
                    <th>Teams</th>
                    <th>PLD</th>
                    <th>GD</th>
                    <th>GF</th>
                    <th>PTS</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="team in teams" :key="team.name">
                    <td class="team-cell">
                      <span class="team-dot" :style="{ backgroundColor: team.dotColor }"></span>
                      {{ team.name }} FC
                    </td>
                    <td>—</td>
                    <td>—</td>
                    <td>—</td>
                    <td>—</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <div style="margin-top: 1.5rem; display: flex; flex-direction: column; gap: 0.75rem;">
              <p class="table-note" style="margin-top: 0;">
                * Each team plays 3 games. The team with the highest points tally wins the league.
              </p>
              <a href="https://www.google.com/maps/place/Landmark+College,+Ikorodu/data=!4m2!3m1!1s0x0:0x5f683c00ec0c6aeb?sa=X&ved=1t:2428&ictx=111" target="_blank" rel="noopener noreferrer" class="gold-button" style="width: 100%; text-decoration: none; padding: 0.75rem 1rem; border-radius: 8px;">
                <!-- MapPin Icon -->
                <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1rem; height: 1rem;">
                  <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                Get Directions to Venue
              </a>
            </div>
          </div>

          <!-- Points Key Card -->
          <div class="card key-card">
            <h3 class="card-title">League Scoring Key</h3>
            <div class="key-grid">
              <div v-for="item in pointsKey" :key="item.label" class="key-item" :class="item.class">
                <span class="key-points">{{ item.points }}</span>
                <span class="key-label">{{ item.label }}</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Right Column: Game Schedule -->
        <div class="right-col">
          <div class="card schedule-card">
            <h3 class="card-title">Match Fixtures</h3>
            
            <div class="fixtures-list">
              <div v-for="(match, index) in schedule" :key="index" class="fixture-item">
                <div class="fixture-main">
                  <span class="fixture-number">Game {{ index + 1 }}</span>
                  <div class="matchup">
                    <div class="matchup-team">
                      <span class="team-dot" :style="{ backgroundColor: match.homeColor }"></span>
                      <span class="team-name">{{ match.home }}</span>
                    </div>
                    <span class="vs-text">VS</span>
                    <div class="matchup-team">
                      <span class="team-dot" :style="{ backgroundColor: match.awayColor }"></span>
                      <span class="team-name">{{ match.away }}</span>
                    </div>
                  </div>
                </div>
                
                <div class="fixture-details">
                  <div class="duration-pill">
                    <span class="duration-label">1st Half</span>
                    <span class="duration-val">{{ match.fh }}</span>
                  </div>
                  <div class="duration-pill rest">
                    <span class="duration-label">Rest</span>
                    <span class="duration-val">{{ match.rest }}</span>
                  </div>
                  <div class="duration-pill">
                    <span class="duration-label">2nd Half</span>
                    <span class="duration-val">{{ match.sh }}</span>
                  </div>
                  <div class="duration-pill total">
                    <span class="duration-label">Total</span>
                    <span class="duration-val">{{ match.total }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<style scoped>
.schedule-page {
  min-height: 100vh;
  background-color: #052014;
  color: #F8FAFC;
  overflow-x: hidden;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  padding-bottom: 5rem;
}

/* Nav Bar */
.navbar {
  position: sticky;
  top: 0;
  z-index: 50;
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
.back-home-btn {
  background-color: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.3);
  color: #D4AF37;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 700;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.2s ease;
}
.back-home-btn:hover {
  background-color: #D4AF37;
  color: #052014;
}

/* Main Content */
.content-wrapper {
  margin-top: 6rem;
}

.schedule-header {
  text-align: center;
  margin-bottom: 3rem;
}
.event-tag {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #D4AF37;
  background-color: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.3);
  padding: 0.375rem 0.875rem;
  border-radius: 9999px;
  margin-bottom: 1rem;
}
.main-title {
  font-size: clamp(1.75rem, 4vw, 2.75rem);
  font-weight: 900;
  line-height: 1.2;
  margin-bottom: 0.5rem;
}
.subtitle {
  font-size: 1rem;
  color: rgba(248, 250, 252, 0.75);
  font-weight: 600;
}

/* Info Metrics Row */
.info-row {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  margin-bottom: 3rem;
}
@media (min-width: 768px) {
  .info-row {
    grid-template-columns: repeat(3, 1fr);
  }
}
.info-metric {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 0.25rem;
}
.info-metric.highlight {
  border-color: #D4AF37;
  background-color: rgba(212, 175, 55, 0.05);
}
.metric-value {
  font-size: 1.75rem;
  font-weight: 900;
  color: #FFFFFF;
}
.info-metric.highlight .metric-value {
  color: #D4AF37;
}
.metric-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: rgba(248, 250, 252, 0.6);
}

/* Grid Layout */
.grid-layout {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
}
@media (min-width: 1024px) {
  .grid-layout {
    grid-template-columns: 1fr 1.2fr;
  }
}

.left-col {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

/* Cards */
.card {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
.card-title {
  font-size: 1.25rem;
  font-weight: 800;
  color: #FFFFFF;
  margin-bottom: 1.5rem;
  border-bottom: 1px solid rgba(39, 82, 61, 0.6);
  padding-bottom: 0.75rem;
}

/* Standings Table */
.table-container {
  overflow-x: auto;
}
.standings-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}
.standings-table th {
  font-size: 0.75rem;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: rgba(248, 250, 252, 0.6);
  padding-bottom: 1rem;
}
.standings-table td {
  padding: 1rem 0;
  border-top: 1px solid rgba(39, 82, 61, 0.4);
  font-weight: 600;
}
.team-cell {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: #FFFFFF;
}
.team-dot {
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 50%;
  flex-shrink: 0;
}
.table-note {
  margin-top: 1.5rem;
  font-size: 0.75rem;
  color: rgba(248, 250, 252, 0.5);
  line-height: 1.5;
}

/* Scoring Key Card */
.key-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  text-align: center;
}
.key-item {
  padding: 1rem;
  border-radius: 12px;
  background-color: #052014;
  border: 1px solid #27523d;
}
.key-points {
  font-size: 1.5rem;
  font-weight: 900;
  display: block;
}
.key-item.win .key-points { color: #3dd68c; }
.key-item.draw .key-points { color: #4ba8e8; }
.key-item.lose .key-points { color: #f59e0b; }
.key-label {
  font-size: 0.675rem;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #FFFFFF;
  margin-top: 0.25rem;
  display: block;
}

/* Fixtures List */
.fixtures-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.fixture-item {
  background-color: #052014;
  border: 1px solid #27523d;
  border-radius: 12px;
  padding: 1.25rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.fixture-main {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(39, 82, 61, 0.4);
  padding-bottom: 0.75rem;
}
.fixture-number {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  color: #D4AF37;
  letter-spacing: 0.05em;
}
.matchup {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.matchup-team {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.team-name {
  font-weight: 700;
  font-size: 0.95rem;
  color: #FFFFFF;
}
.vs-text {
  font-size: 0.75rem;
  font-weight: 800;
  color: #D4AF37;
}

.fixture-details {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 0.5rem;
  text-align: center;
}
.duration-pill {
  background-color: rgba(39, 82, 61, 0.3);
  padding: 0.5rem;
  border-radius: 8px;
  border: 1px solid rgba(39, 82, 61, 0.5);
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
}
.duration-pill.rest {
  background-color: rgba(245, 158, 11, 0.05);
  border-color: rgba(245, 158, 11, 0.2);
  color: #f59e0b;
}
.duration-pill.total {
  background-color: rgba(212, 175, 55, 0.1);
  border-color: rgba(212, 175, 55, 0.3);
  color: #D4AF37;
}
.duration-label {
  font-size: 9px;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.05em;
  opacity: 0.7;
}
.duration-pill.rest .duration-label,
.duration-pill.total .duration-label {
  opacity: 1;
}
.duration-val {
  font-size: 0.75rem;
  font-weight: 700;
}

/* Animations */
.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
}
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.icon {
  display: inline-block;
  vertical-align: middle;
}

.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  max-width: 1280px;
}

.gold-button {
  background: linear-gradient(135deg, #F3C64F 0%, #D4AF37 50%, #B89020 100%);
  color: #052014;
  border: none;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.25);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}
.gold-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
  background: linear-gradient(135deg, #FFE082 0%, #E8C14A 50%, #CFA52D 100%);
}
</style>
