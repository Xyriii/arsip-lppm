/* ============================================================
   TREE SIDEBAR
   ============================================================ */
function initTree() {
  document.querySelectorAll('.tree-toggle').forEach(btn => {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      const item = btn.closest('.tree-item');
      if (!item) return;
      const isOpen = item.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  });

  // Auto-expand path ke current folder
  const activeRow = document.querySelector('.tree-row.is-active');
  if (activeRow) {
    let parent = activeRow.parentElement.closest('.tree-children');
    while (parent) {
      const item = parent.closest('.tree-item');
      if (item) {
        item.classList.add('is-open');
        const toggle = item.querySelector(':scope > .tree-row > .tree-toggle');
        if (toggle) toggle.setAttribute('aria-expanded', 'true');
      }
      parent = parent.parentElement.closest('.tree-children');
    }
  }
}

/* ============================================================
   SIDEBAR MOBILE TOGGLE
   ============================================================ */
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  if (!sidebar) return;
  sidebar.classList.toggle('is-open');
}

// ============================================
// TREE VIEW TOGGLE
// ============================================
document.addEventListener('DOMContentLoaded', function () {
  if (window.lucide) lucide.createIcons();
  updateThemeIcon();
  initPageTransition();
  initModalBackdropClose();
  initDjangoMessages();
  initTree();          // <-- tambahin ini
});
  // Toggle expand/collapse
  document.querySelectorAll('.tree-toggle:not(.empty)').forEach(function (toggle) {
    toggle.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();

      const targetId = this.dataset.target;
      const target = document.getElementById(targetId);

      if (!target) return;

      const isOpen = target.style.display !== 'none';

      if (isOpen) {
        target.style.display = 'none';
        this.classList.remove('open');
      } else {
        target.style.display = 'block';
        this.classList.add('open');
      }
    });
  });

  // Auto-expand folder yang lagi aktif
  const activeItem = document.querySelector('.tree-item.active');
  if (activeItem) {
    let parent = activeItem.parentElement;
    while (parent && parent !== document.body) {
      if (parent.classList.contains('tree-children')) {
        parent.style.display = 'block';
        const toggle = parent.parentElement.querySelector('.tree-toggle');
        if (toggle) toggle.classList.add('open');
      }
      parent = parent.parentElement;
    }
  }
});