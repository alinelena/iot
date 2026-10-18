# Open IoT & Smart Home Ecosystem Website

This repository contains the official documentation website for our open-source IoT, sensor carrier, and smart home automation projects, served at [iot.elena.re](https://iot.elena.re).

The site architecture and design directly mirror [`mlego.elena.re`](https://mlego.elena.re) ([`alinelena/mlego`](https://github.com/alinelena/mlego)): custom Python static site generator using Jinja2, Markdown, and PyYAML with Bootstrap 5.3 dark theme, parallax bands, floating corner navigation, quick-jump pills, instant catalog search, side-by-side specs comparison, and interactive Mermaid diagrams.

---

## Projects Documented

* **[m-lego / sensor](https://gitlab.com/m-lego/sensor)**: Custom 12×6 LEGO-mountable multisensor carrier board (rev 1, 2, 3) supporting ESP32-C3 SuperMini, BME280/BME680, SGP30/SGP40, TEMT6000, and 2.13"/1.54" WeAct E-Paper displays.
* **[m-lego / sensor-1.54](https://gitlab.com/m-lego/sensor-1.54)**: Ultra-compact 8×6 LEGO sensor carrier board with ESP32-C6 SuperMini (Wi-Fi 6, Thread, Zigbee), BME680 SPI, and 1.54" E-Paper display.
* **[48broadbent / broadbent](https://gitlab.com/48broadbent/broadbent)**: Fleet of 41 production ESPHome node configurations, e-paper display drivers, climate telemetry, and holiday lighting controllers.
* **[48broadbent / homeassistant](https://gitlab.com/48broadbent/homeassistant) & [ha-blueprints](https://gitlab.com/48broadbent/ha-blueprints)**: Central Home Assistant automation hub and reusable blueprints for humidity extraction, ambient motion lighting, night mode coordination, and Zigbee remotes.

---

## Architecture & Directory Structure

```text
├── assets/
│   ├── css/style.css         # Custom dark theme, parallax, and UI styling
│   └── js/app.js             # Corner menu toggle, search filter, and lightbox
├── data/
│   ├── site.yml              # Global metadata, nav menus, parallax dividers
│   ├── about.yml             # Project stats and manifesto
│   ├── hardware.yml          # Hardware carriers catalog
│   ├── esphome.yml           # ESPHome fleet catalog & guides
│   ├── homeassistant.yml     # Home Assistant hub and blueprints
│   ├── guides.yml            # Assembly, pinout, and flashing guides
│   └── specs.yml             # Full hardware lineup specifications
├── notes/                    # Core technical markdown content
├── pics/                     # Hardware schematics, renders, photos, and icons
├── templates/                # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── catalog.html
│   ├── detail.html
│   ├── specs.html
│   └── partials/
│       ├── header.html
│       └── footer.html
└── tools/
    └── build.py              # Static site builder (clean markdown, render HTML)
```

---

## Local Development & Build

### 1. Requirements
Python 3.10+ with `pyyaml`, `markdown`, and `jinja2`.

### 2. Build the Static Site
```bash
python3 tools/build.py --outdir _site
```
Or via `uv`:
```bash
uv run --python 3.12 --with-requirements requirements.txt tools/build.py --outdir _site
```

The compiled static website will be placed into the `_site/` directory, ready to serve.

### 3. Local Preview
```bash
python3 -m http.server 8000 --directory _site
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Automated Deployment

Deployments to GitHub Pages ([iot.elena.re](https://iot.elena.re)) are automated via GitHub Actions on every push to `main` using `.github/workflows/ci.yml`.

---

## License

Documentation content and hardware notes: Ⓒ 2020–2026 Alin M. Elena. Open-source hardware and firmware under respective AGPL-3.0 / MIT licenses.
