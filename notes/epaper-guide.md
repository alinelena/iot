# E-Paper Displays & Drivers Guide

This comprehensive reference catalogs the tested electronic paper (e-paper / e-ink) displays, controller drivers, color palettes, partial refresh rules, and configurations across the ESPHome fleet.

---

## Display Matrix & Driver Mapping

The table below summarizes verified hardware modules in the fleet:

| Display Module | Resolution | ESPHome Driver & Dimensions | Example Nodes | MCU Target | Refresh Type | Color Palette |
|---|---|---|---|---|---|---|
| **WeAct 1.54" B&W** | 200 × 200 | `model: SSD1683`<br>`dimensions: {width: 200, height: 200}` | `uranus`, `alichino`, `venus`, `leviathan` | ESP32-C6 / ESP32-C3 | Partial (`full_update_every: 30`, 5-min clock) | `BLACK`, `WHITE` |
| **WeAct 2.13" B&W** | 122 × 250 | `model: ssd1683`<br>`dimensions: {width: 122, height: 250}` | `pluto`, `asmodeus`, `scarmiglione` | ESP32-C3 / ESP32-C6 | Partial (`full_update_every: 30`, 5-min clock) | `BLACK`, `WHITE` |
| **WeAct 2.13" BWR** | 122 × 250 | `model: WeAct-2.13in-3c` | `neptun`, `beelzebub` | ESP32-C3 / ESP32-C6 | **Full Refresh Only** | `BLACK`, `WHITE`, `RED` |
| **WeAct 2.9" B&W** | 128 × 296 | `model: ssd1683`<br>`dimensions: {width: 128, height: 296}` | `jupiter`, `ciriatto` | ESP32-C6 | Partial (`full_update_every: 30`, 5-min clock) | `BLACK`, `WHITE` |
| **WeAct 2.9" BWR** | 128 × 296 | `model: WeAct-2.9in-3c` | `saturn`, `calcabrina` | ESP32-C6 | **Full Refresh Only** | `BLACK`, `WHITE`, `RED` |
| **WeAct 4.2" B&W** | 400 × 300 | `model: GooDisplay-GDEY042T81-4.2` | `cagnazzo`, `moon` | ESP32-C6 | Partial (`full_update_every: 30`, 5-min clock) | `BLACK`, `WHITE` |
| **Waveshare 5.65" 7C** | 600 × 448 | `model: INKPLATE6COLOR`<br>`dimensions: {width: 600, height: 448}` | `mars` | ESP32-S3 (16-8) | **Full Refresh Only** (ACeP) | 7 Colors (White, Black, Red, Orange, Yellow, Green, Blue) |

---

## Refresh Modes: Partial vs Full

### 1. Monochrome Panels (Black & White)
* **Partial Refresh Enabled**: Use `model: ssd1683` with explicit `dimensions`.
* **Ghosting Clearing**: Set `full_update_every: 30`. This instructs the controller to execute 29 fast partial updates followed by 1 full screen inversion to wipe microscopic pigment ghosting.
* **Update Speed**: Fast partial refresh finishes in **< 0.3 seconds** with no screen flashing, making it ideal for desk clocks and living rooms.
* **Configuration Snippet**:
```yaml
display:
  - platform: waveshare_epaper
    id: my_display
    cs_pin: GPIO07
    dc_pin: GPIO01
    busy_pin: GPIO03
    reset_pin: GPIO02
    model: ssd1683
    dimensions:
      width: 122
      height: 250
    full_update_every: 30
    rotation: 90
    lambda: |-
      // Render clock and sensor UI
```

### 2. Tri-Color Panels (Black, White, Red / Yellow)
* **Full Refresh Mandatory**: Due to physical electrophoretic differences (larger red pigment particles require higher voltage pulses and alternating polarity cycles), 3-color panels cannot perform fast partial refresh without severe color distortion.
* **Update Duration**: Full refresh takes approximately **15 to 25 seconds** and exhibits several screen inversions during cycle completion.
* **Fleet Recommendation**: Use tri-color panels (`neptun`, `saturn`, `beelzebub`) for status displays or boards that update infrequently (e.g. 15 to 30 minutes), and monochrome panels for 5-minute clocks.

---

## Ambient Light Gating (Night Mode)

To prevent e-paper displays from refreshing in dark bedrooms—which can generate faint audible coil whine or visual distractions—the firmware monitors ambient lux using the TEMT6000 phototransistor:

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
                # Only refresh if ambient light is greater than 1.0 Lux
                - lambda: return id(my_light).state > 1.0f;
              then:
                - script.execute: refresh_screen
```

When room lights are switched on in the morning (`my_light > 1.0 lx`), the next 5-minute tick immediately updates the screen with current time and weather forecast.

---

## Embedded Typography & Icon Fonts

The repository [`48broadbent/broadbent`](https://gitlab.com/48broadbent/broadbent) bundles true-type font resources loaded via `fonts/fonts.yaml`:

```yaml
font:
  - file: "fonts/DejaVuSans.ttf"
    id: font_time
    size: 42
  - file: "fonts/Hack-Bold.ttf"
    id: font_sensor
    size: 16
  - file: "fonts/droid.ttf"
    id: font_small
    size: 12
  - file: "fonts/materialdesignicons-webfont.ttf"
    id: font_icons
    size: 24
    glyphs:
      - "\U000F0594"  # Weather sunny
      - "\U000F0599"  # Weather cloudy
      - "\U000F0597"  # Weather rainy
      - "\U000F0596"  # Weather pouring
      - "\U000F0598"  # Weather snowy
      - "\U000F0592"  # Weather lightning
```

Weather icons and forecast codes received over MQTT JSON are dynamically mapped into Unicode glyph strings and rendered directly on the e-paper canvas.

