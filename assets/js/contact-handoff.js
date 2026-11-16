/**
 * Ensures the contact enquiry handoff opens WhatsApp / email.
 * The compiled form prepares the message; this patches the email button
 * and documents that nothing is posted to a server.
 */
(function () {
  function buildMailto(subject, body) {
    return 'mailto:info.aliradigital@gmail.com?subject=' +
      encodeURIComponent(subject) +
      '&body=' +
      encodeURIComponent(body);
  }

  function patchEmailButton(root) {
    var btn = root.querySelector('.fo-email');
    if (!btn || btn.dataset.handoffBound) return;
    btn.dataset.handoffBound = '1';
    btn.addEventListener('click', function () {
      var pre = root.querySelector('.fo-msg');
      var body = pre ? pre.textContent : '';
      var nameInput = document.getElementById('f-name');
      var name = nameInput && nameInput.value ? nameInput.value.trim() : 'Website enquiry';
      window.location.href = buildMailto('Website enquiry — ' + name, body);
    });
  }

  var out = document.querySelector('#enquiry .form-out');
  if (!out) return;

  var observer = new MutationObserver(function () {
    if (out.classList.contains('show') || out.innerHTML.indexOf('fo-email') !== -1) {
      patchEmailButton(out);
    }
  });
  observer.observe(out, { childList: true, subtree: true, attributes: true, attributeFilter: ['class'] });
})();
