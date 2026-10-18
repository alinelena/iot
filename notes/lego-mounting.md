# LEGO Mounting & Enclosure System

A distinctive hallmark of the `m-lego` hardware philosophy is using LEGO building elements as precision structural enclosures. Rather than relying on custom 3D-printed plastic cases that warp, fracture, or need frequent reprints, the sensor boards are engineered to standard LEGO mechanical tolerances.

---

## Grid Geometry & Hole Footprints

Standard LEGO bricks use an exact metric grid:

* **Stud Pitch**: `8.0 mm` center-to-center in both X and Y directions.
* **Stud Diameter**: `4.8 mm` nominal (`4.80 mm – 4.85 mm`).
* **Stud Height**: `1.7 mm`.
* **Plate Thickness**: `3.2 mm` (one-third the height of a standard brick).

```
   |<--- 8.0 mm --->|
   +----------------+
   |    (4.8 mm)    |
---+     [Stud]     +---
```

### The `LegoHole_4875` Footprint
In KiCad, the mounting holes are defined with the custom footprint `LegoHole_12x6u_4875.kicad_mod` (and `8x6u` variant):
* **Hole Diameter**: `4.875 mm` (plated or non-plated through-hole).
* **Clearance**: The extra `0.075 mm` diameter allows the PCB to slide smoothly onto LEGO studs without binding or scratching the plastic, while retaining tight friction to prevent lateral shifting.

---

## Available 3D CAD Models (STEP)

The [`m-lego/sensor`](https://gitlab.com/m-lego/sensor) repository provides exact STEP models in the `3d/` directory for full 3D assembly verification:

| Model File | Description |
|---|---|
| `ESP32-C3 supermini v5.step` | ESP32-C3 SuperMini MCU with USB-C connector |
| `WeAct-EpaperModule-2.13 Board 3D.step` | WeAct 2.13" E-Paper display module |
| `WeAct-EpaperModule-1.54 Board 3D.step` | WeAct 1.54" E-Paper display module |
| `Waveshare 1.54 E ink - Display Flat Mount.stp` | Flat display mount adapter |
| `Waveshare 1.54 E ink - Display Flush Folded.stp` | Flush folded display mount |
| `Waveshare 2.13 (D) E-ink - Reverse Mount.stp` | Reverse-mount display configuration |
| `GY-BME280.STEP` / `CJMCU-680.STEP` | Bosch climate breakout board geometry |
| `Gy -SGP30.step` / `GY-SGP40.step` | Sensirion air quality sensor modules |
| `TEMT6000 v2.step` | Ambient light sensor carrier |
| `hexagonal_spacer_MF_M2.5_H09_HEX5.step` | 9 mm M2.5 nylon spacer for display elevation |
| `hexagonal_spacer_MF_M2.5_H11_HEX5.step` | 11 mm M2.5 nylon spacer |

---

## Enclosure Construction Guide

```
+-------------------------------------------------------------+
|                     E-Paper Display                         |
+-------------------------------------------------------------+
  | (9mm Standoffs)                                        |
+-------------------------------------------------------------+
|                      Sensor PCB                             |
+-------------------------------------------------------------+
  | (4.875mm Stud Holes)                                   |
+=============================================================+
|             Baseplate: 12x6 or 8x6 LEGO Plate               |
+=============================================================+
```

### 1. Base Layer
Start with a genuine 12×6 LEGO plate (LEGO part `3028` / `4875`) or an 8×6 plate for the mini board. Ensure the top surface is clean.

### 2. PCB Placement
Press the PCB directly onto the base studs. The corner holes align with the outer studs of the grid. If desired, standard 1×1 round tiles or bushings can be pressed over the studs above the PCB for a lock fit.

### 3. Display Standoffs
To prevent the e-paper ribbon cable from straining against the PCB components, install two **9 mm or 11 mm M2.5 nylon hexagonal spacers** into the designated mounting holes. The e-paper display rests on these standoffs with double-sided tape or M2.5 screws.

### 4. Thermal Insulation Advantage
Unlike tightly sealed commercial plastic enclosures where the Wi-Fi MCU's heat warms the casing and inflates temperature readings by 2°C to 5°C, the LEGO open-stud framework maintains a **natural convection boundary**:
* Ambient air flows freely underneath the carrier.
* The temperature sensor is spaced `35 mm` away from the ESP32 heat sink area.
* Eliminates the need for aggressive software temperature offset compensations.

