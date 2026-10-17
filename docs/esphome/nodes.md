# ESPHome Node Catalog

The [`48broadbent/broadbent`](https://gitlab.com/48broadbent/broadbent) repository maintains configurations for **41 production ESPHome devices** distributed throughout the home, garden, and exterior perimeter.

Nodes are grouped into distinct functional categories below.

---

## E-Paper Sensor Clocks

These nodes combine low-power E-Paper displays with precision climate and ambient light sensors to provide glanceable desktop and wall timepieces with 3-day weather forecasting:

| Node Name | Configuration File | Target Board | Display Module | Sensors Included |
|---|---|---|---|---|
| **Pluto** | `pluto.yaml` | ESP32-C3 DevKitM-1 | WeAct 2.13" B&W (SSD1683) | BME280, SGP40, TEMT6000 |
| **Venus** | `venus.yaml` | ESP32-C3 DevKitM-1 | WeAct 1.54" B&W (SSD1683) | BME280, SGP40, TEMT6000 |
| **Neptun** | `neptun.yaml` | ESP32-C3 DevKitM-1 | WeAct 2.13" BWR (3-Color) | BME280, BME680, TEMT6000 |
| **Saturn** | `saturn.yaml` | ESP32-C6 DevKitM-1 | WeAct 2.9" BWR (3-Color) | BME280, BME680, TEMT6000 |
| **Jupiter** | `jupiter.yaml` | ESP32-C6 DevKitM-1 | WeAct 2.9" B&W (SSD1683) | BME280, BME680, TEMT6000 |
| **Uranus** | `uranus.yaml` | ESP32-C6 DevKitM-1 | WeAct 1.54" B&W (SSD1683) | BME280, BME680, TEMT6000 |
| **Moon** | `moon.yaml` | ESP32-C6 DevKitM-1 | GooDisplay 4.2" B&W (GDEY042T81) | BME280, BME680, TEMT6000 |
| **Mars** | `mars.yaml` | ESP32-S3 DevKitC-1 | Waveshare 5.65" (Inkplate 7-Color ACeP) | BME280 Climate Sensor |
| **Alichino** | `alichino.yaml` | ESP32-C6 DevKitM-1 | WeAct 1.54" B&W (SSD1683) | BME280, BME680, TEMT6000 |
| **Calcabrina** | `calcabrina.yaml` | ESP32-C6 DevKitM-1 | WeAct 2.9" BWR (3-Color) | BME280, BME680, TEMT6000 |
| **Ciriatto** | `ciriatto.yaml` | ESP32-C6 DevKitM-1 | WeAct 2.9" B&W (SSD1683) | BME280, BME680, TEMT6000 |
| **Scarmiglione**| `scarmiglione.yaml` | ESP32-C6 DevKitM-1 | WeAct 2.13" B&W (SSD1683) | BME280, BME680, TEMT6000 |
| **Malacoda** | `malacoda.yaml` | ESP32-C6 DevKitM-1 | WeAct 1.54" B&W (SSD1683) | BME280, BME680, TEMT6000 |
| **Beelzebub** | `beelzebub.yaml` | ESP32-C6 DevKitM-1 | WeAct 2.13" BWR (3-Color) | BME280, BME680, TEMT6000 |
| **Asmodeus** | `asmodeus.yaml` | ESP32-C6 DevKitM-1 | WeAct 2.13" B&W (SSD1683) | BME280, BME680, TEMT6000 |
| **Leviathan** | `leviathan.yaml` | ESP32-C6 DevKitC-1 | WeAct 1.54" B&W (SSD1683) | BME280, BME680, TEMT6000 |

---

## Room Climate & Environmental Monitors

Headless telemetry nodes monitoring microclimates across rooms and outdoor areas:

| Node Name | Configuration File | Target Board | Primary Sensor | Description |
|---|---|---|---|---|
| **Backroom** | `backroom.yaml` | ESP32-C3 DevKitM-1 | BME280 + SGP40 | Rear living area climate & air quality |
| **Frontroom** | `frontroom.yaml` | ESP32-C3 DevKitM-1 | BME280 | Front living room temperature & pressure |
| **Kitchen** | `kitchen.yaml` | NodeMCU ESP8266 | BME280 | Kitchen cooking area humidity & temperature |
| **Middleroom** | `middleroom.yaml` | ESP32-C3 DevKitM-1 | BME280 + SGP40 | Hallway climate & air quality tracking |
| **Office** | `office.yaml` | ESP32-C3 DevKitM-1 | BME280 | Workstation temperature & air pressure |
| **Small Bedroom** | `smallbedroom.yaml` | ESP32-C3 DevKitM-1 | BME280 + SGP40 | Bedroom climate & night air quality |
| **Garden** | `garden.yaml` | NodeMCU ESP8266 | BME280 (Weatherproof) | Outdoor ambient weather station |

---

## Particulate & Dust Monitors

Dedicated air quality units utilizing laser/optical particulate sensors:

| Node Name | Configuration File | Target Board | Sensor Model | Monitoring Scope |
|---|---|---|---|---|
| **Dust-Front** | `dust-front.yaml` | D1 Mini (ESP8266) | PM1006 / PMSX003 | Front entrance ambient PM2.5 dust |
| **Dust-Kitchen** | `dust-kitchen.yaml` | D1 Mini (ESP8266) | PM1006 / PMSX003 | Cooking aerosols & fine particulate matter |
| **Dust-Up** | `dust-up.yaml` | D1 Mini (ESP8266) | PM1006 / PMSX003 | Upper floor hallway dust & pollen levels |

---

## Smart Lighting & Matrix Displays

Controllers for ambient LED installations, holiday lights, and matrix panels:

| Node Name | Configuration File | Target Board | Hardware / Lights | Capabilities |
|---|---|---|---|---|
| **Gutenberg** | `atom_matrix.yaml` | M5Stack Atom Matrix (ESP32-PICO) | 5×5 RGB LED Matrix + SHT30 | Real-time scrolling text, alerts, climate |
| **Tree** | `tree.yaml` | ESP-01 (1MB) | Addressable LED Strip | Holiday tree lighting controller |
| **Tree 1** | `tree1.yaml` / `light_rgb.yaml` | NodeMCU ESP8266 | FastLED / NeoPixel | Primary living room lighting tree |
| **Tree 2** | `tree2.yaml` / `light_rgb_2.yaml` | NodeMCU-32S / ESP32 | FastLED / NeoPixel | Secondary synchronized tree |
| **Tree 3** | `tree3.yaml` | NodeMCU ESP8266 | FastLED / NeoPixel | Accent tree lighting strip |
| **SP501E (Tree 4)** | `sp501e.yaml` | ESP8285 (SP501E) | Commercial Wi-Fi SPI Strip | High-output SPI LED controller running ESPHome |
| **Rainbow** | `rainbow.yaml` | ESP-01 (1MB) | FastLED Strip | Dynamic rainbow color wave effects |

---

## Specialized Infrastructure Nodes

| Node Name | Configuration File | Target Board | Role & Attached Peripherals |
|---|---|---|---|
| **OLED** | `oled.yaml` | ESP32-C3 DevKitM-1 | High-contrast SH1106 128×64 monochrome OLED bedside display |
| **Light Level** | `light_level.yaml` | NodeMCU ESP8266 | Dedicated TEMT6000 light level station (`lbed`) |
| **Lamp Middle** | `lamp_middle.yaml` | ESP8285 Smart Plug | Smart lamp relay & power switching |
| **Light Office**| `light_office.yaml` | ESP8285 Smart Plug | Desk task lamp switching & automation control |
| **Mammon** | `mammon.yaml` | ESP32-C6 DevKitM-1 | Auxiliary network beacon and lighting relay |

