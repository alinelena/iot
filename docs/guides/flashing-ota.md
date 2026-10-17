# Flashing, OTA Updates & Recovery

This guide covers initial USB provisioning, subsequent wireless Over-the-Air (OTA) firmware deployments, and captive portal recovery procedures across the ESPHome fleet.

---

## 1. Initial USB Provisioning

Before a node can communicate wirelessly, its initial firmware image must be compiled and flashed over USB.

### Prerequisites
Ensure your local Python environment or ESPHome dashboard is installed. In this workspace:
```bash
uv pip install esphome
```

### Entering Bootloader Mode on SuperMini Boards
Both the ESP32-C3 SuperMini and ESP32-C6 SuperMini feature native USB-CDC interfaces:
1. Connect the board to your computer using a quality data-capable USB-C cable.
2. If the serial device does not appear automatically:
    * Press and hold the **BOOT** button on the back of the SuperMini.
    * Click and release the **RESET** button.
    * Release the **BOOT** button.
3. The board will enumerate as `/dev/ttyACM0` or `/dev/ttyUSB0` on Linux.

### Compiling and Flashing
Run the compilation command specifying the node file:
```bash
esphome run pluto.yaml --device /dev/ttyACM0
```
ESPHome will download the required framework, compile the Arduino core and custom C++ lambdas, and flash the partition table, bootloader, and application binary.

---

## 2. Wireless Over-the-Air (OTA) Deployments

Once provisioned with initial Wi-Fi credentials, physical USB access is no longer required. All subsequent configuration updates can be compiled and deployed over the air:

```bash
esphome run pluto.yaml
```

When run without the `--device` flag, ESPHome automatically discovers the node on the local subnet via mDNS (`pluto.local`) and transfers the encrypted firmware payload over port `8266` or `3232`.

### OTA Encryption
All fleet nodes define secure OTA authentication:
```yaml
ota:
  - platform: esphome
    password: !secret ota_password
```
This ensures unauthorized devices on the network cannot push modified firmware to your nodes.

---

## 3. Captive Portal Emergency Recovery

If a node cannot connect to the configured Wi-Fi network (for example, if you replace your router, update the SSID, or relocate the sensor to a different building), it activates its built-in **Captive Portal**:

```yaml
wifi:
  ssid: !secret wifi
  password: !secret wifi_password
  ap:
    ssid: ${devicename} Fallback Hotspot
    password: !secret cap_password

captive_portal:
```

### Recovery Procedure
1. After 60 seconds of failed Wi-Fi connection attempts, the node spins up a standalone Wi-Fi Access Point named `${devicename} Fallback Hotspot` (e.g. `pluto Fallback Hotspot`).
2. Connect to this hotspot from your phone, laptop, or tablet using the fallback password defined in `!secret cap_password`.
3. A captive portal page will automatically open (or navigate to `http://192.168.4.1` in your browser).
4. Select your new local Wi-Fi network, enter the password, and click **Save**.
5. The node restarts and joins the new network immediately.

---

## 4. Managing Secrets

To prevent sensitive Wi-Fi credentials, MQTT passwords, and API keys from leaking into version control, the repository [`48broadbent/broadbent`](https://gitlab.com/48broadbent/broadbent) uses a template pattern:

1. Copy `secrets.yaml.template` to `secrets.yaml`:
   ```bash
   cp secrets.yaml.template secrets.yaml
   ```
2. Populate the required keys:
   ```yaml
   wifi: "YourHomeWiFiSSID"
   wifi_password: "YourStrongPassword"
   cap_password: "EmergencyFallbackPassword123"
   api_key: "GeneratedESPHomeNativeAPIEncryptionKey"
   ota_password: "YourOTAPassword"
   mqtt_broker: "192.168.1.50"
   ```
3. `secrets.yaml` is listed in `.gitignore` and is never committed to public repositories.

