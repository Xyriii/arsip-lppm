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
  document.querySelectorAll('.icon-moon').forEach(el => el.classList.toggle('hidden', isDark));
  document.querySelectorAll('.icon-sun').forEach(el => el.classList.toggle('hidden', !isDark));
}

/* ----- Mobile Menu Toggle ----- */
function toggleMenu(btn) {
  const menu = document.getElementById('navbar-menu');
  if (!menu) return;
  const isOpen = menu.classList.toggle('is-open');
  btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
}

/* ============================================================
   TOAST
   ============================================================ */

const TOAST_ICONS = {
  success: 'check-circle-2',
  warning: 'alert-circle',
  danger:  'x-circle',
  info:    'info',
};

function showToast(message, type = 'info', duration = 4000) {
  let container = document.getElementById('toast-container');
  if (!container) {
    container = document.createElement('div');
    container.id = 'toast-container';
    container.className = 'toast-container';
    container.setAttribute('aria-live', 'polite');
    container.setAttribute('aria-atomic', 'true');
    document.body.appendChild(container);
  }

  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.setAttribute('role', 'status');

  const iconName = TOAST_ICONS[type] || TOAST_ICONS.info;

  toast.innerHTML = `
    <span class="toast-icon">
      <i data-lucide="${iconName}" style="width:18px;height:18px;"></i>
    </span>
    <div class="toast-body"></div>
    <button type="button" class="toast-close" aria-label="Tutup notifikasi">
      <i data-lucide="x" style="width:14px;height:14px;"></i>
    </button>
  `;

  // Isi pesan sebagai text biar aman dari XSS
  toast.querySelector('.toast-body').textContent = message;

  container.appendChild(toast);

  if (window.lucide) lucide.createIcons();

  // Tombol close
  toast.querySelector('.toast-close').addEventListener('click', () => {
    removeToast(toast);
  });

  // Auto dismiss
  if (duration > 0) {
    setTimeout(() => removeToast(toast), duration);
  }
}

function removeToast(toast) {
  if (!toast || toast.classList.contains('is-leaving')) return;
  toast.classList.add('is-leaving');
  setTimeout(() => toast.remove(), 200);
}

/* ----- Auto-render Django Messages jadi Toast ----- */
function initDjangoMessages() {
  const holder = document.getElementById('django-messages');
  if (!holder) return;

  holder.querySelectorAll('[data-message]').forEach(el => {
    const type = el.dataset.type || 'info';
    const text = el.dataset.message || el.textContent.trim();
    if (text) showToast(text, type);
  });

  holder.remove();
}

/* ============================================================
   MODAL
   ============================================================ */
let _lastFocused = null;

function openModal(id) {
  const overlay = document.getElementById(id);
  if (!overlay) return;

  _lastFocused = document.activeElement;
  overlay.classList.add('is-open');
  document.body.style.overflow = 'hidden';

  const focusTarget = overlay.querySelector('[data-autofocus]')
                   || overlay.querySelector('.btn-secondary')
                   || overlay.querySelector('.modal-close');
  if (focusTarget) setTimeout(() => focusTarget.focus(), 50);
}

function closeModal(id) {
  const overlay = document.getElementById(id);
  if (!overlay) return;

  overlay.classList.remove('is-open');
  document.body.style.overflow = '';

  if (_lastFocused && typeof _lastFocused.focus === 'function') {
    _lastFocused.focus();
    _lastFocused = null;
  }
}

function initModalBackdropClose() {
  document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) closeModal(overlay.id);
    });
  });
}

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') {
    const open = document.querySelector('.modal-overlay.is-open');
    if (open) closeModal(open.id);
  }
});

/* ============================================================
   PAGE TRANSITION
   ============================================================ */
function initPageTransition() {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReduced) return;

  document.querySelectorAll('a[href]').forEach(link => {
    const href = link.getAttribute('href');
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
      if (e.ctrlKey || e.metaKey || e.shiftKey || e.button !== 0) return;

      e.preventDefault();
      const main = document.querySelector('.main-content');
      if (main) {
        main.classList.add('is-leaving');
        setTimeout(() => { window.location.href = href; }, 150);
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
  initModalBackdropClose();
  initDjangoMessages();
});