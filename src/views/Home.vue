<script setup>
import { ref, onMounted, onUnmounted, computed } from 'vue'
import { supabase } from '../lib/supabase.js'
import TwitterFeed from '../components/TwitterFeed.vue'

const selectedTeam = ref(null)

const teams = [
  {
    id: "umar",
    name: "Umar",
    color: "border-slate-300 text-slate-300 bg-slate-950/40",
    accent: "text-slate-300",
    character: "Silver Shield",
    description: "Representing strength and justice, Umar FC plays with rock-solid defense and tactical discipline.",
    history: "Taking inspiration from the second Caliph, Umar, known for his strength and distinction between truth and falsehood."
  },
  {
    id: "abubakar",
    name: "Abubakar",
    color: "border-cyan-400 text-cyan-400 bg-cyan-950/40",
    accent: "text-cyan-400",
    character: "Cyan Thunder",
    description: "Combining speed, grace, and composure, Abubakar FC dominates the pitch with fluid teamwork and precision passing.",
    history: "Named in honor of the first Caliph, Abubakar, reflecting truthfulness, loyalty, and unwavering devotion."
  },
  {
    id: "uthman",
    name: "Uthman",
    color: "border-emerald-500 text-emerald-400 bg-emerald-950/40",
    accent: "text-emerald-400",
    character: "Green Victory",
    description: "Generous in spirit but ruthless in attack, Uthman FC plays with high energy, creativity, and explosive counter-attacks.",
    history: "Inspired by the third Caliph, Uthman, symbolizing modesty, generosity, and community leadership."
  },
  {
    id: "aliy",
    name: "Aliy",
    color: "border-amber-400 text-amber-400 bg-amber-950/40",
    accent: "text-amber-400",
    character: "Golden Legacy",
    description: "Armed with tactical intelligence and courageous playmaking, Aliy FC commands the midfield and strikes with lethal efficiency.",
    history: "Honoring the fourth Caliph, Aliy, famous for his wisdom, bravery, and chivalry on and off the field."
  }
]

function selectTeam(teamId) {
  selectedTeam.value = selectedTeam.value === teamId ? null : teamId
}

const teamStats = ref([])

async function loadStats() {
  const { data, error } = await supabase
    .from('team_stats')
    .select('*')
    .order('pts', { ascending: false })
    .order('gd', { ascending: false })
    .order('gf', { ascending: false })
    
  if (!error && data) {
    teamStats.value = data
  }
}

let channel
onMounted(() => {
  loadStats()
  channel = supabase
    .channel('public:team_stats_home')
    .on('postgres_changes', { event: '*', schema: 'public', table: 'team_stats' }, () => {
      loadStats()
    })
    .subscribe()
})

onUnmounted(() => {
  if (channel) channel.unsubscribe()
})

const displayTeams = computed(() => {
  if (teamStats.value.length === 0) {
    return teams.map(t => ({
      name: t.name,
      dotColor: t.color.includes('cyan') ? '#22d3ee' :
                t.color.includes('amber') ? '#fbbf24' :
                t.color.includes('slate') ? '#cbd5e1' : '#34d399',
      played: '—', gd: '—', gf: '—', pts: '—'
    }))
  }
  
  return teamStats.value.map(stat => {
    const t = teams.find(x => x.name === stat.name)
    const dotColor = t ? (
      t.color.includes('cyan') ? '#22d3ee' :
      t.color.includes('amber') ? '#fbbf24' :
      t.color.includes('slate') ? '#cbd5e1' : '#34d399'
    ) : '#ffffff'
    return {
      ...stat,
      dotColor
    }
  }).sort((a, b) => {
    if (b.pts !== a.pts) return b.pts - a.pts
    if (b.gd !== a.gd) return b.gd - a.gd
    return b.gf - a.gf
  })
})
</script>

<template>
  <div class="home-page">
    <!-- Shared header rendered globally via App.vue -->

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-bg" style="background-image: url('/ummah_fc_hero.png');">
        <div class="hero-overlay-t"></div>
        <div class="hero-overlay-r"></div>
      </div>

      <div class="container hero-content animate-fade-in-up">
        <div style="max-width: 48rem;">
          <div class="hero-tag">
            <!-- Ticket Icon -->
            <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width: 0.875rem; height: 0.875rem;">
              <path d="M2 9a3 3 0 0 1 0 6v2a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-2a3 3 0 0 1 0-6V7a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z"/>
              <path d="M13 5v2"/>
              <path d="M13 17v2"/>
              <path d="M13 11v2"/>
            </svg>
            Free Spectator Entrance Pass Required
          </div>
          
          <h1 class="hero-title">
            <span class="brand-title" style="font-size: inherit; line-height: inherit; display: inline;">UMMAH TWITTER FC</span>
            <span class="hero-title-sub">BROTHERHOOD BEYOND THE PITCH</span>
          </h1>
          
          <p class="hero-text">
            Uniting Muslims through the beautiful game. Spectators must register online to gain entry to the stadium. All registered attendees receive an official <strong style="color: #D4AF37;">Certificate of Participation</strong> by email after the tournament!
          </p>
          
          <div class="hero-buttons">
            <router-link to="/register" class="gold-button" style="padding: 0.875rem 2rem; font-size: 1rem;">
              Register as Spectator
              <!-- Chevron Right Icon -->
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="width: 1.25rem; height: 1.25rem;">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </router-link>
            <router-link to="/schedule" class="outline-gold-button" style="padding: 0.875rem 2rem; font-size: 1rem;">
              View Game Schedule
            </router-link>
            <router-link to="/about" class="outline-gold-button" style="padding: 0.875rem 2rem; font-size: 1rem; border-color: rgba(248, 250, 252, 0.3); color: #F8FAFC;">
              About Us
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- Info Quick Overview -->
    <section class="info-cards">
      <div class="container">
        <div class="info-grid">
          <div class="info-card">
            <div class="info-icon-wrapper">
              <!-- Calendar Icon -->
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1.5rem; height: 1.5rem;">
                <path d="M8 2v4"/>
                <path d="M16 2v4"/>
                <rect width="18" height="18" x="3" y="4" rx="2"/>
                <path d="M3 10h18"/>
              </svg>
            </div>
            <div>
              <p class="info-label">Annual League Match</p>
              <h4 class="info-title">Saturday, June 6th, 2026</h4>
              <p class="info-desc">Kick-off: 8:00 AM Prompt</p>
            </div>
          </div>

          <a href="https://www.google.com/maps/place/Landmark+College,+Ikorodu/data=!4m2!3m1!1s0x0:0x5f683c00ec0c6aeb?sa=X&ved=1t:2428&ictx=111" target="_blank" rel="noopener noreferrer" class="info-card map-card">
            <div class="info-icon-wrapper">
              <!-- MapPin Icon -->
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1.5rem; height: 1.5rem;">
                <path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/>
                <circle cx="12" cy="10" r="3"/>
              </svg>
            </div>
            <div>
              <p class="info-label">Match Venue ↗</p>
              <h4 class="info-title">Landmark College</h4>
              <p class="info-desc">Ikorodu, Lagos, Nigeria</p>
            </div>
          </a>

          <router-link to="/register" class="info-card map-card">
            <div class="info-icon-wrapper">
              <!-- Mail Icon -->
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1.5rem; height: 1.5rem;">
                <rect width="20" height="16" x="2" y="4" rx="2"/>
                <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
              </svg>
            </div>
            <div>
              <p class="info-label">Attendee Gift ↗</p>
              <h4 class="info-title">Participant Certificate</h4>
              <p class="info-desc">Claim your pass to receive it</p>
            </div>
          </router-link>
        </div>
      </div>
    </section>

    <!-- League Standings Section -->
    <section class="section" style="padding-top: 0; padding-bottom: 2rem;">
      <div class="container">
        <div class="section-header" style="margin-bottom: 2rem;">
          <h2 class="section-title">LEAGUE STANDINGS</h2>
          <div class="section-divider"></div>
        </div>
        
        <div style="max-width: 48rem; margin: 0 auto; background-color: #0a2d1d; border: 1px solid #27523d; border-radius: 16px; padding: 2rem; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);">
          <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; text-align: left;">
              <thead>
                <tr>
                  <th style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; color: rgba(248, 250, 252, 0.6); padding-bottom: 1rem;">Teams</th>
                  <th style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; color: rgba(248, 250, 252, 0.6); padding-bottom: 1rem;">PLD</th>
                  <th style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; color: rgba(248, 250, 252, 0.6); padding-bottom: 1rem;">GD</th>
                  <th style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; color: rgba(248, 250, 252, 0.6); padding-bottom: 1rem;">GF</th>
                  <th style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.05em; color: rgba(248, 250, 252, 0.6); padding-bottom: 1rem;">PTS</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="team in displayTeams" :key="team.name">
                  <td style="padding: 1rem 0; border-top: 1px solid rgba(39, 82, 61, 0.4); font-weight: 600; display: flex; align-items: center; gap: 0.75rem; color: #FFFFFF;">
                    <span style="width: 0.5rem; height: 0.5rem; border-radius: 50%; flex-shrink: 0;" :style="{ backgroundColor: team.dotColor }"></span>
                    {{ team.name }} FC
                  </td>
                  <td style="padding: 1rem 0; border-top: 1px solid rgba(39, 82, 61, 0.4); font-weight: 600;">{{ team.played }}</td>
                  <td style="padding: 1rem 0; border-top: 1px solid rgba(39, 82, 61, 0.4); font-weight: 600;">{{ team.gd }}</td>
                  <td style="padding: 1rem 0; border-top: 1px solid rgba(39, 82, 61, 0.4); font-weight: 600;">{{ team.gf }}</td>
                  <td style="padding: 1rem 0; border-top: 1px solid rgba(39, 82, 61, 0.4); font-weight: 600; color: #D4AF37;">{{ team.pts }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div style="margin-top: 1.5rem; text-align: center;">
            <router-link to="/schedule" class="outline-gold-button" style="padding: 0.75rem 1.5rem; font-size: 0.875rem;">
              View Full Match Schedule
            </router-link>
          </div>
        </div>
      </div>
    </section>

    <!-- The 4 Teams Contenders Section -->
    <section id="teams" class="section teams-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">THE FOUR LEAGUE TEAMS</h2>
          <div class="section-divider"></div>
          <p class="section-subtitle">
            Named after the four Rightly Guided Caliphs, representing the pillars of Islamic legacy.
          </p>
        </div>

        <div class="teams-grid">
          <div 
            v-for="team in teams" 
            :key="team.id"
            @click="selectTeam(team.id)"
            class="team-card"
            :class="[team.color, { selected: selectedTeam === team.id }]"
          >
            <div>
              <div class="team-card-header">
                <span style="font-size: 1.875rem">🛡️</span>
                <span class="team-card-badge">Team</span>
              </div>
              <h3 class="team-card-title">{{ team.name }}</h3>
              <p class="team-card-char" :class="team.accent">{{ team.character }}</p>
              <p class="team-card-desc">{{ team.description }}</p>
            </div>
            
            <div class="team-card-footer">
              {{ selectedTeam === team.id ? "Show Less" : "Learn Brand Origin" }}
              <!-- Chevron Right Icon -->
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 0.875rem; height: 0.875rem;">
                <path d="m9 18 6-6-6-6"/>
              </svg>
            </div>

            <!-- Expanded Info Drawer/Panel on Click -->
            <transition name="fade">
              <div v-if="selectedTeam === team.id" class="expanded-panel" @click.stop>
                <div>
                  <h4 class="expanded-title">{{ team.name }} FC</h4>
                  <p class="expanded-char">"{{ team.character }}"</p>
                  <p class="expanded-history">{{ team.history }}</p>
                </div>
                <button 
                  @click="selectedTeam = null"
                  class="expanded-close-btn"
                >
                  Close Details
                </button>
              </div>
            </transition>
          </div>
        </div>

        <div style="margin-top: 3rem; padding: 1.5rem; border-radius: 8px; background-color: #0a2d1d; border: 1px solid #27523d; text-align: center; max-width: 42rem; margin-left: auto; margin-right: auto; display: flex; flex-direction: column; align-items: center; gap: 1rem;">
          <img src="/logo.jpg" alt="Official Ummah FC Logo" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 2px solid #D4AF37;" />
          <p style="font-size: 0.875rem; color: rgba(248, 250, 252, 0.8); margin: 0;">
            <strong style="color: #D4AF37">Branding Note:</strong> As defined in Appendix 3 of the constitution, a <strong style="color: #FFFFFF">unified Ummah logo</strong> representing our collective brotherhood is utilized by all teams.
          </p>
        </div>
      </div>
    </section>



    <!-- Live Tweet Feed -->
    <TwitterFeed />

    <!-- Twitter/X CTA Banner -->
    <section class="section tweet-section">
      <div class="container">
        <div class="tweet-banner">
          <div class="tweet-banner-glow"></div>
          <div class="tweet-banner-content">
            <div class="tweet-x-icon">
              <!-- X/Twitter logo -->
              <svg viewBox="0 0 24 24" fill="currentColor" style="width: 2.5rem; height: 2.5rem;">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.742l7.742-8.855L1.564 2.25h6.391l4.254 5.622 5.834-5.622Zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
              </svg>
            </div>
            <div class="tweet-banner-text">
              <h2 class="tweet-banner-title">Join the Conversation</h2>
              <p class="tweet-banner-sub">Share the excitement on X (Twitter) — follow us and tag your posts!</p>
              <div class="tweet-tags">
                <span class="tweet-tag-pill hashtag">#UmmahTwitterMatch2026</span>
                <span class="tweet-tag-pill handle">@MuslimUmmahFC</span>
              </div>
            </div>
            <div class="tweet-banner-actions">
              <a
                :href="`https://twitter.com/intent/tweet?text=${encodeURIComponent('🔥 The Ummah Twitter FC match is happening! Follow @MuslimUmmahFC for live updates and join the conversation. #UmmahTwitterMatch2026')}`"
                target="_blank"
                rel="noopener noreferrer"
                class="tweet-btn"
              >
                <svg viewBox="0 0 24 24" fill="currentColor" style="width: 1.1rem; height: 1.1rem;">
                  <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.742l7.742-8.855L1.564 2.25h6.391l4.254 5.622 5.834-5.622Zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                </svg>
                Tweet This
              </a>
              <a
                href="https://x.com/MuslimUmmahFC"
                target="_blank"
                rel="noopener noreferrer"
                class="follow-btn"
              >
                Follow @MuslimUmmahFC
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
*, *::before, *::after {
  box-sizing: border-box;
}

/* Container */
.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  max-width: 1280px;
}

/* Base Styles */
.home-page {
  min-height: 100vh;
  background-color: #052014;
  color: #F8FAFC;
  overflow-x: hidden;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Nav Bar */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
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
  cursor: pointer;
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
.nav-links button,
.nav-link-a {
  background: none;
  border: none;
  color: #F8FAFC;
  cursor: pointer;
  font-weight: 500;
  transition: color 0.2s;
  font-size: inherit;
  text-decoration: none;
}
.nav-links button:hover,
.nav-link-a:hover {
  color: #D4AF37;
}

/* Buttons */
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
  gap: 0.5rem;
}
.gold-button:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
  background: linear-gradient(135deg, #FFE082 0%, #E8C14A 50%, #CFA52D 100%);
}
.gold-button:active {
  transform: translateY(1px);
}

.outline-gold-button {
  background: transparent;
  color: #D4AF37;
  border: 1px solid rgba(212, 175, 55, 0.4);
  border-radius: 999px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s ease;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}
.outline-gold-button:hover {
  background-color: rgba(212, 175, 55, 0.1);
  border-color: #D4AF37;
}

/* Hero Section */
.hero {
  position: relative;
  min-height: 90vh;
  display: flex;
  align-items: center;
  padding-top: 6rem;
  padding-bottom: 5rem;
  overflow: hidden;
}
.hero-bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  z-index: 0;
}
.hero-overlay-t {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, #052014 0%, rgba(5, 32, 20, 0.7) 70%, rgba(5, 32, 20, 0.5) 100%);
}
.hero-overlay-r {
  position: absolute;
  inset: 0;
  background: linear-gradient(to right, #052014 0%, transparent 100%);
}
.hero-content {
  position: relative;
  z-index: 10;
  margin-top: 2rem;
}
.hero-tag {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.375rem 0.875rem;
  border-radius: 9999px;
  background-color: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.3);
  color: #D4AF37;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}
.hero-title {
  font-size: clamp(2.5rem, 8vw, 4.5rem);
  font-weight: 900;
  margin-bottom: 1.5rem;
  line-height: 1.1;
}
.hero-title-sub {
  font-size: clamp(1.5rem, 5vw, 3rem);
  font-weight: 800;
  color: #FFFFFF;
  margin-top: 0.5rem;
  display: block;
}
.hero-text {
  font-size: clamp(1rem, 2vw, 1.25rem);
  color: rgba(248, 250, 252, 0.85);
  margin-bottom: 2.5rem;
  max-width: 42rem;
  line-height: 1.6;
}
.hero-buttons {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
@media (min-width: 640px) {
  .hero-buttons {
    flex-direction: row;
  }
}

/* Info Overview Cards */
.info-cards {
  position: relative;
  z-index: 20;
  margin-top: -2.5rem;
  margin-bottom: 2.5rem;
}
.info-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}
@media (min-width: 768px) {
  .info-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
.info-card {
  background-color: rgba(10, 45, 29, 0.9);
  border: 1px solid rgba(39, 82, 61, 0.6);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  gap: 1.25rem;
}
.info-icon-wrapper {
  width: 3rem;
  height: 3rem;
  border-radius: 8px;
  background-color: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #D4AF37;
  flex-shrink: 0;
}
.info-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #D4AF37;
  font-weight: 600;
}
.info-title {
  font-weight: 700;
  font-size: 1.125rem;
  color: #FFFFFF;
  margin-top: 0.25rem;
}
.info-desc {
  font-size: 0.75rem;
  color: rgba(248, 250, 252, 0.75);
  margin-top: 0.125rem;
}

/* General Section styles */
.section {
  padding-top: 6rem;
  padding-bottom: 6rem;
  border-top: 1px solid #27523d;
}
.section-header {
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  margin-bottom: 4rem;
}
.section-title {
  font-size: clamp(1.75rem, 4vw, 3rem);
  font-weight: 900;
  color: #FFFFFF;
  margin-bottom: 1rem;
}
.section-divider {
  height: 4px;
  width: 5rem;
  background-color: #D4AF37;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 1.5rem;
  border-radius: 2px;
}
.section-subtitle {
  color: rgba(248, 250, 252, 0.8);
  font-size: 1.125rem;
  font-weight: 500;
}

/* About Section */
.about-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
}
@media (min-width: 1024px) {
  .about-grid {
    grid-template-columns: 1.2fr 1fr;
  }
}
.about-card {
  background-color: #0a2d1d;
  padding: 2rem;
  border-radius: 12px;
  border: 1px solid #27523d;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}
.about-card-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #D4AF37;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.about-card-text {
  color: rgba(248, 250, 252, 0.75);
  line-height: 1.7;
}
.mission-vision-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  margin-top: 2rem;
}
@media (min-width: 640px) {
  .mission-vision-grid {
    grid-template-columns: 1fr 1fr;
  }
}
.pillar-card {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
  position: relative;
  overflow: hidden;
}
.pillar-bg-glow {
  position: absolute;
  top: 0;
  right: 0;
  width: 8rem;
  height: 8rem;
  background-color: rgba(212, 175, 55, 0.05);
  border-radius: 9999px;
  filter: blur(24px);
}
.pillar-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #FFFFFF;
  border-bottom: 1px solid #27523d;
  padding-bottom: 1rem;
  margin-bottom: 1.5rem;
}
.pillar-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.pillar-item {
  display: flex;
  gap: 1rem;
}
.pillar-num {
  color: #D4AF37;
  font-weight: 700;
  font-size: 1.125rem;
}
.pillar-name {
  font-weight: 600;
  color: #FFFFFF;
}
.pillar-desc {
  font-size: 0.75rem;
  color: rgba(248, 250, 252, 0.7);
  margin-top: 0.25rem;
  line-height: 1.5;
}
.pillar-footer {
  padding-top: 1rem;
  margin-top: 1.5rem;
  border-top: 1px solid #27523d;
  text-align: center;
  font-size: 0.875rem;
  color: #D4AF37;
  font-style: italic;
  font-weight: 600;
}

/* Teams Section */
.teams-section {
  background-color: #03170e;
}
.teams-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}
@media (min-width: 640px) {
  .teams-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 1024px) {
  .teams-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
.team-card {
  cursor: pointer;
  padding: 1.5rem;
  border: 2px solid;
  border-radius: 12px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.team-card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}
.team-card-badge {
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 700;
  color: #D4AF37;
  background-color: rgba(212, 175, 55, 0.1);
  padding: 0.25rem 0.625rem;
  border-radius: 9999px;
}
.team-card-title {
  font-size: 1.875rem;
  font-weight: 900;
  margin-bottom: 0.25rem;
}
.team-card-char {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
}
.team-card-desc {
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.8);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}
.team-card-footer {
  border-top: 1px solid rgba(39, 82, 61, 0.6);
  padding-top: 1rem;
  margin-top: auto;
  font-size: 0.75rem;
  font-weight: 600;
  color: #D4AF37;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

/* Expanded Card Panel */
.expanded-panel {
  position: absolute;
  inset: 0;
  background-color: #052014;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  z-index: 10;
}
.expanded-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #D4AF37;
  margin-bottom: 0.5rem;
}
.expanded-char {
  font-size: 0.75rem;
  color: rgba(248, 250, 252, 0.9);
  font-weight: 600;
  font-style: italic;
  margin-bottom: 1rem;
}
.expanded-history {
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.8);
  line-height: 1.6;
}
.expanded-close-btn {
  margin-top: 1.5rem;
  font-size: 0.75rem;
  font-weight: 700;
  text-align: center;
  color: #FFFFFF;
  background-color: #27523d;
  border: none;
  padding: 0.5rem;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s;
  width: 100%;
}
.expanded-close-btn:hover {
  background-color: #D4AF37;
  color: #052014;
}

/* Card States */
.team-card.selected {
  transform: scale(1.05);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
}
.team-card:hover:not(.selected) {
  transform: translateY(-4px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}



/* Exco Section */
.exco-section {
  background-color: #03170e;
}
.exco-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}
@media (min-width: 768px) {
  .exco-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (min-width: 1024px) {
  .exco-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
.exco-card {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  padding: 1.5rem;
  border-radius: 12px;
  position: relative;
  overflow: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
}
.exco-card-border {
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background-color: #D4AF37;
  transform: scaleY(0);
  transition: transform 0.3s ease;
}
.exco-card:hover .exco-card-border {
  transform: scaleY(1);
}
.exco-card:hover {
  border-color: rgba(212, 175, 55, 0.5);
  transform: translateY(-2px);
}
.exco-role {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #D4AF37;
  margin-bottom: 0.5rem;
}
.exco-name {
  font-size: 1.125rem;
  font-weight: 900;
  color: #FFFFFF;
  margin-bottom: 0.75rem;
}
.exco-duties {
  font-size: 0.75rem;
  color: rgba(248, 250, 252, 0.7);
  line-height: 1.6;
  border-top: 1px solid rgba(39, 82, 61, 0.6);
  padding-top: 0.75rem;
}

/* Constitution section */
.const-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  max-width: 64rem;
  margin-left: auto;
  margin-right: auto;
}
@media (min-width: 1024px) {
  .const-grid {
    grid-template-columns: 1fr 2fr;
  }
}
.const-sidebar {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
.const-tab-btn {
  text-align: left;
  padding: 1rem;
  border-radius: 8px;
  border: 1px solid #27523d;
  font-weight: 700;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.const-tab-btn.active {
  background-color: #D4AF37;
  color: #052014;
  border-color: #D4AF37;
}
.const-tab-btn:not(.active) {
  background-color: #0a2d1d;
  color: rgba(248, 250, 252, 0.8);
}
.const-tab-btn:not(.active):hover {
  background-color: rgba(10, 45, 29, 0.6);
  color: #FFFFFF;
}
.const-content {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  min-height: 300px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.const-content-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #FFFFFF;
  border-bottom: 1px solid #27523d;
  padding-bottom: 1rem;
  margin-bottom: 1.5rem;
}
.const-points {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.const-point {
  display: flex;
  gap: 0.75rem;
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.8);
  line-height: 1.6;
}
.const-bullet {
  color: #D4AF37;
  font-weight: 700;
}
.const-footer {
  font-size: 11px;
  color: #6e6d80;
  text-align: right;
  margin-top: 2rem;
  font-weight: 500;
}

/* Pricing Section */
.pricing-section {
  background-color: #03170e;
}
.pricing-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  max-width: 64rem;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 4rem;
}
@media (min-width: 1024px) {
  .pricing-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
.pricing-card {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  padding: 2rem;
  border-radius: 12px;
  text-align: center;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.3s ease;
}
.pricing-card.spectator {
  border: 2px solid #D4AF37;
  box-shadow: 0 10px 30px rgba(212, 175, 55, 0.15);
}
.pricing-card:hover:not(.spectator) {
  border-color: #D4AF37;
}
.pricing-badge {
  position: absolute;
  top: 0;
  right: 0;
  background-color: #D4AF37;
  color: #052014;
  font-size: 9px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 0.25rem 0.75rem;
  border-radius: 0 0 0 8px;
}
.pricing-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 9999px;
  background-color: rgba(212, 175, 55, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #D4AF37;
  margin: 0 auto 1rem;
}
.pricing-card.spectator .pricing-icon {
  background-color: rgba(212, 175, 55, 0.15);
  border: 1px solid rgba(212, 175, 55, 0.45);
}
.pricing-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #FFFFFF;
  margin-bottom: 0.25rem;
}
.pricing-subtitle {
  font-size: 0.75rem;
  color: #D4AF37;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
}
.pricing-price {
  font-size: 2.25rem;
  font-weight: 900;
  color: #FFFFFF;
  margin-bottom: 1.5rem;
}
.pricing-features {
  text-align: left;
  border-top: 1px solid rgba(39, 82, 61, 0.6);
  padding-top: 1.5rem;
  margin-bottom: 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.875rem;
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.8);
}
.pricing-feature-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.pricing-feature-item span {
  color: #D4AF37;
}

/* Payment Card */
.payment-card {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  padding: 2rem;
  border-radius: 12px;
  max-width: 42rem;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  scroll-margin-top: 5rem;
}
.payment-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #FFFFFF;
  border-bottom: 1px solid #27523d;
  padding-bottom: 1rem;
  margin-bottom: 1.5rem;
  text-align: center;
}
.payment-details {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
  text-align: center;
}
@media (min-width: 768px) {
  .payment-details {
    grid-template-columns: repeat(3, 1fr);
    text-align: left;
  }
}
.payment-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: #D4AF37;
  font-weight: 600;
  letter-spacing: 0.05em;
  margin-bottom: 0.25rem;
  display: block;
}
.payment-value {
  font-weight: 700;
  font-size: 1.125rem;
  color: #FFFFFF;
}
.payment-value.account-number {
  letter-spacing: 0.1em;
}
.payment-notice {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(39, 82, 61, 0.6);
  font-size: 0.75rem;
  color: rgba(248, 250, 252, 0.7);
  line-height: 1.6;
  text-align: center;
}

/* Footer styling */
.footer {
  background-color: #052014;
  border-top: 1px solid #27523d;
  padding-top: 4rem;
  padding-bottom: 2rem;
}
.footer-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-bottom: 3rem;
}
@media (min-width: 768px) {
  .footer-grid {
    grid-template-columns: 2fr 1fr 1fr 1fr;
  }
}
.footer-nav-btn {
  background: none;
  border: none;
  color: inherit;
  font-family: inherit;
  font-size: inherit;
  cursor: pointer;
  padding: 0;
  text-align: left;
  transition: color 0.2s;
}
.footer-nav-btn:hover {
  color: #D4AF37;
}
.info-card.map-card {
  text-decoration: none;
  transition: transform 0.2s, border-color 0.2s;
}
.info-card.map-card:hover {
  border-color: #D4AF37;
  transform: translateY(-2px);
}
.footer-about {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-size: 1.5rem;
  font-weight: 900;
  background: linear-gradient(to right, #F3C64F, #A07817);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.footer-desc {
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.75);
  line-height: 1.6;
  max-width: 24rem;
}
.footer-tagline {
  font-size: 0.75rem;
  color: #D4AF37;
  font-weight: 600;
  letter-spacing: 0.05em;
}
.footer-title {
  font-size: 0.875rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #FFFFFF;
  margin-bottom: 1rem;
}
.footer-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.75);
  padding: 0;
  margin: 0;
}
.footer-links li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.footer-links a {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s;
}
.footer-links a:hover {
  color: #D4AF37;
}
.footer-support {
  font-size: 0.75rem;
  border-top: 1px solid #27523d;
  padding-top: 0.5rem;
  margin-top: 0.5rem;
}
.footer-support a {
  color: #D4AF37;
  text-decoration: underline;
}
.footer-hashtags {
  font-size: 0.75rem;
  color: rgba(248, 250, 252, 0.6);
  line-height: 1.5;
}
.footer-hashtag-bold {
  display: block;
  margin-top: 0.25rem;
  font-weight: 700;
  color: #FFFFFF;
}

.footer-bottom {
  border-top: 1px solid rgba(39, 82, 61, 0.6);
  padding-top: 2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  font-size: 0.75rem;
  color: rgba(248, 250, 252, 0.6);
}
@media (min-width: 640px) {
  .footer-bottom {
    flex-direction: row;
  }
}

.footer-built-by {
  font-size: 0.7rem;
  color: rgba(248, 250, 252, 0.45);
  font-style: italic;
}
.footer-built-by-names {
  font-style: normal;
  font-weight: 700;
  background: linear-gradient(to right, #F3C64F, #A07817);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.icon {
  display: inline-block;
  vertical-align: middle;
}
</style>
