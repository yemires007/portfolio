// loading splash — show once per session, fade out after load
(function () {
  const l = document.getElementById('loader');
  if (!l) return;
  if (document.documentElement.classList.contains('no-loader')) { l.remove(); return; }
  const hide = () => { l.classList.add('hide'); setTimeout(() => l.remove(), 600); };
  if (document.readyState === 'complete') setTimeout(hide, 550);
  else window.addEventListener('load', () => setTimeout(hide, 550));
  sessionStorage.setItem('pf_loaded', '1');
})();

// footer year
const yr = document.getElementById('yr');
if (yr) yr.textContent = new Date().getFullYear();

// scroll reveal + gauge fill
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const io = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('in');
      const bar = e.target.querySelector('.gauge i');
      if (bar && !reduce) {
        requestAnimationFrame(() => { bar.style.width = bar.dataset.w + '%'; });
      } else if (bar) {
        bar.style.width = bar.dataset.w + '%';
      }
      io.unobserve(e.target);
    }
  });
}, { threshold: 0.15 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// if the page loaded with a flash message, jump to the contact section
if (document.querySelector('.flash')) {
  const c = document.getElementById('contact');
  if (c) c.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' });
}
