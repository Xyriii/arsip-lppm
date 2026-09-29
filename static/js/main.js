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