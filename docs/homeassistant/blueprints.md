# Home Assistant Blueprints

The repository [`48broadbent/ha-blueprints`](https://gitlab.com/48broadbent/ha-blueprints) contains a suite of reusable Home Assistant automation blueprints authored to streamline recurring smart home behaviors across lighting, climate, wireless switches, and security.

---

## Blueprints Index

| Blueprint Name | Source File | Triggers & Inputs | Action & Scope |
|---|---|---|---|
| **Humidity Controlled Switch** | `humidity.yaml` | Humidity sensor (BME280), high threshold %, low threshold % | Automates bathroom ventilation / extraction fans when shower runs |
| **Motion & Light-Level Control** | `motion_light_level.yaml` | Motion detector, TEMT6000 light level sensor, target lights | Activates lighting only when motion is detected *and* ambient lux is low |
| **Night Mode Coordinator** | `night_mode.yaml` | Bedtime switch, time schedule, or NFC scan | Houses-wide transition into low-brightness, zero-audible-alert state |
| **IKEA Rodret & Somrig Control** | `ikea_rodret_somrig_onoff.yaml` | IKEA Rodret (E2201) / Somrig (E2213) Zigbee remote | Maps click, double-click, and long-press to toggles and smooth dimming |
| **IKEA Trådfri 5-Button Remote** | `ikea_tradfri_five_buttons.yaml` | Classic round Trådfri 5-button remote | Maps center, up, down, left, right buttons to color temperature and scenes |
| **IKEA Trådfri On/Off Dimmer** | `ikea_tradfri_onoff.yaml` | Trådfri 2-button wireless dimmer | Simple on/off and step dimming for desk and bedside lamps |
| **Xiaomi Mijia Wireless Switch** | `xiaomi-mijia-switch.yaml` | Round Mijia wireless button | Handles single click, double click, and press-and-hold events |
| **Holiday Lighting Sequences** | `holiday_lights.yaml` | Solar elevation, calendar period, LED tree nodes | Schedules decorative illumination patterns between sunset and bedtime |
| **Smart Bulb State Reset** | `reset_light.yaml` | Wall switch power cycle or morning timer | Restores smart bulbs to neutral warm-white (2700K) and 80% brightness |
| **Alarm & Perimeter Monitor** | `alarm.yaml` | Door/window contact sensors, motion, camera tripwires | Arming states, countdown beepers, and mobile alert dispatch |

---

## Blueprint Spotlight: Humidity Controlled Switch

Automatically extracts moisture after showers using feedback from ESPHome nodes (`my_hum` from BME280):

```yaml
blueprint:
  name: Humidity Controlled Switch
  description: Turn on a switch when humidity exceeds high_humidity% and turn off below low_humidity%.
  source_url: https://gitlab.com/48broadbent/ha-blueprints/-/raw/main/humidity.yaml
  author: drFaustroll
  domain: automation
  input:
    humidity_sensor:
      name: Humidity Sensor
      selector:
        entity:
          domain: sensor
          device_class: humidity
    switch:
      name: Switch
      selector:
        entity:
          domain: switch
    high_humidity:
      name: High Humidity Threshold
      default: 58
      selector:
        number:
          min: 0
          max: 100
          unit_of_measurement: "%"
    low_humidity:
      name: Low Humidity Threshold
      default: 53
      selector:
        number:
          min: 0
          max: 100
          unit_of_measurement: "%"

trigger:
  - platform: state
    entity_id: !input humidity_sensor

action:
  - choose:
      - conditions:
          - condition: numeric_state
            entity_id: !input humidity_sensor
            above: !input high_humidity
        sequence:
          - service: switch.turn_on
            target:
              entity_id: !input switch
      - conditions:
          - condition: numeric_state
            entity_id: !input humidity_sensor
            below: !input low_humidity
        sequence:
          - service: switch.turn_off
            target:
              entity_id: !input switch
```

---

## Importing Blueprints into Home Assistant

To import any of these blueprints directly into your Home Assistant instance:

1. In Home Assistant, navigate to **Settings** > **Automations & Scenes** > **Blueprints**.
2. Click **Import Blueprint** in the bottom right corner.
3. Paste the raw GitLab URL of the blueprint:
   ```
   https://gitlab.com/48broadbent/ha-blueprints/-/raw/main/humidity.yaml
   ```
4. Click **Preview** and then **Save Blueprint**.
5. Create an automation directly from the UI with your preferred sensor entities and threshold sliders!

