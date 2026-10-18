# 8×6 Mini Indoor Sensor Board (ESP32-C6)

The **8×6 Mini Sensor Carrier** (`m-lego/sensor-1.54`) is an ultra-compact, high-efficiency sensor node specifically engineered for the **ESP32-C6 SuperMini** and a **1.54" E-Paper** display. Sized to an 8×6 LEGO baseplate (`64 mm × 48 mm`), it brings modern Wi-Fi 6, Thread, and Zigbee wireless capabilities to home environmental telemetry.

---

## Key Hardware Features

<div class="grid cards" markdown>

-   :material-microchip: **ESP32-C6 SuperMini**

    ---

    * Single-core 32-bit RISC-V processor clocked up to 160 MHz.
    * 2.4 GHz Wi-Fi 6 (802.11ax) + Bluetooth 5 (LE) + IEEE 802.15.4 (Zigbee 3.0 / Thread).
    * Ultra-compact form factor with USB-C for flashing and continuous power.
    * LCSC Part Number: `C5364646`.

-   :material-monitor-dashboard: **WeAct 1.54" E-Paper**

    ---

    * 200 × 200 pixel square e-ink screen (`SSD1680` / `SSD1681` controller).
    * Fits seamlessly inside the 8-stud width with zero overhang.
    * Crisp black and white output with sub-second partial refresh capabilities.

-   :material-molecule: **Bosch BME680 (SPI)**

    ---

    * Measures temperature, barometric pressure, relative humidity, and VOC gas resistance.
    * Dedicated hardware SPI bus connection prevents I2C address lockouts.

-   :material-white-balance-sunny: **TEMT6000 Light Sensor**

    ---

    * Analog phototransistor measuring ambient illumination.
    * Controls night-mode sleep and suppresses screen refresh in dark rooms.

</div>

---

## Production Bill of Materials (BOM)

Directly sourced from [`production/bom.csv`](https://gitlab.com/m-lego/sensor-1.54/-/raw/main/production/bom.csv):

| Designator | Footprint | Qty | Value / Component | LCSC Part # | Notes |
|---|---|:---:|---|---|---|
| **DS1** | `weact-eink-154` | 1 | eink-ssd1680 (1.54") | — | WeAct 1.54" E-Paper display module |
| **H1** | `LegoHole_8x6u_4875` | 1 | MountingHole | — | 4× corner 4.8 mm stud-clearance holes |
| **JP1 – JP6** | `SolderJumper-2_P1.3mm` | 6 | Jumper_2_Open | — | Open triangle pads (`1.0 × 1.5 mm`) |
| **R1, R2** | `R-dual` | 2 | 4.7 kΩ | — | Surface-mount pull-up resistors |
| **U1** | `bme680_spi` | 1 | BME680 (T / hPa / % / VOC) | — | 4-in-1 SPI environmental sensor |
| **U2** | `ESP32-C6-SuperMini_TH` | 1 | ESP32-C6-SuperMini | **C5364646** | 160MHz RISC-V, Wi-Fi 6, BLE 5, Zigbee |
| **U5** | `temt6000` | 1 | TEMT6000 | — | Analog ambient light phototransistor |

---

## Solder Jumpers (JP1–JP6)

The board incorporates six configurable solder jumpers (`JP1` through `JP6`) to give makers complete flexibility over bus assignments and display pin routing:

| Jumper | Function | Default State | Custom Option |
|---|---|---|---|
| **JP1** | Display `CS` (Chip Select) | GPIO 20 | Reroute to secondary GPIO if daisy-chaining SPI devices |
| **JP2** | Display `DC` (Data/Command) | GPIO 21 | Standard WeAct pin mapping |
| **JP3** | Display `RST` (Reset) | GPIO 22 | Hardware reset line |
| **JP4** | Display `BUSY` (Busy state) | GPIO 23 | Active-low busy notification line |
| **JP5** | BME680 `CS` line | GPIO 19 | Dedicated SPI chip select for sensor |
| **JP6** | Light Sensor Output | GPIO 0 (ADC1_CH0) | Analog voltage feedback to ESP32 ADC |

---

## Production Files in Repository

The [`m-lego/sensor-1.54`](https://gitlab.com/m-lego/sensor-1.54) repository contains complete KiCad 8 source files ready for fabrication:

```
├── footprints/
│   ├── ESP32-C3_SUPERMINI.kicad_mod
│   ├── ESP32-C6-SuperMini_TH.kicad_mod
│   ├── LegoHole_8x6u_4875.kicad_mod
│   ├── bme680_spi.kicad_mod
│   ├── temt6000.kicad_mod
│   └── weact-eink-154.kicad_mod
├── multi-sensor-1.54.kicad_pcb      # KiCad PCB layout
├── multi-sensor-1.54.kicad_sch      # KiCad schematic diagram
└── production/
    ├── bom.csv                      # Complete LCSC BOM
    └── designators.csv              # Component placement reference
```

> [!TIP]
> **Fabrication Tip:** When ordering from JLCPCB or PCBWay, select **FR-4 1.6 mm** board thickness and **black solder mask** with **white silkscreen** for an elegant finish that matches dark LEGO bricks.

