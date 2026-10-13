// ============================================
// THEME INIT (paling awal, biar gak flash)
// ============================================
(function initTheme() {
  const saved = localStorage.getItem('theme');
  if (saved === 'dark') {
    document.documentElement.classList.add('dark');
  }
})();

// ============================================
// HELPER: Lucide icons
// ============================================
function refreshLucide() {
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
}

// ============================================
// DARK MODE TOGGLE
// ============================================
function toggleDarkMode() {
  const html = document.documentElement;
  const isDark = html.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');

  const icon = document.getElementById('themeIcon');
  if (icon) {
    icon.setAttribute('data-lucide', isDark ? 'sun' : 'moon');
    refreshLucide();
  }
}

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
// BULK DELETE MODAL
// ============================================
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

// ============================================
// BULK MOVE MODAL
// ============================================
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
        entry.target.classList.remove('in-view');
      }
    });
  }, {
    threshold: 0.05,
    rootMargin: '0px 0px 0px 0px'
  });

  elements.forEach(function (el) { observer.observe(el); });
}

// ============================================
// COUNT-UP ANIMATION
// ============================================
function initCountUp() {
  const els = document.querySelectorAll('[data-count-up]');

  function animate(el) {
    const target = parseInt(el.dataset.countUp, 10) || 0;
    const duration = 1500;
    const start = performance.now();

    function tick(now) {
      const progress = Math.min((now - start) / duration, 1);
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

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animate(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });

  els.forEach(function (el) { observer.observe(el); });
}

// ============================================
// MAGNETIC TITLE
// ============================================
function initMagneticTitle() {
  const title = document.querySelector('[data-cursor-follow]');
  if (!title) return;

  const spans = title.querySelectorAll('span');
  if (spans.length === 0) return;

  const MAX_DIST = 200;
  const POWER = 14;

  title.addEventListener('mousemove', function (e) {
    const mx = e.clientX;
    const my = e.clientY;

    spans.forEach(function (span) {
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
        span.style.transform = 'translate(' + (Math.cos(angle) * power) + 'px, ' + (Math.sin(angle) * power) + 'px)';
      } else {
        span.style.transform = 'translate(0, 0)';
      }
    });
  });

  title.addEventListener('mouseleave', function () {
    spans.forEach(function (span) {
      span.style.transform = 'translate(0, 0)';
    });
  });
}

// ============================================
// RECENT CARDS (Mobile focus)
// ============================================
function initRecentCards() {
  const cards = document.querySelectorAll('.recent-card-v3');
  if (!cards.length) return;

  cards.forEach(function (card) {
    card.addEventListener('click', function (e) {
      if (!card.classList.contains('is-active')) {
        const isTouch = window.matchMedia('(hover: none)').matches;
        if (isTouch) {
          e.preventDefault();
          cards.forEach(function (c) { c.classList.remove('is-active'); });
          card.classList.add('is-active');
        }
      }
    });
  });
}

// ============================================
// DOC STACK — Mouse Parallax
// ============================================
function initDocStack() {
  const stack = document.getElementById('docStack');
  if (!stack) return;

  const cards = stack.querySelectorAll('.doc-card');
  if (cards.length === 0) return;

  let isAnimating = false;

  stack.addEventListener('mousemove', function (e) {
    if (isAnimating) return;
    isAnimating = true;

    requestAnimationFrame(function () {
      const rect = stack.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width;
      const y = (e.clientY - rect.top) / rect.height;

      const tiltX = (y - 0.5) * -18;
      const tiltY = (x - 0.5) * 18;

      stack.style.transform = 'rotateX(' + tiltX + 'deg) rotateY(' + tiltY + 'deg)';

      cards.forEach(function (card) {
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

        card.style.transform = base + ' translate(' + px + 'px, ' + py + 'px)';
      });

      isAnimating = false;
    });
  });

  stack.addEventListener('mouseleave', function () {
    stack.style.transform = '';
    cards.forEach(function (card) {
      card.style.transform = '';
      card.style.animationPlayState = 'running';
    });
  });
}

// ============================================
// INIT ALL ANIMATIONS (single entry point)
// ============================================
function initAllAnimations() {
  refreshLucide();
  updateBulkBar();
  initScrollReveal();
  initCountUp();
  initMagneticTitle();
  initRecentCards();
  initDocStack();
}
window.initAllAnimations = initAllAnimations;

// ============================================
// SPLASH SCREEN — Bulletproof Version
// ============================================
(function () {
  const splash = document.getElementById('splash');
  const KEY = 'splash_shown';

  function readyAndInit() {
    document.body.classList.add('page-ready');
    document.body.style.overflow = '';
    initAllAnimations();
  }

  // Gak ada splash → langsung init
  if (!splash) {
    readyAndInit();
    return;
  }

  // Splash udah pernah muncul → skip
  if (sessionStorage.getItem(KEY) === 'true') {
    splash.remove();
    readyAndInit();
    return;
  }

  // Reduced motion → skip
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    sessionStorage.setItem(KEY, 'true');
    splash.remove();
    readyAndInit();
    return;
  }

  // Kunci scroll
  document.body.style.overflow = 'hidden';

  // Trigger Hello animation setelah splash render
  setTimeout(function () {
    splash.classList.add('is-ready');
  }, 100);

  let canDismiss = false;

  function dismiss() {
    if (!canDismiss) return;

    splash.classList.add('is-hidden');
    sessionStorage.setItem(KEY, 'true');

    // Cleanup listeners
    document.removeEventListener('keydown', dismiss);
    document.removeEventListener('click', dismiss);
    document.removeEventListener('touchstart', dismiss);

    // Setelah splash fade, baru init
    setTimeout(function () {
      readyAndInit();
    }, 700);

    setTimeout(function () {
      splash.remove();
    }, 900);
  }

  // Aktifkan dismiss setelah 1.8s (kasih waktu animasi Hello + logo selesai)
  setTimeout(function () { canDismiss = true; }, 1800);

  document.addEventListener('keydown', dismiss);
  document.addEventListener('click', dismiss);
  document.addEventListener('touchstart', dismiss);
})();