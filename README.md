# IoT Projects & Home Automation Website

This repository contains the official documentation website for our open-source IoT, sensor carrier, and smart home automation projects.

The site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and [glightbox](https://github.com/blueswen/mkdocs-glightbox), adopting the architectural documentation approach and visual aesthetic of [`alinelena/mlego`](https://github.com/alinelena/mlego).

---

## Projects Documented

* **[m-lego / sensor](https://gitlab.com/m-lego/sensor)**: Custom 12×6 LEGO-mountable multisensor carrier board (rev 1, 2, 3) supporting ESP32-C3 SuperMini, BME280/BME680, SGP30/SGP40, TEMT6000, and 2.13"/1.54" WeAct E-Paper displays.
* **[m-lego / sensor-1.54](https://gitlab.com/m-lego/sensor-1.54)**: Ultra-compact 8×6 LEGO sensor carrier board with ESP32-C6 SuperMini (Wi-Fi 6, Thread, Zigbee), BME680 SPI, and 1.54" E-Paper display.
* **[48broadbent / broadbent](https://gitlab.com/48broadbent/broadbent)**: Fleet of 40+ production ESPHome node configurations, e-paper display drivers, climate telemetry, and holiday lighting controllers.
* **[48broadbent / homeassistant](https://gitlab.com/48broadbent/homeassistant) & [ha-blueprints](https://gitlab.com/48broadbent/ha-blueprints)**: Central Home Assistant automation hub and reusable blueprints for humidity extraction, ambient motion lighting, night mode coordination, and Zigbee remotes.

---

## Local Development & Preview

### 1. Requirements
Ensure [`uv`](https://github.com/astral-sh/uv) and Python 3.10+ are available on your system.

### 2. Setup Virtual Environment
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 3. Run Development Server
```bash
uv run mkdocs serve
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser with hot reload.

### 4. Build Production Site
```bash
uv run mkdocs build --clean --strict
```
The compiled static website will be placed into the `public/` directory.

---

## Automated Deployment

Deployments to GitHub Pages are fully automated via GitHub Actions on every push to `main` using `.github/workflows/ci.yml`.

---

## License

Documentation content and hardware notes: Ⓒ 2020–2026 Alin M. Elena. Open-source hardware and firmware under respective AGPL-3.0 / MIT licenses.
