/* Al-Khair Academy — site script: navigation, gallery, enquiry form */
(function () {
  'use strict';

  /* ---------- SETTINGS ---------- */
  var SETTINGS = {
    whatsapp: '916264672034',          // school WhatsApp number, country code first, digits only (same as src/config.py)
    // Optional form service URL (e.g. a Formspree endpoint). Leave empty to send enquiries through WhatsApp only.
    formEndpoint: ''
  };

  /* ---------- mobile menu ---------- */
  var menuBtn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (menuBtn && nav) {
    menuBtn.addEventListener('click', function () {
      var open = !nav.classList.contains('open');
      nav.classList.toggle('open', open);
      document.body.classList.toggle('nav-locked', open);
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        nav.classList.remove('open');
        document.body.classList.remove('nav-locked');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* ---------- gallery filter + lightbox ---------- */
  var gallery = document.querySelector('.gallery');
  if (gallery) {
    var groups = Array.prototype.slice.call(gallery.querySelectorAll('.g-group'));
    var items = Array.prototype.slice.call(gallery.querySelectorAll('.g-grid button'));
    document.querySelectorAll('.filters button').forEach(function (fb) {
      fb.addEventListener('click', function () {
        var cat = fb.getAttribute('data-filter');
        document.querySelectorAll('.filters button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === fb)); });
        groups.forEach(function (g) { g.hidden = !(cat === 'all' || g.getAttribute('data-cat') === cat); });
      });
    });

    var lb = document.getElementById('lightbox');
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('.lb-cap');
    var current = 0, startX = null, lastFocus = null;
    function visible() { return items.filter(function (i) { return !i.closest('.g-group').hidden; }); }
    function show(idx) {
      var list = visible(); if (!list.length) return;
      current = (idx + list.length) % list.length;
      var img = list[current].querySelector('img');
      lbImg.src = img.getAttribute('data-full') || img.src;
      lbImg.alt = img.alt;
      lbCap.textContent = img.alt;
    }
    function open(btn) {
      lastFocus = btn;
      lb.hidden = false;
      document.body.classList.add('nav-locked');
      show(visible().indexOf(btn));
      lb.querySelector('.lb-close').focus();
    }
    function close() {
      lb.hidden = true;
      document.body.classList.remove('nav-locked');
      if (lastFocus) lastFocus.focus();
    }
    items.forEach(function (it) { it.addEventListener('click', function () { open(it); }); });
    lb.querySelector('.lb-close').addEventListener('click', close);
    lb.querySelector('.lb-prev').addEventListener('click', function () { show(current - 1); });
    lb.querySelector('.lb-next').addEventListener('click', function () { show(current + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.tagName === 'FIGURE') close(); });
    document.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(current - 1);
      if (e.key === 'ArrowRight') show(current + 1);
    });
    lb.addEventListener('touchstart', function (e) { startX = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) {
      if (startX === null) return;
      var dx = e.changedTouches[0].clientX - startX;
      if (Math.abs(dx) > 40) show(current + (dx < 0 ? 1 : -1));
      startX = null;
    });
  }

  /* ---------- enquiry form ---------- */
  var CONFIRM = 'Thank you. Your enquiry has been received. The Al-Khair Academy office will get in touch with you.';
  document.querySelectorAll('form.enquiry').forEach(function (form) {
    var same = form.querySelector('[name="same_wa"]');
    var wa = form.querySelector('[name="whatsapp"]');
    var phone = form.querySelector('[name="phone"]');
    if (same && wa) {
      same.addEventListener('change', function () {
        wa.disabled = same.checked;
        if (same.checked) wa.value = phone.value;
      });
      phone.addEventListener('input', function () { if (same.checked) wa.value = phone.value; });
    }

    function setErr(name, on) {
      var f = form.querySelector('[name="' + name + '"]').closest('.field');
      f.classList.toggle('err', on);
      var m = f.querySelector('.err-msg'); if (m) m.hidden = !on;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = {
        parent: form.parent.value.trim(),
        student: form.student.value.trim(),
        cls: form.cls.value,
        phone: form.phone.value.replace(/\D/g, ''),
        whatsapp: (same && same.checked ? form.phone.value : (wa ? wa.value : '')).replace(/\D/g, ''),
        method: (form.querySelector('[name="method"]:checked') || {}).value || 'Phone call',
        message: form.message.value.trim()
      };
      var okParent = !!d.parent, okStudent = !!d.student, okPhone = d.phone.length >= 10;
      setErr('parent', !okParent); setErr('student', !okStudent); setErr('phone', !okPhone);
      if (!(okParent && okStudent && okPhone)) return;

      var text = 'Assalamu Alaikum. Admission enquiry for Al-Khair Academy.' +
        '\nParent/Guardian: ' + d.parent +
        '\nStudent: ' + d.student +
        '\nClass seeking admission: ' + d.cls +
        '\nPhone: ' + d.phone +
        (d.whatsapp ? '\nWhatsApp: ' + d.whatsapp : '') +
        '\nPreferred contact: ' + d.method +
        (d.message ? '\nMessage: ' + d.message : '');
      var waUrl = 'https://wa.me/' + SETTINGS.whatsapp + '?text=' + encodeURIComponent(text);
      var box = form.parentElement.querySelector('.confirm');
      var btn = form.querySelector('button[type="submit"]');

      function showConfirm(viaWhatsapp) {
        box.querySelector('p').textContent = viaWhatsapp
          ? 'Your enquiry is ready. Please tap the button below to send it to the school office on WhatsApp.'
          : CONFIRM;
        var link = box.querySelector('a');
        link.hidden = !viaWhatsapp;
        link.href = waUrl;
        form.hidden = true;
        box.hidden = false;
        box.focus();
      }

      if (SETTINGS.formEndpoint) {
        btn.disabled = true; btn.textContent = 'Sending…';
        fetch(SETTINGS.formEndpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(d)
        }).then(function (r) {
          if (!r.ok) throw new Error('bad status');
          showConfirm(false);
        }).catch(function () {
          showConfirm(true); // fall back to WhatsApp if the form service fails
        });
      } else {
        showConfirm(true);
      }
    });

    var box = form.parentElement.querySelector('.confirm');
    if (box) {
      var link = box.querySelector('a');
      link.addEventListener('click', function () {
        setTimeout(function () { box.querySelector('p').textContent = CONFIRM; link.hidden = true; }, 600);
      });
    }
  });

  /* ---------- footer year ---------- */
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
