import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ArrowStyle
import numpy as np

# تنظیمات عمومی برای استایل آکادمیک و کیفیت چاپ
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['axes.edgecolor'] = '#2c3e50'
plt.rcParams['axes.linewidth'] = 0.8

output_dir = '/mnt/data'
os.makedirs(output_dir, exist_ok=True)

# ==========================================
# FIGURE 1: MMM Framework Architecture (Chapter 3)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# پس‌زمینه لایه‌ها
colors = ['#e8f4f8', '#fef5e7', '#eafaf1']
borders = ['#2980b9', '#d35400', '#27ae60']
titles = ['Layer 1: Multimodal Inputs', 'Layer 2: Cognitive-Analytical Engines', 'Layer 3: Emergent Constructs']

for i in range(3):
    rect = FancyBboxPatch((0.5 + i*3.1, 0.5), 2.8, 6.0, boxstyle="round,pad=0.2",
                          ec=borders[i], fc=colors[i], lw=1.5, alpha=0.9)
    ax.add_patch(rect)
    ax.text(1.9 + i*3.1, 6.2, titles[i], ha='center', va='center', fontsize=11, fontweight='bold', color=borders[i])

# باکس‌های لایه ۱
inputs = [
    ("Lyrical Stream", "Metaphor Identification\n(MIPVU Protocol)\nLexical-semantic field"),
    ("Acoustic Stream", "Spectral Centroid, RMS\nDistortion, Dynamic Range\nTremolo & Spatial Width"),
    ("Structural Stream", "Bipartite shifts, Transitions\nRhythmic Syncopation\nBeat drops & Pauses")
]
for j, (h, b) in enumerate(inputs):
    y = 4.8 - j*1.8
    box = FancyBboxPatch((0.8, y-0.6), 2.2, 1.2, boxstyle="round,pad=0.1", ec='#7f8c8d', fc='white', lw=1)
    ax.add_patch(box)
    ax.text(1.9, y+0.25, h, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#2c3e50')
    ax.text(1.9, y-0.2, b, ha='center', va='center', fontsize=7.5, color='#555555')

# باکس‌های لایه ۲
engines = [
    ("Conceptual Metaphor", "Source-Target Mappings\n(e.g., SOUND IS CONTAINER)\nCross-modal projections"),
    ("Force Dynamics (Talmy)", "Agonist vs. Antagonist\nBLOCKAGE, REMOVAL\nCOMPULSION & RESISTANCE"),
    ("Image Schemas & Blends", "CONTAINER, VERTICALITY, PATH\nCyber-Tribal Blending\nMental Space Integration")
]
for j, (h, b) in enumerate(engines):
    y = 4.8 - j*1.8
    box = FancyBboxPatch((3.9, y-0.6), 2.2, 1.2, boxstyle="round,pad=0.1", ec='#7f8c8d', fc='white', lw=1)
    ax.add_patch(box)
    ax.text(5.0, y+0.25, h, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#2c3e50')
    ax.text(5.0, y-0.2, b, ha='center', va='center', fontsize=7.5, color='#555555')

# باکس‌های لایه ۳
constructs = [
    ("Cyber-Tribal Blend", "Anachronistic tension\nAfro-futurist grounding\n(HYAENA)"),
    ("Force-Dynamic Utopia", "Acoustic friction &\nSystemic impediment\n(SIRENS)"),
    ("Utopian Vertigo", "Catastrophic acceleration &\nVertical disorientation\n(MY EYES)")
]
for j, (h, b) in enumerate(constructs):
    y = 4.8 - j*1.8
    box = FancyBboxPatch((7.0, y-0.6), 2.2, 1.2, boxstyle="round,pad=0.1", ec='#7f8c8d', fc='white', lw=1)
    ax.add_patch(box)
    ax.text(8.1, y+0.25, h, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#2c3e50')
    ax.text(8.1, y-0.2, b, ha='center', va='center', fontsize=7.5, color='#555555')

# فلش‌های ارتباطی بین لایه‌ها
arrow_style = ArrowStyle("->", head_length=4, head_width=2.5)
for y_pos in [4.8, 3.0, 1.2]:
    ax.annotate('', xy=(3.8, y_pos), xytext=(3.1, y_pos),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#2980b9"))
    ax.annotate('', xy=(6.9, y_pos), xytext=(6.2, y_pos),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#d35400"))

# فلش بازخورد و پایایی ارزیابان
ax.annotate('Inter-Rater Reliability Protocol (Cohen\'s $\\kappa = 0.84$)', xy=(8.1, 0.4), xytext=(1.9, 0.4),
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#2c3e50',
            bbox=dict(boxstyle="square,pad=0.4", fc="#ecf0f1", ec="#95a5a6", lw=1))

plt.title("Figure 1: Multimodal Mapping Matrix (MMM) Triangulation Architecture", fontsize=13, fontweight='bold', pad=15)
plt.tight_layout()
plt.savefig(f"{output_dir}/figure1_mmm_methodology.png", dpi=300, bbox_inches='tight')
plt.close()


# ==========================================
# FIGURE 2: HYAENA - Cyber-Tribal Blend (Chapter 4)
# ==========================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 6), sharex=True, dpi=300, gridspec_kw={'height_ratios': [1.8, 1.2]})

t = np.linspace(0, 222, 500) # طول ترَک: ۳:۴۲ (۲۲۲ ثانیه)

# شبیه‌سازی لایه‌های آکوستیک و درگیری شماها
tribal_intensity = np.where(t < 35, 0.85, np.where(t < 130, 0.4, 0.6))
cyber_intensity = np.where(t < 35, 0.1, np.where(t < 130, 0.85, 0.75))
noise = np.random.normal(0, 0.03, len(t))

ax1.plot(t, np.clip(tribal_intensity + noise, 0, 1), color='#d35400', lw=2, label="Organic/Tribal Input (Funkadelic Sample, Congas, Breath)")
ax1.plot(t, np.clip(cyber_intensity + noise, 0, 1), color='#2980b9', lw=2, linestyle='--', label="Cyber/Synthetic Input (Distorted 808s, Digital Glitch, Auto-Tune)")
ax1.fill_between(t, 0, np.minimum(tribal_intensity, cyber_intensity), color='#8e44ad', alpha=0.25, label="Emergent Cyber-Tribal Blend Zone")

# تفکیک بخش‌های ترَک
sections = [(0, 35, "Intro / Sample Hook"), (35, 120, "Verse 1 (Cyber Dominance)"), (120, 165, "Chorus / Poly-Rhythm"), (165, 222, "Outro (Tribal-Industrial Fade)")]
for start, end, label in sections:
    ax1.axvline(start, color='#7f8c8d', linestyle=':', lw=1)
    ax1.text((start+end)/2, 0.93, label, ha='center', va='center', fontsize=8, fontweight='bold', bbox=dict(boxstyle='round,pad=0.2', fc='white', ec='none', alpha=0.7))

ax1.set_ylabel("Salience / Acoustic Weight", fontsize=9.5, fontweight='bold')
ax1.set_title("Figure 2: HYAENA — Emergence of the Cyber-Tribal Blend Across Structural Timeline", fontsize=11.5, fontweight='bold')
ax1.legend(loc="lower left", fontsize=8.5, framealpha=0.9)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.set_ylim(-0.05, 1.05)

# نمودار پایین: فعال‌سازی شماهای تصویری
schemas = ['CONTAINER (Insularity)', 'FORCE (Primal Aggression)', 'PATH (Afro-Futurist Trajectory)']
schema_vals = np.array([
    np.where(t < 50, 0.8, 0.45),
    np.where((t >= 35) & (t < 165), 0.9, 0.5),
    np.where(t >= 120, 0.85, 0.3)
])

for i, s in enumerate(schemas):
    ax2.plot(t, schema_vals[i], lw=1.8, label=s)

ax2.set_xlabel("Time (seconds)", fontsize=9.5, fontweight='bold')
ax2.set_ylabel("Schema Activation", fontsize=9.5, fontweight='bold')
ax2.set_ylim(0, 1.1)
ax2.legend(loc="upper right", fontsize=8, ncol=3)
ax2.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig(f"{output_dir}/figure2_hyaena_cybertribal.png", dpi=300, bbox_inches='tight')
plt.close()


# ==========================================
# FIGURE 3: SIRENS - Force Dynamics (Chapter 4)
# ==========================================
fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
t = np.linspace(0, 204, 500) # طول ترَک: ۳:۲۴ (۲۰۴ ثانیه)

# مدل‌سازی کشمکش آگونیست و آنتاگونیست
agonist_force = 0.5 + 0.35 * np.sin(t / 20) + 0.1 * np.cos(t / 5)
antagonist_resistance = 0.6 + 0.25 * np.cos(t / 15)

ax.plot(t, agonist_force, color='#c0392b', lw=2.2, label=r"Agonist Vector ($\mathbf{F}_A$): Lyrical Drive / Vocal Urgency")
ax.plot(t, antagonist_resistance, color='#2c3e50', lw=2.2, linestyle='--', label=r"Antagonist Vector ($\mathbf{F}_R$): Rhythmic Syncopation / Sonic Blockage")

# تشخیص نقاط شکست سد (Breakthrough) و انسداد (Blockage)
breakthrough = agonist_force > antagonist_resistance
ax.fill_between(t, agonist_force, antagonist_resistance, where=breakthrough, color='#27ae60', alpha=0.2, label="Force Overcoming Blockage (Breakthrough)")
ax.fill_between(t, agonist_force, antagonist_resistance, where=~breakthrough, color='#e74c3c', alpha=0.2, label="Force Impeded (Acoustic Compression/Entrapment)")

# رویدادهای بحرانی ترَک
events = [(42, "Sub-bass Drop\n(Resistance Surge)"), (112, "Siren Ostinato Peak\n(Sensory Saturation)"), (175, "Beat Mutilation\n(Systemic Collapse)")]
for x, text in events:
    ax.axvline(x, color='#8e44ad', linestyle='-.', lw=1.2)
    ax.annotate(text, xy=(x, 0.88), xytext=(x+3, 0.96),
                arrowprops=dict(arrowstyle="->", color='#8e44ad', lw=1),
                fontsize=8, fontweight='bold', bbox=dict(boxstyle="round,pad=0.2", fc="#f4ecf7", ec="#8e44ad"))

ax.set_title("Figure 3: SIRENS — Force-Dynamic Modeling of Agonist-Antagonist Friction", fontsize=11.5, fontweight='bold')
ax.set_xlabel("Time (seconds)", fontsize=9.5, fontweight='bold')
ax.set_ylabel("Dynamic Intensity Arbitrary Units", fontsize=9.5, fontweight='bold')
ax.set_ylim(0.1, 1.1)
ax.legend(loc="lower left", fontsize=8.5, framealpha=0.9)
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig(f"{output_dir}/figure3_sirens_forcedynamics.png", dpi=300, bbox_inches='tight')
plt.close()


# ==========================================
# FIGURE 4: MY EYES - Utopian Vertigo (Chapter 4)
# ==========================================
fig, ax = plt.subplots(figsize=(10.5, 5.5), dpi=300)

# دو فاز متمایز ترَک (تقسیم در ثانیه ۱32)
split_point = 132
t_part1 = np.linspace(0, split_point, 250)
t_part2 = np.linspace(split_point, 251, 250)

# پارت ۱: فرورفتگی درون‌گرایانه (CONTAINER / DOWN)
bpm_part1 = np.full_like(t_part1, 118)
vertigo_part1 = 0.2 + 0.1 * np.sin(t_part1/15)

# پارت ۲: شتاب عمودی ناگهانی و سرگیجه (UP / VERTIGO)
bpm_part2 = np.linspace(148, 160, 250)
vertigo_part2 = np.linspace(0.4, 0.98, 250) + 0.05 * np.sin(t_part2/4)

ax.plot(np.concatenate([t_part1, t_part2]), np.concatenate([vertigo_part1, vertigo_part2]),
        color='#e67e22', lw=2.5, label="Utopian Vertigo Index (Ascent Velocity × Harmonic Instability)")

# شیدینگ دو فاز ساختاری
ax.axvspan(0, split_point, color='#34495e', alpha=0.1, label="Phase I: Somber Contemplation (CONTAINMENT / GROUNDED)")
ax.axvspan(split_point, 251, color='#e74c3c', alpha=0.12, label="Phase II: Manic Vertical Acceleration (VERTICALITY / FLIGHT)")

ax.axvline(split_point, color='#c0392b', linestyle='--', lw=2)
ax.text(split_point, 0.98, "METAMORPHIC RUPTURE (2:12)\nSudden Tempo Jump (118 -> 148 BPM)",
        ha='center', va='top', fontsize=8.5, fontweight='bold', color='#c0392b',
        bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2e9", ec="#c0392b"))

# نشانه‌گذاری‌های شمای تصویری
ax.text(60, 0.25, "Dominated by:\n• CONTAINER (Isolation)\n• DOWN (Melancholia)\n• REPOSE",
        fontsize=8.5, ha='center', bbox=dict(boxstyle='square,pad=0.4', fc='white', ec='#7f8c8d'))
ax.text(195, 0.65, "Dominated by:\n• VERTICALITY (Ascent)\n• COMPULSION\n• DIZZINESS / LOSS OF CONTROL",
        fontsize=8.5, ha='center', bbox=dict(boxstyle='square,pad=0.4', fc='white', ec='#7f8c8d'))

ax.set_title("Figure 4: MY EYES — Bipartite Metamorphosis and Induction of Utopian Vertigo", fontsize=11.5, fontweight='bold')
ax.set_xlabel("Time (seconds)", fontsize=9.5, fontweight='bold')
ax.set_ylabel("Cognitive / Affective Vertigo Metric", fontsize=9.5, fontweight='bold')
ax.set_ylim(0, 1.1)
ax.legend(loc="lower right", fontsize=8.5, framealpha=0.9)
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
plt.savefig(f"{output_dir}/figure4_myeyes_vertigo.png", dpi=300, bbox_inches='tight')
plt.close()


# ==========================================
# FIGURE 5: Cross-Track Synthesis & Reliability (Chapter 4)
# ==========================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5), dpi=300, gridspec_kw={'width_ratios': [1.3, 1]})

# ۱. توزیع بسامد شماهای تصویری در ۳ ترَک
schemas = ['CONTAINER', 'FORCE', 'PATH', 'VERTICALITY', 'BALANCE']
tracks_data = {
    'HYAENA': [0.85, 0.90, 0.70, 0.35, 0.20],
    'SIRENS': [0.45, 0.95, 0.80, 0.50, 0.15],
    'MY EYES': [0.90, 0.60, 0.40, 0.95, 0.30]
}

x = np.arange(len(schemas))
width = 0.25

rects1 = ax1.bar(x - width, tracks_data['HYAENA'], width, label='HYAENA', color='#d35400', alpha=0.85)
rects2 = ax1.bar(x, tracks_data['SIRENS'], width, label='SIRENS', color='#2980b9', alpha=0.85)
rects3 = ax1.bar(x + width, tracks_data['MY EYES'], width, label='MY EYES', color='#8e44ad', alpha=0.85)

ax1.set_ylabel('Dominant Schema Incidence Index', fontsize=9.5, fontweight='bold')
ax1.set_title('A: Cross-Track Schema Profiles', fontsize=10.5, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(schemas, fontsize=8.5, fontweight='bold')
ax1.legend(fontsize=8.5)
ax1.grid(True, linestyle=':', axis='y', alpha=0.6)
ax1.set_ylim(0, 1.15)

# ۲. شاخص پایایی بین ارزیابان (Cohen's Kappa)
dimensions = ['Image Schemas', 'Force Dynamics', 'Metaphor (MIPVU)', 'Conceptual Blends', 'Overall Agreement']
kappa_scores = [0.86, 0.82, 0.85, 0.81, 0.84]
colors = ['#27ae60' if k >= 0.8 else '#f39c12' for k in kappa_scores]

y_pos = np.arange(len(dimensions))
ax2.barh(y_pos, kappa_scores, color=colors, height=0.55, edgecolor='#2c3e50', lw=0.8)
ax2.axvline(0.80, color='#c0392b', linestyle='--', lw=1.2, label='Almost Perfect Agreement (0.80)')

for i, v in enumerate(kappa_scores):
    ax2.text(v + 0.02, i, f"$\\kappa = {v:.2f}$", va='center', fontsize=8.5, fontweight='bold', color='#2c3e50')

ax2.set_yticks(y_pos)
ax2.set_yticklabels(dimensions, fontsize=8.5, fontweight='bold')
ax2.set_xlabel("Cohen's Kappa ($\\kappa$)", fontsize=9.5, fontweight='bold')
ax2.set_title('B: Inter-Rater Reliability Calibration', fontsize=10.5, fontweight='bold')
ax2.set_xlim(0.6, 1.0)
ax2.legend(loc='lower left', fontsize=8)
ax2.grid(True, linestyle=':', axis='x', alpha=0.6)

plt.suptitle("Figure 5: Cross-Case Comparative Synthesis and Analytical Reliability", fontsize=12, fontweight='bold', y=0.98)
plt.tight_layout()
plt.savefig(f"{output_dir}/figure5_crosstrack_reliability.png", dpi=300, bbox_inches='tight')
plt.close()

print("All 5 figures generated successfully at 300 DPI.")
