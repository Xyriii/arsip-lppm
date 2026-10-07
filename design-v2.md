# DESIGN-V2.MD — Arsip LPPM UNS

> Reference: **Linear.app** — minimalis, elegant, subtle animation.
> Warna utama: **UNS Blue #0058A8** (tetap).
> Vibe: Clean, calm, no AI-generated look.

---

## 1. PRINSIP

- **Whitespace generus** — jarak lebih lega
- **Subtle > Bold** — border tipis, shadow halus
- **Motion as feedback** — animasi untuk nunjukin "hidup"
- **Typography scale konsisten**
- **Dark mode first** — design di dark dulu

---

## 2. WARNA

### Light Mode
```css
--bg-base: #FAFBFC;
--bg-surface: #FFFFFF;
--bg-hover: #F5F7FA;

--border-subtle: #E8EBEF;
--border-strong: #D1D5DB;
--border-focus: #0058A8;

--text-primary: #0A0E17;
--text-secondary: #4B5563;
--text-tertiary: #9CA3AF;
--text-inverse: #FFFFFF;

--accent: #0058A8;
--accent-hover: #003D75;
--accent-soft: rgba(0, 88, 168, 0.08);
--accent-border: rgba(0, 88, 168, 0.2);

Aturan:
Max 2 aksen warna (UNS Blue + 1 status)
Jangan gradient colorful
Boleh gradient subtle (UNS Blue → UNS Blue Dark)

TYPOGRAPHY
Font: Inter (dengan font-feature-settings: "cv11", "ss01")
--text-xs: 11px;
--text-sm: 13px;
--text-base: 14px;    /* body default */
--text-md: 15px;
--text-lg: 18px;
--text-xl: 24px;
--text-2xl: 32px;
--text-3xl: 44px;

Weight: 400 (body), 500 (label), 600 (heading), 700 (hero)
Line-height: 1.5 (body), 1.2 (heading)
Letter-spacing: -0.01em (heading), 0 (body)

SPACING (8px based)
--space-1: 4px;   --space-2: 8px;   --space-3: 12px;
--space-4: 16px;  --space-5: 20px;  --space-6: 24px;
--space-8: 32px;  --space-10: 40px; --space-12: 48px;
--space-16: 64px;

RADIUS & BORDER
--radius-sm: 6px;
--radius-md: 8px;
--radius-lg: 12px;
--radius-xl: 16px;
--radius-full: 999px;

--border-width: 1px;

SHADOW
--shadow-xs: 0 1px 2px rgba(10, 14, 23, 0.04);
--shadow-sm: 0 1px 3px rgba(10, 14, 23, 0.06), 0 1px 2px rgba(10, 14, 23, 0.04);
--shadow-md: 0 4px 12px rgba(10, 14, 23, 0.08), 0 2px 4px rgba(10, 14, 23, 0.04);
--shadow-lg: 0 12px 32px rgba(10, 14, 23, 0.12), 0 4px 8px rgba(10, 14, 23, 0.06);
--shadow-focus: 0 0 0 4px rgba(0, 88, 168, 0.12);

Aturan:
Card default: --shadow-xs (flat)
Hover: --shadow-md
Modal: --shadow-lg

MOTION
--motion-fast: 150ms;
--motion-base: 200ms;
--motion-slow: 300ms;
--motion-spring: cubic-bezier(0.16, 1, 0.3, 1);

Animasi Wajib
Page Enter (fade-up):
@keyframes fade-up {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: translateY(0); }
}
Scroll Reveal (via IntersectionObserver):
.reveal {
  opacity: 0;
  transform: translateY(12px);
  transition: opacity 400ms cubic-bezier(0.16, 1, 0.3, 1),
              transform 400ms cubic-bezier(0.16, 1, 0.3, 1);
}
.reveal.in-view {
  opacity: 1;
  transform: translateY(0);
}
Hover Lift (card):
.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}
Button Press:
.btn:active { transform: scale(0.97); }

Aturan:
Durasi max 300ms (kecuali scroll reveal 400ms)
Easing: cubic-bezier(0.16, 1, 0.3, 1) (spring feel)
Respect prefers-reduced-motion

KOMPONEN
Button
Primary: Height 36px, padding 0 16px, radius 8px, bg --accent, font-size 13px, weight 500
Secondary: Bg --bg-surface, border 1px --border-subtle, text --text-primary
Ghost: Transparent, text --text-secondary, hover bg --bg-hover

Input
Height 36px, padding 0 12px, bg --bg-surface, border 1px --border-subtle, radius 8px
Focus: border --border-focus, shadow --shadow-focus

Card
Bg --bg-surface, border 1px --border-subtle, radius 12px, padding 20px, shadow --shadow-xs
Hover: translateY(-2px), shadow --shadow-md

Chip
Height 22px, padding 0 8px, radius 6px, font-size 11px, uppercase, letter-spacing 0.04em

Table
Header bg --bg-hover, padding 10px 16px, font-size 12px, uppercase, color --text-tertiary
Row padding 12px 16px, border-bottom 1px --border-subtle, hover bg --bg-hover

Navbar (Topbar)
Height 56px, bg rgba(255,255,255,0.8) + backdrop-filter: blur(12px), border-bottom 1px --border-subtle, sticky top 0

Modal
Max-width 480px, bg --bg-surface, border 1px --border-strong, radius 16px, padding 24px, shadow --shadow-lg
Backdrop: rgba(10, 14, 23, 0.4) + blur(4px)

LAYOUT
Hybrid — Topbar + Sidebar Collapsible
┌─────────────────────────────────────────┐
│ TOPBAR (56px, sticky, glass)            │
├──────┬──────────────────────────────────┤
│      │                                  │
│ SIDE │  CONTENT                         │
│ BAR  │  (max-width 1280px, center)      │
│ 240/ │  Padding 32px                    │
│ 60px │                                  │
└──────┴──────────────────────────────────┘

Sidebar:
Width 240px (expanded) / 60px (collapsed)
Bisa di-toggle
Sticky, scroll sendiri
Icon-only kalau collapsed

Topbar:
Logo (kiri)
Global Search (tengah)
Dark mode, User menu (kanan)

LANDING PAGE (Public)
Multi-section:
Hero — Headline besar + subheadline + search prominent + 3 stat
Quick Access — 4 card (Cari, Jelajah, Kategori, Panduan)
Arsip Terbaru — grid 4 card preview
Cara Penggunaan — 3 langkah (Cari → Lihat → Download)
Statistik Highlight — grafik sederhana
Link Terkait — UNS, LPPM, sosmed
Footer — Copyright + link
Animasi: Setiap section pakai .reveal (IntersectionObserver)

DO'S & DON'TS
✅ DO:
Whitespace generus
Border tipis 1px subtle
Shadow halus (cuma saat hover)
Font Inter, ukuran 13-15px
Animasi fade-up saat scroll
Icon Lucide stroke 1.5
Dark mode first

❌ DON'T:
Shadow tebal
Border 2px+
Warna >2 aksen
Gradient colorful
Emoji
Card glass/blur berlebihan
Border radius >16px
Animasi >300ms
Font >4 ukuran per halaman

REFERENSI
linear.app — utama
vercel.com/dashboard — layout
notion.so — typography
stripe.com — subtle detail

Versi: 2.0
Status: Active
Maintainer: Lead Developer + Backend (Prof. Eyiri)
            Frontend (Andika)
            DataEnrty (Dewa)
            QA (Anggi)