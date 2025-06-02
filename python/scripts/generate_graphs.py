#!/usr/bin/env python
"""
generate_graphs.py
Gera G1.png, G2.png, G3.png em relatorio/img/ a partir de:
  dados/resultados/tempos_python.csv
  dados/resultados/tempos_c.csv
Requer: pandas, matplotlib
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = Path("dados/resultados")
IMG_DIR  = Path("relatorio/img")
IMG_DIR.mkdir(parents=True, exist_ok=True)

df_py = pd.read_csv(DATA_DIR / "tempos_python.csv")
df_c  = pd.read_csv(DATA_DIR / "tempos_c.csv")

df_py["linguagem"] = "Python"
df_c ["linguagem"] = "C"
df = pd.concat([df_py, df_c], ignore_index=True)

stats = (
    df.groupby(["tamanho", "linguagem"])["tempo"]
      .agg(["mean", "std"])
      .reset_index()
)
pivot_mean = stats.pivot(index="tamanho", columns="linguagem", values="mean")
pivot_std  = stats.pivot(index="tamanho", columns="linguagem", values="std")
pivot_cv   = pivot_std / pivot_mean * 100
speedup    = pivot_mean["Python"] / pivot_mean["C"]

colors = {"Python": "#1f77b4", "C": "#ff7f0e"}
bar_w  = 0.35

# Gráfico 1
plt.figure(figsize=(10, 6))
for i, n in enumerate(pivot_mean.index):
    for j, lang in enumerate(["Python", "C"]):
        x = i + (j - 0.5) * bar_w
        plt.bar(x,
                pivot_mean.loc[n, lang],
                width=bar_w,
                color=colors[lang],
                label=lang if i == 0 else "")
        plt.errorbar(x,
                     pivot_mean.loc[n, lang],
                     yerr=pivot_std.loc[n, lang],
                     fmt="none", ecolor="black",
                     capsize=4, lw=1)

box_data, box_pos, box_cols = [], [], []
for i, n in enumerate(pivot_mean.index):
    for j, lang in enumerate(["Python", "C"]):
        x = i + (j - 0.5) * bar_w
        sub = df[(df.tamanho == n) & (df.linguagem == lang)]["tempo"]
        box_data.append(sub.values)
        box_pos.append(x)
        box_cols.append(colors[lang])

bp = plt.boxplot(box_data, positions=box_pos,
                 widths=bar_w*0.6, patch_artist=True,
                 showfliers=False)
for b, c in zip(bp["boxes"], box_cols):
    b.set_facecolor(c); b.set_alpha(0.35)

plt.yscale("log")
plt.xticks(range(len(pivot_mean.index)), [str(n) for n in pivot_mean.index])
plt.xlabel("Tamanho da entrada (n)")
plt.ylabel("Tempo de execução (s)")
plt.title("G1 – Tempo médio + distribuição  |  QuickSort Python vs C")
plt.legend()
plt.tight_layout()
plt.savefig(IMG_DIR / "G1.png", dpi=300)
plt.close()

# Gráfico 2
plt.figure(figsize=(8, 5))
plt.plot(pivot_mean.index, speedup, marker="o", color="black")
for x, y in zip(pivot_mean.index, speedup):
    plt.annotate(f"{y:.1f}×", (x, y),
                 textcoords="offset points", xytext=(0, 5),
                 ha="center")
plt.xscale("log")
plt.xticks(pivot_mean.index, [str(n) for n in pivot_mean.index])
plt.xlabel("Tamanho da entrada (n)")
plt.ylabel("Speed-up (Python ÷ C)")
plt.title("G2 – Fator de ganho de desempenho")
plt.tight_layout()
plt.savefig(IMG_DIR / "G2.png", dpi=300)
plt.close()


# Gráfico 3
plt.figure(figsize=(8, 5))
for lang, marker in zip(["Python", "C"], ["o", "s"]):
    plt.plot(pivot_cv.index, pivot_cv[lang],
             marker=marker, label=lang, color=colors[lang])
    for x, y in zip(pivot_cv.index, pivot_cv[lang]):
        plt.annotate(f"{y:.1f}%", (x, y),
                     textcoords="offset points", xytext=(0, 5),
                     ha="center")
plt.xscale("log")
plt.xticks(pivot_cv.index, [str(n) for n in pivot_cv.index])
plt.xlabel("Tamanho da entrada (n)")
plt.ylabel("Coef. de variação (%)")
plt.title("G3 – Estabilidade relativa dos tempos (CV)")
plt.legend()
plt.tight_layout()
plt.savefig(IMG_DIR / "G3.png", dpi=300)
plt.close()

print("✅ Figuras criadas em relatorio/img/: G1.png, G2.png, G3.png")
