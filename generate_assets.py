"""
THE FUTURE OF CLASSROOMS
Reimagining Education Through Innovation, Intelligence and Technology
File: generate_assets.py

Scientific Asset, Dataset, Visualization & Audio Generator
Generates:
1. Synthetic Reproducible Educational Dataset (N=500, Seed=42)
2. Calculated Statistical Metrics & Learning Model Comparisons
3. Five MATLAB-Grade Scientific Visualizations (PNG at 300 DPI)
4. Export to CSV and JSON (data/ and static/results/)
5. Synthesized Audio Assets (.wav): ambient conference, transition, ui click
"""

import os
import math
import struct
import wave
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
STATIC_RESULTS_DIR = os.path.join(BASE_DIR, "static", "results")
STATIC_AUDIO_DIR = os.path.join(BASE_DIR, "static", "audio")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(STATIC_RESULTS_DIR, exist_ok=True)
os.makedirs(STATIC_AUDIO_DIR, exist_ok=True)

# ==============================================================================
# 1. SYNTHETIC EDUCATIONAL DATASET GENERATION
# ==============================================================================

def generate_classroom_dataset(n_samples=500, random_seed=42):
    """
    Generates a reproducible synthetic educational simulation dataset (N=500)
    representing student learning sessions, feedback metrics, and outcomes across
    two educational modalities:
      1. Adaptive AI-Assisted (N=250)
      2. Traditional Standardized (N=250)

    Parameters (0-100 scale unless noted):
      - Engagement_Score: Active attention, interaction frequency, session immersion
      - Participation_Rate: Question asking, discussions, digital board contribution
      - Assessment_Performance: Mastery of core concepts, quizzes, project reviews
      - Learning_Time_Hours: Weekly self-paced learning time (15-55 hours)
      - Feedback_Frequency: Formative recommendations/interventions received per week (2-14)
      - Collaborative_Participation: Peer problem-solving, group innovation projects
      - Concept_Retention: Long-term retention test score measured at 8 weeks post-instruction
    """
    np.random.seed(random_seed)
    n_half = n_samples // 2

    # Group 1: Traditional Standardized Model (Fixed pace, periodic batch grading)
    latent_trad_ability = np.random.normal(0, 1, n_half)
    latent_trad_grit = np.random.normal(0, 1, n_half)

    trad_engagement = 62.0 + 8.5 * latent_trad_ability + 4.0 * latent_trad_grit + np.random.normal(0, 4.0, n_half)
    trad_participation = 58.5 + 9.0 * latent_trad_ability + 3.5 * latent_trad_grit + np.random.normal(0, 4.5, n_half)
    trad_assessment = 69.0 + 10.0 * latent_trad_ability + 5.0 * latent_trad_grit + np.random.normal(0, 3.5, n_half)
    trad_hours = 28.0 + 4.5 * latent_trad_grit + np.random.normal(0, 3.0, n_half)
    trad_feedback = 3.5 + 1.0 * latent_trad_ability + np.random.normal(0, 0.8, n_half)
    trad_collaborative = 59.0 + 8.0 * latent_trad_ability + np.random.normal(0, 5.0, n_half)
    # Traditional concept retention decays faster without timely adaptive feedback
    trad_retention = 61.5 + 7.5 * latent_trad_ability + 4.0 * latent_trad_grit + 0.8 * trad_feedback + np.random.normal(0, 4.0, n_half)

    # Group 2: Adaptive AI-Assisted Model (Personalized scaffolding, instant feedback)
    latent_ai_ability = np.random.normal(0, 1, n_half)
    latent_ai_grit = np.random.normal(0, 1, n_half)

    ai_engagement = 82.5 + 6.5 * latent_ai_ability + 5.0 * latent_ai_grit + np.random.normal(0, 3.5, n_half)
    ai_participation = 79.0 + 7.5 * latent_ai_ability + 4.5 * latent_ai_grit + np.random.normal(0, 4.0, n_half)
    ai_assessment = 84.5 + 7.0 * latent_ai_ability + 5.5 * latent_ai_grit + np.random.normal(0, 3.0, n_half)
    ai_hours = 34.5 + 5.0 * latent_ai_grit + np.random.normal(0, 3.2, n_half)
    ai_feedback = 9.8 + 1.8 * latent_ai_ability + np.random.normal(0, 1.2, n_half)
    ai_collaborative = 78.5 + 7.0 * latent_ai_ability + 3.5 * latent_ai_grit + np.random.normal(0, 4.0, n_half)
    # Retention bolstered by formative spaced repetition & immediate interactive correction
    ai_retention = 81.0 + 6.5 * latent_ai_ability + 4.5 * latent_ai_grit + 1.1 * ai_feedback + np.random.normal(0, 3.5, n_half)

    # Assemble arrays
    modalities = ["Traditional Standardized"] * n_half + ["Adaptive AI-Assisted"] * n_half
    engagements = np.concatenate([trad_engagement, ai_engagement])
    participations = np.concatenate([trad_participation, ai_participation])
    assessments = np.concatenate([trad_assessment, ai_assessment])
    hours = np.concatenate([trad_hours, ai_hours])
    feedbacks = np.concatenate([trad_feedback, ai_feedback])
    collaboratives = np.concatenate([trad_collaborative, ai_collaborative])
    retentions = np.concatenate([trad_retention, ai_retention])

    # Clip to realistic physiological/pedagogical bounds
    engagements = np.clip(np.round(engagements, 1), 35.0, 99.5)
    participations = np.clip(np.round(participations, 1), 30.0, 99.0)
    assessments = np.clip(np.round(assessments, 1), 40.0, 99.5)
    hours = np.clip(np.round(hours, 1), 14.0, 58.0)
    feedbacks = np.clip(np.round(feedbacks, 1), 1.0, 15.0)
    collaboratives = np.clip(np.round(collaboratives, 1), 30.0, 99.0)
    retentions = np.clip(np.round(retentions, 1), 35.0, 99.5)

    # Composite Holistic Mastery Index
    mastery_index = np.round(
        0.25 * assessments +
        0.25 * retentions +
        0.20 * engagements +
        0.15 * collaboratives +
        0.15 * participations,
        1
    )

    df = pd.DataFrame({
        "Student_ID": [f"STU-{1001 + i}" for i in range(n_samples)],
        "Learning_Model": modalities,
        "Engagement_Score": engagements,
        "Participation_Rate": participations,
        "Assessment_Performance": assessments,
        "Learning_Time_Hours": hours,
        "Feedback_Frequency": feedbacks,
        "Collaborative_Score": collaboratives,
        "Concept_Retention": retentions,
        "Mastery_Index": mastery_index
    })

    return df

# ==============================================================================
# 2. STATISTICAL ANALYSIS & METRICS EXPORT
# ==============================================================================

def compute_statistics(df):
    """Computes comprehensive descriptive and comparative analytics."""
    trad_df = df[df["Learning_Model"] == "Traditional Standardized"]
    ai_df = df[df["Learning_Model"] == "Adaptive AI-Assisted"]

    numeric_cols = [
        "Engagement_Score", "Participation_Rate", "Assessment_Performance",
        "Learning_Time_Hours", "Feedback_Frequency", "Collaborative_Score",
        "Concept_Retention", "Mastery_Index"
    ]

    corr_matrix = df[numeric_cols].corr().round(3).to_dict()

    metrics = {
        "meta": {
            "title": "THE FUTURE OF CLASSROOMS - SYNTHETIC SIMULATION DATASET",
            "sample_size": len(df),
            "seed": 42,
            "disclaimer": "EDUCATIONAL SIMULATION — SYNTHETIC DATA. Generated for academic visualization and conceptual modelling."
        },
        "overall_summary": {},
        "model_comparison": {
            "Traditional_Standardized": {},
            "Adaptive_AI_Assisted": {}
        },
        "correlation_matrix": corr_matrix,
        "key_insights": {
            "retention_gain_pct": round(float((ai_df["Concept_Retention"].mean() - trad_df["Concept_Retention"].mean()) / trad_df["Concept_Retention"].mean() * 100), 1),
            "engagement_delta": round(float(ai_df["Engagement_Score"].mean() - trad_df["Engagement_Score"].mean()), 1),
            "feedback_multiplier": round(float(ai_df["Feedback_Frequency"].mean() / trad_df["Feedback_Frequency"].mean()), 2),
            "assessment_delta": round(float(ai_df["Assessment_Performance"].mean() - trad_df["Assessment_Performance"].mean()), 1),
            "mastery_delta": round(float(ai_df["Mastery_Index"].mean() - trad_df["Mastery_Index"].mean()), 1)
        }
    }

    for col in numeric_cols:
        metrics["overall_summary"][col] = {
            "mean": round(float(df[col].mean()), 2),
            "std": round(float(df[col].std()), 2),
            "median": round(float(df[col].median()), 2),
            "min": round(float(df[col].min()), 2),
            "max": round(float(df[col].max()), 2)
        }
        metrics["model_comparison"]["Traditional_Standardized"][col] = {
            "mean": round(float(trad_df[col].mean()), 2),
            "std": round(float(trad_df[col].std()), 2)
        }
        metrics["model_comparison"]["Adaptive_AI_Assisted"][col] = {
            "mean": round(float(ai_df[col].mean()), 2),
            "std": round(float(ai_df[col].std()), 2)
        }

    # Save to data/ and static/results/
    csv_path1 = os.path.join(DATA_DIR, "classroom_dataset.csv")
    csv_path2 = os.path.join(STATIC_RESULTS_DIR, "classroom_dataset.csv")
    df.to_csv(csv_path1, index=False)
    df.to_csv(csv_path2, index=False)

    json_path1 = os.path.join(DATA_DIR, "analysis_results.json")
    json_path2 = os.path.join(RESULTS_DIR, "analysis_results.json")
    json_path3 = os.path.join(STATIC_RESULTS_DIR, "analysis_results.json")
    for p in [json_path1, json_path2, json_path3]:
        with open(p, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=2)

    print(f"  -> Exported CSV: {csv_path1}")
    print(f"  -> Exported JSON: {json_path1}")
    return metrics

# ==============================================================================
# 3. FIVE SCIENTIFIC VISUALIZATIONS (MATLAB-GRADE, 300 DPI)
# ==============================================================================

def set_academic_plot_style():
    """Sets a premium dark academic cyber-palette for scientific plots."""
    plt.rcParams.update({
        'font.sans-serif': 'DejaVu Sans',
        'font.family': 'sans-serif',
        'axes.edgecolor': '#334155',
        'axes.linewidth': 1.2,
        'axes.labelcolor': '#cbd5e1',
        'xtick.color': '#94a3b8',
        'ytick.color': '#94a3b8',
        'text.color': '#f8fafc',
        'grid.color': '#1e293b',
        'grid.linestyle': '--',
        'grid.alpha': 0.6
    })

def generate_visualizations(df, metrics):
    set_academic_plot_style()
    trad = df[df["Learning_Model"] == "Traditional Standardized"]
    ai = df[df["Learning_Model"] == "Adaptive AI-Assisted"]

    # --------------------------------------------------------------------------
    # PLOT A: Student Engagement Trends (student_engagement.png)
    # --------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    fig.patch.set_facecolor('#070d18')
    ax.set_facecolor('#0b1626')

    # Scatter with transparency
    ax.scatter(trad["Learning_Time_Hours"], trad["Engagement_Score"], color='#38bdf8', alpha=0.55, s=28, label='Traditional Model (N=250)', edgecolors='none')
    ax.scatter(ai["Learning_Time_Hours"], ai["Engagement_Score"], color='#00e5ff', alpha=0.65, s=32, label='Adaptive AI-Assisted (N=250)', edgecolors='none')

    # Polynomial trend lines
    p_trad = np.poly1d(np.polyfit(trad["Learning_Time_Hours"], trad["Engagement_Score"], 2))
    p_ai = np.poly1d(np.polyfit(ai["Learning_Time_Hours"], ai["Engagement_Score"], 2))
    x_grid = np.linspace(15, 55, 100)

    ax.plot(x_grid, p_trad(x_grid), color='#0284c7', linewidth=2.8, linestyle='--', label=f'Traditional Fit (μ={trad["Engagement_Score"].mean():.1f})')
    ax.plot(x_grid, p_ai(x_grid), color='#22d3ee', linewidth=3.2, label=f'Adaptive AI Fit (μ={ai["Engagement_Score"].mean():.1f})')

    ax.set_title('Student Engagement vs. Weekly Learning Time [MATLAB Sim]', color='#ffffff', fontsize=12.5, fontweight='bold', pad=14)
    ax.set_xlabel('Weekly Self-Paced Learning Time (Hours)', color='#cbd5e1', fontsize=10.5)
    ax.set_ylabel('Active Engagement Score (0-100 Scale)', color='#cbd5e1', fontsize=10.5)
    ax.legend(facecolor='#0f1b2d', edgecolor='#334155', fontsize=9, loc='upper left')
    ax.grid(True)
    ax.text(0.98, 0.04, 'SYNTHETIC SIMULATION DATA — N=500', transform=ax.transAxes, fontsize=8, color='#64748b', ha='right', family='monospace')

    plt.tight_layout()
    p1 = os.path.join(RESULTS_DIR, "student_engagement.png")
    fig.savefig(p1, dpi=300)
    fig.savefig(os.path.join(STATIC_RESULTS_DIR, "student_engagement.png"), dpi=300)
    plt.close(fig)
    print("  -> Saved student_engagement.png")

    # --------------------------------------------------------------------------
    # PLOT B: Personalized vs Standardized Learning Comparison (learning_comparison.png)
    # --------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    fig.patch.set_facecolor('#070d18')
    ax.set_facecolor('#0b1626')

    categories = ['Engagement', 'Participation', 'Assessment', 'Collaborative', 'Retention', 'Mastery']
    cols = ['Engagement_Score', 'Participation_Rate', 'Assessment_Performance', 'Collaborative_Score', 'Concept_Retention', 'Mastery_Index']

    trad_means = [trad[c].mean() for c in cols]
    trad_stds = [trad[c].std() for c in cols]
    ai_means = [ai[c].mean() for c in cols]
    ai_stds = [ai[c].std() for c in cols]

    x = np.arange(len(categories))
    width = 0.36

    rects1 = ax.bar(x - width/2, trad_means, width, yerr=trad_stds, capsize=4, label='Traditional Standardized', color='#1e3a5f', edgecolor='#38bdf8', linewidth=1.2, alpha=0.9)
    rects2 = ax.bar(x + width/2, ai_means, width, yerr=ai_stds, capsize=4, label='Adaptive AI-Assisted', color='#0284c7', edgecolor='#00e5ff', linewidth=1.5, alpha=0.95)

    ax.set_ylabel('Score / Index (0-100)', color='#cbd5e1', fontsize=10.5)
    ax.set_title('Comparative Learning Model Analysis Across Core Competencies', color='#ffffff', fontsize=12.5, fontweight='bold', pad=14)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10, fontweight='bold')
    ax.set_ylim(0, 115)
    ax.legend(facecolor='#0f1b2d', edgecolor='#334155', fontsize=9.5, loc='upper left')
    ax.grid(axis='y', alpha=0.6)

    # Value callouts on top of bars
    for rect in rects1:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}', xy=(rect.get_x() + rect.get_width()/2, h + 3.5), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8, color='#94a3b8', fontweight='bold')
    for rect in rects2:
        h = rect.get_height()
        ax.annotate(f'{h:.1f}', xy=(rect.get_x() + rect.get_width()/2, h + 3.5), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8, color='#00e5ff', fontweight='bold')

    ax.text(0.98, 0.04, 'SYNTHETIC SIMULATION DATA — N=500', transform=ax.transAxes, fontsize=8, color='#64748b', ha='right', family='monospace')
    plt.tight_layout()
    p2 = os.path.join(RESULTS_DIR, "learning_comparison.png")
    fig.savefig(p2, dpi=300)
    fig.savefig(os.path.join(STATIC_RESULTS_DIR, "learning_comparison.png"), dpi=300)
    plt.close(fig)
    print("  -> Saved learning_comparison.png")

    # --------------------------------------------------------------------------
    # PLOT C: Learning Parameter Correlation Heatmap (learning_correlation.png)
    # --------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8.5, 6.5), dpi=300)
    fig.patch.set_facecolor('#070d18')
    ax.set_facecolor('#0b1626')

    short_labels = ['Engage', 'Participate', 'Assess', 'Hours', 'Feedback', 'Collab', 'Retain', 'Mastery']
    numeric_cols = [
        "Engagement_Score", "Participation_Rate", "Assessment_Performance",
        "Learning_Time_Hours", "Feedback_Frequency", "Collaborative_Score",
        "Concept_Retention", "Mastery_Index"
    ]
    corr = df[numeric_cols].corr().values

    im = ax.imshow(corr, cmap='Blues', vmin=-0.2, vmax=1.0)
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(colors='#94a3b8')
    cbar.set_label('Pearson Correlation Coefficient (r)', color='#cbd5e1', fontsize=9.5)

    ax.set_xticks(np.arange(len(short_labels)))
    ax.set_yticks(np.arange(len(short_labels)))
    ax.set_xticklabels(short_labels, color='#cbd5e1', fontsize=9.5, rotation=35, ha='right')
    ax.set_yticklabels(short_labels, color='#cbd5e1', fontsize=9.5)

    for i in range(len(short_labels)):
        for j in range(len(short_labels)):
            val = corr[i, j]
            color = '#ffffff' if val < 0.65 else '#0f172a'
            ax.text(j, i, f'{val:.2f}', ha='center', va='center', color=color, fontsize=8.5, fontweight='bold')

    ax.set_title('Educational Simulation Parameter Correlation Heatmap', color='#ffffff', fontsize=12, fontweight='bold', pad=14)
    ax.text(0.98, -0.12, 'SYNTHETIC SIMULATION DATA — N=500', transform=ax.transAxes, fontsize=8, color='#64748b', ha='right', family='monospace')
    plt.tight_layout()
    p3 = os.path.join(RESULTS_DIR, "learning_correlation.png")
    fig.savefig(p3, dpi=300)
    fig.savefig(os.path.join(STATIC_RESULTS_DIR, "learning_correlation.png"), dpi=300)
    plt.close(fig)
    print("  -> Saved learning_correlation.png")

    # --------------------------------------------------------------------------
    # PLOT D: Concept Retention Analysis (concept_retention.png)
    # --------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    fig.patch.set_facecolor('#070d18')
    ax.set_facecolor('#0b1626')

    # Scatter with feedback frequency bubble size
    scatter = ax.scatter(
        df["Feedback_Frequency"],
        df["Concept_Retention"],
        c=df["Mastery_Index"],
        cmap='viridis',
        s=df["Engagement_Score"] * 0.7,
        alpha=0.7,
        edgecolors='#38bdf8',
        linewidth=0.6
    )
    cbar = fig.colorbar(scatter, ax=ax, fraction=0.046, pad=0.04)
    cbar.ax.tick_params(colors='#94a3b8')
    cbar.set_label('Composite Mastery Index', color='#cbd5e1', fontsize=9.5)

    # Linear regression fit line
    m, b = np.polyfit(df["Feedback_Frequency"], df["Concept_Retention"], 1)
    x_line = np.linspace(df["Feedback_Frequency"].min(), df["Feedback_Frequency"].max(), 100)
    ax.plot(x_line, m*x_line + b, color='#f59e0b', linewidth=2.6, linestyle='-', label=f'Linear Retention Trajectory (Slope: +{m:.2f} pts/intervention)')

    ax.set_title('8-Week Concept Retention vs. Weekly Feedback Interventions', color='#ffffff', fontsize=12.5, fontweight='bold', pad=14)
    ax.set_xlabel('Personalized Feedback Frequency (Interventions / Week)', color='#cbd5e1', fontsize=10.5)
    ax.set_ylabel('Long-Term Concept Retention Score (0-100)', color='#cbd5e1', fontsize=10.5)
    ax.legend(facecolor='#0f1b2d', edgecolor='#334155', fontsize=9.5, loc='upper left')
    ax.grid(True)
    ax.text(0.98, 0.04, 'Bubble size = Engagement Score | Color = Mastery Index (N=500)', transform=ax.transAxes, fontsize=8, color='#94a3b8', ha='right', family='monospace')

    plt.tight_layout()
    p4 = os.path.join(RESULTS_DIR, "concept_retention.png")
    fig.savefig(p4, dpi=300)
    fig.savefig(os.path.join(STATIC_RESULTS_DIR, "concept_retention.png"), dpi=300)
    plt.close(fig)
    print("  -> Saved concept_retention.png")

    # --------------------------------------------------------------------------
    # PLOT E: Future Classroom Performance Dashboard (future_classroom_dashboard.png)
    # --------------------------------------------------------------------------
    fig = plt.figure(figsize=(12, 6.5), dpi=300)
    fig.patch.set_facecolor('#070d18')

    gs = fig.add_gridspec(2, 2, hspace=0.32, wspace=0.25)

    # Subplot 1: Distribution of Mastery Index
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor('#0b1626')
    ax1.hist(trad["Mastery_Index"], bins=15, alpha=0.6, color='#38bdf8', edgecolor='#0284c7', label=f'Traditional (μ={trad["Mastery_Index"].mean():.1f})')
    ax1.hist(ai["Mastery_Index"], bins=15, alpha=0.65, color='#00e5ff', edgecolor='#06b6d4', label=f'Adaptive AI (μ={ai["Mastery_Index"].mean():.1f})')
    ax1.set_title('Mastery Index Density Distribution', color='#ffffff', fontsize=10.5, fontweight='bold')
    ax1.set_xlabel('Mastery Score (0-100)', color='#94a3b8', fontsize=8.5)
    ax1.legend(facecolor='#0f1b2d', edgecolor='#334155', fontsize=7.5)
    ax1.grid(True)

    # Subplot 2: Assessment vs Retention Scatter
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor('#0b1626')
    ax2.scatter(trad["Assessment_Performance"], trad["Concept_Retention"], color='#38bdf8', alpha=0.45, s=20, label='Traditional')
    ax2.scatter(ai["Assessment_Performance"], ai["Concept_Retention"], color='#00e5ff', alpha=0.6, s=25, label='Adaptive AI')
    ax2.set_title('Exam Performance vs. 8-Wk Retention', color='#ffffff', fontsize=10.5, fontweight='bold')
    ax2.set_xlabel('Assessment Score', color='#94a3b8', fontsize=8.5)
    ax2.set_ylabel('Concept Retention', color='#94a3b8', fontsize=8.5)
    ax2.legend(facecolor='#0f1b2d', edgecolor='#334155', fontsize=7.5)
    ax2.grid(True)

    # Subplot 3: Radar Chart of Modalities
    ax3 = fig.add_subplot(gs[1, 0], polar=True)
    ax3.set_facecolor('#0b1626')
    labels = ['Engagement', 'Participate', 'Assessment', 'Collaborative', 'Retention']
    r_cols = ['Engagement_Score', 'Participation_Rate', 'Assessment_Performance', 'Collaborative_Score', 'Concept_Retention']
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    val_trad = [trad[c].mean() for c in r_cols] + [trad[r_cols[0]].mean()]
    val_ai = [ai[c].mean() for c in r_cols] + [ai[r_cols[0]].mean()]

    ax3.plot(angles, val_trad, color='#38bdf8', linewidth=1.8, label='Traditional')
    ax3.fill(angles, val_trad, color='#38bdf8', alpha=0.15)
    ax3.plot(angles, val_ai, color='#00e5ff', linewidth=2.2, label='Adaptive AI')
    ax3.fill(angles, val_ai, color='#00e5ff', alpha=0.25)
    ax3.set_xticks(angles[:-1])
    ax3.set_xticklabels(labels, color='#cbd5e1', fontsize=8)
    ax3.set_ylim(0, 100)
    ax3.tick_params(colors='#64748b', labelsize=7)
    ax3.set_title('Holistic Competency Radar', color='#ffffff', fontsize=10.5, fontweight='bold', pad=12)

    # Subplot 4: Summary KPIs and Model Gain
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_facecolor('#0b1626')
    ax4.axis('off')

    kpi_text = (
        "FUTURE CLASSROOM SIMULATION SUMMARY\n"
        "──────────────────────────────────────────────\n"
        f"• Total Synthetic Cohort:    N = {len(df)} Students\n"
        f"• Adaptive AI Retention:    μ = {ai['Concept_Retention'].mean():.1f}  (+{metrics['key_insights']['retention_gain_pct']}% vs Trad)\n"
        f"• Traditional Retention:     μ = {trad['Concept_Retention'].mean():.1f}\n"
        f"• Formative Feedback Rate:   {ai['Feedback_Frequency'].mean():.1f}/wk (vs {trad['Feedback_Frequency'].mean():.1f}/wk)\n"
        f"• Engagement Delta:         +{metrics['key_insights']['engagement_delta']} pts (AI Scaffolding)\n"
        f"• Holistic Mastery Delta:    +{metrics['key_insights']['mastery_delta']} pts\n"
        "──────────────────────────────────────────────\n"
        "CONCLUSION: Formative AI scaffolding supports deeper\n"
        "concept retention when paired with teacher mentorship."
    )
    ax4.text(0.04, 0.90, kpi_text, color='#f8fafc', fontsize=9.2, family='monospace', va='top', bbox=dict(boxstyle='round,pad=0.8', facecolor='#0f1b2d', edgecolor='#38bdf8', alpha=0.85))

    fig.suptitle('Future Classroom Scientific Simulation Dashboard [MATLAB/Octave Bridge]', color='#ffffff', fontsize=14, fontweight='bold', y=0.98)

    plt.tight_layout()
    p5 = os.path.join(RESULTS_DIR, "future_classroom_dashboard.png")
    fig.savefig(p5, dpi=300)
    fig.savefig(os.path.join(STATIC_RESULTS_DIR, "future_classroom_dashboard.png"), dpi=300)
    plt.close(fig)
    print("  -> Saved future_classroom_dashboard.png")

# ==============================================================================
# 4. HIGH-FIDELITY SYNTHESIZED AUDIO ASSETS (.WAV)
# ==============================================================================

def write_wav(filename, samples, sample_rate=44100):
    filepath = os.path.join(STATIC_AUDIO_DIR, filename)
    with wave.open(filepath, 'w') as wav_file:
        nchannels = 1
        sampwidth = 2
        nframes = len(samples)
        wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, 'NONE', 'not compressed'))
        raw_bytes = bytearray()
        for s in samples:
            val = max(min(s, 1.0), -1.0)
            int_val = int(val * 32767.0)
            raw_bytes.extend(struct.pack('<h', int_val))
        wav_file.writeframes(raw_bytes)
    print(f"  -> Generated audio: {filepath}")

def generate_audio_assets():
    sr = 44100

    # 1. UI Click: High crisp glass-tactile chime click (0.12s)
    click_dur = 0.12
    click_samples = []
    for i in range(int(click_dur * sr)):
        t = i / sr
        env = math.exp(-t * 42.0)
        s = 0.45 * math.sin(2.0 * math.pi * 1450 * t) * env
        s += 0.25 * math.sin(2.0 * math.pi * 2900 * t) * env
        click_samples.append(s)
    write_wav("ui_click.wav", click_samples, sr)

    # 2. Scene Transition: Smooth futuristic resonant sweep (1.25s)
    trans_dur = 1.25
    trans_samples = []
    for i in range(int(trans_dur * sr)):
        t = i / sr
        phase = t / trans_dur
        freq = 320 + 1600 * math.sin(math.pi * phase)
        env = (math.sin(math.pi * phase) ** 1.6) * 0.42
        s = env * math.sin(2.0 * math.pi * freq * t)
        s += env * 0.3 * math.sin(2.0 * math.pi * (freq * 1.5) * t)
        trans_samples.append(s)
    write_wav("transition.wav", trans_samples, sr)

    # 3. Ambient Conference: Futuristic warm education research atmosphere (10.0s loopable)
    ambient_dur = 10.0
    ambient_samples = []
    for i in range(int(ambient_dur * sr)):
        t = i / sr
        # E Major 9 chord harmonics (E: 164.81 Hz, B: 246.94 Hz, G#: 207.65 Hz, D#: 311.13 Hz)
        lfo1 = 0.82 + 0.18 * math.sin(2.0 * math.pi * 0.18 * t)
        lfo2 = 0.85 + 0.15 * math.cos(2.0 * math.pi * 0.12 * t)

        s1 = 0.11 * math.sin(2.0 * math.pi * 164.81 * t) * lfo1
        s2 = 0.08 * math.sin(2.0 * math.pi * 246.94 * t) * lfo2
        s3 = 0.06 * math.sin(2.0 * math.pi * 207.65 * t)
        s4 = 0.04 * math.sin(2.0 * math.pi * 311.13 * t)

        # Micro-air hiss for acoustic realism
        noise = (np.random.random() - 0.5) * 0.004

        combined = (s1 + s2 + s3 + s4 + noise) * 0.38
        ambient_samples.append(combined)
    write_wav("ambient_conference.wav", ambient_samples, sr)

# ==============================================================================
# MAIN ENTRYPOINT
# ==============================================================================

def main():
    print("=" * 70)
    print("THE FUTURE OF CLASSROOMS: ASSET & SCIENTIFIC GENERATOR")
    print("=" * 70)

    print("\n1. Generating Synthetic Educational Dataset (N=500)...")
    df = generate_classroom_dataset()

    print("\n2. Computing Statistical Metrics & Analytics...")
    metrics = compute_statistics(df)

    print("\n3. Generating Five Scientific Visualizations (300 DPI)...")
    generate_visualizations(df, metrics)

    print("\n4. Synthesizing Audio Assets (.wav)...")
    generate_audio_assets()

    print("\n[COMPLETE] All scientific data, plots, and audio generated successfully!")

if __name__ == "__main__":
    main()
