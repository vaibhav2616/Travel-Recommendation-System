/**
 * SAFARNAMA - Frontend Interactive Engine
 * Handles Dynamic Weather Canvas, Ambient Audio, Multi-Level Filters,
 * Tiered Package Switcher, Route Timelines, and Gemini AI Customization.
 */

// Global Application State
const state = {
  destinations: [],
  currentDestinationId: "delhi-manali",
  currentSeason: "monsoon",
  currentDuration: 4,
  currentPackageId: "comfort",
  recommendationData: null,
  geminiApiKey: localStorage.getItem("safarnama_gemini_key") || "",
  isAudioPlaying: false,
  audioContext: null,
  audioGainNode: null,
};

// ==========================================================================
// 1. Dynamic Atmospheric Canvas (Rain, Snow, Autumn Leaves, Golden Dust)
// ==========================================================================
class WeatherCanvas {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas.getContext("2d");
    this.particles = [];
    this.animationId = null;
    this.width = (this.canvas.width = window.innerWidth);
    this.height = (this.canvas.height = window.innerHeight);

    window.addEventListener("resize", () => this.resize());
    this.initParticles(state.currentSeason);
    this.animate();
  }

  resize() {
    this.width = this.canvas.width = window.innerWidth;
    this.height = this.canvas.height = window.innerHeight;
    this.initParticles(state.currentSeason);
  }

  setSeason(season) {
    state.currentSeason = season;
    document.body.className = `season-${season}`;
    this.initParticles(season);
  }

  initParticles(season) {
    this.particles = [];
    let count = 70;

    if (season === "monsoon") {
      count = 110;
      for (let i = 0; i < count; i++) {
        this.particles.push({
          x: Math.random() * this.width,
          y: Math.random() * this.height,
          length: 18 + Math.random() * 22,
          speedY: 14 + Math.random() * 10,
          speedX: -2.5,
          opacity: 0.25 + Math.random() * 0.45,
          type: "rain"
        });
      }
    } else if (season === "winter") {
      count = 80;
      for (let i = 0; i < count; i++) {
        this.particles.push({
          x: Math.random() * this.width,
          y: Math.random() * this.height,
          radius: 1.5 + Math.random() * 3.5,
          speedY: 0.8 + Math.random() * 1.8,
          speedX: Math.sin(Math.random() * Math.PI) * 1.2,
          opacity: 0.35 + Math.random() * 0.5,
          swing: Math.random() * 2,
          type: "snow"
        });
      }
    } else if (season === "autumn") {
      count = 45;
      for (let i = 0; i < count; i++) {
        this.particles.push({
          x: Math.random() * this.width,
          y: Math.random() * this.height,
          size: 7 + Math.random() * 10,
          speedY: 1.2 + Math.random() * 2,
          speedX: Math.cos(Math.random() * Math.PI) * 1.5,
          rotation: Math.random() * 360,
          rotationSpeed: (Math.random() - 0.5) * 2,
          color: Math.random() > 0.5 ? "rgba(223, 106, 79, " : "rgba(245, 158, 11, ",
          opacity: 0.4 + Math.random() * 0.4,
          type: "leaf"
        });
      }
    } else {
      // Summer twilight dust motes & golden fireflies
      count = 55;
      for (let i = 0; i < count; i++) {
        this.particles.push({
          x: Math.random() * this.width,
          y: Math.random() * this.height,
          radius: 1.2 + Math.random() * 2.5,
          speedY: -0.4 - Math.random() * 0.6,
          speedX: (Math.random() - 0.5) * 0.8,
          opacity: 0.2 + Math.random() * 0.6,
          pulse: Math.random() * Math.PI,
          type: "dust"
        });
      }
    }
  }

  animate() {
    this.ctx.clearRect(0, 0, this.width, this.height);

    for (let p of this.particles) {
      if (p.type === "rain") {
        this.ctx.beginPath();
        this.ctx.moveTo(p.x, p.y);
        this.ctx.lineTo(p.x + p.speedX, p.y + p.length);
        this.ctx.strokeStyle = `rgba(165, 243, 252, ${p.opacity})`;
        this.ctx.lineWidth = 1.3;
        this.ctx.stroke();

        p.x += p.speedX;
        p.y += p.speedY;
        if (p.y > this.height) {
          p.y = -p.length;
          p.x = Math.random() * this.width;
        }
      } else if (p.type === "snow") {
        this.ctx.beginPath();
        this.ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        this.ctx.fillStyle = `rgba(240, 249, 255, ${p.opacity})`;
        this.ctx.fill();

        p.x += p.speedX + Math.sin(p.y * 0.01) * p.swing;
        p.y += p.speedY;
        if (p.y > this.height) {
          p.y = -p.radius * 2;
          p.x = Math.random() * this.width;
        }
      } else if (p.type === "leaf") {
        this.ctx.save();
        this.ctx.translate(p.x, p.y);
        this.ctx.rotate((p.rotation * Math.PI) / 180);
        this.ctx.fillStyle = `${p.color}${p.opacity})`;
        this.ctx.beginPath();
        this.ctx.ellipse(0, 0, p.size, p.size * 0.45, 0, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.restore();

        p.x += p.speedX;
        p.y += p.speedY;
        p.rotation += p.rotationSpeed;
        if (p.y > this.height) {
          p.y = -p.size;
          p.x = Math.random() * this.width;
        }
      } else if (p.type === "dust") {
        p.pulse += 0.03;
        const currentOpacity = p.opacity * (0.6 + 0.4 * Math.sin(p.pulse));
        this.ctx.beginPath();
        this.ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        this.ctx.fillStyle = `rgba(253, 230, 138, ${currentOpacity})`;
        this.ctx.shadowBlur = 8;
        this.ctx.shadowColor = "rgba(245, 158, 11, 0.4)";
        this.ctx.fill();
        this.ctx.shadowBlur = 0;

        p.x += p.speedX;
        p.y += p.speedY;
        if (p.y < 0) {
          p.y = this.height + p.radius;
          p.x = Math.random() * this.width;
        }
      }
    }

    this.animationId = requestAnimationFrame(() => this.animate());
  }
}

// ==========================================================================
// 2. Synthesized Ambient Soundscape Engine (Web Audio API)
// ==========================================================================
class SoundscapeEngine {
  constructor() {
    this.ctx = null;
    this.isPlaying = false;
    this.gainNode = null;
    this.bufferSource = null;
  }

  toggle() {
    if (this.isPlaying) {
      this.stop();
    } else {
      this.start();
    }
  }

  start() {
    try {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioContext();

      // Create 5 seconds of pink noise buffer
      const bufferSize = this.ctx.sampleRate * 4;
      const noiseBuffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
      const output = noiseBuffer.getChannelData(0);

      let b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
      for (let i = 0; i < bufferSize; i++) {
        const white = Math.random() * 2 - 1;
        b0 = 0.99886 * b0 + white * 0.0555179;
        b1 = 0.99332 * b1 + white * 0.0750759;
        b2 = 0.96900 * b2 + white * 0.1538520;
        b3 = 0.86650 * b3 + white * 0.3104856;
        b4 = 0.55000 * b4 + white * 0.5329522;
        b5 = -0.7616 * b5 - white * 0.0168980;
        output[i] = (b0 + b1 + b2 + b3 + b4 + b5 + b6 + white * 0.5362) * 0.04;
        b6 = white * 0.115926;
      }

      this.bufferSource = this.ctx.createBufferSource();
      this.bufferSource.buffer = noiseBuffer;
      this.bufferSource.loop = true;

      // Filter to simulate soft rainfall / mountain wind breeze
      const filter = this.ctx.createBiquadFilter();
      filter.type = "lowpass";
      filter.frequency.setValueAtTime(800, this.ctx.currentTime);

      this.gainNode = this.ctx.createGain();
      this.gainNode.gain.setValueAtTime(0.01, this.ctx.currentTime);
      this.gainNode.gain.exponentialRampToValueAtTime(0.12, this.ctx.currentTime + 2);

      this.bufferSource.connect(filter);
      filter.connect(this.gainNode);
      this.gainNode.connect(this.ctx.destination);

      this.bufferSource.start(0);
      this.isPlaying = true;
      this.updateUI(true);
    } catch (e) {
      console.warn("Audio playback not supported or user blocked audio context", e);
    }
  }

  stop() {
    if (this.gainNode && this.ctx) {
      this.gainNode.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.8);
      setTimeout(() => {
        if (this.bufferSource) {
          try { this.bufferSource.stop(); } catch (e) {}
        }
        this.isPlaying = false;
        this.updateUI(false);
      }, 800);
    } else {
      this.isPlaying = false;
      this.updateUI(false);
    }
  }

  updateUI(active) {
    const btn = document.getElementById("soundscapeBtn");
    const icon = document.getElementById("soundIcon");
    if (active) {
      btn.classList.add("active");
      icon.className = "fa-solid fa-volume-high";
    } else {
      btn.classList.remove("active");
      icon.className = "fa-solid fa-volume-xmark";
    }
  }
}

// Global Instances
let weatherEngineInstance = null;
let soundEngineInstance = null;

// ==========================================================================
// 3. API Communication Layer
// ==========================================================================
const API = {
  async fetchDestinations() {
    try {
      const res = await fetch("/api/destinations");
      return await res.json();
    } catch (err) {
      console.error("Error fetching destinations:", err);
      return [];
    }
  },

  async fetchRecommendations(filters) {
    const headers = { "Content-Type": "application/json" };
    if (state.geminiApiKey) {
      headers["X-Gemini-Key"] = state.geminiApiKey;
    }

    const res = await fetch("/api/recommendations", {
      method: "POST",
      headers,
      body: JSON.stringify(filters)
    });

    if (!res.ok) {
      throw new Error(`Server returned ${res.status}: ${await res.text()}`);
    }
    return await res.json();
  },

  async customizeWithAI(itineraryContext, prompt) {
    const headers = { "Content-Type": "application/json" };
    if (state.geminiApiKey) {
      headers["X-Gemini-Key"] = state.geminiApiKey;
    }

    const res = await fetch("/api/ai/customize", {
      method: "POST",
      headers,
      body: JSON.stringify({
        itinerary_context: itineraryContext,
        user_prompt: prompt,
        api_key: state.geminiApiKey || null
      })
    });

    if (!res.ok) {
      throw new Error("Failed to customize with AI");
    }
    return await res.json();
  },

  async fetchRouteWeatherProfile(destId, origin, userTemp, month, hour) {
    const res = await fetch("/api/ml/route-weather-profile", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        destination_id: destId,
        origin: origin,
        user_temperature_c: userTemp,
        month: month,
        departure_hour: hour
      })
    });
    if (!res.ok) throw new Error("Failed to fetch ML route weather");
    return await res.json();
  },

  async predictPointWeather(lat, lon, alt, month, hour, terrain) {
    const res = await fetch("/api/ml/predict-weather", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        latitude: lat,
        longitude: lon,
        altitude_m: alt,
        month: month,
        hour: hour,
        terrain_code: terrain
      })
    });
    if (!res.ok) throw new Error("Failed to predict ML weather");
    return await res.json();
  }
};

// ==========================================================================
// 3.5 Highway Route Weather Simulator (Deep Neural Network Driven)
// ==========================================================================
class RouteWeatherSimulator {
  constructor() {
    this.routeData = null;
    this.currentIndex = 0;
    this.isPlaying = false;
    this.playTimer = null;
  }

  async loadRoute(destId, origin, userTemp = null, month = 7, hour = 6) {
    try {
      const data = await API.fetchRouteWeatherProfile(destId, origin, userTemp, month, hour);
      this.routeData = data;
      this.currentIndex = 0;

      // Update total KM and range stats
      document.getElementById("scrubberTotalKm").textContent = `${data.total_distance_km} KM`;
      document.getElementById("chartRangeStats").textContent = 
        `Min: ${data.min_temperature_c}°C • Max: ${data.max_temperature_c}°C • Peak Hazard: ${data.highest_hazard_segment.hazard_index}`;

      this.renderTicks(data.checkpoints);
      this.renderElevationChart(data.checkpoints);
      this.updateCheckpoint(0, true);
    } catch (err) {
      console.warn("Error loading ML route weather profile:", err);
    }
  }

  renderTicks(checkpoints) {
    const row = document.getElementById("scrubberTicksRow");
    row.innerHTML = "";
    checkpoints.forEach((cp, idx) => {
      const tick = document.createElement("span");
      tick.className = `s-tick ${idx === 0 ? 'active' : ''}`;
      tick.textContent = `${cp.km_marker}k`;
      tick.title = `${cp.location_name} (${cp.elevation_m}m)`;
      tick.addEventListener("click", () => {
        this.updateCheckpoint(idx, true);
      });
      row.appendChild(tick);
    });

    const slider = document.getElementById("routeScrubber");
    slider.max = checkpoints.length - 1;
    slider.value = 0;
  }

  updateCheckpoint(index, syncCanvas = true) {
    if (!this.routeData || !this.routeData.checkpoints[index]) return;
    this.currentIndex = index;
    const cp = this.routeData.checkpoints[index];

    // Update Slider & Labels
    const slider = document.getElementById("routeScrubber");
    slider.value = index;

    const progressPct = Math.round((cp.km_marker / this.routeData.total_distance_km) * 100);
    document.getElementById("scrubberPosLabel").innerHTML = 
      `Highway Progress: <strong>${progressPct}% (${cp.km_marker} KM)</strong>`;

    document.getElementById("hudKmBadge").textContent = 
      `CHECKPOINT 0${index + 1} / 0${this.routeData.checkpoints.length} • ${cp.km_marker} KM • ARRIVAL ~${cp.hour_of_arrival}`;
    document.getElementById("hudLocationName").textContent = cp.location_name;
    document.getElementById("hudAdvisoryText").textContent = cp.driving_advisory;

    // Gauges
    document.getElementById("hudTempVal").textContent = `${cp.temperature_c}°C`;
    document.getElementById("hudElevationVal").textContent = `Elevation: ${cp.elevation_m}m`;

    const condEmojiMap = {
      "clear": "☀️ Clear",
      "cloudy": "⛅ Overcast / Mist",
      "rain": "🌧️ Rain Showers",
      "heavy_rain": "⛈️ Monsoon Downpour",
      "fog": "🌫️ Dense Highway Fog",
      "snow": "❄️ High Pass Snow"
    };
    document.getElementById("hudCondVal").textContent = condEmojiMap[cp.condition] || cp.condition.toUpperCase();
    document.getElementById("hudPrecipVal").textContent = `Rain Chance: ${Math.round(cp.precipitation_prob * 100)}%`;

    const hazardPct = Math.round(cp.road_hazard_index * 100);
    let hazardLevel = "Safe";
    if (hazardPct > 65) hazardLevel = "Severe Alert";
    else if (hazardPct > 35) hazardLevel = "Caution";

    document.getElementById("hudHazardVal").textContent = `${cp.road_hazard_index} (${hazardLevel})`;
    document.getElementById("hudHazardBar").style.width = `${hazardPct}%`;

    // Highlight Ticks
    document.querySelectorAll(".s-tick").forEach((t, i) => {
      t.classList.toggle("active", i === index);
    });

    // Synchronize full screen weather canvas with the microclimate at this checkpoint
    if (syncCanvas && weatherEngineInstance) {
      if (cp.condition === "snow") {
        weatherEngineInstance.setSeason("winter");
      } else if (cp.condition === "rain" || cp.condition === "heavy_rain") {
        weatherEngineInstance.setSeason("monsoon");
      } else if (cp.condition === "fog" || cp.condition === "cloudy") {
        weatherEngineInstance.setSeason("autumn");
      } else {
        weatherEngineInstance.setSeason("summer");
      }
    }
  }

  renderElevationChart(checkpoints) {
    const wrap = document.getElementById("elevationChartWrap");
    if (!checkpoints || checkpoints.length < 2) return;

    const w = 800;
    const h = 130;
    const padding = 25;

    const maxElev = Math.max(...checkpoints.map(c => c.elevation_m), 500);
    const minElev = Math.min(...checkpoints.map(c => c.elevation_m), 0);
    const elevRange = (maxElev - minElev) || 1;

    // Generate Path Points
    const pts = checkpoints.map((c, i) => {
      const x = padding + (i / (checkpoints.length - 1)) * (w - 2 * padding);
      const y = h - padding - ((c.elevation_m - minElev) / elevRange) * (h - 2 * padding);
      return { x, y, c, i };
    });

    // Path string
    let pathD = `M ${pts[0].x} ${pts[0].y}`;
    for (let i = 1; i < pts.length; i++) {
      pathD += ` L ${pts[i].x} ${pts[i].y}`;
    }
    const areaD = `${pathD} L ${pts[pts.length - 1].x} ${h - 5} L ${pts[0].x} ${h - 5} Z`;

    const svg = `
      <svg viewBox="0 0 ${w} ${h}" preserveAspectRatio="none">
        <defs>
          <linearGradient id="elevGrad" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.35"/>
            <stop offset="100%" stop-color="#df6a4f" stop-opacity="0.02"/>
          </linearGradient>
        </defs>
        <!-- Area Fill -->
        <path d="${areaD}" fill="url(#elevGrad)"/>
        <!-- Line Stroke -->
        <path d="${pathD}" fill="none" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
        <!-- Checkpoint Dots & Labels -->
        ${pts.map(p => `
          <g class="chart-point" style="cursor:pointer;" onclick="routeSimulatorInstance.updateCheckpoint(${p.i}, true)">
            <circle cx="${p.x}" cy="${p.y}" r="4.5" fill="${p.c.condition === 'snow' ? '#38bdf8' : (p.c.precipitation_prob > 0.4 ? '#10b981' : '#f59e0b')}" stroke="#070a0e" stroke-width="1.5"/>
            <text x="${p.x}" y="${p.y - 10}" font-size="9" fill="#9ba3af" text-anchor="middle">${p.c.temperature_c}°C</text>
          </g>
        `).join('')}
      </svg>
    `;
    wrap.innerHTML = svg;
  }

  togglePlay() {
    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  }

  play() {
    if (!this.routeData) return;
    this.isPlaying = true;
    const btn = document.getElementById("playRouteBtn");
    const icon = document.getElementById("playIcon");
    btn.classList.add("playing");
    btn.innerHTML = `<i class="fa-solid fa-pause" id="playIcon"></i> <span>Pause Drive</span>`;

    this.playTimer = setInterval(() => {
      let nextIndex = this.currentIndex + 1;
      if (nextIndex >= this.routeData.checkpoints.length) {
        nextIndex = 0;
      }
      this.updateCheckpoint(nextIndex, true);
    }, 2400);
  }

  pause() {
    this.isPlaying = false;
    clearInterval(this.playTimer);
    const btn = document.getElementById("playRouteBtn");
    btn.classList.remove("playing");
    btn.innerHTML = `<i class="fa-solid fa-play" id="playIcon"></i> <span>Drive Route</span>`;
  }
}

let routeSimulatorInstance = null;

// ==========================================================================
// 4. UI Rendering Functions
// ==========================================================================
function renderCorridorBadges(destinations) {
  const container = document.getElementById("corridorBadges");
  container.innerHTML = "";

  destinations.forEach((d) => {
    const badge = document.createElement("button");
    badge.className = `corridor-badge ${d.id === state.currentDestinationId ? "active" : ""}`;
    badge.dataset.id = d.id;
    badge.innerHTML = `<i class="fa-solid fa-route"></i> <span>${d.name} (${d.state})</span>`;
    badge.addEventListener("click", () => {
      document.querySelectorAll(".corridor-badge").forEach(b => b.classList.remove("active"));
      badge.classList.add("active");
      document.getElementById("destinationSelect").value = d.id;
      triggerRecommendationFetch();
    });
    container.appendChild(badge);
  });
}

function renderDestinationDropdown(destinations) {
  const select = document.getElementById("destinationSelect");
  select.innerHTML = "";

  destinations.forEach((d) => {
    const opt = document.createElement("option");
    opt.value = d.id;
    opt.textContent = `${d.name} (${d.region} • ${d.state})`;
    if (d.id === state.currentDestinationId) opt.selected = true;
    select.appendChild(opt);
  });

  select.addEventListener("change", (e) => {
    state.currentDestinationId = e.target.value;
    document.querySelectorAll(".corridor-badge").forEach(b => {
      b.classList.toggle("active", b.dataset.id === state.currentDestinationId);
    });
    triggerRecommendationFetch();
  });
}

function renderTripPlan(data) {
  state.recommendationData = data;

  // 1. Destination Banner
  document.getElementById("destName").textContent = data.destination_name;
  document.getElementById("destTagline").textContent = data.tagline;
  document.getElementById("destState").textContent = data.state;
  document.getElementById("destHighway").innerHTML = `<i class="fa-solid fa-road"></i> ${data.route.primary_highway}`;
  document.getElementById("destSeasonBadge").innerHTML = `<i class="fa-solid fa-cloud-sun"></i> ${data.weather.season_display}`;
  document.getElementById("destCoverImage").src = data.cover_image;

  // Vibe Tags
  const tagsContainer = document.getElementById("destVibeTags");
  tagsContainer.innerHTML = data.vibe_tags.map(t => `<span class="vibe-tag">${t}</span>`).join("");

  // AI Story & Tips
  document.getElementById("aiStoryText").textContent = data.ai_story || "A breathtaking expedition awaits across the timeless corridors of India.";
  const tipsContainer = document.getElementById("aiTipsContainer");
  tipsContainer.innerHTML = data.ai_personalized_tips.map(tip => `
    <div class="tip-item">
      <i class="fa-solid fa-compass tip-icon"></i>
      <span>${tip}</span>
    </div>
  `).join("");

  // 2. Weather Module
  document.getElementById("weatherSeasonTitle").textContent = `${data.weather.season_display}`;
  document.getElementById("weatherTempBadge").textContent = data.weather.temp_range;
  document.getElementById("weatherRainVal").textContent = data.weather.rainfall_level;

  const advList = document.getElementById("weatherAdvisoriesList");
  advList.innerHTML = data.weather.advisories.map(a => `<li>${a}</li>`).join("");

  const packList = document.getElementById("weatherPackingChips");
  packList.innerHTML = data.weather.what_to_pack.map(p => `<span class="pack-chip">${p}</span>`).join("");

  // 3. Tiered Packages Switcher
  renderPackages(data.packages, data.active_package_id);

  // 4. Highway Route & Multi-Modal Transit
  document.getElementById("routeDistance").textContent = `${data.route.distance_km} KM`;
  document.getElementById("routeDuration").textContent = `${data.route.driving_time_hours} Hours`;
  document.getElementById("routeTolls").textContent = `₹${data.route.toll_estimate_inr} Tolls`;

  // Transit cards
  const transitRow = document.getElementById("transitCardsRow");
  transitRow.innerHTML = "";

  // Always show primary Roadway
  const roadCard = document.createElement("div");
  roadCard.className = "transit-card";
  roadCard.innerHTML = `
    <div class="transit-card-header">
      <span class="transit-mode-title"><i class="fa-solid fa-car"></i> Scenic Roadway</span>
      <span class="scenic-stars">★★★★★</span>
    </div>
    <div class="transit-time-price">
      <span>${data.route.driving_time_hours} Hours Drive</span>
      <strong>~₹${Math.round(data.route.distance_km * 4.2)} Fuel + Tolls</strong>
    </div>
    <p class="transit-desc">${data.route.road_condition}</p>
  `;
  transitRow.appendChild(roadCard);

  // Alternate Transits (Vande Bharat / Flights)
  data.route.alternate_transits.forEach(alt => {
    const card = document.createElement("div");
    card.className = "transit-card";
    const icon = alt.mode === "train" ? "fa-train" : (alt.mode === "flight" ? "fa-plane" : "fa-bus");
    const stars = "★".repeat(alt.scenic_rating) + "☆".repeat(5 - alt.scenic_rating);
    card.innerHTML = `
      <div class="transit-card-header">
        <span class="transit-mode-title"><i class="fa-solid ${icon}"></i> ${alt.title}</span>
        <span class="scenic-stars">${stars}</span>
      </div>
      <div class="transit-time-price">
        <span>${alt.duration_str}</span>
        <strong>~₹${alt.approx_cost_inr} / seat</strong>
      </div>
      <p class="transit-desc">${alt.description}</p>
    `;
    transitRow.appendChild(card);
  });

  // Pitstops Timeline
  const pitstopsTimeline = document.getElementById("pitstopsTimeline");
  pitstopsTimeline.innerHTML = data.route.pitstops.map(p => `
    <div class="pitstop-item">
      <div class="pitstop-info">
        <div class="pitstop-tag-strip">
          <span class="km-marker">${p.km_from_origin} KM</span>
          <span class="highway-badge">${p.highway}</span>
          ${p.pure_veg ? '<span class="diet-pill veg">🌱 Pure Veg</span>' : ''}
          ${p.jain_available ? '<span class="diet-pill jain">🪷 Jain Option</span>' : ''}
        </div>
        <h5 class="pitstop-name">${p.name}</h5>
        <p class="pitstop-location"><i class="fa-solid fa-map-pin"></i> ${p.location}</p>
        ${p.highlight_dish ? `<p class="pitstop-dish"><strong>Famous Dish:</strong> ${p.highlight_dish}</p>` : ''}
      </div>
      <div class="pitstop-price">
        <span>Avg ₹${p.avg_cost_inr}</span>
      </div>
    </div>
  `).join("");

  // 5. Day-by-Day Itinerary Accordions
  const itineraryContainer = document.getElementById("itineraryDaysContainer");
  itineraryContainer.innerHTML = data.itinerary.map((day, idx) => `
    <div class="day-card ${idx === 0 ? 'open' : ''}" data-day="${day.day}">
      <div class="day-header">
        <div class="day-title-wrap">
          <span class="day-number-badge">Day 0${day.day}</span>
          <h4 class="day-title">${day.title}</h4>
        </div>
        <i class="fa-solid fa-chevron-down day-expand-icon"></i>
      </div>
      <div class="day-content" style="${idx === 0 ? '' : 'display:none;'}">
        <div class="activities-grid">
          ${day.activities.map(act => `
            <div class="activity-card">
              <div>
                <span class="slot-tag">${act.time_of_day}</span>
                <h6 class="act-title">${act.title}</h6>
                <p class="act-desc">${act.description}</p>
              </div>
              ${act.food_recommendation ? `<div class="act-food"><i class="fa-solid fa-bowl-rice"></i> ${act.food_recommendation}</div>` : ''}
            </div>
          `).join('')}
        </div>
        <div class="day-footer-strip">
          <span class="day-tip"><strong>Desi Tip:</strong> ${day.local_tip}</span>
          <span class="day-stay"><i class="fa-solid fa-bed"></i> Recommended Stay: ${day.stay_recommendation}</span>
        </div>
      </div>
    </div>
  `).join("");

  // Accordion click handlers
  document.querySelectorAll(".day-header").forEach(header => {
    header.addEventListener("click", () => {
      const card = header.closest(".day-card");
      const content = card.querySelector(".day-content");
      const isOpen = card.classList.contains("open");
      card.classList.toggle("open", !isOpen);
      content.style.display = isOpen ? "none" : "flex";
    });
  });

  // 6. Stays & Food Showcase
  renderStaysAndFood("all");
}

function renderPackages(packages, activeTierId) {
  const container = document.getElementById("packagesContainer");
  container.innerHTML = "";

  packages.forEach(pkg => {
    const card = document.createElement("div");
    card.className = `package-card ${pkg.id === activeTierId ? 'active' : ''}`;
    card.dataset.tier = pkg.id;

    card.innerHTML = `
      <div class="pkg-top">
        <span class="pkg-badge ${pkg.is_recommended ? 'recommended' : 'standard'}">
          ${pkg.is_recommended ? '★ Recommended' : 'Package Tier'}
        </span>
        <h4 class="pkg-name">${pkg.name}</h4>
        <p class="pkg-tagline">${pkg.tagline}</p>
      </div>

      <div class="pkg-price-row">
        <span class="pkg-price-val">₹${pkg.cost_per_person.toLocaleString("en-IN")}</span>
        <span class="pkg-price-sub">/ person for ${state.currentDuration} days</span>
      </div>

      <div class="pkg-specs">
        <span><i class="fa-solid fa-hotel"></i> ${pkg.stay_style}</span>
        <span><i class="fa-solid fa-utensils"></i> ${pkg.dining_style}</span>
        <span><i class="fa-solid fa-train"></i> ${pkg.transport_type}</span>
      </div>

      <ul class="pkg-features-list">
        ${pkg.features.map(f => `<li>${f}</li>`).join('')}
      </ul>

      <button class="select-tier-btn">
        ${pkg.id === activeTierId ? 'Active Tier' : 'Select Tier'}
      </button>
    `;

    card.addEventListener("click", () => {
      document.querySelectorAll(".package-card").forEach(c => {
        c.classList.remove("active");
        c.querySelector(".select-tier-btn").textContent = "Select Tier";
      });
      card.classList.add("active");
      card.querySelector(".select-tier-btn").textContent = "Active Tier";
      state.currentPackageId = pkg.id;
      updateCostBreakdown(pkg);
    });

    container.appendChild(card);
  });

  // Update cost breakdown for active tier
  const activePkg = packages.find(p => p.id === activeTierId) || packages[0];
  updateCostBreakdown(activePkg);
}

function updateCostBreakdown(pkg) {
  document.getElementById("activeTierName").textContent = pkg.name;
  document.getElementById("groupTotalCost").textContent = `₹${pkg.total_group_cost.toLocaleString("en-IN")}`;

  const b = pkg.breakdown;
  const total = b.total_cost_per_person;
  const barsContainer = document.getElementById("costBarsGrid");

  const items = [
    { label: "Stay & Accommodation", val: b.stay_cost, icon: "fa-hotel" },
    { label: "Transit & Fuel / Tickets", val: b.transport_cost, icon: "fa-gas-pump" },
    { label: "Food & Dhabas", val: b.food_cost, icon: "fa-utensils" },
    { label: "Activities & Entries", val: b.activities_permits_cost, icon: "fa-ticket" },
    { label: "Contingency Buffer", val: b.buffer_cost, icon: "fa-shield-halved" }
  ];

  barsContainer.innerHTML = items.map(item => {
    const percent = Math.min(100, Math.round((item.val / total) * 100));
    return `
      <div class="cost-bar-item">
        <div class="cost-bar-labels">
          <span class="bar-cat"><i class="fa-solid ${item.icon}"></i> ${item.label}</span>
          <span class="bar-val">₹${item.val.toLocaleString("en-IN")} (${percent}%)</span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" style="width: ${percent}%;"></div>
        </div>
      </div>
    `;
  }).join("");
}

function renderStaysAndFood(filterTab) {
  const container = document.getElementById("staysAndFoodGrid");
  container.innerHTML = "";
  const data = state.recommendationData;
  if (!data) return;

  const items = [];

  // Add stays
  if (filterTab === "all" || filterTab === "stays") {
    data.hotels_and_stays.forEach(s => {
      items.push({
        type: "STAY",
        badge: s.type.replace("_", " ").toUpperCase(),
        name: s.name,
        location: s.location,
        vibe: s.vibe,
        rating: s.rating,
        priceStr: `₹${s.approx_price_per_night_inr.toLocaleString("en-IN")} / night`
      });
    });
  }

  // Add food spots
  if (filterTab === "all" || filterTab === "food") {
    data.curated_food_spots.forEach(f => {
      items.push({
        type: "FOOD",
        badge: f.category.toUpperCase(),
        name: f.name,
        location: `${f.location} (${f.highway})`,
        vibe: f.famous_for,
        rating: f.rating,
        priceStr: `Avg ₹${f.avg_cost_inr} per person`
      });
    });
  }

  items.forEach(item => {
    const card = document.createElement("div");
    card.className = "showcase-card";
    card.innerHTML = `
      <div>
        <div class="sc-header">
          <span class="sc-type">${item.badge}</span>
          <span class="sc-rating">★ ${item.rating}</span>
        </div>
        <h5 class="sc-name">${item.name}</h5>
        <p class="sc-location"><i class="fa-solid fa-map-pin"></i> ${item.location}</p>
        <p class="sc-vibe">${item.vibe}</p>
      </div>
      <div class="sc-footer">
        <span class="sc-price">${item.priceStr}</span>
      </div>
    `;
    container.appendChild(card);
  });
}

// ==========================================================================
// 5. Interactive Flow & Event Listeners
// ==========================================================================
async function triggerRecommendationFetch() {
  const loading = document.getElementById("loadingState");
  const results = document.getElementById("resultsContent");
  loading.classList.remove("hidden");
  results.style.opacity = "0.3";

  const filters = {
    origin: document.getElementById("originSelect").value,
    destination_id: document.getElementById("destinationSelect").value,
    group_type: document.getElementById("groupSelect").value,
    diet_preference: document.getElementById("dietSelect").value,
    transport_mode: document.getElementById("transportSelect").value,
    duration_days: parseInt(document.getElementById("durationSlider").value),
    budget_tier: state.currentPackageId,
    season: state.currentSeason
  };

  try {
    const data = await API.fetchRecommendations(filters);
    renderTripPlan(data);
    results.style.opacity = "1";
    document.getElementById("activeFilterSummary").innerHTML = `
      <span><i class="fa-solid fa-compass"></i> Curated: <strong>${filters.origin} &rarr; ${data.destination_name}</strong> (${filters.duration_days} Days, ${data.weather.season_display})</span>
    `;

    // Load Deep Neural Network Highway Route Simulator
    if (routeSimulatorInstance) {
      const month = parseInt(document.getElementById("simMonthSelect")?.value || 7);
      const hour = parseInt(document.getElementById("simHourSelect")?.value || 6);
      const userTemp = parseFloat(document.getElementById("userLiveTempInput")?.value || 28);
      routeSimulatorInstance.loadRoute(data.destination_id, filters.origin, userTemp, month, hour);
    }
  } catch (err) {
    console.error("Failed to generate recommendations:", err);
    alert("Could not load recommendations. Please verify the backend service is running.");
  } finally {
    loading.classList.add("hidden");
  }
}

function setupEventListeners() {
  // 1. Season Switcher HUD
  document.querySelectorAll(".season-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".season-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      const season = btn.dataset.season;
      weatherEngineInstance.setSeason(season);
      triggerRecommendationFetch();
    });
  });

  // 2. Audio Vibe Toggle
  document.getElementById("soundscapeBtn").addEventListener("click", () => {
    soundEngineInstance.toggle();
  });

  // 3. Quick Preset Chips
  document.querySelectorAll(".preset-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      document.querySelectorAll(".preset-chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      const preset = chip.dataset.preset;

      if (preset === "monsoon-ghats") {
        document.getElementById("destinationSelect").value = "kochi-munnar-alleppey";
        weatherEngineInstance.setSeason("monsoon");
      } else if (preset === "winter-himalayas") {
        document.getElementById("destinationSelect").value = "delhi-manali";
        weatherEngineInstance.setSeason("winter");
      } else if (preset === "royal-rajasthan") {
        document.getElementById("destinationSelect").value = "jaipur-jodhpur-jaisalmer";
        weatherEngineInstance.setSeason("autumn");
      } else if (preset === "spiritual-kashi") {
        document.getElementById("destinationSelect").value = "varanasi-ayodhya-prayagraj";
        weatherEngineInstance.setSeason("winter");
      } else if (preset === "coastal-goa") {
        document.getElementById("destinationSelect").value = "mumbai-goa-nh66";
        weatherEngineInstance.setSeason("monsoon");
      }

      // Sync season HUD
      document.querySelectorAll(".season-btn").forEach(b => {
        b.classList.toggle("active", b.dataset.season === state.currentSeason);
      });

      triggerRecommendationFetch();
    });
  });

  // 4. Duration Range Slider
  const slider = document.getElementById("durationSlider");
  slider.addEventListener("input", (e) => {
    const val = parseInt(e.target.value);
    state.currentDuration = val;
    document.getElementById("durationValue").textContent = `${val} Days`;
    const paceBadge = document.getElementById("paceBadge");
    if (val <= 3) paceBadge.textContent = "Quick Sprint";
    else if (val <= 6) paceBadge.textContent = "Balanced";
    else paceBadge.textContent = "Slow & Soulful";
  });

  // 5. Generate Button
  document.getElementById("generateBtn").addEventListener("click", triggerRecommendationFetch);

  // 6. Stays and Food Tabs
  document.querySelectorAll(".stays-tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".stays-tab-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      renderStaysAndFood(btn.dataset.tab);
    });
  });

  // 7. Print Button
  document.getElementById("printBtn").addEventListener("click", () => {
    window.print();
  });

  // 8. AI Customizer Drawer
  const drawer = document.getElementById("aiDrawer");
  const overlay = document.getElementById("aiDrawerOverlay");

  const openDrawer = () => {
    drawer.classList.remove("hidden");
    overlay.classList.remove("hidden");
  };

  const closeDrawer = () => {
    drawer.classList.add("hidden");
    overlay.classList.add("hidden");
  };

  document.getElementById("openAICustomizerBtn").addEventListener("click", openDrawer);
  document.getElementById("closeDrawerBtn").addEventListener("click", closeDrawer);
  overlay.addEventListener("click", closeDrawer);

  // Quick Prompt Chips in Drawer
  document.querySelectorAll(".prompt-chip").forEach(chip => {
    chip.addEventListener("click", () => {
      document.getElementById("aiPromptInput").value = chip.dataset.prompt;
    });
  });

  // Send AI Customization Request
  document.getElementById("sendAICustomizeBtn").addEventListener("click", async () => {
    const prompt = document.getElementById("aiPromptInput").value.trim();
    if (!prompt) return;

    const btn = document.getElementById("sendAICustomizeBtn");
    btn.disabled = true;
    btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Customizing Itinerary...`;

    try {
      const result = await API.customizeWithAI({
        origin: document.getElementById("originSelect").value,
        destination_name: state.recommendationData.destination_name,
        season: state.currentSeason,
        budget_tier: state.currentPackageId
      }, prompt);

      const output = document.getElementById("aiCustomOutput");
      output.classList.remove("hidden");
      document.getElementById("customStoryText").textContent = result.modified_story;
      document.getElementById("customRecsList").innerHTML = result.custom_recommendations.map(r => `<li>${r}</li>`).join("");

      if (result.suggested_adjustments && result.suggested_adjustments.length) {
        document.getElementById("customAdjustmentsGrid").innerHTML = result.suggested_adjustments.map(adj => `
          <div style="font-size: 0.78rem; color: #fde68a; margin-top: 0.4rem;">
            <strong>${adj.aspect}:</strong> ${adj.adjustment}
          </div>
        `).join("");
      }
    } catch (e) {
      alert("Failed to customize with AI: " + e.message);
    } finally {
      btn.disabled = false;
      btn.innerHTML = `<span><i class="fa-solid fa-paper-plane"></i> Apply Customization</span>`;
    }
  });

  // 9. Gemini API Key Modal
  const keyModal = document.getElementById("apiKeyModal");
  document.getElementById("apiKeyModalBtn").addEventListener("click", () => {
    document.getElementById("geminiKeyInput").value = state.geminiApiKey;
    keyModal.classList.remove("hidden");
  });

  document.getElementById("closeApiKeyModal").addEventListener("click", () => {
    keyModal.classList.add("hidden");
  });

  document.getElementById("saveApiKeyBtn").addEventListener("click", () => {
    const key = document.getElementById("geminiKeyInput").value.trim();
    state.geminiApiKey = key;
    if (key) {
      localStorage.setItem("safarnama_gemini_key", key);
    } else {
      localStorage.removeItem("safarnama_gemini_key");
    }
    keyModal.classList.add("hidden");
    alert("API Key configuration saved!");
    triggerRecommendationFetch();
  });

  document.getElementById("clearApiKeyBtn").addEventListener("click", () => {
    state.geminiApiKey = "";
    localStorage.removeItem("safarnama_gemini_key");
    document.getElementById("geminiKeyInput").value = "";
    keyModal.classList.add("hidden");
    alert("Gemini API Key cleared. Safarnama will use the built-in offline engine.");
    triggerRecommendationFetch();
  });

  // 10. Footer corridor links
  document.querySelectorAll(".footer-corridor-link").forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      const destId = link.dataset.id;
      document.getElementById("destinationSelect").value = destId;
      window.scrollTo({ top: 0, behavior: "smooth" });
      triggerRecommendationFetch();
    });
  });

  // 11. Route Weather Simulator & ML Triggers
  const scrubber = document.getElementById("routeScrubber");
  if (scrubber) {
    scrubber.addEventListener("input", (e) => {
      if (routeSimulatorInstance) {
        routeSimulatorInstance.updateCheckpoint(parseInt(e.target.value), true);
      }
    });
  }

  const playBtn = document.getElementById("playRouteBtn");
  if (playBtn) {
    playBtn.addEventListener("click", () => {
      if (routeSimulatorInstance) {
        routeSimulatorInstance.togglePlay();
      }
    });
  }

  const simMonth = document.getElementById("simMonthSelect");
  if (simMonth) simMonth.addEventListener("change", reloadSimulator);

  const simHour = document.getElementById("simHourSelect");
  if (simHour) simHour.addEventListener("change", reloadSimulator);

  const applyTempBtn = document.getElementById("applyUserTempBtn");
  if (applyTempBtn) applyTempBtn.addEventListener("click", reloadSimulator);

  const detectBtn = document.getElementById("detectLocationBtn");
  if (detectBtn) {
    detectBtn.addEventListener("click", async () => {
      detectBtn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> Detecting...`;

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
          async (pos) => {
            try {
              const lat = pos.coords.latitude;
              const lon = pos.coords.longitude;
              const month = parseInt(document.getElementById("simMonthSelect").value || 7);
              const hour = parseInt(document.getElementById("simHourSelect").value || 12);

              const pred = await API.predictPointWeather(lat, lon, 150.0, month, hour, 0);
              document.getElementById("userLiveTempInput").value = pred.temperature_c;
              detectBtn.innerHTML = `<i class="fa-solid fa-circle-check"></i> ${pred.temperature_c}°C Detected`;
              reloadSimulator();
            } catch (e) {
              detectBtn.innerHTML = `<i class="fa-solid fa-location-crosshairs"></i> Detect My Location`;
              alert("Could not predict location weather. Using default baseline.");
            }
          },
          (err) => {
            detectBtn.innerHTML = `<i class="fa-solid fa-location-crosshairs"></i> Detect My Location`;
            alert("Location access denied or unavailable. You can enter your current temperature manually!");
          }
        );
      } else {
        detectBtn.innerHTML = `<i class="fa-solid fa-location-crosshairs"></i> Detect My Location`;
        alert("Geolocation is not supported by your browser.");
      }
    });
  }
}

function reloadSimulator() {
  if (!routeSimulatorInstance || !state.recommendationData) return;
  const month = parseInt(document.getElementById("simMonthSelect")?.value || 7);
  const hour = parseInt(document.getElementById("simHourSelect")?.value || 6);
  const userTemp = parseFloat(document.getElementById("userLiveTempInput")?.value || 28);
  routeSimulatorInstance.loadRoute(
    state.recommendationData.destination_id,
    document.getElementById("originSelect").value,
    userTemp,
    month,
    hour
  );
}

// ==========================================================================
// 6. Application Initialization
// ==========================================================================
document.addEventListener("DOMContentLoaded", async () => {
  weatherEngineInstance = new WeatherCanvas("weatherCanvas");
  soundEngineInstance = new SoundscapeEngine();
  routeSimulatorInstance = new RouteWeatherSimulator();

  setupEventListeners();

  // Load destinations
  const destinations = await API.fetchDestinations();
  state.destinations = destinations;
  renderCorridorBadges(destinations);
  renderDestinationDropdown(destinations);

  // Initial recommendation fetch
  triggerRecommendationFetch();
});

