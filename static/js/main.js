// ============================================
// TREE VIEW TOGGLE
// ============================================
document.addEventListener('DOMContentLoaded', function () {
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