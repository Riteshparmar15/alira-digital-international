// Production-safe site helpers (formerly local-demo only).
// No refresh-to-home redirect. No form interception.

try {
  localStorage.removeItem('alira-theme');
  sessionStorage.removeItem('alira-theme');
  document.documentElement.removeAttribute('data-theme');
} catch (e) {}

if (new URLSearchParams(window.location.search).has('loader') || window.location.hash === '#loader') {
  try {
    sessionStorage.removeItem('pd-seen');
    document.documentElement.classList.remove('no-loader');
  } catch (e) {}
}

document.addEventListener('DOMContentLoaded', function () {
  var form = document.querySelector('#enquiry');
  if (form && !form.querySelector('.handoff-note')) {
    var note = document.createElement('p');
    note.className = 'handoff-note';
    note.textContent = 'This form prepares your message for WhatsApp or email. Nothing is posted to a server.';
    form.prepend(note);
  }
  document.querySelectorAll('a[href]').forEach(function (a) {
    if (/^https?:/.test(a.href) && a.origin !== location.origin) {
      if (!/(noopener)/.test(a.rel || '')) {
        a.rel = ((a.rel || '') + ' noopener noreferrer').trim();
      }
    }
  });
});
