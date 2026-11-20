"""
THE FUTURE OF CLASSROOMS
Reimagining Education Through Innovation, Intelligence and Technology
File: build_index_html.py

Builds templates/index.html and root index.html with inlined SVG assets
for seamless DOM viseme manipulation, character lip-sync, and static GitHub Pages deployment.
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
IMAGES_DIR = os.path.join(BASE_DIR, "static", "images")
os.makedirs(TEMPLATES_DIR, exist_ok=True)

def load_svg(filename):
    path = os.path.join(IMAGES_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # Strip XML declaration if present
    if content.startswith("<?xml"):
        content = content.split("?>", 1)[1].strip()
    return content

def build_html():
    sophia_svg = load_svg("dr_sophia_bennett.svg")
    emily_svg = load_svg("emily_carter.svg")
    environment_svg = load_svg("classroom_environment.svg")
    visualizations_svg = load_svg("education_visualizations.svg")

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Future of Classrooms: Reimagining Education Through Innovation, Intelligence and Technology</title>
  <meta name="description" content="Cinematic Animated Academic Presentation & MATLAB Scientific Simulation Platform featuring Dr. Sophia Bennett and Emily Carter.">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎓</text></svg>">
  <link rel="stylesheet" href="static/css/style.css">
  <link rel="stylesheet" href="static/css/animations.css">
</head>
<body>

  <!-- 1. Master Cinematic Viewport -->
  <div id="presentation-viewport">
    <div id="presentation-stage">

      <!-- Layer 1: Futuristic Conference Room Environment -->
      <div id="environment-layer">
        {environment_svg}
      </div>

      <!-- Layer 2: Central Smart Display Interactive Content Layer -->
      <div id="smartboard-content-layer">
        {visualizations_svg}
      </div>

      <!-- Layer 3: Scene 5 Interactive MATLAB Scientific Dashboard -->
      <div id="matlab-interactive-stage" style="display:none;">
        <div class="matlab-header-row">
          <div class="matlab-badge">MATLAB SCIENTIFIC SIMULATION PLATFORM</div>
          <div class="matlab-synthetic-tag">EDUCATIONAL SIMULATION — SYNTHETIC DATA (N=500)</div>
        </div>

        <!-- 4 Key Descriptive Metrics Cards -->
        <div class="matlab-kpi-ribbon">
          <div class="kpi-card">
            <div class="kpi-label">Concept Retention</div>
            <div id="stat-retention-val" class="kpi-value">+40.9%</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-label">Engagement Delta</div>
            <div id="stat-engagement-val" class="kpi-value">+21.0 pts</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-label">Feedback Frequency</div>
            <div id="stat-feedback-val" class="kpi-value">2.8x Freq</div>
          </div>
          <div class="kpi-card">
            <div class="kpi-label">Mastery Index Delta</div>
            <div id="stat-mastery-val" class="kpi-value">+18.5 pts</div>
          </div>
        </div>

        <!-- Plot Switching Tabs -->
        <div id="matlab-tabs-nav"></div>

        <!-- Plot Viewport -->
        <div class="matlab-plot-viewport">
          <img id="matlab-plot-img" src="results/student_engagement.png" alt="Student Engagement Trends">
          <div class="matlab-plot-footer">
            <span id="matlab-plot-title" style="font-weight:bold; color:#00e5ff;">Figure 1: Student Engagement Trends</span>
            <span id="matlab-plot-desc">Engagement vs. Weekly Learning Time with 2nd-order polynomial fits.</span>
          </div>
        </div>
      </div>

      <!-- Layer 4: Face-to-Face Dual Female Professional Characters -->
      <div id="characters-layer">
        <!-- Dr. Sophia Bennett (Left zone, seated, facing right) -->
        <div id="char-sophia-wrap" class="character-wrap listening">
          <div class="character-svg-container">
            {sophia_svg}
          </div>
          <div class="character-badge">
            <div class="char-name">DR. SOPHIA BENNETT</div>
            <div class="char-role">Senior Education Researcher &amp; Director</div>
          </div>
        </div>

        <!-- Emily Carter (Right zone, seated, facing left) -->
        <div id="char-emily-wrap" class="character-wrap listening">
          <div class="character-svg-container">
            {emily_svg}
          </div>
          <div class="character-badge">
            <div class="char-name">EMILY CARTER</div>
            <div class="char-role">EdTech Consultant &amp; AI Specialist</div>
          </div>
        </div>
      </div>

      <!-- Layer 5: Subtitles Glass Container -->
      <div id="subtitles-container">
        <div id="subtitles-speaker" class="subtitle-speaker-tag speaker-sophia">DR. SOPHIA BENNETT:</div>
        <div id="subtitles-text">"Welcome everyone. Across educational institutions worldwide, classrooms long relied on standardized lectures..."</div>
      </div>

      <!-- Layer 6: Master HUD Controls & Timeline Bar -->
      <div id="hud-controls-container">
        <div id="timeline-track-wrap">
          <div id="timeline-track">
            <div id="timeline-progress-fill"></div>
            <div id="timeline-markers"></div>
          </div>
        </div>

        <div id="hud-toolbar">
          <div class="hud-left">
            <button id="btn-play-pause" class="hud-btn btn-primary">▶ Play</button>
            <button id="btn-restart" class="hud-btn">↺ Restart</button>
            <button id="btn-prev-scene" class="hud-btn">⏮ Prev</button>
            <button id="btn-next-scene" class="hud-btn">⏭ Next</button>
            <span id="presentation-timer">00:00 / 02:45</span>
          </div>

          <div class="hud-center">
            <div id="current-scene-badge">
              <span id="current-scene-title">SCENE 1: THE CLASSROOM OF TOMORROW</span>
              <span id="current-scene-desc">Designing learning around how students actually learn.</span>
            </div>
          </div>

          <div class="hud-right">
            <button id="btn-toggle-subtitles" class="hud-btn active">💬 Subtitles</button>
            <button id="btn-toggle-sound" class="hud-btn">🔊 Sound</button>
            <button id="btn-toggle-fullscreen" class="hud-btn">⛶ Fullscreen</button>
          </div>
        </div>
      </div>

      <!-- Layer 7: Intro Landing Modal Overlay -->
      <div id="intro-modal-overlay">
        <div class="intro-modal-card">
          <div class="intro-badge">ACADEMIC RESEARCH &amp; SCIENTIFIC SIMULATION</div>
          <h1 class="intro-title">THE FUTURE OF CLASSROOMS</h1>
          <p class="intro-subtitle">Reimagining Education Through Innovation, Intelligence and Technology</p>

          <div class="intro-speakers-grid">
            <div class="intro-speaker-box sophia">
              <div class="intro-speaker-name">Dr. Sophia Bennett</div>
              <div class="intro-speaker-role">Senior Education Researcher and Director of Learning Innovation. Introduces systemic constraints of traditional models and the vital primacy of human mentorship.</div>
            </div>
            <div class="intro-speaker-box emily">
              <div class="intro-speaker-name">Emily Carter</div>
              <div class="intro-speaker-role">Educational Technology Consultant &amp; AI Systems Specialist. Explores AI-driven personalized scaffolding, adaptive learning pathways, and virtual science laboratories.</div>
            </div>
          </div>

          <div class="intro-meta-info">
            <span>DURATION: 165 SECONDS (02:45)</span>
            <span>•</span>
            <span>MATLAB SIMULATION: FutureClassrooms.m (N=500)</span>
            <span>•</span>
            <span>FACE-TO-FACE CONVERSATION</span>
          </div>

          <button id="btn-start-presentation" class="intro-start-btn">START PRESENTATION ▶</button>
        </div>
      </div>

    </div>
  </div>

  <!-- Scripts -->
  <script src="static/js/speech.js"></script>
  <script src="static/js/lab_effects.js"></script>
  <script src="static/js/matlab_viewer.js"></script>
  <script src="static/js/app.js"></script>
</body>
</html>
'''

    # Write templates/index.html
    template_path = os.path.join(TEMPLATES_DIR, "index.html")
    with open(template_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  -> Generated: {template_path}")

    # Write root index.html
    root_path = os.path.join(BASE_DIR, "index.html")
    with open(root_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"  -> Generated: {root_path}")

if __name__ == "__main__":
    build_html()
