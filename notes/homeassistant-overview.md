# Home Assistant Integration

[Home Assistant](https://www.home-assistant.io) serves as the central brain and command center for the entire IoT ecosystem. The repository [`48broadbent/homeassistant`](https://gitlab.com/48broadbent/homeassistant) manages the core configuration, Lovelace dashboard layouts, and integration pipelines that coordinate the hardware nodes.

---

## Centralized Architecture

```mermaid
flowchart LR
    subgraph ESPHomeNodes ["41 ESPHome Nodes"]
        Sensors["Indoor Sensors<br>(BME280/680, SGP40)"]
        Displays["E-Paper Clocks<br>(1.54'', 2.13'', 2.9'', 4.2'')"]
        Lighting["Lights & Strips<br>(SP501E, NeoPixel, Tree)"]
    end

    subgraph Hub ["Home Assistant Server"]
        API["ESPHome Native API<br>(Encrypted Stream)"]
        MQTT["Mosquitto MQTT<br>(Weather JSON & Events)"]
        Z2M["Zigbee2MQTT<br>(IKEA & Xiaomi Switches)"]
        Automations["Automation Blueprints<br>(Humidity, Motion, Night, Alarm)"]
    end

    subgraph ExternalServices ["External Telemetry"]
        MetOffice["Weather Forecast Integration"]
        Mobile["Home Assistant Mobile Apps"]
    end

    Sensors -->|Encrypted API| API
    Displays <-->|Status & API| API
    Lighting <-->|State & Colors| API
    MetOffice -->|3-Day Forecast| MQTT
    MQTT -->|JSON Forecast| Displays
    Z2M --> Automations
    Automations --> Lighting
    Automations --> Displays
    Hub <--> Mobile
```

---

## Integration Highlights

### 1. Instant ESPHome Auto-Discovery
Thanks to the ESPHome native API integration, newly powered-up sensor carriers (such as the 12×6 or 8×6 board) are discovered by Home Assistant within seconds over mDNS. All entities—temperature, pressure, humidity, VOC index, ambient light, Wi-Fi RSSI, and uptime—are automatically registered with appropriate icons and units of measurement.

### 2. High-Frequency Environmental Analytics
Data from across the rooms is fed into long-term statistics and climate history graphs. This enables monitoring:
* **Microclimate variations** between floors and individual rooms.
* **Ventilation adequacy** via Sensirion SGP40 VOC trends.
* **Heating efficiency** by correlating boiler firing with room temperature curves.

### 3. Coordinated Night Mode & Lighting
Home Assistant maintains a global `input_boolean.night_mode` state. Triggered by Bedtime NFC tags, bedside IKEA switches, or automated schedules, this mode:
* Suppresses audible notifications.
* Dims smart lighting strips to deep amber/warm red.
* Coordinates with e-paper clocks to enter silent standby.

