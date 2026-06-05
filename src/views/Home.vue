<script setup>
import { ref } from 'vue'

const activeTab = ref('objectives')
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

const excos = [
  { name: "Habeeb Adebayo Abd-Azeez", role: "Chairman", duties: "Provides overall leadership, presides over meetings, and represents the organization externally." },
  { name: "Adam Abidemi Opeloyeru", role: "Secretary", duties: "Manages official correspondence, records minutes, and maintains organizational custody." },
  { name: "Bunkunmi Dhikrullahi Shittu", role: "Accounting Officer", duties: "Oversees financial records, compliance, and accounts transparency." },
  { name: "Oriyomi Hakeem Sulaimon", role: "Public Relations Officer (PRO)", duties: "Directs media channels, announcements, and sponsor relations." },
  { name: "Olorunjuwon Gbolahan Alimi", role: "Welfare Officer", duties: "Coordinates member wellbeing, event support, and emergency initiatives." },
  { name: "Olayiwola AbdulGafar Ademola", role: "Event Coordinator", duties: "Executes football leagues, schedules matches, and manages stadium logistics." }
]

const constitutionArticles = {
  objectives: {
    title: "Article 2: Objectives",
    content: [
      "To foster unity among Muslims through annual football competitions and related sporting activities.",
      "To promote healthy recreation, teamwork, and community development.",
      "To provide a transparent and accountable system for managing donations and sponsorships.",
      "To represent Muslim youths in football and other social engagements."
    ]
  },
  membership: {
    title: "Article 3: Membership",
    content: [
      "Membership is open to all Muslims who register with UMMAH TWITTER FC.",
      "Members must abide by the constitution and rules of the association.",
      "Membership may be revoked for misconduct or actions contrary to the objectives of UMMAH TWITTER FC."
    ]
  },
  selection: {
    title: "Article 5: Team Selection",
    content: [
      "UMMAH TWITTER FC shall consist of four teams: Umar, Abubakar, Uthman, and Aliy.",
      "Members shall be assigned to teams through a transparent selection process.",
      "Payment of registration fees or contributions guarantees inclusion in one of the teams."
    ]
  },
  finance: {
    title: "Article 7: Finance & Banking",
    content: [
      "UMMAH TWITTER FC shall maintain a corporate bank account with The Alternative Bank.",
      "All donations, sponsorships, and funds shall be paid into the corporate account.",
      "Withdrawals shall require signatures of the Secretary and Accounting Officer.",
      "Annual financial reports shall be presented to members."
    ]
  },
  governance: {
    title: "Article 8 & 9: Amendments & Dissolution",
    content: [
      "The constitution may be amended by a two-thirds majority of registered members present at a general meeting.",
      "UMMAH TWITTER FC may be dissolved by a two-thirds majority vote of members.",
      "In the event of dissolution, assets shall be donated to a recognized Muslim charity."
    ]
  }
}

function scrollToSection(id) {
  const element = document.getElementById(id)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

function selectTeam(teamId) {
  selectedTeam.value = selectedTeam.value === teamId ? null : teamId
}
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
            <button @click="scrollToSection('teams')" class="outline-gold-button" style="padding: 0.875rem 2rem; font-size: 1rem; border-color: rgba(248, 250, 252, 0.3); color: #F8FAFC;">
              Meet the Teams
            </button>
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

    <!-- About & Origin Story Section -->
    <section id="about" class="section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">THE STORY OF UMMAH TWITTER FC</h2>
          <div class="section-divider"></div>
          <p class="section-subtitle">
            Fostering unity, friendship, and spiritual connection among Muslim youth through sport.
          </p>
        </div>

        <div class="about-grid">
          <div style="display: flex; flex-direction: column; gap: 2rem;">
            <div class="about-card">
              <h3 class="about-card-title">
                <!-- Star Icon -->
                <svg class="icon" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1.25rem; height: 1.25rem; color: #D4AF37; fill-opacity: 0.2;">
                  <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
                </svg>
                Our Origins
              </h3>
              <p class="about-card-text">
                Ummah Twitter FC is a community-driven football organization that has spent the past six years fostering unity and brotherhood among Muslims. What began as a social initiative on Twitter has grown into an annual football league that brings people together beyond cultural and social differences, using sport as a powerful tool for connection.
              </p>
            </div>

            <div class="mission-vision-grid">
              <div class="about-card">
                <h4 class="about-card-title" style="color: #FFFFFF;">Our Mission</h4>
                <p class="about-card-text" style="font-size: 0.875rem;">
                  To unite Muslims through football by creating a platform that promotes brotherhood, teamwork, and mutual respect beyond all differences.
                </p>
              </div>
              <div class="about-card">
                <h4 class="about-card-title" style="color: #FFFFFF;">Our Vision</h4>
                <p class="about-card-text" style="font-size: 0.875rem;">
                  To build a global community where Muslims are connected through shared values, using sport as a pathway toward unity and the ultimate goal: attaining Jannah.
                </p>
              </div>
            </div>
          </div>

          <div class="pillar-card">
            <div class="pillar-bg-glow"></div>
            <h3 class="pillar-title">Constitutional Pillars</h3>
            
            <div class="pillar-list">
              <div class="pillar-item">
                <div class="pillar-num">01.</div>
                <div>
                  <h5 class="pillar-name">United Stand (Saff alignment)</h5>
                  <p class="pillar-desc">Inspired by the alignment in solat (prayer), symbolizing Muslim brothers standing firmly united, side-by-side.</p>
                </div>
              </div>

              <div class="pillar-item">
                <div class="pillar-num">02.</div>
                <div>
                  <h5 class="pillar-name">Championship Integrity</h5>
                  <p class="pillar-desc">A transparent administration managing the team selection, finances, rules, and scoring to ensure absolute fairness.</p>
                </div>
              </div>

              <div class="pillar-item">
                <div class="pillar-num">03.</div>
                <div>
                  <h5 class="pillar-name">Community Welfare</h5>
                  <p class="pillar-desc">More than a tournament—supporting brothers through welfare initiatives, emergency responses, and regular fellowship.</p>
                </div>
              </div>
            </div>

            <div class="pillar-footer">
              "Brotherhood Beyond the Pitch."
            </div>
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

    <!-- Rules & Scoring Section -->
    <section id="rules" class="section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">FORMAT & SCORING SYSTEM</h2>
          <div class="section-divider"></div>
          <p class="section-subtitle">
            How the league is played, managed, and won under the official constitution.
          </p>
        </div>

        <div class="rules-grid">
          <div class="rules-card">
            <h3 class="rules-card-title">League Play Format</h3>
            
            <div class="rules-list">
              <div class="rule-item">
                <div class="rule-num">1</div>
                <div>
                  <h5 class="rule-title">Single Round-Robin Format</h5>
                  <p class="rule-desc">Each of the 4 teams plays every other team once during the match day, guaranteeing competitive play for everyone.</p>
                </div>
              </div>

              <div class="rule-item">
                <div class="rule-num">2</div>
                <div>
                  <h5 class="rule-title">Back-to-Back Fixtures</h5>
                  <p class="rule-desc">Each team will play one scheduled back-to-back game to test endurance, depth, and tactical resilience.</p>
                </div>
              </div>

              <div class="rule-item">
                <div class="rule-num">3</div>
                <div>
                  <h5 class="rule-title">Championship Declaration</h5>
                  <p class="rule-desc">The team with the highest point tally at the end of all matches is crowned the Champion, taking home the Ummah Cup Trophy.</p>
                </div>
              </div>
            </div>
          </div>

          <div class="rules-card">
            <h3 class="rules-card-title">Constitutional Points System</h3>
            <p class="points-intro">
              Unlike traditional leagues, the Ummah Twitter FC constitution utilizes an inclusive, participation-encouraging scoring system. Every outcome secures points toward the team total.
            </p>

            <div class="points-grid">
              <div class="point-card">
                <div class="point-value win">3</div>
                <div class="point-label">Points</div>
                <div class="point-badge win">WIN</div>
              </div>
              
              <div class="point-card">
                <div class="point-value draw">2</div>
                <div class="point-label">Points</div>
                <div class="point-badge draw">DRAW</div>
              </div>

              <div class="point-card">
                <div class="point-value loss">1</div>
                <div class="point-label">Point</div>
                <div class="point-badge loss">LOSS</div>
              </div>
            </div>

            <div class="points-notice">
              <!-- ShieldCheck Icon -->
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1.25rem; height: 1.25rem; color: #D4AF37; flex-shrink: 0; margin-top: 0.125rem;">
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                <path d="m9 12 2 2 4-4"/>
              </svg>
              <span>Notice: All points are tracked by the Executive Accounting Officer and verified on-pitch immediately after referee whistles.</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Leadership & Executive Exco Council Section -->
    <section id="leadership" class="section exco-section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">THE EXECUTIVE COUNCIL</h2>
          <div class="section-divider"></div>
          <p class="section-subtitle">
            Meet the officers governing Ummah Twitter FC as established in Appendix 1 of the constitution.
          </p>
        </div>

        <div class="exco-grid">
          <div v-for="(exco, idx) in excos" :key="idx" class="exco-card">
            <div class="exco-card-border"></div>
            <div class="exco-role">{{ exco.role }}</div>
            <h4 class="exco-name">{{ exco.name }}</h4>
            <p class="exco-duties">{{ exco.duties }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Interactive Constitution Viewer -->
    <section id="constitution" class="section">
      <div class="container">
        <div class="section-header">
          <h2 class="section-title">THE LEAGUE CONSTITUTION</h2>
          <div class="section-divider"></div>
          <p class="section-subtitle">
            Explore the core governing rules of the Ummah Twitter FC organization.
          </p>
        </div>

        <div class="const-grid">
          <!-- Tabs Sidebar -->
          <div class="const-sidebar">
            <button
              v-for="(val, key) in constitutionArticles"
              :key="key"
              @click="activeTab = key"
              class="const-tab-btn"
              :class="{ active: activeTab === key }"
            >
              {{ val.title.split(":")[0] }}
              <!-- BookOpen Icon -->
              <svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1rem; height: 1rem;">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
                <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
              </svg>
            </button>
          </div>

          <!-- Tabs Content -->
          <div class="const-content">
            <div>
              <h3 class="const-content-title">
                {{ constitutionArticles[activeTab].title }}
              </h3>
              
              <ul class="const-points">
                <li v-for="(point, index) in constitutionArticles[activeTab].content" :key="index" class="const-point">
                  <span class="const-bullet">•</span>
                  <span>{{ point }}</span>
                </li>
              </ul>
            </div>

            <div class="const-footer">
              Verified: Ummah Twitter FC Constitutional Charter
            </div>
          </div>
        </div>
      </div>
    </section>

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
      </div  </div>
</template>ter>
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

/* Rule/Scoring Section */
.rules-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 3rem;
}
@media (min-width: 1024px) {
  .rules-grid {
    grid-template-columns: 1fr 1fr;
  }
}
.rules-card {
  background-color: #0a2d1d;
  border: 1px solid #27523d;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
}
.rules-card-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #FFFFFF;
  border-bottom: 1px solid #27523d;
  padding-bottom: 1rem;
  margin-bottom: 1.5rem;
}
.rules-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}
.rule-item {
  display: flex;
  gap: 1rem;
}
.rule-num {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 9999px;
  background-color: rgba(212, 175, 55, 0.1);
  border: 1px solid rgba(212, 175, 55, 0.2);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #D4AF37;
  font-weight: 700;
  flex-shrink: 0;
}
.rule-title {
  font-weight: 600;
  color: #FFFFFF;
  font-size: 1.125rem;
}
.rule-desc {
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.7);
  margin-top: 0.25rem;
  line-height: 1.5;
}
.points-intro {
  font-size: 0.875rem;
  color: rgba(248, 250, 252, 0.7);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}
.points-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  text-align: center;
}
.point-card {
  padding: 1rem;
  border-radius: 8px;
  background-color: #052014;
  border: 1px solid #27523d;
}
.point-value {
  font-size: 1.875rem;
  font-weight: 900;
  margin-bottom: 0.25rem;
}
.point-value.win { color: #3dd68c; }
.point-value.draw { color: #4ba8e8; }
.point-value.loss { color: #f59e0b; }
.point-label {
  font-size: 0.75rem;
  text-transform: uppercase;
  font-weight: 700;
  letter-spacing: 0.05em;
  color: #FFFFFF;
}
.point-badge {
  font-size: 10px;
  font-weight: 600;
  margin-top: 0.5rem;
  display: inline-block;
  padding: 0.125rem 0.5rem;
  border-radius: 4px;
}
.point-badge.win { background-color: rgba(61, 214, 140, 0.1); color: #3dd68c; }
.point-badge.draw { background-color: rgba(75, 168, 232, 0.1); color: #4ba8e8; }
.point-badge.loss { background-color: rgba(245, 158, 11, 0.1); color: #f59e0b; }

.points-notice {
  margin-top: 1.5rem;
  padding: 1rem;
  border-radius: 4px;
  background-color: rgba(212, 175, 55, 0.05);
  border: 1px solid rgba(212, 175, 55, 0.2);
  font-size: 0.75rem;
  color: #D4AF37;
  line-height: 1.5;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
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
