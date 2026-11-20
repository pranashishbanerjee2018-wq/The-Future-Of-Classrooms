"""
THE FUTURE OF CLASSROOMS
Reimagining Education Through Innovation, Intelligence and Technology
File: generate_svgs.py

Generates professional vector SVG assets:
1. dr_sophia_bennett.svg - Senior Education Researcher (Female, 34-38, navy blazer, cream blouse, seated facing right)
2. emily_carter.svg - EdTech & AI Specialist (Female, 28-32, cobalt jacket, light shirt, tablet, seated facing left)
3. classroom_environment.svg - Modern futuristic glass innovation conference room, table, chairs, background
4. education_visualizations.svg - Dynamic HUD displays for all 7 scenes
"""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "static", "images")
os.makedirs(IMAGES_DIR, exist_ok=True)

# ==============================================================================
# 1. DR. SOPHIA BENNETT (SENIOR EDUCATION RESEARCHER) SVG
# Seated in executive chair, angled facing right toward Emily
# ==============================================================================
def create_dr_sophia_bennett_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 620" width="380" height="620" id="svg-sophia">
  <defs>
    <linearGradient id="sophia-blazer-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#14223d" />
      <stop offset="50%" stop-color="#0c172a" />
      <stop offset="100%" stop-color="#060c16" />
    </linearGradient>
    <linearGradient id="sophia-blouse-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fdfbf7" />
      <stop offset="100%" stop-color="#e2dcce" />
    </linearGradient>
    <linearGradient id="sophia-skin-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fce8d5" />
      <stop offset="60%" stop-color="#f2cfb2" />
      <stop offset="100%" stop-color="#e0b292" />
    </linearGradient>
    <linearGradient id="sophia-hair-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b2014" />
      <stop offset="50%" stop-color="#24130a" />
      <stop offset="100%" stop-color="#120803" />
    </linearGradient>
    <linearGradient id="sophia-chair-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="50%" stop-color="#334155" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <filter id="sophia-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.55"/>
    </filter>
  </defs>

  <g id="sophia-character" filter="url(#sophia-shadow)">
    <!-- 1. Executive Chair Backrest & Armrest (Sophia is seated) -->
    <g id="sophia-chair">
      <!-- Chair high mesh backrest -->
      <path d="M 60 140 C 60 100, 110 80, 140 85 L 140 380 L 50 360 Z" fill="url(#sophia-chair-grad)" stroke="#475569" stroke-width="2"/>
      <line x1="75" y1="120" x2="75" y2="360" stroke="#38bdf8" stroke-width="1.5" opacity="0.3"/>
      <!-- Chair lumbar curve -->
      <path d="M 45 280 Q 70 340 100 370" stroke="#1e293b" stroke-width="8" fill="none"/>
      <!-- Chair armrest -->
      <path d="M 70 310 L 160 320 L 155 332 L 65 322 Z" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
      <line x1="140" y1="332" x2="140" y2="400" stroke="#334155" stroke-width="5"/>
    </g>

    <!-- 2. Seated Legs & Professional Slacks (Angled right towards table) -->
    <g id="sophia-legs">
      <!-- Thighs / seated lap (extending towards the discussion table) -->
      <path d="M 110 370 Q 210 380 270 395 L 265 440 Q 180 435 95 410 Z" fill="#0d1829" stroke="#1e293b" stroke-width="1"/>
      <!-- Lower leg angled down -->
      <path d="M 250 410 L 275 560 L 245 565 L 220 425 Z" fill="#0a121f"/>
      <path d="M 200 420 L 225 560 L 195 565 L 175 425 Z" fill="#070d17"/>
      <!-- Elegant professional low-heel shoes -->
      <path d="M 265 558 L 295 570 L 285 582 L 240 572 Z" fill="#020408"/>
      <path d="M 215 558 L 245 570 L 235 582 L 190 572 Z" fill="#020408"/>
    </g>

    <!-- 3. Torso, Blouse & Tailored Navy Blazer -->
    <g id="sophia-torso">
      <!-- Cream Silk Inner Blouse -->
      <path d="M 155 170 L 205 170 L 210 270 L 150 270 Z" fill="url(#sophia-blouse-grad)"/>
      <path d="M 175 180 L 185 240" stroke="#d5cebe" stroke-width="1.2"/>
      
      <!-- Subtle Elegant Gold Pendant Necklace -->
      <path d="M 166 182 Q 182 208 198 182" stroke="#f59e0b" stroke-width="1.2" fill="none"/>
      <circle cx="182" cy="207" r="3" fill="#f59e0b"/>

      <!-- Tailored Navy Blazer (Seated ergonomic posture) -->
      <path d="M 125 170 C 145 155, 220 158, 235 175 L 245 380 C 215 390, 130 385, 110 370 Z" fill="url(#sophia-blazer-grad)"/>
      
      <!-- Lapels (Curved professional cut) -->
      <path d="M 148 168 L 172 270 L 158 275 L 135 180 Z" fill="#1e2d48"/>
      <path d="M 218 168 L 192 270 L 206 275 L 228 180 Z" fill="#1e2d48"/>

      <!-- Researcher Credential Badge -->
      <g id="sophia-badge" transform="translate(195, 230)">
        <rect x="0" y="0" width="22" height="32" rx="2.5" fill="#0b1728" stroke="#38bdf8" stroke-width="1"/>
        <rect x="3" y="3" width="16" height="10" fill="#38bdf8" opacity="0.35"/>
        <circle cx="11" cy="8" r="2.8" fill="#ffffff"/>
        <line x1="4" y1="17" x2="18" y2="17" stroke="#38bdf8" stroke-width="1.2"/>
        <line x1="4" y1="21" x2="14" y2="21" stroke="#94a3b8" stroke-width="1"/>
        <line x1="4" y1="25" x2="10" y2="25" stroke="#f59e0b" stroke-width="1"/>
      </g>
    </g>

    <!-- 4. Head, Hair, Face & Visemes (Angled in 3/4 right profile looking at Emily) -->
    <g id="sophia-head-group">
      <!-- Neck -->
      <path d="M 166 142 L 198 142 L 202 175 L 162 175 Z" fill="url(#sophia-skin-grad)"/>
      <path d="M 164 165 Q 182 174 200 165" stroke="#cf9f7e" stroke-width="1.2" fill="none"/>

      <!-- Head Base (Female jawline angled 3/4 right) -->
      <path d="M 150 92 C 150 50, 215 48, 222 92 C 226 130, 208 152, 190 154 C 172 154, 150 132, 150 92 Z" fill="url(#sophia-skin-grad)"/>

      <!-- Ear with Gold Pearl Earring -->
      <ellipse cx="152" cy="100" rx="6" ry="9" fill="url(#sophia-skin-grad)"/>
      <circle cx="152" cy="108" r="2.8" fill="#f59e0b"/>
      <circle cx="152" cy="108" r="1.5" fill="#ffffff"/>

      <!-- Sophisticated Professional Hair (Elegant French twist / updo) -->
      <path d="M 144 92 C 142 55, 170 32, 205 34 C 230 35, 238 60, 230 92 C 224 68, 205 58, 185 60 C 165 62, 152 75, 144 92 Z" fill="url(#sophia-hair-grad)"/>
      <!-- Soft sweeping side bang -->
      <path d="M 172 45 C 195 48, 220 62, 225 85 C 222 75, 205 60, 172 56 Z" fill="url(#sophia-hair-grad)"/>
      <!-- Rear hair bun -->
      <ellipse cx="138" cy="85" rx="14" ry="18" fill="url(#sophia-hair-grad)"/>

      <!-- Eyebrows (Thoughtful, intelligent arch) -->
      <path d="M 168 80 Q 178 76 186 80" stroke="#1f1109" stroke-width="2.2" fill="none" stroke-linecap="round"/>
      <path d="M 196 79 Q 206 75 214 78" stroke="#1f1109" stroke-width="2.2" fill="none" stroke-linecap="round"/>

      <!-- Eyes looking forward-right towards Emily -->
      <g id="sophia-eyes">
        <!-- Left eye -->
        <ellipse cx="177" cy="88" rx="5.5" ry="3.2" fill="#ffffff"/>
        <circle cx="179" cy="88" r="2.2" fill="#2c1a11"/>
        <circle cx="180" cy="87.2" r="0.7" fill="#ffffff"/>
        <!-- Right eye -->
        <ellipse cx="205" cy="87" rx="5.5" ry="3.2" fill="#ffffff"/>
        <circle cx="207" cy="87" r="2.2" fill="#2c1a11"/>
        <circle cx="208" cy="86.2" r="0.7" fill="#ffffff"/>
        <!-- Eyelashes -->
        <path d="M 172 86 Q 177 84 183 86 M 200 85 Q 205 83 211 85" stroke="#120803" stroke-width="1.2" fill="none"/>
        <!-- Blinking eyelid -->
        <path id="sophia-blink" d="M 172 88 Q 177 91 183 88 M 200 87 Q 205 90 211 87" stroke="#cf9f7e" stroke-width="1.8" fill="none" opacity="0"/>
      </g>

      <!-- Nose (Refined female contour) -->
      <path d="M 194 84 L 198 100 L 193 103 L 200 102" stroke="#c08d6c" stroke-width="1.6" fill="none" stroke-linecap="round"/>

      <!-- Mouth Visemes (Looking right towards Emily) -->
      <g id="sophia-mouth-group">
        <!-- 1. Rest mouth (natural, closed, gentle smile) -->
        <path id="sophia-mouth-rest" d="M 185 118 Q 194 121 204 117" stroke="#a33d3d" stroke-width="2.2" fill="none" stroke-linecap="round" />
        <!-- 2. Vowel A mouth (open) -->
        <ellipse id="sophia-mouth-vowel-a" cx="194" cy="119" rx="6" ry="5.2" fill="#4a1515" stroke="#a33d3d" stroke-width="1.8" style="display:none;" />
        <!-- 3. Round O mouth -->
        <ellipse id="sophia-mouth-round-o" cx="194" cy="119" rx="4.2" ry="5.2" fill="#4a1515" stroke="#a33d3d" stroke-width="1.8" style="display:none;" />
        <!-- 4. Wide E mouth -->
        <path id="sophia-mouth-wide-e" d="M 183 118 Q 194 115 205 117 Q 194 123 183 118 Z" fill="#ffffff" stroke="#a33d3d" stroke-width="1.8" style="display:none;" />
        <!-- 5. Mid mouth -->
        <ellipse id="sophia-mouth-mid" cx="194" cy="118" rx="5.2" ry="3.0" fill="#4a1515" stroke="#a33d3d" stroke-width="1.8" style="display:none;" />
      </g>
    </g>

    <!-- 5. Left Arm (Resting gracefully near chair armrest) -->
    <g id="sophia-arm-left">
      <path d="M 130 180 L 105 260 L 145 320" stroke="#0c172a" stroke-width="20" stroke-linecap="round" fill="none"/>
      <!-- Hand resting on armrest -->
      <ellipse cx="152" cy="324" rx="8" ry="10" fill="url(#sophia-skin-grad)"/>
    </g>

    <!-- 6. Right Arm (Active Explanatory Gesture towards Emily & Smart Board) -->
    <g id="sophia-arm-right">
      <path id="sophia-arm-right-path" d="M 235 185 L 280 255 L 325 240" stroke="#0c172a" stroke-width="20" stroke-linecap="round" fill="none"/>
      <!-- Elegant hand open-palm explaining -->
      <g id="sophia-hand-right" transform="translate(320, 230)">
        <ellipse cx="10" cy="10" rx="9" ry="8" fill="url(#sophia-skin-grad)"/>
        <!-- Fingers gesturing open towards discussion -->
        <path d="M 16 6 L 32 3" stroke="#e0b292" stroke-width="3.5" stroke-linecap="round"/>
        <path d="M 17 10 L 33 9" stroke="#e0b292" stroke-width="3.2" stroke-linecap="round"/>
        <path d="M 16 14 L 30 15" stroke="#e0b292" stroke-width="3" stroke-linecap="round"/>
      </g>
    </g>

    <!-- 7. Sophia's Research Tablet & Stylus on table edge -->
    <g id="sophia-notes" transform="translate(240, 370)">
      <rect x="0" y="0" width="85" height="50" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" opacity="0.9"/>
      <rect x="4" y="4" width="77" height="42" rx="2" fill="#09131f"/>
      <text x="8" y="14" fill="#38bdf8" font-size="5" font-family="monospace" font-weight="bold">PEDAGOGICAL RESEARCH</text>
      <line x1="8" y1="18" x2="75" y2="18" stroke="#38bdf8" stroke-width="0.6" opacity="0.5"/>
      <line x1="8" y1="24" x2="60" y2="24" stroke="#94a3b8" stroke-width="1"/>
      <line x1="8" y1="29" x2="70" y2="29" stroke="#94a3b8" stroke-width="1"/>
      <line x1="8" y1="34" x2="50" y2="34" stroke="#f59e0b" stroke-width="1"/>
      <!-- Gold stylus -->
      <line x1="72" y1="38" x2="88" y2="48" stroke="#f59e0b" stroke-width="2" stroke-linecap="round"/>
    </g>
  </g>
</svg>'''
    with open(os.path.join(IMAGES_DIR, "dr_sophia_bennett.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("  -> Saved dr_sophia_bennett.svg")

# ==============================================================================
# 2. EMILY CARTER (EDTECH CONSULTANT & AI SPECIALIST) SVG
# Seated in executive chair, angled facing left toward Sophia
# ==============================================================================
def create_emily_carter_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 620" width="380" height="620" id="svg-emily">
  <defs>
    <linearGradient id="emily-jacket-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1d4ed8" />
      <stop offset="50%" stop-color="#1e40af" />
      <stop offset="100%" stop-color="#172554" />
    </linearGradient>
    <linearGradient id="emily-shirt-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#e0f2fe" />
    </linearGradient>
    <linearGradient id="emily-skin-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef0e2" />
      <stop offset="60%" stop-color="#f7dac0" />
      <stop offset="100%" stop-color="#e8be9e" />
    </linearGradient>
    <linearGradient id="emily-hair-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6b3a19" />
      <stop offset="50%" stop-color="#4a220b" />
      <stop offset="100%" stop-color="#2c1204" />
    </linearGradient>
    <linearGradient id="emily-tablet-holo" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00e5ff" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#0284c7" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#082f49" stop-opacity="0.95" />
    </linearGradient>
    <linearGradient id="emily-chair-grad" x1="100%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="50%" stop-color="#334155" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <filter id="emily-shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.55"/>
    </filter>
  </defs>

  <g id="emily-character" filter="url(#emily-shadow)">
    <!-- 1. Executive Chair Backrest & Armrest (Emily is seated on right, facing left) -->
    <g id="emily-chair">
      <!-- Chair high mesh backrest -->
      <path d="M 320 140 C 320 100, 270 80, 240 85 L 240 380 L 330 360 Z" fill="url(#emily-chair-grad)" stroke="#475569" stroke-width="2"/>
      <line x1="305" y1="120" x2="305" y2="360" stroke="#00e5ff" stroke-width="1.5" opacity="0.3"/>
      <!-- Chair lumbar curve -->
      <path d="M 335 280 Q 310 340 280 370" stroke="#1e293b" stroke-width="8" fill="none"/>
      <!-- Chair armrest -->
      <path d="M 310 310 L 220 320 L 225 332 L 315 322 Z" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
      <line x1="240" y1="332" x2="240" y2="400" stroke="#334155" stroke-width="5"/>
    </g>

    <!-- 2. Seated Legs & Modern Slacks (Angled left towards table) -->
    <g id="emily-legs">
      <!-- Thighs / seated lap extending left towards discussion table -->
      <path d="M 270 370 Q 170 380 110 395 L 115 440 Q 200 435 285 410 Z" fill="#0f1f38" stroke="#1e293b" stroke-width="1"/>
      <!-- Lower leg angled down -->
      <path d="M 130 410 L 105 560 L 135 565 L 160 425 Z" fill="#0a162b"/>
      <path d="M 180 420 L 155 560 L 185 565 L 205 425 Z" fill="#07101f"/>
      <!-- Modern stylish ankle boots / heels -->
      <path d="M 115 558 L 85 570 L 95 582 L 140 572 Z" fill="#020408"/>
      <path d="M 165 558 L 135 570 L 145 582 L 190 572 Z" fill="#020408"/>
    </g>

    <!-- 3. Torso, Crisp Shirt & Cobalt-Blue Jacket -->
    <g id="emily-torso">
      <!-- Crisp White Inner Shirt -->
      <path d="M 175 170 L 225 170 L 230 270 L 170 270 Z" fill="url(#emily-shirt-grad)"/>
      <path d="M 195 175 L 205 175 L 200 250" stroke="#bae6fd" stroke-width="1.2"/>

      <!-- Modern Cobalt-Blue Tailored Jacket -->
      <path d="M 145 175 C 160 158, 235 155, 255 170 L 270 370 C 250 385, 165 390, 135 380 Z" fill="url(#emily-jacket-grad)"/>

      <!-- Lapels (Modern crisp cut) -->
      <path d="M 162 168 L 188 270 L 174 275 L 152 180 Z" fill="#1e3a8a"/>
      <path d="M 232 168 L 208 270 L 222 275 L 245 180 Z" fill="#1e3a8a"/>

      <!-- Smartwatch on left wrist & EdTech Pin -->
      <circle cx="160" cy="225" r="4.5" fill="#00e5ff" opacity="0.8"/>
      <circle cx="160" cy="225" r="2" fill="#ffffff"/>
    </g>

    <!-- 4. Head, Hair, Face & Visemes (Angled in 3/4 left profile looking at Sophia) -->
    <g id="emily-head-group">
      <!-- Neck -->
      <path d="M 182 142 L 214 142 L 218 175 L 178 175 Z" fill="url(#emily-skin-grad)"/>
      <path d="M 180 165 Q 198 174 216 165" stroke="#cf9f7e" stroke-width="1.2" fill="none"/>

      <!-- Head Base (Female jawline angled 3/4 left) -->
      <path d="M 158 92 C 154 50, 226 48, 230 92 C 230 132, 210 154, 190 154 C 172 154, 154 130, 158 92 Z" fill="url(#emily-skin-grad)"/>

      <!-- Ear with Cyan Tech Stud -->
      <ellipse cx="228" cy="100" rx="6" ry="9" fill="url(#emily-skin-grad)"/>
      <circle cx="228" cy="107" r="2.5" fill="#00e5ff"/>

      <!-- Modern Professional Hairstyle (Layered shoulder lob with subtle waves) -->
      <path d="M 150 92 C 142 60, 160 34, 195 34 C 230 34, 246 55, 236 92 C 240 120, 232 155, 222 170 C 218 140, 228 110, 225 85 C 220 62, 185 58, 168 64 C 158 68, 152 78, 150 92 Z" fill="url(#emily-hair-grad)"/>
      <!-- Soft front swept locks -->
      <path d="M 185 45 C 160 52, 150 75, 146 105 C 152 82, 168 62, 185 54 Z" fill="url(#emily-hair-grad)"/>
      <path d="M 226 90 C 234 125, 228 165, 215 185 C 224 165, 230 130, 226 90 Z" fill="url(#emily-hair-grad)"/>

      <!-- Eyebrows (Dynamic, enthusiastic arch) -->
      <path d="M 166 79 Q 174 75 184 79" stroke="#2c1204" stroke-width="2.2" fill="none" stroke-linecap="round"/>
      <path d="M 194 80 Q 202 76 212 80" stroke="#2c1204" stroke-width="2.2" fill="none" stroke-linecap="round"/>

      <!-- Eyes looking forward-left towards Sophia -->
      <g id="emily-eyes">
        <!-- Left eye -->
        <ellipse cx="175" cy="87" rx="5.5" ry="3.2" fill="#ffffff"/>
        <circle cx="173" cy="87" r="2.2" fill="#3b2014"/>
        <circle cx="172" cy="86.2" r="0.7" fill="#ffffff"/>
        <!-- Right eye -->
        <ellipse cx="203" cy="88" rx="5.5" ry="3.2" fill="#ffffff"/>
        <circle cx="201" cy="88" r="2.2" fill="#3b2014"/>
        <circle cx="200" cy="87.2" r="0.7" fill="#ffffff"/>
        <!-- Eyelashes -->
        <path d="M 169 85 Q 175 83 181 85 M 197 86 Q 203 84 209 86" stroke="#2c1204" stroke-width="1.2" fill="none"/>
        <!-- Blinking eyelid -->
        <path id="emily-blink" d="M 169 87 Q 175 90 181 87 M 197 88 Q 203 91 209 88" stroke="#e8be9e" stroke-width="1.8" fill="none" opacity="0"/>
      </g>

      <!-- Nose (Modern delicate contour) -->
      <path d="M 186 84 L 182 100 L 187 103 L 180 102" stroke="#c08d6c" stroke-width="1.6" fill="none" stroke-linecap="round"/>

      <!-- Mouth Visemes (Looking left towards Sophia) -->
      <g id="emily-mouth-group">
        <!-- 1. Rest mouth (natural, closed, friendly conversational) -->
        <path id="emily-mouth-rest" d="M 176 117 Q 186 121 195 118" stroke="#b91c1c" stroke-width="2.2" fill="none" stroke-linecap="round" />
        <!-- 2. Vowel A mouth (open) -->
        <ellipse id="emily-mouth-vowel-a" cx="186" cy="119" rx="6" ry="5.2" fill="#4a1515" stroke="#b91c1c" stroke-width="1.8" style="display:none;" />
        <!-- 3. Round O mouth -->
        <ellipse id="emily-mouth-round-o" cx="186" cy="119" rx="4.2" ry="5.2" fill="#4a1515" stroke="#b91c1c" stroke-width="1.8" style="display:none;" />
        <!-- 4. Wide E mouth -->
        <path id="emily-mouth-wide-e" d="M 175 117 Q 186 115 197 117 Q 186 123 175 117 Z" fill="#ffffff" stroke="#b91c1c" stroke-width="1.8" style="display:none;" />
        <!-- 5. Mid mouth -->
        <ellipse id="emily-mouth-mid" cx="186" cy="118" rx="5.2" ry="3.0" fill="#4a1515" stroke="#b91c1c" stroke-width="1.8" style="display:none;" />
      </g>
    </g>

    <!-- 5. Right Arm (Resting comfortably on chair armrest) -->
    <g id="emily-arm-right">
      <path d="M 250 180 L 275 260 L 235 320" stroke="#172554" stroke-width="20" stroke-linecap="round" fill="none"/>
      <!-- Hand resting -->
      <ellipse cx="228" cy="324" rx="8" ry="10" fill="url(#emily-skin-grad)"/>
    </g>

    <!-- 6. Left Arm (Interacting with the Digital Holographic Tablet on the table) -->
    <g id="emily-arm-left">
      <path id="emily-arm-left-path" d="M 145 185 L 100 255 L 75 285" stroke="#1e40af" stroke-width="20" stroke-linecap="round" fill="none"/>
      <!-- Hand poised over digital tablet -->
      <g id="emily-hand-left" transform="translate(60, 275)">
        <ellipse cx="12" cy="12" rx="9" ry="8" fill="url(#emily-skin-grad)"/>
        <!-- Fingers tapping / controlling telemetry HUD -->
        <path d="M 6 8 L -6 18" stroke="#e8be9e" stroke-width="3.5" stroke-linecap="round"/>
        <path d="M 10 12 L 0 24" stroke="#e8be9e" stroke-width="3.2" stroke-linecap="round"/>
      </g>
    </g>

    <!-- 7. Digital Holographic Tablet on Table (AI Learning Systems Telemetry) -->
    <g id="emily-tablet" transform="translate(45, 305)">
      <!-- Glass tablet chassis -->
      <rect x="0" y="0" width="115" height="80" rx="6" fill="url(#emily-tablet-holo)" stroke="#00e5ff" stroke-width="1.8" filter="drop-shadow(0 0 10px rgba(0, 229, 255, 0.6))"/>
      <!-- Tablet Screen Content -->
      <text x="8" y="14" fill="#ffffff" font-size="7" font-family="monospace" font-weight="bold">AI LEARNING PLATFORM</text>
      <text x="8" y="24" fill="#00e5ff" font-size="5.5" font-family="monospace">ADAPTIVE SCAFFOLDING: ON</text>
      <line x1="8" y1="28" x2="107" y2="28" stroke="#00e5ff" stroke-width="0.8" opacity="0.6"/>
      <!-- Live mini telemetry bars -->
      <rect x="8" y="34" width="18" height="32" fill="#03152d" stroke="#00e5ff" stroke-width="0.5"/>
      <rect x="10" y="42" width="14" height="22" fill="#00e5ff" opacity="0.85"/>
      <rect x="32" y="34" width="18" height="32" fill="#03152d" stroke="#38bdf8" stroke-width="0.5"/>
      <rect x="34" y="38" width="14" height="26" fill="#38bdf8" opacity="0.85"/>
      <rect x="56" y="34" width="18" height="32" fill="#03152d" stroke="#10b981" stroke-width="0.5"/>
      <rect x="58" y="44" width="14" height="20" fill="#10b981" opacity="0.85"/>
      <!-- Circular retention dial -->
      <circle cx="92" cy="50" r="12" fill="none" stroke="#00e5ff" stroke-width="2" stroke-dasharray="5 2"/>
      <text x="92" y="53" fill="#ffffff" font-size="6.5" font-family="monospace" text-anchor="middle" font-weight="bold">81%</text>
    </g>
  </g>
</svg>'''
    with open(os.path.join(IMAGES_DIR, "emily_carter.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("  -> Saved emily_carter.svg")

# ==============================================================================
# 3. CLASSROOM ENVIRONMENT SVG (Futuristic Conference Room & Central Board)
# ==============================================================================
def create_classroom_environment_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080" id="svg-environment">
  <defs>
    <!-- Background Space & Wall Gradients -->
    <linearGradient id="env-bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#040812" />
      <stop offset="50%" stop-color="#091426" />
      <stop offset="100%" stop-color="#0d1b33" />
    </linearGradient>
    <linearGradient id="env-floor" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#070f1e" />
      <stop offset="40%" stop-color="#050a14" />
      <stop offset="100%" stop-color="#020409" />
    </linearGradient>
    <linearGradient id="env-table-top" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1e293b" stop-opacity="0.95" />
      <stop offset="25%" stop-color="#38bdf8" stop-opacity="0.3" />
      <stop offset="50%" stop-color="#0f172a" stop-opacity="0.9" />
      <stop offset="75%" stop-color="#00e5ff" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#1e293b" stop-opacity="0.95" />
    </linearGradient>
    <linearGradient id="env-smartboard-frame" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="50%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <filter id="glow-ambient" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- 1. Deep Wall Background -->
  <rect x="0" y="0" width="1920" height="1080" fill="url(#env-bg)"/>

  <!-- 2. Panoramic Architectural Grid Windows looking onto Education Innovation Campus -->
  <g id="campus-skyline" opacity="0.45">
    <line x1="240" y1="0" x2="240" y2="680" stroke="#1e293b" stroke-width="2"/>
    <line x1="640" y1="0" x2="640" y2="680" stroke="#1e293b" stroke-width="2"/>
    <line x1="1280" y1="0" x2="1280" y2="680" stroke="#1e293b" stroke-width="2"/>
    <line x1="1680" y1="0" x2="1680" y2="680" stroke="#1e293b" stroke-width="2"/>
    <!-- Futuristic architectural campus dome & academic research towers -->
    <path d="M 0 660 L 140 590 L 260 610 L 420 540 L 560 600 L 750 510 L 960 580 L 1180 500 L 1380 570 L 1580 520 L 1760 600 L 1920 550 L 1920 680 L 0 680 Z" fill="#081324"/>
    <circle cx="750" cy="510" r="45" fill="#00e5ff" opacity="0.1" filter="url(#glow-ambient)"/>
    <circle cx="1180" cy="500" r="50" fill="#38bdf8" opacity="0.1" filter="url(#glow-ambient)"/>
  </g>

  <!-- 3. High-Tech Reflective Conference Floor -->
  <rect x="0" y="680" width="1920" height="400" fill="url(#env-floor)"/>
  <line x1="0" y1="680" x2="1920" y2="680" stroke="#00e5ff" stroke-width="2" opacity="0.75"/>

  <!-- Perspective Floor Grid -->
  <g id="floor-perspective" opacity="0.3">
    <line x1="0" y1="680" x2="0" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="200" y1="680" x2="60" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="400" y1="680" x2="280" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="600" y1="680" x2="520" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="800" y1="680" x2="760" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="960" y1="680" x2="960" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="1120" y1="680" x2="1160" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="1320" y1="680" x2="1400" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="1520" y1="680" x2="1640" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="1720" y1="680" x2="1860" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <line x1="1920" y1="680" x2="1920" y2="1080" stroke="#00e5ff" stroke-width="1"/>
    <!-- Transverse Floor Lines -->
    <line x1="0" y1="720" x2="1920" y2="720" stroke="#00e5ff" stroke-width="1" opacity="0.4"/>
    <line x1="0" y1="775" x2="1920" y2="775" stroke="#00e5ff" stroke-width="1.2" opacity="0.5"/>
    <line x1="0" y1="845" x2="1920" y2="845" stroke="#00e5ff" stroke-width="1.5" opacity="0.6"/>
    <line x1="0" y1="935" x2="1920" y2="935" stroke="#00e5ff" stroke-width="1.8" opacity="0.7"/>
    <line x1="0" y1="1045" x2="1920" y2="1045" stroke="#00e5ff" stroke-width="2.2" opacity="0.8"/>
  </g>

  <!-- 4. Studio Architectural Columns & Neon Channels -->
  <rect x="50" y="0" width="70" height="680" fill="#0c172a" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="1800" y="0" width="70" height="680" fill="#0c172a" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="85" y1="30" x2="85" y2="660" stroke="#38bdf8" stroke-width="3" opacity="0.7" filter="url(#glow-ambient)"/>
  <line x1="1835" y1="30" x2="1835" y2="660" stroke="#00e5ff" stroke-width="3" opacity="0.7" filter="url(#glow-ambient)"/>

  <!-- 5. Overhead Conference Lighting Canopy -->
  <polygon points="280,0 1640,0 1540,55 380,55" fill="#070e1b" stroke="#334155" stroke-width="2"/>
  <line x1="400" y1="52" x2="1520" y2="52" stroke="#00e5ff" stroke-width="2.8" opacity="0.85" filter="url(#glow-ambient)"/>

  <!-- 6. CENTRAL LARGE INTERACTIVE SMART DISPLAY FRAME (Behind the Table) -->
  <g id="central-smartboard-frame" transform="translate(480, 80)">
    <!-- Outer Bezel -->
    <rect x="0" y="0" width="960" height="540" rx="14" fill="#08101e" stroke="#1e293b" stroke-width="3" filter="drop-shadow(0 0 25px rgba(0, 229, 255, 0.2))"/>
    <!-- Glowing Inner Edge -->
    <rect x="6" y="6" width="948" height="528" rx="10" fill="none" stroke="url(#env-smartboard-frame)" stroke-width="1.5" opacity="0.8"/>
    <!-- Top Header Bar of Smart Display -->
    <rect x="6" y="6" width="948" height="34" rx="10" fill="#0f1b2d" opacity="0.95"/>
    <text x="24" y="28" fill="#00e5ff" font-size="12" font-family="monospace" font-weight="bold" letter-spacing="1.5">FUTURE EDUCATION INNOVATION PLATFORM</text>
    <circle cx="925" cy="23" r="5" fill="#10b981" filter="url(#glow-ambient)"/>
    <text x="860" y="27" fill="#94a3b8" font-size="10" font-family="monospace">LIVE TELEMETRY</text>
  </g>

  <!-- 7. MODERN EXECUTIVE DISCUSSION TABLE (Face-to-Face Bridge) -->
  <g id="discussion-table" transform="translate(240, 640)">
    <!-- Metallic Table Base Pillars -->
    <rect x="220" y="110" width="28" height="180" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <rect x="1190" y="110" width="28" height="180" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <line x1="200" y1="285" x2="270" y2="285" stroke="#475569" stroke-width="5"/>
    <line x1="1170" y1="285" x2="1240" y2="285" stroke="#475569" stroke-width="5"/>

    <!-- Discussion Table Top (Curved modern conference surface) -->
    <path d="M 40 100 Q 720 70 1400 100 L 1420 130 Q 720 105 20 130 Z" fill="url(#env-table-top)" stroke="#38bdf8" stroke-width="2" filter="drop-shadow(0 15px 25px rgba(0, 0, 0, 0.7))"/>
    
    <!-- Table Surface Glow Reflection Strip -->
    <path d="M 60 105 Q 720 80 1380 105" stroke="#00e5ff" stroke-width="1.5" fill="none" opacity="0.7" filter="url(#glow-ambient)"/>

    <!-- Subtle Table Center Embellishment (Embedded Connectivity Hub) -->
    <ellipse cx="720" cy="98" rx="80" ry="12" fill="#091322" stroke="#38bdf8" stroke-width="1"/>
    <circle cx="720" cy="98" r="4" fill="#00e5ff" filter="url(#glow-ambient)"/>
  </g>
</svg>'''
    with open(os.path.join(IMAGES_DIR, "classroom_environment.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("  -> Saved classroom_environment.svg")

# ==============================================================================
# 4. EDUCATION VISUALIZATIONS SVG (Dynamic Smart Board Visuals for 7 Scenes)
# ==============================================================================
def create_education_visualizations_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 480" width="940" height="480" id="svg-edu-visualizations">
  <defs>
    <linearGradient id="vis-card-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e1a2f" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="#070d18" stop-opacity="0.98"/>
    </linearGradient>
    <filter id="vis-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- ======================================================================= -->
  <!-- SCENE 1: THE CLASSROOM OF TOMORROW (Transformation Hub) -->
  <!-- ======================================================================= -->
  <g id="vis-scene-1" class="edu-vis-panel" style="display:block;">
    <!-- Background Card -->
    <rect x="0" y="0" width="940" height="480" fill="url(#vis-card-grad)" rx="8"/>
    <!-- Left: Traditional Classroom Split -->
    <rect x="40" y="50" width="410" height="380" rx="8" fill="#0a1424" stroke="#334155" stroke-width="1.5"/>
    <text x="60" y="85" fill="#f59e0b" font-size="14" font-family="monospace" font-weight="bold">CONVENTIONAL CLASSROOM</text>
    <text x="60" y="108" fill="#94a3b8" font-size="11">• Standardized pace &amp; fixed curriculum</text>
    <text x="60" y="128" fill="#94a3b8" font-size="11">• One-way lecture transmission</text>
    <text x="60" y="148" fill="#94a3b8" font-size="11">• Batch grading with delayed feedback</text>
    <!-- Visual of blackboard & rows -->
    <rect x="60" y="170" width="370" height="140" rx="4" fill="#0f1b2d" stroke="#475569" stroke-width="1"/>
    <text x="80" y="210" fill="#64748b" font-size="16" font-family="monospace">f(x) = standard_curriculum</text>
    <text x="80" y="240" fill="#475569" font-size="12">Row 1: [●] [●] [●] [●]  (Fixed)</text>
    <text x="80" y="265" fill="#475569" font-size="12">Row 2: [●] [●] [●] [●]  (Uniform)</text>
    <text x="80" y="290" fill="#475569" font-size="12">Row 3: [●] [●] [●] [●]  (Static)</text>
    <rect x="60" y="330" width="370" height="70" rx="4" fill="#141f32"/>
    <text x="80" y="360" fill="#f87171" font-size="11.5" font-weight="bold">CHALLENGE: 42% report pacing mismatch</text>
    <text x="80" y="380" fill="#94a3b8" font-size="10">High performers constrained; struggling learners isolated.</text>

    <!-- Center Arrow Transition -->
    <circle cx="470" cy="240" r="24" fill="#00e5ff" opacity="0.15" filter="url(#vis-glow)"/>
    <path d="M 460 230 L 480 240 L 460 250 Z" fill="#00e5ff"/>

    <!-- Right: Future Learning Pods Split -->
    <rect x="490" y="50" width="410" height="380" rx="8" fill="#08182b" stroke="#00e5ff" stroke-width="1.8" filter="drop-shadow(0 0 12px rgba(0, 229, 255, 0.2))"/>
    <text x="510" y="85" fill="#00e5ff" font-size="14" font-family="monospace" font-weight="bold">FUTURE ADAPTIVE CLASSROOM</text>
    <text x="510" y="108" fill="#cbd5e1" font-size="11">• Individualized learning trajectories</text>
    <text x="510" y="128" fill="#cbd5e1" font-size="11">• Real-time formative intelligence</text>
    <text x="510" y="148" fill="#cbd5e1" font-size="11">• Collaborative project inquiry</text>
    <!-- Visual of networked pods -->
    <rect x="510" y="170" width="370" height="140" rx="4" fill="#0b213a" stroke="#00e5ff" stroke-width="1"/>
    <circle cx="560" cy="225" r="22" fill="#0284c7" opacity="0.6"/>
    <text x="560" y="230" fill="#ffffff" font-size="10" text-anchor="middle" font-weight="bold">POD A</text>
    <circle cx="695" cy="210" r="22" fill="#0284c7" opacity="0.6"/>
    <text x="695" y="215" fill="#ffffff" font-size="10" text-anchor="middle" font-weight="bold">POD B</text>
    <circle cx="830" cy="235" r="22" fill="#0284c7" opacity="0.6"/>
    <text x="830" y="240" fill="#ffffff" font-size="10" text-anchor="middle" font-weight="bold">POD C</text>
    <!-- Interconnecting neural data links -->
    <line x1="582" y1="225" x2="673" y2="210" stroke="#00e5ff" stroke-width="2" stroke-dasharray="4 2"/>
    <line x1="717" y1="210" x2="808" y2="235" stroke="#00e5ff" stroke-width="2" stroke-dasharray="4 2"/>
    <circle cx="695" cy="275" r="14" fill="#10b981" opacity="0.8"/>
    <text x="695" y="279" fill="#ffffff" font-size="8" text-anchor="middle" font-weight="bold">AI MENTOR</text>
    <line x1="695" y1="232" x2="695" y2="261" stroke="#10b981" stroke-width="1.5"/>

    <rect x="510" y="330" width="370" height="70" rx="4" fill="#092947"/>
    <text x="530" y="360" fill="#38bdf8" font-size="11.5" font-weight="bold">TRANSFORMATION: +40.9% Concept Retention</text>
    <text x="530" y="380" fill="#cbd5e1" font-size="10">Adaptive scaffolding meets human teacher guidance.</text>
  </g>

  <!-- ======================================================================= -->
  <!-- SCENE 2: BEYOND TRADITIONAL TEACHING (Analysis of Conventional Model) -->
  <!-- ======================================================================= -->
  <g id="vis-scene-2" class="edu-vis-panel" style="display:none;">
    <rect x="0" y="0" width="940" height="480" fill="url(#vis-card-grad)" rx="8"/>
    <text x="40" y="45" fill="#f59e0b" font-size="16" font-family="monospace" font-weight="bold">CRITICAL ANALYSIS: TRADITIONAL EDUCATIONAL ARCHITECTURE</text>
    <text x="40" y="70" fill="#94a3b8" font-size="12">Evaluating systemic strengths versus modern pedagogical constraints.</text>

    <!-- Gaussian Standardized Bell Curve Diagram -->
    <rect x="40" y="90" width="460" height="340" rx="8" fill="#0b1728" stroke="#334155" stroke-width="1.5"/>
    <text x="60" y="120" fill="#38bdf8" font-size="12" font-family="monospace" font-weight="bold">STANDARDIZED ASSESSMENT DISTRIBUTION</text>
    <!-- Bell Curve Path -->
    <path d="M 80 340 C 180 340, 220 180, 270 180 C 320 180, 360 340, 460 340" fill="none" stroke="#f59e0b" stroke-width="3.5"/>
    <path d="M 80 340 C 180 340, 220 180, 270 180 C 320 180, 360 340, 460 340 Z" fill="#f59e0b" opacity="0.12"/>
    <line x1="270" y1="180" x2="270" y2="340" stroke="#f59e0b" stroke-width="1.8" stroke-dasharray="4 3"/>
    <text x="270" y="165" fill="#f59e0b" font-size="11" text-anchor="middle" font-family="monospace">Standard Pace (μ = 69.0)</text>
    <!-- Standardized Exam Axis -->
    <line x1="80" y1="340" x2="460" y2="340" stroke="#475569" stroke-width="1.5"/>
    <text x="120" y="365" fill="#ef4444" font-size="10">Under-Scaffolded (35%)</text>
    <text x="360" y="365" fill="#38bdf8" font-size="10">Under-Challenged (25%)</text>
    <text x="60" y="405" fill="#94a3b8" font-size="10.5">Fixed exam pacing measures memorization rather than deep conceptual agility.</text>

    <!-- Right Side: Structural Limitations Cards -->
    <rect x="520" y="90" width="380" height="100" rx="6" fill="#0f1b2d" stroke="#f59e0b" stroke-width="1"/>
    <text x="540" y="118" fill="#f59e0b" font-size="12" font-weight="bold">1. TIME-LOCKED INSTRUCTION</text>
    <text x="540" y="140" fill="#cbd5e1" font-size="10.5">Lectures move by academic calendar, not student mastery.</text>
    <text x="540" y="160" fill="#94a3b8" font-size="10">Students carry unaddressed knowledge gaps into advanced modules.</text>

    <rect x="520" y="210" width="380" height="100" rx="6" fill="#0f1b2d" stroke="#38bdf8" stroke-width="1"/>
    <text x="540" y="238" fill="#38bdf8" font-size="12" font-weight="bold">2. DELAYED FEEDBACK CYCLES</text>
    <text x="540" y="260" fill="#cbd5e1" font-size="10.5">Batch homework returned days or weeks after submission.</text>
    <text x="540" y="280" fill="#94a3b8" font-size="10">Cognitive window for formative correction is frequently lost.</text>

    <rect x="520" y="330" width="380" height="100" rx="6" fill="#0f1b2d" stroke="#10b981" stroke-width="1"/>
    <text x="540" y="358" fill="#10b981" font-size="12" font-weight="bold">3. TEACHER OVERLOAD</text>
    <text x="540" y="380" fill="#cbd5e1" font-size="10.5">Heavy administrative grading consumes 40%+ of teacher time.</text>
    <text x="540" y="400" fill="#94a3b8" font-size="10">Limits capacity for one-on-one mentorship and emotional support.</text>
  </g>

  <!-- ======================================================================= -->
  <!-- SCENE 3: AI-POWERED PERSONALIZED LEARNING (Adaptive Intelligence) -->
  <!-- ======================================================================= -->
  <g id="vis-scene-3" class="edu-vis-panel" style="display:none;">
    <rect x="0" y="0" width="940" height="480" fill="url(#vis-card-grad)" rx="8"/>
    <text x="40" y="45" fill="#00e5ff" font-size="16" font-family="monospace" font-weight="bold">AI ADAPTIVE LEARNING ASSISTANT &amp; KNOWLEDGE GRAPH</text>
    <text x="40" y="70" fill="#94a3b8" font-size="12">Continuous formative scaffolding based on student problem-solving telemetry.</text>

    <!-- Left: Dynamic Knowledge Concept Graph -->
    <rect x="40" y="90" width="460" height="340" rx="8" fill="#0b1728" stroke="#00e5ff" stroke-width="1.5"/>
    <text x="60" y="118" fill="#00e5ff" font-size="12" font-family="monospace" font-weight="bold">CONCEPT READINESS GRAPH</text>
    <!-- Graph Nodes & Connections -->
    <line x1="120" y1="180" x2="220" y2="150" stroke="#00e5ff" stroke-width="2"/>
    <line x1="120" y1="180" x2="220" y2="240" stroke="#10b981" stroke-width="2"/>
    <line x1="220" y1="150" x2="330" y2="170" stroke="#00e5ff" stroke-width="2.5"/>
    <line x1="220" y1="240" x2="330" y2="210" stroke="#f59e0b" stroke-width="2"/>
    <line x1="330" y1="170" x2="420" y2="200" stroke="#00e5ff" stroke-width="3"/>
    
    <!-- Nodes -->
    <circle cx="120" cy="180" r="18" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
    <text x="120" y="184" fill="#ffffff" font-size="8.5" text-anchor="middle" font-weight="bold">ALGEBRA</text>

    <circle cx="220" cy="150" r="22" fill="#0369a1" stroke="#00e5ff" stroke-width="2"/>
    <text x="220" y="154" fill="#ffffff" font-size="9" text-anchor="middle" font-weight="bold">CALCULUS</text>

    <circle cx="220" cy="240" r="20" fill="#065f46" stroke="#10b981" stroke-width="2"/>
    <text x="220" y="244" fill="#ffffff" font-size="8.5" text-anchor="middle" font-weight="bold">GEOMETRY</text>

    <circle cx="330" cy="170" r="26" fill="#0891b2" stroke="#22d3ee" stroke-width="2.5" filter="url(#vis-glow)"/>
    <text x="330" y="174" fill="#ffffff" font-size="9.5" text-anchor="middle" font-weight="bold">PHYSICS I</text>

    <circle cx="420" cy="200" r="22" fill="#1e1b4b" stroke="#818cf8" stroke-width="2"/>
    <text x="420" y="204" fill="#c7d2fe" font-size="8" text-anchor="middle" font-weight="bold">QUANTUM</text>

    <!-- Legend & Real-time AI Status -->
    <rect x="60" y="310" width="420" height="100" rx="4" fill="#071322" stroke="#1e293b" stroke-width="1"/>
    <text x="75" y="332" fill="#10b981" font-size="10.5" font-weight="bold">• Mastered Concept: Calculus (94% Accuracy)</text>
    <text x="75" y="352" fill="#f59e0b" font-size="10.5" font-weight="bold">• In-Progress Scaffolding: Physics Vector Mechanics</text>
    <text x="75" y="372" fill="#00e5ff" font-size="10.5" font-weight="bold">• AI Action: Deployed targeted visual simulation exercise</text>
    <text x="75" y="392" fill="#94a3b8" font-size="9.5">Formative recommendations dynamically reviewed by course instructor.</text>

    <!-- Right: Student Learning Analytics Telemetry -->
    <rect x="520" y="90" width="380" height="340" rx="8" fill="#0b1728" stroke="#1e293b" stroke-width="1.5"/>
    <text x="540" y="118" fill="#ffffff" font-size="12" font-family="monospace" font-weight="bold">STUDENT PROGRESS METRICS</text>

    <!-- Progress Bar 1 -->
    <text x="540" y="150" fill="#94a3b8" font-size="11">Concept Mastery Index</text>
    <rect x="540" y="160" width="340" height="14" rx="4" fill="#1e293b"/>
    <rect x="540" y="160" width="285" height="14" rx="4" fill="#00e5ff"/>
    <text x="835" y="152" fill="#00e5ff" font-size="11" font-weight="bold">84%</text>

    <!-- Progress Bar 2 -->
    <text x="540" y="205" fill="#94a3b8" font-size="11">Engagement &amp; Persistence</text>
    <rect x="540" y="215" width="340" height="14" rx="4" fill="#1e293b"/>
    <rect x="540" y="215" width="300" height="14" rx="4" fill="#38bdf8"/>
    <text x="835" y="207" fill="#38bdf8" font-size="11" font-weight="bold">88%</text>

    <!-- Progress Bar 3 -->
    <text x="540" y="260" fill="#94a3b8" font-size="11">Peer Collaboration Score</text>
    <rect x="540" y="270" width="340" height="14" rx="4" fill="#1e293b"/>
    <rect x="540" y="270" width="265" height="14" rx="4" fill="#10b981"/>
    <text x="835" y="262" fill="#10b981" font-size="11" font-weight="bold">78%</text>

    <rect x="540" y="310" width="340" height="100" rx="6" fill="#0e223d" stroke="#38bdf8" stroke-width="1"/>
    <text x="555" y="335" fill="#38bdf8" font-size="11" font-weight="bold">PEDAGOGICAL PRINCIPLE:</text>
    <text x="555" y="355" fill="#f8fafc" font-size="10">"AI supports teacher decision-making with actionable data,</text>
    <text x="555" y="372" fill="#f8fafc" font-size="10">preserving human judgment, ethics, and emotional care."</text>
    <text x="555" y="392" fill="#94a3b8" font-size="9">— Dr. Sophia Bennett &amp; Emily Carter</text>
  </g>

  <!-- ======================================================================= -->
  <!-- SCENE 4: IMMERSIVE AND INTERACTIVE CLASSROOMS (VR & Virtual Labs) -->
  <!-- ======================================================================= -->
  <g id="vis-scene-4" class="edu-vis-panel" style="display:none;">
    <rect x="0" y="0" width="940" height="480" fill="url(#vis-card-grad)" rx="8"/>
    <text x="40" y="45" fill="#38bdf8" font-size="16" font-family="monospace" font-weight="bold">VIRTUAL LABORATORIES &amp; IMMERSIVE SCIENCE PLATFORMS</text>
    <text x="40" y="70" fill="#94a3b8" font-size="12">High-fidelity 3D simulations enabling experiential learning without equipment limits.</text>

    <!-- Left: Virtual Chemistry / Molecular Orbitals -->
    <rect x="40" y="90" width="420" height="340" rx="8" fill="#09182d" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="60" y="118" fill="#38bdf8" font-size="12" font-family="monospace" font-weight="bold">VIRTUAL MOLECULAR LAB: BENZENE RING</text>
    <!-- 3D Molecular Model Visual -->
    <g transform="translate(180, 220)">
      <polygon points="70,0 35,60 -35,60 -70,0 -35,-60 35,-60" fill="none" stroke="#00e5ff" stroke-width="3" filter="url(#vis-glow)"/>
      <circle cx="70" cy="0" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
      <circle cx="35" cy="60" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
      <circle cx="-35" cy="60" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
      <circle cx="-70" cy="0" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
      <circle cx="-35" cy="-60" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
      <circle cx="35" cy="-60" r="14" fill="#0284c7" stroke="#ffffff" stroke-width="2"/>
      <!-- Delocalized electron pi-cloud -->
      <circle cx="0" cy="0" r="45" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="6 3"/>
      <text x="0" y="4" fill="#f59e0b" font-size="10" text-anchor="middle" font-weight="bold">π-ORBITAL</text>
    </g>
    <rect x="60" y="340" width="380" height="70" rx="4" fill="#071322"/>
    <text x="75" y="365" fill="#cbd5e1" font-size="10.5">Real-time thermodynamic reaction modeling</text>
    <text x="75" y="385" fill="#38bdf8" font-size="10">Zero chemical waste • 100% Student safety • Infinite repetitions</text>

    <!-- Right: Aerospace & Anatomy Virtual Models -->
    <rect x="480" y="90" width="420" height="340" rx="8" fill="#09182d" stroke="#00e5ff" stroke-width="1.5"/>
    <text x="500" y="118" fill="#00e5ff" font-size="12" font-family="monospace" font-weight="bold">AEROSPACE WIND TUNNEL SIMULATION</text>
    <!-- Airfoil and Streamlines -->
    <g transform="translate(520, 200)">
      <!-- Curved Airfoil cross section -->
      <path d="M 40 40 Q 140 0 280 40 Q 140 60 40 40 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5"/>
      <!-- Streamlines -->
      <path d="M 0 10 Q 140 -25 340 15" stroke="#00e5ff" stroke-width="2" fill="none" opacity="0.8"/>
      <path d="M 0 30 Q 140 10 340 35" stroke="#00e5ff" stroke-width="2.5" fill="none"/>
      <path d="M 0 50 Q 140 70 340 60" stroke="#38bdf8" stroke-width="2" fill="none" opacity="0.8"/>
      <path d="M 0 70 Q 140 85 340 80" stroke="#38bdf8" stroke-width="1.5" fill="none" opacity="0.6"/>
      <!-- Pressure Differential Vectors -->
      <line x1="160" y1="18" x2="160" y2="-10" stroke="#f59e0b" stroke-width="2.5"/>
      <polygon points="160,-15 155,-7 165,-7" fill="#f59e0b"/>
      <text x="175" y="-3" fill="#f59e0b" font-size="10" font-weight="bold">LIFT (ΔP)</text>
    </g>
    <rect x="500" y="340" width="380" height="70" rx="4" fill="#071322"/>
    <text x="515" y="365" fill="#cbd5e1" font-size="10.5">Collaborative remote engineering sandbox</text>
    <text x="515" y="385" fill="#10b981" font-size="10">Global student teams collaborate in shared virtual space in real time</text>
  </g>

  <!-- ======================================================================= -->
  <!-- SCENE 5: MATLAB SCIENTIFIC ANALYSIS (Scientific Simulation Platform) -->
  <!-- ======================================================================= -->
  <g id="vis-scene-5" class="edu-vis-panel" style="display:none;">
    <rect x="0" y="0" width="940" height="480" fill="url(#vis-card-grad)" rx="8"/>
    <text x="40" y="42" fill="#00e5ff" font-size="15" font-family="monospace" font-weight="bold">MATLAB SCIENTIFIC SIMULATION: FutureClassrooms.m [N=500]</text>
    <text x="40" y="65" fill="#94a3b8" font-size="11">Empirical evaluation of learning modalities • EDUCATIONAL SIMULATION — SYNTHETIC DATA</text>

    <!-- Key Metrics Ribbon -->
    <g transform="translate(40, 80)">
      <rect x="0" y="0" width="160" height="60" rx="6" fill="#0c1e36" stroke="#00e5ff" stroke-width="1"/>
      <text x="15" y="22" fill="#94a3b8" font-size="9" font-family="monospace">CONCEPT RETENTION</text>
      <text x="15" y="48" fill="#00e5ff" font-size="18" font-weight="bold">+40.9%</text>

      <rect x="175" y="0" width="160" height="60" rx="6" fill="#0c1e36" stroke="#38bdf8" stroke-width="1"/>
      <text x="190" y="22" fill="#94a3b8" font-size="9" font-family="monospace">ENGAGEMENT DELTA</text>
      <text x="190" y="48" fill="#38bdf8" font-size="18" font-weight="bold">+21.0 pts</text>

      <rect x="350" y="0" width="160" height="60" rx="6" fill="#0c1e36" stroke="#10b981" stroke-width="1"/>
      <text x="365" y="22" fill="#94a3b8" font-size="9" font-family="monospace">FEEDBACK RATE</text>
      <text x="365" y="48" fill="#10b981" font-size="18" font-weight="bold">2.8x Freq</text>

      <rect x="525" y="0" width="160" height="60" rx="6" fill="#0c1e36" stroke="#f59e0b" stroke-width="1"/>
      <text x="540" y="22" fill="#94a3b8" font-size="9" font-family="monospace">MASTERY INDEX</text>
      <text x="540" y="48" fill="#f59e0b" font-size="18" font-weight="bold">+18.5 pts</text>

      <rect x="700" y="0" width="160" height="60" rx="6" fill="#0c1e36" stroke="#a855f7" stroke-width="1"/>
      <text x="715" y="22" fill="#94a3b8" font-size="9" font-family="monospace">COHORT SIZE</text>
      <text x="715" y="48" fill="#a855f7" font-size="18" font-weight="bold">N = 500</text>
    </g>

    <!-- Split Visual Comparison Chart -->
    <rect x="40" y="155" width="460" height="280" rx="8" fill="#081426" stroke="#1e293b" stroke-width="1.5"/>
    <text x="60" y="180" fill="#ffffff" font-size="11" font-weight="bold">CORE COMPETENCY DELTA (TRADITIONAL VS. ADAPTIVE)</text>
    
    <!-- Bar 1: Retention -->
    <text x="60" y="210" fill="#94a3b8" font-size="10">8-Wk Retention: Trad (61.5) vs AI (81.0)</text>
    <rect x="60" y="218" width="180" height="12" rx="3" fill="#1e3a5f"/>
    <rect x="60" y="218" width="254" height="12" rx="3" fill="#00e5ff" opacity="0.85"/>

    <!-- Bar 2: Engagement -->
    <text x="60" y="255" fill="#94a3b8" font-size="10">Engagement: Trad (62.0) vs AI (82.5)</text>
    <rect x="60" y="263" width="182" height="12" rx="3" fill="#1e3a5f"/>
    <rect x="60" y="263" width="258" height="12" rx="3" fill="#38bdf8" opacity="0.85"/>

    <!-- Bar 3: Assessment -->
    <text x="60" y="300" fill="#94a3b8" font-size="10">Assessment: Trad (69.0) vs AI (84.5)</text>
    <rect x="60" y="308" width="202" height="12" rx="3" fill="#1e3a5f"/>
    <rect x="60" y="308" width="264" height="12" rx="3" fill="#10b981" opacity="0.85"/>

    <!-- Bar 4: Collaborative -->
    <text x="60" y="345" fill="#94a3b8" font-size="10">Collaborative: Trad (59.0) vs AI (78.5)</text>
    <rect x="60" y="353" width="173" height="12" rx="3" fill="#1e3a5f"/>
    <rect x="60" y="353" width="245" height="12" rx="3" fill="#f59e0b" opacity="0.85"/>

    <text x="60" y="415" fill="#64748b" font-size="9" family="monospace">Blue bar = Traditional Base | Bright bar = Adaptive Scaffolding Model</text>

    <!-- Right Side: Five Scientific Plot Tabs Switcher Mockup -->
    <rect x="520" y="155" width="380" height="280" rx="8" fill="#081426" stroke="#00e5ff" stroke-width="1.2"/>
    <text x="540" y="180" fill="#00e5ff" font-size="11" font-weight="bold">MATLAB EXPORTED VISUALIZATION INDEX</text>
    <text x="540" y="205" fill="#cbd5e1" font-size="10">• Plot 1: Student Engagement vs. Weekly Hours</text>
    <text x="540" y="230" fill="#cbd5e1" font-size="10">• Plot 2: Learning Model Comparative Bar Analysis</text>
    <text x="540" y="255" fill="#cbd5e1" font-size="10">• Plot 3: Pearson Correlation Heatmap (r = 0.81)</text>
    <text x="540" y="280" fill="#cbd5e1" font-size="10">• Plot 4: Concept Retention vs. Feedback Interventions</text>
    <text x="540" y="305" fill="#cbd5e1" font-size="10">• Plot 5: Multi-Panel Future Classroom Dashboard</text>

    <rect x="540" y="335" width="340" height="85" rx="4" fill="#0d2138" stroke="#38bdf8" stroke-width="0.8"/>
    <text x="555" y="360" fill="#38bdf8" font-size="10" font-weight="bold">TRANSPARENT SCIENTIFIC NOTE:</text>
    <text x="555" y="378" fill="#94a3b8" font-size="9">Simulation parameters reflect hypothesized pedagogical</text>
    <text x="555" y="394" fill="#94a3b8" font-size="9">scaffolding benefits, reproducible via FutureClassrooms.m.</text>
  </g>

  <!-- ======================================================================= -->
  <!-- SCENE 6: THE TEACHER OF THE FUTURE (Human Mentorship & AI Co-Pilot) -->
  <!-- ======================================================================= -->
  <g id="vis-scene-6" class="edu-vis-panel" style="display:none;">
    <rect x="0" y="0" width="940" height="480" fill="url(#vis-card-grad)" rx="8"/>
    <text x="40" y="45" fill="#f59e0b" font-size="16" font-family="monospace" font-weight="bold">THE HUMAN TEACHER AT THE CENTER OF INNOVATION</text>
    <text x="40" y="70" fill="#94a3b8" font-size="12">Technology handles administrative computation; humans provide inspiration, empathy, and wisdom.</text>

    <!-- Visual 1: Human Irreplaceable Competencies Matrix -->
    <rect x="40" y="90" width="420" height="340" rx="8" fill="#0b1728" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="60" y="120" fill="#f59e0b" font-size="12" font-family="monospace" font-weight="bold">IRREPLACEABLE HUMAN CAPABILITIES</text>

    <g transform="translate(60, 140)">
      <circle cx="20" cy="20" r="16" fill="#f59e0b" opacity="0.2"/>
      <text x="20" y="24" fill="#f59e0b" font-size="12" text-anchor="middle">♥</text>
      <text x="50" y="20" fill="#ffffff" font-size="11" font-weight="bold">Empathy &amp; Emotional Support</text>
      <text x="50" y="35" fill="#94a3b8" font-size="9.5">Recognizing burnout, anxiety, and student motivation.</text>
    </g>

    <g transform="translate(60, 200)">
      <circle cx="20" cy="20" r="16" fill="#00e5ff" opacity="0.2"/>
      <text x="20" y="24" fill="#00e5ff" font-size="12" text-anchor="middle">⚖</text>
      <text x="50" y="20" fill="#ffffff" font-size="11" font-weight="bold">Ethical Discernment &amp; Values</text>
      <text x="50" y="35" fill="#94a3b8" font-size="9.5">Teaching integrity, critical skepticism, and social justice.</text>
    </g>

    <g transform="translate(60, 260)">
      <circle cx="20" cy="20" r="16" fill="#10b981" opacity="0.2"/>
      <text x="20" y="24" fill="#10b981" font-size="12" text-anchor="middle">★</text>
      <text x="50" y="20" fill="#ffffff" font-size="11" font-weight="bold">Creative Inspiration &amp; Passion</text>
      <text x="50" y="35" fill="#94a3b8" font-size="9.5">Igniting intrinsic intellectual curiosity through storytelling.</text>
    </g>

    <g transform="translate(60, 320)">
      <circle cx="20" cy="20" r="16" fill="#a855f7" opacity="0.2"/>
      <text x="20" y="24" fill="#a855f7" font-size="12" text-anchor="middle">✦</text>
      <text x="50" y="20" fill="#ffffff" font-size="11" font-weight="bold">Personal Mentorship</text>
      <text x="50" y="35" fill="#94a3b8" font-size="9.5">Guiding life choices, career direction, and character growth.</text>
    </g>

    <!-- Right Side: The Symbiotic Model (Teacher + AI Assistant) -->
    <rect x="480" y="90" width="420" height="340" rx="8" fill="#0b1728" stroke="#10b981" stroke-width="1.5"/>
    <text x="500" y="120" fill="#10b981" font-size="12" font-family="monospace" font-weight="bold">THE SYMBIOTIC CO-PILOT MODEL</text>

    <rect x="500" y="140" width="380" height="65" rx="6" fill="#08233d"/>
    <text x="520" y="165" fill="#38bdf8" font-size="11" font-weight="bold">AI AUTOMATES (40% Time Saved):</text>
    <text x="520" y="185" fill="#cbd5e1" font-size="10">Automated grading • Attendance • Routine drill generation</text>

    <rect x="500" y="220" width="380" height="65" rx="6" fill="#08332d"/>
    <text x="520" y="245" fill="#10b981" font-size="11" font-weight="bold">TEACHER REINVESTS TIME INTO:</text>
    <text x="520" y="265" fill="#cbd5e1" font-size="10">Deep 1-on-1 coaching • Group project facilitation • Moral growth</text>

    <rect x="500" y="300" width="380" height="110" rx="6" fill="#192841" stroke="#f59e0b" stroke-width="1"/>
    <text x="520" y="325" fill="#f59e0b" font-size="10.5" font-weight="bold">CORE CONSENSUS:</text>
    <text x="520" y="348" fill="#f8fafc" font-size="10.5" font-style="italic">"The classroom of the future will not be defined</text>
    <text x="520" y="368" fill="#f8fafc" font-size="10.5" font-style="italic">by technology alone. It will be defined by how</text>
    <text x="520" y="388" fill="#f8fafc" font-size="10.5" font-style="italic">intelligently we combine technology with human understanding."</text>
  </g>

  <!-- ======================================================================= -->
  <!-- SCENE 7: REIMAGINING EDUCATION (Future Educational Ecosystem) -->
  <!-- ======================================================================= -->
  <g id="vis-scene-7" class="edu-vis-panel" style="display:none;">
    <rect x="0" y="0" width="940" height="480" fill="url(#vis-card-grad)" rx="8"/>
    
    <!-- Planetary Educational Ecosystem Illustration -->
    <circle cx="470" cy="200" r="110" fill="#031633" stroke="#00e5ff" stroke-width="2" filter="url(#vis-glow)"/>
    <circle cx="470" cy="200" r="135" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-dasharray="6 4"/>
    <circle cx="470" cy="200" r="160" fill="none" stroke="#f59e0b" stroke-width="1" stroke-dasharray="3 5"/>

    <!-- Satellites / Global Learning Nodes -->
    <circle cx="370" cy="110" r="14" fill="#0284c7"/>
    <text x="370" y="114" fill="#ffffff" font-size="7" text-anchor="middle" font-weight="bold">VR LAB</text>
    <line x1="380" y1="120" x2="430" y2="160" stroke="#00e5ff" stroke-width="1.5"/>

    <circle cx="580" cy="130" r="14" fill="#10b981"/>
    <text x="580" y="134" fill="#ffffff" font-size="7" text-anchor="middle" font-weight="bold">AI MENTOR</text>
    <line x1="570" y1="140" x2="510" y2="170" stroke="#10b981" stroke-width="1.5"/>

    <circle cx="560" cy="290" r="14" fill="#a855f7"/>
    <text x="560" y="294" fill="#ffffff" font-size="7" text-anchor="middle" font-weight="bold">GLOBAL POD</text>
    <line x1="550" y1="280" x2="500" y2="230" stroke="#a855f7" stroke-width="1.5"/>

    <circle cx="360" cy="270" r="14" fill="#f59e0b"/>
    <text x="360" y="274" fill="#ffffff" font-size="7" text-anchor="middle" font-weight="bold">EQUITY</text>
    <line x1="375" y1="260" x2="430" y2="220" stroke="#f59e0b" stroke-width="1.5"/>

    <!-- Central Globe Emblem -->
    <text x="470" y="195" fill="#00e5ff" font-size="16" text-anchor="middle" font-family="monospace" font-weight="bold">THE FUTURE OF</text>
    <text x="470" y="218" fill="#ffffff" font-size="18" text-anchor="middle" font-family="monospace" font-weight="bold">CLASSROOMS</text>

    <!-- Final Concluding Banner -->
    <rect x="80" y="380" width="780" height="80" rx="8" fill="#07182f" stroke="#38bdf8" stroke-width="1.8" filter="drop-shadow(0 0 15px rgba(56, 189, 248, 0.3))"/>
    <text x="470" y="412" fill="#ffffff" font-size="14" text-anchor="middle" font-family="monospace" font-weight="bold">"Where Human Potential Meets Intelligent Education"</text>
    <text x="470" y="440" fill="#00e5ff" font-size="12" text-anchor="middle">Tomorrow's classroom is not simply a smarter room. It is a smarter way of helping every learner discover their potential.</text>
  </g>
</svg>'''
    with open(os.path.join(IMAGES_DIR, "education_visualizations.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("  -> Saved education_visualizations.svg")

def main():
    print("="*70)
    print("THE FUTURE OF CLASSROOMS: VECTOR SVG ASSET GENERATOR")
    print("="*70)
    create_dr_sophia_bennett_svg()
    create_emily_carter_svg()
    create_classroom_environment_svg()
    create_education_visualizations_svg()
    print("\n[COMPLETE] All vector SVG assets created successfully!")

if __name__ == "__main__":
    main()
