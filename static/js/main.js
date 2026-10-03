// ============================================
// TREE VIEW
// ============================================
document.addEventListener('DOMContentLoaded', function () {
  console.log('[tree] init');

  // Toggle click handler
  document.querySelectorAll('.tree-toggle:not(.empty)').forEach(function (toggle) {
    toggle.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();

      const targetId = this.dataset.target;
      const target = document.getElementById(targetId);
      if (!target) return;

      const isHidden = target.classList.contains('is-hidden');

      if (isHidden) {
        target.classList.remove('is-hidden');
        this.classList.add('open');
        console.log('[tree] OPEN:', targetId);
      } else {
        target.classList.add('is-hidden');
        this.classList.remove('open');
        console.log('[tree] CLOSE:', targetId);
      }
    });
  });

  // DEFAULT: SEMUA TERBUKA
  document.querySelectorAll('.tree-toggle:not(.empty)').forEach(function (t) {
    t.classList.add('open');
  });

  console.log('[tree] done');
});

// ============================================
// TOGGLE SIDEBAR (Mobile)
// ============================================
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  if (!sidebar) return;
  sidebar.classList.toggle('open');
}