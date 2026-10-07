// ============================================
// LUCIDE ICONS
// ============================================
document.addEventListener('DOMContentLoaded', function () {
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});

// ============================================
// DARK MODE TOGGLE
// ============================================
function toggleDarkMode() {
  const html = document.documentElement;
  const isDark = html.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
  
  // Update icon
  const icon = document.getElementById('themeIcon');
  if (icon) {
    icon.setAttribute('data-lucide', isDark ? 'sun' : 'moon');
    if (typeof lucide !== 'undefined') lucide.createIcons();
  }
}

// Load theme saat page load
(function initTheme() {
  const saved = localStorage.getItem('theme');
  if (saved === 'dark') {
    document.documentElement.classList.add('dark');
  }
})();

// ============================================
// BULK ACTIONS
// ============================================
function toggleSelectAll(checkbox) {
  document.querySelectorAll('.arsip-checkbox').forEach(function (cb) {
    cb.checked = checkbox.checked;
  });
  updateBulkBar();
}

function updateBulkBar() {
  const selected = document.querySelectorAll('.arsip-checkbox:checked');
  const count = selected.length;

  const bar = document.getElementById('bulkBar');
  const countEl = document.getElementById('selectedCount');

  if (bar && countEl) {
    countEl.textContent = count;
    bar.style.display = count > 0 ? 'flex' : 'none';
  }

  const selectAll = document.getElementById('selectAll');
  const total = document.querySelectorAll('.arsip-checkbox').length;
  if (selectAll) {
    selectAll.checked = count > 0 && count === total;
    selectAll.indeterminate = count > 0 && count < total;
  }
}

// ============================================
// BULK DELETE — Custom Modal
// ============================================
function submitBulkDelete() {
  const count = document.querySelectorAll('.arsip-checkbox:checked').length;
  if (count === 0) return;

  // Update count di modal
  const countEl = document.getElementById('deleteCount');
  if (countEl) countEl.textContent = count;

  // Buka modal
  const modal = document.getElementById('deleteModal');
  if (modal) modal.classList.add('is-open');
}

function closeDeleteModal() {
  const modal = document.getElementById('deleteModal');
  if (modal) modal.classList.remove('is-open');
}

function submitBulkDelete() {
  const count = document.querySelectorAll('.arsip-checkbox:checked').length;
  if (count === 0) return;

  const countEl = document.getElementById('deleteCount');
  if (countEl) countEl.textContent = count;

  const modal = document.getElementById('deleteModal');
  if (modal) modal.classList.add('is-open');
}

function closeDeleteModal() {
  const modal = document.getElementById('deleteModal');
  if (modal) modal.classList.remove('is-open');
}

function confirmBulkDelete() {
  const form = document.getElementById('bulkForm');
  if (!form) return;
  form.action = '/arsip/bulk-delete/';
  form.submit();
}

function openMoveModal() {
  const count = document.querySelectorAll('.arsip-checkbox:checked').length;
  const modal = document.getElementById('moveModal');
  const moveCount = document.getElementById('moveCount');

  if (count === 0) return;

  if (moveCount) moveCount.textContent = count;
  if (modal) modal.classList.add('is-open');
}

function closeMoveModal() {
  const modal = document.getElementById('moveModal');
  if (modal) modal.classList.remove('is-open');
}

function submitBulkMove() {
  const folderId = document.getElementById('moveFolderSelect').value;
  if (!folderId) {
    alert('Pilih folder tujuan dulu.');
    return;
  }

  const form = document.getElementById('bulkForm');
  const folderInput = document.getElementById('bulkFolderId');
  
  if (folderInput) folderInput.value = folderId;
  if (form) {
    form.action = '/arsip/bulk-move/';
    form.submit();
  }
}

// Update bulk bar saat page load
document.addEventListener('DOMContentLoaded', function () {
  updateBulkBar();
});
// ============================================
// SCROLL REVEAL
// ============================================
function initScrollReveal() {
  const elements = document.querySelectorAll('.reveal');
  if (elements.length === 0) return;
  
  if (!('IntersectionObserver' in window)) {
    elements.forEach(function (el) { el.classList.add('in-view'); });
    return;
  }
  
  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
      } else {
        // Hilang saat keluar viewport (biar bisa re-play)
        entry.target.classList.remove('in-view');
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -60px 0px'
  });
  
  elements.forEach(function (el) { observer.observe(el); });
}

// Panggil saat DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initScrollReveal);
} else {
  initScrollReveal();
}

// ============================================
// KEYBOARD SHORTCUT — `/` focus search
// ============================================
document.addEventListener('keydown', function (e) {
  // Skip kalau lagi ngetik di input/textarea
  const tag = (e.target.tagName || '').toLowerCase();
  if (tag === 'input' || tag === 'textarea' || e.target.isContentEditable) return;
  
  // Skip kalau ada modifier key
  if (e.ctrlKey || e.metaKey || e.altKey) return;
  
  if (e.key === '/') {
    const search = document.querySelector('.navbar-search-input');
    if (search) {
      e.preventDefault();
      search.focus();
      search.select();
    }
  }
});

// ============================================
// PAGE TRANSITION
// ============================================
(function () {
  // Fade in saat page load
  window.addEventListener('load', function () {
    document.body.classList.add('page-loaded');
  });
  
  // Fallback kalau load event gak ke-trigger
  setTimeout(function () {
    document.body.classList.add('page-loaded');
  }, 100);
  
  // Fade out saat klik link internal
  document.addEventListener('click', function (e) {
    const link = e.target.closest('a');
    if (!link) return;
    
    const href = link.getAttribute('href');
    if (!href) return;
    
    // Skip kalau:
    // - Link eksternal
    // - Target _blank
    // - Anchor (#)
    // - Download
    // - Ctrl/Cmd + klik (buka tab baru)
    if (
      href.startsWith('http') ||
      href.startsWith('//') ||
      link.target === '_blank' ||
      href.startsWith('#') ||
      href.startsWith('mailto:') ||
      link.hasAttribute('download') ||
      e.ctrlKey || e.metaKey
    ) return;
    
    // Fade out
    e.preventDefault();
    document.body.classList.remove('page-loaded');
    document.body.classList.add('page-leaving');
    
    setTimeout(function () {
      window.location.href = href;
    }, 180);
  });
})();
// ============================================
// AUTO-INIT TREE
// ============================================
document.addEventListener('DOMContentLoaded', function () {
  if (document.querySelector('.tree-list') || document.querySelector('.tree-toggle')) {
    if (typeof initTree === 'function') {
      console.log('[auto] initTree called');
      initTree();
    }
  }
});

// ============================================
// HERO V3 — Rolling Number
// ============================================
function initCountUp() {
  const els = document.querySelectorAll('[data-count-up]');
  
  function animate(el) {
    const target = parseInt(el.dataset.countUp, 10) || 0;
    const duration = 1500;
    const start = performance.now();
    
    function tick(now) {
      const progress = Math.min((now - start) / duration, 1);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.floor(target * eased).toLocaleString('id-ID');
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  
  if (!('IntersectionObserver' in window)) {
    els.forEach(animate);
    return;
  }
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animate(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  
  els.forEach(el => observer.observe(el));
}


// ============================================
// MAGNETIC TITLE — per span (bukan per huruf)
// ============================================
function initMagneticTitle() {
  const title = document.querySelector('[data-cursor-follow]');
  if (!title) return;

  const spans = title.querySelectorAll('span');
  if (spans.length === 0) return;

  const MAX_DIST = 200;
  const POWER = 14;

  title.addEventListener('mousemove', (e) => {
    const mx = e.clientX;
    const my = e.clientY;

    spans.forEach((span) => {
      const rect = span.getBoundingClientRect();
      const sx = rect.left + rect.width / 2;
      const sy = rect.top + rect.height / 2;

      const dx = sx - mx;
      const dy = sy - my;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < MAX_DIST && dist > 0) {
        const influence = 1 - dist / MAX_DIST;
        const power = influence * POWER;
        const angle = Math.atan2(dy, dx);
        const moveX = Math.cos(angle) * power;
        const moveY = Math.sin(angle) * power;

        span.style.transform = `translate(${moveX}px, ${moveY}px)`;
      } else {
        span.style.transform = 'translate(0, 0)';
      }
    });
  });

  title.addEventListener('mouseleave', () => {
    spans.forEach((span) => {
      span.style.transform = 'translate(0, 0)';
    });
  });
}

// ============================================
// RECENT CARDS — Click to focus (mobile)
// ============================================
function initRecentCards() {
  const cards = document.querySelectorAll('.recent-card-v3');
  if (!cards.length) return;

  cards.forEach((card) => {
    card.addEventListener('click', (e) => {
      // Kalau belum aktif, aktifkan dulu (gak langsung navigasi)
      if (!card.classList.contains('is-active')) {
        // Cek apakah di mobile (gak ada hover)
        const isTouch = window.matchMedia('(hover: none)').matches;
        if (isTouch) {
          e.preventDefault();
          cards.forEach((c) => c.classList.remove('is-active'));
          card.classList.add('is-active');
        }
      }
    });
  });
}

// ============================================
// INIT
// ============================================
document.addEventListener('DOMContentLoaded', function () {
  initCountUp();
  initMagneticTitle();
  initRecentCards();
});

// ============================================
// DOC STACK — Mouse Parallax
// ============================================
function initDocStack() {
  const stack = document.getElementById('docStack');
  if (!stack) return;

  const cards = stack.querySelectorAll('.doc-card');
  if (cards.length === 0) return;

  let isAnimating = false;

  stack.addEventListener('mousemove', (e) => {
    if (isAnimating) return;
    isAnimating = true;

    requestAnimationFrame(() => {
      const rect = stack.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width;
      const y = (e.clientY - rect.top) / rect.height;

      // Tilt: -15deg to +15deg (lebih sensitif)
      const tiltX = (y - 0.5) * -18;
      const tiltY = (x - 0.5) * 18;

      // Apply tilt ke seluruh stack
      stack.style.transform = `rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;

      // Parallax per card
      cards.forEach((card) => {
        // Hentikan floating animation sementara
        card.style.animationPlayState = 'paused';

        let base = '';
        let depth = 0;

        if (card.classList.contains('doc-card-3')) {
          base = 'rotate(-10deg) translateZ(-60px) translateY(-20px)';
          depth = 24;
        } else if (card.classList.contains('doc-card-2')) {
          base = 'rotate(-5deg) translateZ(-30px) translateY(-10px)';
          depth = 16;
        } else {
          base = 'rotate(0deg)';
          depth = 10;
        }

        const px = (x - 0.5) * depth;
        const py = (y - 0.5) * depth;

        card.style.transform = `${base} translate(${px}px, ${py}px)`;
      });

      isAnimating = false;
    });
  });

  stack.addEventListener('mouseleave', () => {
    stack.style.transform = '';
    cards.forEach((card) => {
      card.style.transform = '';
      card.style.animationPlayState = 'running';
    });
  });
}

// ============================================
// INIT
// ============================================
document.addEventListener('DOMContentLoaded', function () {
  initDocStack();
  initCountUp();
  initMagneticTitle();
  initRecentCards();
});