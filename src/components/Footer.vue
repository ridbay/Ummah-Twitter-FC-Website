<template>
  <footer class="footer no-print">
    <div class="container">
      <div class="footer-grid">
        <!-- Brand -->
        <div class="footer-about">
          <div class="footer-logo">
            <img src="/logo.jpg" alt="Ummah FC Logo" style="width: 38px; height: 38px; border-radius: 50%; object-fit: cover; border: 1px solid #D4AF37;" />
            <span class="brand-title">UMMAH FC</span>
          </div>
          <p class="footer-desc">
            Fostering unity, teamwork, and brotherhood among the Muslim youth in Nigeria. Utilizing sports to build relationships that extend past the field and into Jannah.
          </p>
          <div class="footer-tagline">
            Lagos, Nigeria • Brotherhood Beyond the Pitch
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="footer-title">Quick Links</h4>
          <ul class="footer-links">
            <li><router-link to="/about" class="footer-nav-link">About</router-link></li>
            <li><router-link to="/#teams" class="footer-nav-link">The Teams</router-link></li>
            <li><router-link to="/schedule" class="footer-nav-link">Game Schedule</router-link></li>
            <li><router-link to="/#rules" class="footer-nav-link">Format &amp; Scoring</router-link></li>
            <li><router-link to="/#leadership" class="footer-nav-link">Leadership</router-link></li>
            <li><router-link to="/#constitution" class="footer-nav-link">Constitution</router-link></li>
          </ul>
        </div>

        <!-- Official Channels -->
        <div>
          <h4 class="footer-title">Official Channels</h4>
          <ul class="footer-links">
            <li>
              <!-- Phone Icon -->
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1rem; height: 1rem; color: #D4AF37; flex-shrink: 0;">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>
              </svg>
              <a href="tel:09169015718">09169015718</a>
            </li>
            <li>
              <!-- Mail Icon -->
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width: 1rem; height: 1rem; color: #D4AF37; flex-shrink: 0;">
                <rect width="20" height="16" x="2" y="4" rx="2"/>
                <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
              </svg>
              <a href="mailto:ummahfc@gmail.com">ummahfc@gmail.com</a>
            </li>
          
          </ul>
        </div>

        <!-- Social Media -->
        <div>
          <h4 class="footer-title">Social Media</h4>
          <ul class="footer-links">
            <li>
              <a
                href="https://x.com/MuslimUmmahFC"
                target="_blank"
                rel="noopener noreferrer"
                style="color: #D4AF37; font-weight: 600;"
              >
                @MuslimUmmahFC
              </a>
            </li>
            <li class="footer-hashtags">
              Tag us on Twitter/X with:
              <a
                href="https://x.com/hashtag/UmmahTwitterMatch2026"
                target="_blank"
                rel="noopener noreferrer"
                class="footer-hashtag-bold"
              >#UmmahTwitterMatch2026</a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Credit Banner -->
      <div class="credit-banner">
        <div class="credit-glow"></div>
        <p class="credit-label">✦ Crafted with passion by</p>
        <div class="credit-names">
          <a
            href="https://balogunridwan.com"
            target="_blank"
            rel="noopener noreferrer"
            class="credit-person"
          >
            <span class="credit-avatar">R</span>
            <span class="credit-name">ridbay</span>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="credit-ext-icon"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
          </a>
          <span class="credit-amp">&amp;</span>
          <a
            href="mailto:quincysdesign@gmail.com"
            class="credit-person"
          >
            <span class="credit-avatar alt">G</span>
            <span class="credit-name">geekmaros</span>
          </a>
        </div>
      </div>

      <div class="footer-bottom">
        <div>© 2026 Ummah Twitter FC. All Rights Reserved. Lagos, Nigeria.</div>
        <div>Alternative Bank Account: 0514013964</div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  background-color: #052014;
  border-top: 1px solid #27523d;
  padding-top: 4rem;
  padding-bottom: 2rem;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}
.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  max-width: 1280px;
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
.footer-about {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.brand-title {
  font-weight: 900;
  font-size: 1.5rem;
  letter-spacing: 0.05em;
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
.footer-links a,
.footer-nav-link {
  color: inherit;
  text-decoration: none;
  transition: color 0.2s;
}
.footer-links a:hover,
.footer-nav-link:hover {
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
  text-decoration: none;
  transition: color 0.2s;
}
.footer-hashtag-bold:hover {
  color: #D4AF37;
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
/* Credit Banner */
.credit-banner {
  position: relative;
  margin: 2.5rem 0 0;
  padding: 1.75rem 2rem;
  border-radius: 16px;
  background: linear-gradient(135deg, rgba(10, 45, 29, 0.95) 0%, rgba(5, 32, 20, 0.98) 100%);
  border: 1px solid rgba(212, 175, 55, 0.25);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  overflow: hidden;
  text-align: center;
}
.credit-glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 300px;
  height: 80px;
  background: radial-gradient(ellipse, rgba(212, 175, 55, 0.12) 0%, transparent 70%);
  pointer-events: none;
}
.credit-label {
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: rgba(212, 175, 55, 0.6);
  font-weight: 600;
  margin: 0;
}
.credit-names {
  display: flex;
  align-items: center;
  gap: 1.25rem;
  flex-wrap: wrap;
  justify-content: center;
}
.credit-person {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  text-decoration: none;
  transition: transform 0.2s;
}
a.credit-person:hover {
  transform: translateY(-2px);
}
.credit-avatar {
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 50%;
  background: linear-gradient(135deg, #F3C64F, #A07817);
  color: #052014;
  font-weight: 900;
  font-size: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 12px rgba(212, 175, 55, 0.4);
  flex-shrink: 0;
}
.credit-avatar.alt {
  background: linear-gradient(135deg, #6ee7b7, #059669);
  box-shadow: 0 0 12px rgba(6, 150, 105, 0.4);
}
.credit-name {
  font-size: 1.15rem;
  font-weight: 800;
  letter-spacing: 0.02em;
  background: linear-gradient(135deg, #F3C64F 0%, #ffffff 60%, #F3C64F 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer 3s linear infinite;
}
a.credit-person .credit-name {
  background: linear-gradient(135deg, #F3C64F 0%, #ffe599 50%, #A07817 100%);
  background-size: 200% auto;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmer 3s linear infinite;
}
.credit-ext-icon {
  width: 0.85rem;
  height: 0.85rem;
  color: rgba(212, 175, 55, 0.5);
  flex-shrink: 0;
}
.credit-amp {
  font-size: 1.25rem;
  font-weight: 300;
  color: rgba(248, 250, 252, 0.3);
  user-select: none;
}
@keyframes shimmer {
  0%   { background-position: 0% center; }
  100% { background-position: 200% center; }
}

@media print {
  .no-print {
    display: none !important;
  }
}
</style>
