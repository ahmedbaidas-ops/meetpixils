// motion durations on demo cards
document.querySelectorAll('.motion-card[data-dur]').forEach((c) => {
  const dur = c.dataset.dur;
  const demo = c.querySelector('.mdemo');
  if (demo) demo.style.transitionDuration = `${dur}ms`;
});

// active section dot in topbar
const sections = document.querySelectorAll('main > section[id]');
const navLinks = document.querySelectorAll('.topbar-nav a[href^="#"]');
const linkMap = new Map(
  [...navLinks].map((a) => [a.getAttribute('href').slice(1), a])
);

const obs = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      const link = linkMap.get(e.target.id);
      if (!link) return;
      if (e.isIntersecting) {
        navLinks.forEach((a) => a.style.color = '');
        link.style.color = 'var(--color-orange-500)';
      }
    });
  },
  { rootMargin: '-30% 0px -60% 0px' }
);
sections.forEach((s) => obs.observe(s));

// mark hero focus button as focused on load (demo)
window.addEventListener('load', () => {
  const f = document.querySelector('.btn.focused');
  if (f) f.classList.add('focused');
});
