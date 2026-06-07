const fs = require('fs');
const filePath = '/Users/ridbay/Downloads/Ummah-Twitter-FC-Website/src/views/CheckIn.vue';
let content = fs.readFileSync(filePath, 'utf8');

const replacement = `<div class="event-ended-state" style="text-align: center; padding: 2rem 0;">
            <div class="success-icon" aria-hidden="true" style="background-color: rgba(212, 175, 55, 0.1); border-color: rgba(212, 175, 55, 0.3); margin: 0 auto 1.5rem auto;">
              <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#D4AF37" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
              </svg>
            </div>
            <h2 style="font-size: 1.5rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.5rem;">The Match Has Concluded!</h2>
            <p style="color: rgba(248, 250, 252, 0.8); line-height: 1.6; margin-bottom: 2rem; max-width: 400px; margin-left: auto; margin-right: auto;">
              Check-ins for Ummah Twitter FC 2026 are now closed. Thank you to everyone who participated and made it a memorable event.
            </p>
            <router-link to="/certificate" class="btn-submit" style="text-decoration: none; display: inline-flex; justify-content: center; align-items: center; width: auto; padding: 0.875rem 1.5rem;">
              Download Certificate of Participation
            </router-link>
          </div>`;

// Find <Transition name="fade" mode="out-in"> and </Transition> inside <div class="card">
const startIndex = content.indexOf('<Transition name="fade" mode="out-in">');
const endIndex = content.indexOf('</Transition>', startIndex) + '</Transition>'.length;

if (startIndex !== -1 && endIndex !== -1) {
  content = content.substring(0, startIndex) + replacement + content.substring(endIndex);
  fs.writeFileSync(filePath, content);
  console.log('Successfully updated CheckIn.vue');
} else {
  console.log('Could not find transition block to replace.');
}
