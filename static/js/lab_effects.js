/**
 * THE FUTURE OF CLASSROOMS
 * Reimagining Education Through Innovation, Intelligence and Technology
 * File: lab_effects.js
 * 
 * Ambient Audio, Sound Effects & Procedural Character Micro-Animations.
 * Handles:
 * - Natural independent eye blinking for Dr. Sophia Bennett and Emily Carter
 * - Ambient conference atmosphere and sound transitions
 * - Gesture state transitions and nodding
 */

class LabEffectsEngine {
  constructor() {
    this.audioAmbient = null;
    this.audioTransition = null;
    this.audioClick = null;
    this.isMuted = false;
    this.blinkTimers = [];

    this.initAudio();
    this.startBlinkingEngine();
  }

  initAudio() {
    try {
      this.audioAmbient = new Audio('static/audio/ambient_conference.wav');
      this.audioAmbient.loop = true;
      this.audioAmbient.volume = 0.28;

      this.audioTransition = new Audio('static/audio/transition.wav');
      this.audioTransition.volume = 0.35;

      this.audioClick = new Audio('static/audio/ui_click.wav');
      this.audioClick.volume = 0.40;
    } catch (e) {
      console.warn("Audio initialization warning:", e);
    }
  }

  setMuted(muted) {
    this.isMuted = muted;
    if (this.audioAmbient) {
      if (this.isMuted) {
        this.audioAmbient.pause();
      } else if (window.presentationApp && window.presentationApp.isPlaying) {
        this.audioAmbient.play().catch(() => {});
      }
    }
  }

  playAmbient() {
    if (!this.isMuted && this.audioAmbient) {
      this.audioAmbient.play().catch(e => console.log("Ambient autoplay waiting for user interaction:", e));
    }
  }

  pauseAmbient() {
    if (this.audioAmbient) {
      this.audioAmbient.pause();
    }
  }

  playTransition() {
    if (!this.isMuted && this.audioTransition) {
      try {
        this.audioTransition.currentTime = 0;
        this.audioTransition.play().catch(() => {});
      } catch (e) {}
    }
  }

  playClick() {
    if (!this.isMuted && this.audioClick) {
      try {
        this.audioClick.currentTime = 0;
        this.audioClick.play().catch(() => {});
      } catch (e) {}
    }
  }

  /**
   * Procedural Blinking Engine:
   * Triggers independent natural blinks (120-180ms duration) for both characters.
   */
  startBlinkingEngine() {
    const triggerBlink = (charKey) => {
      const blinkEl = document.getElementById(`${charKey}-blink`);
      if (blinkEl) {
        blinkEl.style.opacity = '1';
        setTimeout(() => {
          blinkEl.style.opacity = '0';
        }, 140);
      }
    };

    // Sophia blinks every 3.5 - 5.0 seconds
    const scheduleSophiaBlink = () => {
      const delay = 3500 + Math.random() * 1500;
      const t = setTimeout(() => {
        triggerBlink('sophia');
        scheduleSophiaBlink();
      }, delay);
      this.blinkTimers.push(t);
    };

    // Emily blinks every 3.0 - 4.5 seconds
    const scheduleEmilyBlink = () => {
      const delay = 3000 + Math.random() * 1500;
      const t = setTimeout(() => {
        triggerBlink('emily');
        scheduleEmilyBlink();
      }, delay);
      this.blinkTimers.push(t);
    };

    scheduleSophiaBlink();
    scheduleEmilyBlink();
  }

  /**
   * Subtle listening nod for the character currently listening.
   */
  triggerListeningNod(charKey) {
    const headGroup = document.getElementById(`${charKey}-head-group`);
    if (!headGroup) return;

    headGroup.classList.remove('listening-nod');
    // Force reflow
    void headGroup.offsetWidth;
    headGroup.classList.add('listening-nod');
    setTimeout(() => {
      headGroup.classList.remove('listening-nod');
    }, 1200);
  }

  cleanup() {
    if (this.audioAmbient) {
      this.audioAmbient.pause();
    }
    this.blinkTimers.forEach(t => clearTimeout(t));
    this.blinkTimers = [];
  }
}

window.LabEffectsEngine = LabEffectsEngine;
