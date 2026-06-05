<script setup>
import { ref } from 'vue'

const activeTab = ref('objectives')

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
</script>

<template>
  <div class="about-page">

    <!-- Page Hero -->
    <section class="page-hero">
      <div class="page-hero-glow"></div>
      <div class="container page-hero-content animate-fade-in-up">
        <div class="page-hero-tag">Our Story</div>
        <h1 class="page-hero-title">About Ummah Twitter FC</h1>
        <p class="page-hero-sub">
          Six years of brotherhood, unity, and football in Lagos.
        </p>
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

  </div>
</template>

<style scoped>
*, *::before, *::after {
  box-sizing: border-box;
}

.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  max-width: 1280px;
}

.about-page {
  min-height: 100vh;
  background-color: #052014;
  color: #F8FAFC;
  overflow-x: hidden;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Page Hero */
.page-hero {
  position: relative;
  padding-top: 9rem;
  padding-bottom: 5rem;
  overflow: hidden;
  text-align: center;
  border-bottom: 1px solid #27523d;
}
.page-hero-glow {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 600px;
  height: 300px;
  background: radial-gradient(ellipse, rgba(212, 175, 55, 0.12) 0%, transparent 70%);
  pointer-events: none;
}
.page-hero-content {
  position: relative;
  z-index: 1;
}
.page-hero-tag {
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
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 1.25rem;
}
.page-hero-title {
  font-size: clamp(2rem, 6vw, 3.5rem);
  font-weight: 900;
  color: #FFFFFF;
  margin-bottom: 1rem;
  line-height: 1.1;
}
.page-hero-sub {
  font-size: 1.125rem;
  color: rgba(248, 250, 252, 0.75);
  max-width: 36rem;
  margin: 0 auto;
  line-height: 1.6;
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

/* Animations */
.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.icon {
  display: inline-block;
  vertical-align: middle;
}
</style>
