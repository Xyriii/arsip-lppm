/* ============================================================
   Website Arsip LPPM UNS — main.js
   ============================================================ */

/* ----- Dark Mode Toggle ----- */
function toggleTheme() {
  const root = document.documentElement;
  const isDark = root.classList.toggle('dark');
  try { localStorage.setItem('theme', isDark ? 'dark' : 'light'); } catch (e) {}
  updateThemeIcon();
}

function updateThemeIcon() {
  const isDark = document.documentElement.classList.contains('dark');
  document.querySelectorAll('.icon-moon').forEach(el => {
    el.classList.toggle('hidden', isDark);
  });
  document.querySelectorAll('.icon-sun').forEach(el => {
    el.classList.toggle('hidden', !isDark);
  });
}

/* ----- Mobile Menu Toggle ----- */
function toggleMenu(btn) {
  const menu = document.getElementById('navbar-menu');
  if (!menu) return;
  const isOpen = menu.classList.toggle('is-open');
  btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
}

/* ----- Init ----- */
document.addEventListener('DOMContentLoaded', function () {
  if (window.lucide) lucide.createIcons();
  updateThemeIcon();
});
/* ============================================================
   Website Arsip LPPM UNS — main.js
   ============================================================ */

/* ----- Dark Mode Toggle ----- */
function toggleTheme() {
  const root = document.documentElement;
  const isDark = root.classList.toggle('dark');
  try { localStorage.setItem('theme', isDark ? 'dark' : 'light'); } catch (e) {}
  updateThemeIcon();
}

function updateThemeIcon() {
  const isDark = document.documentElement.classList.contains('dark');
  document.querySelectorAll('.icon-moon').forEach(el => {
    el.classList.toggle('hidden', isDark);
  });
  document.querySelectorAll('.icon-sun').forEach(el => {
    el.classList.toggle('hidden', !isDark);
  });
}

/* ----- Mobile Menu Toggle ----- */
function toggleMenu(btn) {
  const menu = document.getElementById('navbar-menu');
  if (!menu) return;
  const isOpen = menu.classList.toggle('is-open');
  btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
}

/* ============================================================
   PAGE TRANSITION
   Fade-out halaman sekarang → navigate ke halaman baru
   Halaman baru otomatis fade-in via CSS (.main-content)
   ============================================================ */
function initPageTransition() {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return;

  document.querySelectorAll('a[href]').forEach(link => {
    const href = link.getAttribute('href');

    // Skip: anchor (#), external, download, target="_blank", tombol, atau kosong
    if (!href ||
        href.startsWith('#') ||
        href.startsWith('http') ||
        href.startsWith('mailto:') ||
        href.startsWith('tel:') ||
        link.hasAttribute('download') ||
        link.getAttribute('target') === '_blank') {
      return;
    }

    link.addEventListener('click', function (e) {
      // Skip kalau user pake Ctrl/Cmd/Shift click (buat buka tab baru)
      if (e.ctrlKey || e.metaKey || e.shiftKey || e.button !== 0) return;

      e.preventDefault();
      const main = document.querySelector('.main-content');
      if (main) {
        main.classList.add('is-leaving');
        setTimeout(() => {
          window.location.href = href;
        }, 150);
      } else {
        window.location.href = href;
      }
    });
  });
}

/* ----- Init ----- */
document.addEventListener('DOMContentLoaded', function () {
  if (window.lucide) lucide.createIcons();
  updateThemeIcon();
  initPageTransition();
});