<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  // Load Twitter widgets.js if not already loaded
  if (window.twttr && window.twttr.widgets) {
    window.twttr.widgets.load()
  } else {
    const script = document.createElement('script')
    script.src = 'https://platform.twitter.com/widgets.js'
    script.async = true
    script.charset = 'utf-8'
    script.onload = () => {
      if (window.twttr && window.twttr.widgets) {
        window.twttr.widgets.load()
      }
    }
    document.head.appendChild(script)
  }
})
</script>

<template>
  <section class="tweet-feed-section">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">LIVE TWEET FEED</h2>
        <div class="section-divider"></div>
        <p class="section-subtitle">
          See what the Ummah community is saying — real-time tweets tagged
          <a
            href="https://x.com/hashtag/UmmahTwitterMatch2026"
            target="_blank"
            rel="noopener noreferrer"
            class="hashtag-link"
          >#UmmahTwitterMatch2026</a>
        </p>
      </div>

      <div class="feed-wrapper">
        <!-- Decorative glow -->
        <div class="feed-glow"></div>

        <div class="feed-inner">
          <a
            class="twitter-timeline"
            href="https://twitter.com/hashtag/UmmahTwitterMatch2026?src=hashtag_click"
            data-tweet-limit="6"
            data-theme="dark"
            data-chrome="nofooter noheader noborders"
            data-border-color="#D4AF37"
            data-link-color="#D4AF37"
            data-aria-polite="assertive"
            data-height="600"
          >
            #UmmahTwitterMatch2026 Tweets
          </a>
        </div>

        <div class="feed-cta">
          <a
            :href="`https://twitter.com/intent/tweet?text=${encodeURIComponent('🔥 Ummah Twitter FC is live! Join the brotherhood. #UmmahTwitterMatch2026 @MuslimUmmahFC')}`"
            target="_blank"
            rel="noopener noreferrer"
            class="tweet-btn"
          >
            <svg viewBox="0 0 24 24" fill="currentColor" style="width: 1rem; height: 1rem;">
              <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.742l7.742-8.855L1.564 2.25h6.391l4.254 5.622 5.834-5.622Zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
            </svg>
            Add Your Tweet
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
  </section>
</template>

<style scoped>
.tweet-feed-section {
  padding-top: 6rem;
  padding-bottom: 6rem;
  border-top: 1px solid #27523d;
  background-color: #03170e;
}

.container {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  max-width: 1280px;
}

.section-header {
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  margin-bottom: 3rem;
}

.section-title {
  font-size: clamp(1.75rem, 4vw, 3rem);
  font-weight: 900;
  color: #FFFFFF;
  margin-bottom: 1rem;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
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
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.hashtag-link {
  color: #D4AF37;
  text-decoration: none;
  font-weight: 700;
  transition: color 0.2s;
}
.hashtag-link:hover {
  color: #F3C64F;
}

/* Feed wrapper */
.feed-wrapper {
  position: relative;
  max-width: 680px;
  margin: 0 auto;
}

.feed-glow {
  position: absolute;
  top: -60px;
  left: 50%;
  transform: translateX(-50%);
  width: 400px;
  height: 200px;
  background: radial-gradient(ellipse, rgba(212, 175, 55, 0.1) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.feed-inner {
  position: relative;
  z-index: 1;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(212, 175, 55, 0.25);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.4);
  background-color: #15202b; /* Twitter dark bg */
}

.feed-inner a {
  display: block;
}

/* CTA row below feed */
.feed-cta {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 1.5rem;
  flex-wrap: wrap;
}

.tweet-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 9999px;
  background: linear-gradient(135deg, #F3C64F 0%, #D4AF37 50%, #B89020 100%);
  color: #052014;
  font-weight: 700;
  font-size: 0.875rem;
  text-decoration: none;
  transition: all 0.2s ease;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.25);
  font-family: 'Inter', -apple-system, sans-serif;
}
.tweet-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
}

.follow-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.75rem 1.5rem;
  border-radius: 9999px;
  background: transparent;
  color: #D4AF37;
  border: 1px solid rgba(212, 175, 55, 0.4);
  font-weight: 700;
  font-size: 0.875rem;
  text-decoration: none;
  transition: all 0.2s ease;
  font-family: 'Inter', -apple-system, sans-serif;
}
.follow-btn:hover {
  background-color: rgba(212, 175, 55, 0.1);
  border-color: #D4AF37;
}
</style>
