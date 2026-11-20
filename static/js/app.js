/**
 * THE FUTURE OF CLASSROOMS
 * Reimagining Education Through Innovation, Intelligence and Technology
 * File: app.js
 * 
 * Master Presentation State Machine, Character State Controller & Dialogue Sequencer.
 * Total Presentation Duration: Exactly 165 Seconds (2 minutes 45 seconds).
 * Features 7 Continuous Scenes, Dual-Researcher Face-to-Face Animation,
 * Deterministic Dialogue Sequencing, and MATLAB Scientific Integration.
 */

// =============================================================================
// 1. CENTRAL CHARACTER STATE CONTROLLER
// =============================================================================

class CharacterStateController {
  constructor() {
    this.states = {
      sophia: 'IDLE',
      emily: 'IDLE'
    };
    this.wrapSophia = document.getElementById('char-sophia-wrap');
    this.wrapEmily = document.getElementById('char-emily-wrap');
  }

  setState(character, newState) {
    if (this.states[character] === newState) return;
    this.states[character] = newState;

    const wrap = (character === 'sophia') ? this.wrapSophia : this.wrapEmily;
    if (wrap) {
      wrap.classList.remove('state-idle', 'state-speaking', 'state-listening', 'state-thinking', 'state-paused', 'speaking', 'listening');
      const lower = newState.toLowerCase();
      wrap.classList.add(`state-${lower}`);
      if (newState === 'SPEAKING') {
        wrap.classList.add('speaking');
      } else if (newState === 'LISTENING') {
        wrap.classList.add('listening');
      }
    }
    console.log(`[STATE] ${character.toUpperCase()} -> ${newState}`);
  }

  setBoth(sophiaState, emilyState) {
    this.setState('sophia', sophiaState);
    this.setState('emily', emilyState);
  }

  getState(character) {
    return this.states[character];
  }
}

// =============================================================================
// 2. MASTER PRESENTATION APPLICATION
// =============================================================================

class PresentationApp {
  constructor() {
    this.TOTAL_DURATION = 165.0; // Exact 165 seconds
    this.currentTime = 0.0;
    this.isPlaying = false;
    this.isPaused = false;
    this.showSubtitles = true;
    this.currentSceneIdx = 0;
    this.playbackInterval = null;

    // Subsystems
    this.speechCoord = new window.SpeechCoordinator();
    this.labEffects = new window.LabEffectsEngine();
    this.matlabViewer = new window.MatlabViewer();
    this.stateController = new CharacterStateController();

    // Active dialogue queue state
    this.currentDialogueQueue = [];
    this.currentDialogueIdx = -1;
    this.dialogueTimer = null;
    this.activeUtteranceId = null;

    // Master scene definitions with sequential dialogue entries (Exactly 333 words across 14 lines)
    this.scenes = [
      {
        id: 1,
        title: "The Classroom of Tomorrow",
        start: 0.0,
        end: 22.0,
        desc: "Designing learning around how students actually learn rather than expecting uniform conformity.",
        dialogue: [
          {
            id: "s1-d1",
            sceneId: 1,
            speaker: 'sophia',
            text: "Across educational institutions worldwide, classrooms long relied on standardized lectures. What if classrooms were designed around how students actually learn, rather than expecting everyone to learn identically?",
            delaySec: 0.8
          },
          {
            id: "s1-d2",
            sceneId: 1,
            speaker: 'emily',
            text: "Precisely, Sophia. When each student possesses unique cognitive paces and passions, rigid models struggle. Thoughtful technology and artificial intelligence can transform how we learn and teach.",
            pauseBefore: 0.35
          }
        ]
      },
      {
        id: 2,
        title: "Beyond Traditional Teaching",
        start: 22.0,
        end: 44.0,
        desc: "Recognizing historical strengths while overcoming pacing bottlenecks and delayed feedback cycles.",
        dialogue: [
          {
            id: "s2-d1",
            sceneId: 2,
            speaker: 'sophia',
            text: "Traditional classrooms built modern society, fostering discipline and shared learning. Yet standardized lectures often move too quickly for some students while holding back advanced thinkers.",
            delaySec: 0.5
          },
          {
            id: "s2-d2",
            sceneId: 2,
            speaker: 'emily',
            text: "Standardized tests often measure memorization rather than deep comprehension. To unlock human capability, education must evolve from rigid uniformity into interactive, adaptive learning environments.",
            pauseBefore: 0.35
          }
        ]
      },
      {
        id: 3,
        title: "AI-Powered Personalized Learning",
        start: 44.0,
        end: 68.0,
        desc: "Real-time adaptive curriculum scaffolding paired with continuous human teacher oversight.",
        dialogue: [
          {
            id: "s3-d1",
            sceneId: 3,
            speaker: 'emily',
            text: "Artificial intelligence enables continuous personalized guidance. Adaptive platforms analyze problem-solving in real time, scaffolding complex lessons and offering tailored practice matched to each student's progress.",
            delaySec: 0.5
          },
          {
            id: "s3-d2",
            sceneId: 3,
            speaker: 'sophia',
            text: "Crucially, AI acts as an assistant, never a replacement. Smart algorithms highlight learning patterns, but qualified teachers interpret the pedagogical context, guiding students with genuine human insight.",
            pauseBefore: 0.35
          }
        ]
      },
      {
        id: 4,
        title: "Immersive & Interactive Classrooms",
        start: 68.0,
        end: 93.0,
        desc: "Virtual science laboratories, molecular simulations, and collaborative engineering sandboxes.",
        dialogue: [
          {
            id: "s4-d1",
            sceneId: 4,
            speaker: 'emily',
            text: "Immersive technology brings abstract science to life. In virtual laboratories, students explore molecular structures, inspect anatomical models, and simulate engineering experiments safely without costly physical facilities.",
            delaySec: 0.5
          },
          {
            id: "s4-d2",
            sceneId: 4,
            speaker: 'sophia',
            text: "These virtual spaces spark authentic scientific curiosity. Combined with collaborative inquiry and equitable accessibility, simulations empower students to master demanding concepts through direct experiential exploration.",
            pauseBefore: 0.35
          }
        ]
      },
      {
        id: 5,
        title: "MATLAB Scientific Simulation",
        start: 93.0,
        end: 120.0,
        desc: "Measuring the Transformation of Learning: FutureClassrooms.m empirical evaluation (N=500).",
        dialogue: [
          {
            id: "s5-d1",
            sceneId: 5,
            speaker: 'sophia',
            text: "To examine these dynamics, we created a scientific simulation in MATLAB, evaluating synthetic student sessions across engagement, adaptive feedback, collaborative participation, and concept retention.",
            delaySec: 0.5
          },
          {
            id: "s5-d2",
            sceneId: 5,
            speaker: 'emily',
            text: "Our simulation shows that interactive participation and timely adaptive feedback strongly correlate with sustained concept retention, illustrating how data-driven personalization elevates academic mastery.",
            pauseBefore: 0.35
          }
        ]
      },
      {
        id: 6,
        title: "The Teacher of the Future",
        start: 120.0,
        end: 145.0,
        desc: "Intelligent systems handle administration; human teachers provide empathy, ethics, and mentorship.",
        dialogue: [
          {
            id: "s6-d1",
            sceneId: 6,
            speaker: 'sophia',
            text: "Yet technology must elevate teachers, not replace them. Empathy, ethical discernment, creative mentorship, and emotional resilience cannot be automated. Teachers remain the compassionate heartbeat of education.",
            delaySec: 0.5
          },
          {
            id: "s6-d2",
            sceneId: 6,
            speaker: 'emily',
            text: "By streamlining administrative grading, intelligent tools liberate educators to mentor students directly, foster collaborative teamwork, and nurture curiosity with individualized human attention.",
            pauseBefore: 0.35
          }
        ]
      },
      {
        id: 7,
        title: "Reimagining Education",
        start: 145.0,
        end: 165.0,
        desc: "Where human potential meets intelligent education: helping every learner discover their potential.",
        dialogue: [
          {
            id: "s7-d1",
            sceneId: 7,
            speaker: 'sophia',
            text: "The future of education harmonizes advanced intelligence with human mentorship, creativity, and empathy.",
            delaySec: 0.5
          },
          {
            id: "s7-d2",
            sceneId: 7,
            speaker: 'emily',
            text: "Tomorrow's classroom is not simply a smarter room. It is a smarter way of helping every learner discover their potential.",
            pauseBefore: 0.35
          }
        ]
      }
    ];

    // Build flat dialogue list for lookup
    this.dialogueLines = [];
    this.scenes.forEach(sc => {
      sc.dialogue.forEach(d => this.dialogueLines.push(d));
    });

    this.initUI();
    this.initTimelineMarkers();
  }

  initUI() {
    // Start presentation button on intro modal
    const startBtn = document.getElementById('btn-start-presentation');
    if (startBtn) {
      startBtn.addEventListener('click', () => {
        const overlay = document.getElementById('intro-modal-overlay');
        if (overlay) overlay.style.display = 'none';
        this.labEffects.playClick();
        this.startPresentation();
      });
    }

    // Play / Pause button
    const playPauseBtn = document.getElementById('btn-play-pause');
    if (playPauseBtn) {
      playPauseBtn.addEventListener('click', () => {
        this.labEffects.playClick();
        this.togglePlayPause();
      });
    }

    // Restart button
    const restartBtn = document.getElementById('btn-restart');
    if (restartBtn) {
      restartBtn.addEventListener('click', () => {
        this.labEffects.playClick();
        this.restartPresentation();
      });
    }

    // Prev Scene button
    const prevBtn = document.getElementById('btn-prev-scene');
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        this.labEffects.playClick();
        this.prevScene();
      });
    }

    // Next Scene button
    const nextBtn = document.getElementById('btn-next-scene');
    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        this.labEffects.playClick();
        this.nextScene();
      });
    }

    // Subtitles toggle button
    const subBtn = document.getElementById('btn-toggle-subtitles');
    if (subBtn) {
      subBtn.addEventListener('click', () => {
        this.labEffects.playClick();
        this.showSubtitles = !this.showSubtitles;
        subBtn.classList.toggle('active', this.showSubtitles);
        const subBox = document.getElementById('subtitles-container');
        if (subBox) subBox.style.display = this.showSubtitles ? 'flex' : 'none';
      });
    }

    // Audio/Mute toggle button
    const soundBtn = document.getElementById('btn-toggle-sound');
    if (soundBtn) {
      soundBtn.addEventListener('click', () => {
        this.labEffects.playClick();
        const isMuted = !this.labEffects.isMuted;
        this.labEffects.setMuted(isMuted);
        this.speechCoord.setMuted(isMuted);
        soundBtn.classList.toggle('muted', isMuted);
        soundBtn.textContent = isMuted ? '🔇 Unmute' : '🔊 Sound';
      });
    }

    // Fullscreen toggle button
    const fsBtn = document.getElementById('btn-toggle-fullscreen');
    if (fsBtn) {
      fsBtn.addEventListener('click', () => {
        this.labEffects.playClick();
        if (!document.fullscreenElement) {
          document.documentElement.requestFullscreen().catch(() => {});
        } else {
          document.exitFullscreen().catch(() => {});
        }
      });
    }

    // Scrubbing on Timeline Track
    const track = document.getElementById('timeline-track');
    if (track) {
      track.addEventListener('click', (e) => {
        const rect = track.getBoundingClientRect();
        const clickX = e.clientX - rect.left;
        const pct = Math.max(0, Math.min(1, clickX / rect.width));
        this.seekTo(pct * this.TOTAL_DURATION);
      });
    }
  }

  initTimelineMarkers() {
    const markersContainer = document.getElementById('timeline-markers');
    if (!markersContainer) return;

    markersContainer.innerHTML = '';
    this.scenes.forEach((sc, idx) => {
      const marker = document.createElement('div');
      marker.className = `timeline-marker ${idx === 0 ? 'active' : ''}`;
      marker.style.left = `${(sc.start / this.TOTAL_DURATION) * 100}%`;
      marker.title = `Scene ${sc.id}: ${sc.title}`;
      marker.addEventListener('click', (e) => {
        e.stopPropagation();
        this.labEffects.playClick();
        this.seekTo(sc.start);
      });
      markersContainer.appendChild(marker);
    });
  }

  // ===========================================================================
  // 3. DIALOGUE QUEUE & SEQUENTIAL SPEAKER DISPATCH
  // ===========================================================================

  startSceneDialogueQueue(sceneIdx) {
    this.clearDialogueTimers();
    this.speechCoord.stop();

    const scene = this.scenes[sceneIdx];
    if (!scene || !scene.dialogue || scene.dialogue.length === 0) return;

    this.currentDialogueQueue = [...scene.dialogue];
    this.currentDialogueIdx = -1;

    // First dialogue begins after initial delay
    const firstEntry = this.currentDialogueQueue[0];
    const initialDelay = (firstEntry.delaySec !== undefined) ? firstEntry.delaySec : 0.6;

    this.dialogueTimer = setTimeout(() => {
      if (this.isPlaying && !this.isPaused && this.currentSceneIdx === sceneIdx) {
        this.executeNextDialogueInScene();
      }
    }, initialDelay * 1000);
  }

  executeNextDialogueInScene() {
    this.clearDialogueTimers();
    if (!this.isPlaying || this.isPaused) return;

    this.currentDialogueIdx++;
    if (this.currentDialogueIdx >= this.currentDialogueQueue.length) {
      // Scene dialogue completed; characters return to resting IDLE state
      console.log(`[DIALOGUE] All dialogue in Scene ${this.scenes[this.currentSceneIdx].id} finished.`);
      this.stateController.setBoth('IDLE', 'IDLE');
      this.speechCoord.resetMouths();
      return;
    }

    const entry = this.currentDialogueQueue[this.currentDialogueIdx];
    this.activeUtteranceId = entry.id;

    console.log(`[DIALOGUE] Scene ${entry.sceneId}: ${entry.speaker.toUpperCase()} starts speaking (Dialogue ID: ${entry.id}).`);

    // Deterministic Character State Transition
    if (entry.speaker === 'sophia') {
      this.stateController.setBoth('SPEAKING', 'LISTENING');
      this.labEffects.triggerListeningNod('emily');
    } else {
      this.stateController.setBoth('LISTENING', 'SPEAKING');
      this.labEffects.triggerListeningNod('sophia');
    }

    // Subtitle update in lockstep with dialogue
    const subText = document.getElementById('subtitles-text');
    const subSpeaker = document.getElementById('subtitles-speaker');
    if (subText) subText.textContent = `"${entry.text}"`;
    if (subSpeaker) {
      subSpeaker.textContent = entry.speaker === 'sophia' ? 'DR. SOPHIA BENNETT:' : 'EMILY CARTER:';
      subSpeaker.className = `subtitle-speaker-tag speaker-${entry.speaker}`;
    }

    // Speak with deterministic completion callback
    this.speechCoord.speak(
      entry.speaker,
      entry.text,
      // onEnd Callback: Automatically triggers the next speaker!
      () => {
        console.log(`[DIALOGUE] Scene ${entry.sceneId}: ${entry.speaker.toUpperCase()} finished speaking.`);
        
        // Active speaker transitions to IDLE/resting mouth
        if (entry.speaker === 'sophia') {
          this.stateController.setState('sophia', 'IDLE');
        } else {
          this.stateController.setState('emily', 'IDLE');
        }
        this.speechCoord.resetMouths();

        // Check if there is another dialogue entry in this scene
        if (this.currentDialogueIdx + 1 < this.currentDialogueQueue.length) {
          const nextEntry = this.currentDialogueQueue[this.currentDialogueIdx + 1];
          const pauseSec = nextEntry.pauseBefore || 0.35;
          console.log(`[DIALOGUE] Next speaker (${nextEntry.speaker.toUpperCase()}) will start in ${pauseSec}s.`);

          this.dialogueTimer = setTimeout(() => {
            if (this.isPlaying && !this.isPaused) {
              this.executeNextDialogueInScene();
            }
          }, pauseSec * 1000);
        } else {
          console.log(`[LIPSYNC] Both characters returned to resting states.`);
          this.stateController.setBoth('IDLE', 'IDLE');
        }
      },
      // onError Callback: Safe recovery without freezing presentation
      (err) => {
        console.warn(`[DIALOGUE RECOVERY] Dialogue ${entry.id} encountered error (${err}). Advancing queue safely.`);
        this.stateController.setBoth('IDLE', 'IDLE');
        this.speechCoord.resetMouths();

        if (this.currentDialogueIdx + 1 < this.currentDialogueQueue.length) {
          this.dialogueTimer = setTimeout(() => {
            if (this.isPlaying && !this.isPaused) {
              this.executeNextDialogueInScene();
            }
          }, 400);
        }
      }
    );
  }

  clearDialogueTimers() {
    if (this.dialogueTimer) {
      clearTimeout(this.dialogueTimer);
      this.dialogueTimer = null;
    }
  }

  // ===========================================================================
  // 4. TIMELINE PLAYBACK & SCENE TRANSITIONS
  // ===========================================================================

  startPresentation() {
    this.isPlaying = true;
    this.isPaused = false;
    this.labEffects.playAmbient();
    this.updatePlayPauseIcon();

    if (this.playbackInterval) clearInterval(this.playbackInterval);
    const tickRateMs = 100;
    this.playbackInterval = setInterval(() => {
      if (this.isPlaying && !this.isPaused) {
        this.tick(tickRateMs / 1000);
      }
    }, tickRateMs);

    this.updateSceneState(0, true);
    this.startSceneDialogueQueue(0);
  }

  togglePlayPause() {
    if (!this.isPlaying) {
      this.startPresentation();
      return;
    }
    this.isPaused = !this.isPaused;
    if (this.isPaused) {
      this.labEffects.pauseAmbient();
      this.speechCoord.pause();
      this.clearDialogueTimers();
      this.stateController.setBoth('PAUSED', 'PAUSED');
    } else {
      this.labEffects.playAmbient();
      this.speechCoord.resume();
      this.updatePlayPauseIcon();
      // If no speech active, resume queue
      if (!this.speechCoord.isSpeaking) {
        this.executeNextDialogueInScene();
      }
    }
    this.updatePlayPauseIcon();
  }

  updatePlayPauseIcon() {
    const btn = document.getElementById('btn-play-pause');
    if (btn) {
      btn.textContent = (this.isPlaying && !this.isPaused) ? '⏸ Pause' : '▶ Play';
    }
  }

  restartPresentation() {
    this.currentTime = 0.0;
    this.currentSceneIdx = 0;
    this.clearDialogueTimers();
    this.speechCoord.stop();
    this.stateController.setBoth('IDLE', 'IDLE');
    this.updateSceneState(0, true);
    this.updateProgressUI();

    if (!this.isPlaying) {
      this.startPresentation();
    } else {
      this.isPaused = false;
      this.updatePlayPauseIcon();
      this.labEffects.playAmbient();
      this.startSceneDialogueQueue(0);
    }
  }

  seekTo(seconds) {
    this.currentTime = Math.max(0, Math.min(this.TOTAL_DURATION, seconds));
    this.clearDialogueTimers();
    this.speechCoord.stop();
    this.stateController.setBoth('IDLE', 'IDLE');

    // Locate target scene
    let targetIdx = 0;
    for (let i = 0; i < this.scenes.length; i++) {
      if (this.currentTime >= this.scenes[i].start && this.currentTime < this.scenes[i].end) {
        targetIdx = i;
        break;
      }
    }

    this.updateSceneState(targetIdx, true);
    this.updateProgressUI();

    if (this.isPlaying && !this.isPaused) {
      this.startSceneDialogueQueue(targetIdx);
    }
  }

  prevScene() {
    if (this.currentSceneIdx > 0) {
      this.seekTo(this.scenes[this.currentSceneIdx - 1].start);
    } else {
      this.seekTo(0);
    }
  }

  nextScene() {
    if (this.currentSceneIdx < this.scenes.length - 1) {
      this.seekTo(this.scenes[this.currentSceneIdx + 1].start);
    } else {
      this.seekTo(this.TOTAL_DURATION);
    }
  }

  tick(dt) {
    this.currentTime += dt;
    if (this.currentTime >= this.TOTAL_DURATION) {
      this.currentTime = this.TOTAL_DURATION;
      this.isPlaying = false;
      clearInterval(this.playbackInterval);
      this.clearDialogueTimers();
      this.speechCoord.stop();
      this.stateController.setBoth('IDLE', 'IDLE');
      this.updatePlayPauseIcon();
      this.updateProgressUI();
      return;
    }

    this.checkSceneTransition(this.currentTime);
    this.updateProgressUI();
  }

  checkSceneTransition(time) {
    const sc = this.scenes[this.currentSceneIdx];
    if (time >= sc.end && this.currentSceneIdx < this.scenes.length - 1) {
      const nextIdx = this.currentSceneIdx + 1;
      this.updateSceneState(nextIdx, false);
      this.labEffects.playTransition();
      this.startSceneDialogueQueue(nextIdx);
    }
  }

  updateSceneState(newIdx, force) {
    if (newIdx === this.currentSceneIdx && !force) return;

    this.currentSceneIdx = newIdx;
    const scene = this.scenes[newIdx];

    // Update Header labels
    const titleEl = document.getElementById('current-scene-title');
    if (titleEl) titleEl.textContent = `SCENE ${scene.id}: ${scene.title.toUpperCase()}`;

    const descEl = document.getElementById('current-scene-desc');
    if (descEl) descEl.textContent = scene.desc;

    // Update markers
    const markers = document.querySelectorAll('.timeline-marker');
    markers.forEach((m, i) => m.classList.toggle('active', i === newIdx));

    // Update Dynamic Smart Display SVG Overlay
    for (let i = 1; i <= 7; i++) {
      const panel = document.getElementById(`vis-scene-${i}`);
      if (panel) {
        panel.style.display = (i === scene.id) ? 'block' : 'none';
      }
    }

    // Toggle interactive MATLAB Dashboard overlay in Scene 5
    const matlabStage = document.getElementById('matlab-interactive-stage');
    if (matlabStage) {
      matlabStage.style.display = (scene.id === 5) ? 'flex' : 'none';
    }
  }

  updateProgressUI() {
    const pct = Math.min(100, (this.currentTime / this.TOTAL_DURATION) * 100);
    const fill = document.getElementById('timeline-progress-fill');
    if (fill) fill.style.width = `${pct}%`;

    const timer = document.getElementById('presentation-timer');
    if (timer) {
      timer.textContent = `${this.formatTime(this.currentTime)} / ${this.formatTime(this.TOTAL_DURATION)}`;
    }
  }

  formatTime(secs) {
    const m = Math.floor(secs / 60);
    const s = Math.floor(secs % 60);
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }
}

// Global initialization
window.addEventListener('DOMContentLoaded', () => {
  window.presentationApp = new PresentationApp();
});
