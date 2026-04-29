// gentle parallax for clouds + butterflies on scroll
const clouds = document.querySelectorAll('.cloud');
const butterflies = document.querySelectorAll('.butterfly');
let ticking = false;

function onScroll() {
  if (ticking) return;
  ticking = true;
  requestAnimationFrame(() => {
    const y = window.scrollY;
    clouds.forEach((c, i) => {
      const speed = 0.06 + i * 0.04;
      c.style.transform = `translate3d(0, ${y * speed}px, 0)`;
    });
    butterflies.forEach((b, i) => {
      const speed = 0.18 + i * 0.06;
      b.style.translate = `0 ${-y * speed}px`;
    });
    ticking = false;
  });
}
window.addEventListener('scroll', onScroll, { passive: true });

// reveal-on-scroll for sections
const io = new IntersectionObserver(
  (entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.classList.add('in');
        io.unobserve(e.target);
      }
    });
  },
  { threshold: 0.12 }
);
document
  .querySelectorAll('.why-card, .service, .card, .person, .cta, .section-head')
  .forEach((el) => {
    el.classList.add('reveal');
    io.observe(el);
  });

// inject reveal styles
const s = document.createElement('style');
s.textContent = `
  .reveal { opacity: 0; transform: translateY(24px); transition: opacity .8s ease, transform .8s cubic-bezier(.2,.7,.2,1); }
  .reveal.in { opacity: 1; transform: none; }
`;
document.head.appendChild(s);

// nav pill follower
const pills = document.querySelectorAll('.nav-pills .pill');
pills.forEach((p) => {
  p.addEventListener('click', (e) => {
    pills.forEach((x) => x.classList.remove('pill-active'));
    p.classList.add('pill-active');
  });
});
