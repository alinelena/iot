# ESPHome Fleet Overview

The software engine powering all ambient displays, environmental monitors, and smart lighting across the house is built on [ESPHome](https://esphome.io). The repository [`48broadbent/broadbent`](https://gitlab.com/48broadbent/broadbent) maintains over **40 production device configurations**, unified by standardized architectural principles.

---

## Architecture & Conventions

Every node in the fleet adheres to a clean, maintainable structure:

```
├── substitutions:        # Per-node variables (devicename, sensor types, update intervals)
├── esphome:              # Node name & build platform definition
├── wifi:                 # Fast connect credentials + fallback captive portal AP
├── api:                  # Encrypted native Home Assistant API
├── ota:                  # Secure wireless Over-the-Air updates
├── mqtt:                 # Fallback pub/sub for cross-network telemetry & weather JSON
├── sensor / display:     # Hardware-specific components
└── script / time:        # Local automation scripts & SNTP wall clock scheduling
```

---

## Core Fleet Standards

### 1. Variables & Substitutions
Device names, update cadences, and sensor identifiers are parameterized at the top of each file:
```yaml
substitutions:
  devicename: pluto
  sensor: bme280
  sensor_airq2: sgp4x
  sensor_light: temt6000
  update: 300s
  update_force: 300s
```

### 2. Fast Wi-Fi & Resilient Recovery
To minimize reconnect latency and power consumption, nodes use `fast_connect: true`. If the local Wi-Fi network is ever offline or changed, the node automatically spins up its own captive portal hotspot (`${devicename} Fallback Hotspot`) allowing recovery over smartphone without requiring a USB cable.

### 3. Dual Communication: Native API & MQTT
* **Primary**: The ESPHome native API provides sub-millisecond bidirectional communication with Home Assistant using pre-shared encryption keys.
* **Secondary**: A lightweight local MQTT client listens for weather forecast JSON payloads (`sensor/weather/forecast`) and broadcasts high-priority alerts across subnets.

### 4. Coordinated Time & E-Paper Scheduling
All e-paper nodes synchronize with SNTP against `Europe/London`:
```yaml
time:
  - platform: sntp
    timezone: 'Europe/London'
    id: my_time
    on_time_sync:
      then:
        - script.execute: refresh_screen
    on_time:
      - cron: '0 */5 * * * *'
        then:
          - if:
              condition:
                - lambda: return id(my_light).state > 1.0f;
              then:
                - script.execute: refresh_screen
```

* **5-Minute Wall Clock Alignment**: The cron trigger ticks precisely on 5-minute boundaries (`12:00`, `12:05`, `12:10`, etc.).
* **Nighttime Ambient Gating**: When ambient illumination drops below `1.0 lx` (bedroom lights turned off), the screen update is suppressed to eliminate residual clicking, refresh flashes, and unnecessary wakeups.

---

## Fleet Categories

<div class="grid cards" markdown>

-   :material-clock-outline: **E-Paper Sensor Clocks**

    ---

    16 active nodes displaying time, temperature, humidity, pressure, VOC levels, and 3-day weather forecasts on monochrome & 3-color e-paper displays.

    [:octicons-arrow-right-24: View e-paper nodes](nodes.md#e-paper-sensor-clocks)

-   :material-home-thermometer: **Room Climate Nodes**

    ---

    Headless environmental monitors located in bedrooms, kitchen, office, living room, and outdoors tracking temperature, humidity, and atmospheric trends.

    [:octicons-arrow-right-24: View room monitors](nodes.md#room-climate-environmental-monitors)

-   :material-weather-dust: **Particulate & Dust Monitors**

    ---

    High-precision optical particulate sensors (PM1006 / PMSX003) sampling PM2.5 and PM10 concentrations indoors and at the front door.

    [:octicons-arrow-right-24: View dust monitors](nodes.md#particulate-dust-monitors)

-   :material-led-strip: **Smart Lighting & LED Strips**

    ---

    Controllers for decorative lighting, Christmas trees (SP501E, NodeMCU), Rainbow strips, and the Gutenberg M5Stack Atom Matrix 5×5 LED display.

    [:octicons-arrow-right-24: View lighting nodes](nodes.md#smart-lighting-matrix-displays)

</div>
