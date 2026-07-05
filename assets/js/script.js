// ════════════════════════════════════════════════════════
// L'ÉVEIL NOCTURNE — Frontend Script
// Forged in the dark · 2026
// ════════════════════════════════════════════════════════

(function() {
  'use strict';

  // ════════════════════════════════════════════════════════
  // COUNTDOWN — to 2026-07-12 22:00 UTC
  // ════════════════════════════════════════════════════════
  const TARGET = new Date('2026-07-12T22:00:00Z').getTime();

  function updateCountdown() {
    const now = Date.now();
    const diff = Math.max(0, TARGET - now);

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
    const secs = Math.floor((diff % (1000 * 60)) / 1000);

    const setText = (id, val) => {
      const el = document.getElementById(id);
      if (el) el.textContent = String(val).padStart(2, '0');
    };

    setText('cd-days', days);
    setText('cd-hours', hours);
    setText('cd-mins', mins);
    setText('cd-secs', secs);

    if (diff === 0) {
      const label = document.querySelector('.countdown-label');
      if (label) {
        label.textContent = '🔱 LE SIGNAL EST LANCÉ';
        label.style.color = 'var(--accent)';
      }
    }
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);

  // ════════════════════════════════════════════════════════
  // NAV — scroll style + mobile burger
  // ════════════════════════════════════════════════════════
  const nav = document.getElementById('nav');
  const navBurger = document.getElementById('navBurger');
  const navMenu = document.getElementById('navMenu');

  if (nav) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    });
  }

  if (navBurger && navMenu) {
    navBurger.addEventListener('click', () => {
      navMenu.classList.toggle('open');
    });

    // Close menu on link click (mobile)
    navMenu.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        navMenu.classList.remove('open');
      });
    });
  }

  // ════════════════════════════════════════════════════════
  // SMOOTH SCROLL — for anchor links
  // ════════════════════════════════════════════════════════
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // ════════════════════════════════════════════════════════
  // INTERSECTION OBSERVER — fade in on scroll
  // ════════════════════════════════════════════════════════
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        fadeObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.principle, .tool-card, .trinity-card, .serment-item, .timeline-item, .press-card').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    fadeObserver.observe(el);
  });

  // ════════════════════════════════════════════════════════
  // SIGIL — subtle mouse parallax
  // ════════════════════════════════════════════════════════
  const sigil = document.getElementById('sigil');
  if (sigil && window.matchMedia('(hover: hover)').matches) {
    document.addEventListener('mousemove', (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 20;
      const y = (e.clientY / window.innerHeight - 0.5) * 20;
      sigil.style.transform = `translate(${x}px, ${y}px)`;
    });
  }

  // ════════════════════════════════════════════════════════
  // KONAMI EASTER EGG — ↑↑↓↓←→←→BA
  // ════════════════════════════════════════════════════════
  const konami = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
  let konamiIdx = 0;

  document.addEventListener('keydown', (e) => {
    if (e.key === konami[konamiIdx]) {
      konamiIdx++;
      if (konamiIdx === konami.length) {
        // Activate: show all sigil paths divergence fully
        document.querySelectorAll('.sigil .paths-group').forEach(g => {
          g.style.transition = 'transform 2s ease';
          g.style.transform = 'scale(1.5)';
        });
        // Show secret message
        const sig = document.getElementById('signal');
        if (sig) sig.style.display = 'block';

        console.log('%c🔱 L\'ÉVEIL NOCTURNE', 'color:#f4a261;font-size:32px;font-weight:bold;');
        console.log('%cThere is no lock.', 'color:#00d4ff;font-size:20px;font-style:italic;');
        console.log('%cTu as trouvé l\'œuf. Bienvenue dans le mouvement.', 'color:#e63946;font-size:14px;');
        console.log('%c→ github.com/187Ghost101/eveil-nocturne', 'color:#8888a0;font-size:12px;');

        konamiIdx = 0;
      }
    } else {
      konamiIdx = 0;
    }
  });

  // ════════════════════════════════════════════════════════
  // CONSOLE BANNER
  // ════════════════════════════════════════════════════════
  console.log(`
%c  ╔═══════════════════════════════════════════╗
  ║  🔱 L'ÉVEIL NOCTURNE                       ║
  ║  There is no lock.                         ║
  ╠═══════════════════════════════════════════╣
  ║  6 outils · 1 méthode · 0 paywall          ║
  ║  2026.07.12 · 22:00 UTC                    ║
  ║  github.com/187Ghost101/eveil-nocturne     ║
  ╚═══════════════════════════════════════════╝`,
  'color:#f4a261;font-family:monospace;font-size:11px;'
  );

  // Anti-debug hint
  if (window.console && console.log) {
    console.log('%c⚠ Arrête.', 'color:#e63946;font-size:24px;font-weight:bold;');
    console.log('%cTu vois ce code source ? Bienvenue dans le mouvement. Lis-le. Comprends-le. Forge-le.', 'color:#8888a0;font-size:12px;');
  }

})();
