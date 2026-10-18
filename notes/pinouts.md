# Hardware Pinout Reference

This reference documents the hardware pin assignments across the microcontroller targets deployed in the fleet.

---

## ESP32-C3 SuperMini (12×6 Carrier)

The ESP32-C3 is a single-core RISC-V 32-bit MCU with 400KB SRAM and 4MB Flash.

| Function | GPIO Pin | Bus / Signal | Description |
|---|---|---|---|
| **Display SPI SCK** | `GPIO4` | Hardware SPI Bus A | Clock signal to WeAct e-paper |
| **Display SPI MOSI** | `GPIO6` | Hardware SPI Bus A | Master-Out-Slave-In data to display |
| **Display SPI MISO** | `GPIO5` | Hardware SPI Bus A | Master-In-Slave-Out (optional) |
| **Display CS** | `GPIO7` | Chip Select | Active-low display enable |
| **Display DC** | `GPIO1` | Data / Command | Selects register command vs data |
| **Display RST** | `GPIO2` | Hardware Reset | Active-low display reset |
| **Display BUSY** | `GPIO3` | Status Line | Busy signal from SSD1680 controller |
| **Sensor I2C SDA** | `GPIO8` | Hardware I2C Bus B | Data line for BME280 & SGP40 |
| **Sensor I2C SCL** | `GPIO9` | Hardware I2C Bus B | Clock line for BME280 & SGP40 |
| **Ambient Light ADC** | `GPIO0` | ADC1_CH0 | Analog voltage from TEMT6000 phototransistor |

---

## ESP32-C6 SuperMini (8×6 Mini Carrier)

The ESP32-C6 features Wi-Fi 6, Bluetooth 5.3, Zigbee, and Thread.

| Function | GPIO Pin | Bus / Signal | Description |
|---|---|---|---|
| **Display SPI SCK** | `GPIO6` | Hardware SPI Bus | Clock signal to 1.54" e-paper |
| **Display SPI MOSI** | `GPIO7` | Hardware SPI Bus | Master-Out-Slave-In data |
| **Display SPI MISO** | `GPIO2` | Hardware SPI Bus | Master-In-Slave-Out data |
| **Display CS** | `GPIO20` | Chip Select | Active-low display select (`alichino`, `leviathan`) |
| **Display DC** | `GPIO21` | Data / Command | Mode select line |
| **Display RST** | `GPIO22` | Hardware Reset | Display reset |
| **Display BUSY** | `GPIO23` | Status Line | Busy state |
| **BME680 SPI CS** | `GPIO19` | Chip Select | Dedicated SPI select line for BME680 |
| **Ambient Light ADC** | `GPIO0` | ADC1_CH0 | Analog voltage from TEMT6000 |

---

## ESP8266 & D1 Mini (Dust & Climate Nodes)

Used on nodes such as `dust-front`, `dust-kitchen`, `kitchen`, and `garden`:

| Function | Pin Name | Physical GPIO | Hardware Role |
|---|---|---|---|
| **Dust Sensor RX** | `D2` | `GPIO4` | Software/Hardware UART RX from PM1006 dust sensor (9600 baud) |
| **Dust Sensor TX** | `D1` | `GPIO5` | UART TX (optional configuration) |
| **Climate I2C SDA** | `D3` | `GPIO0` | I2C Data line for external BME280 weather breakout |
| **Climate I2C SCL** | `D4` | `GPIO2` | I2C Clock line for BME280 |
| **Status LED** | `D0` | `GPIO16` | On-board activity / Wi-Fi indicator |

---

## M5Stack Atom Matrix (ESP32-PICO)

Used in `atom_matrix.yaml` (`gutenberg`):

| Peripheral | GPIO Pin | Notes |
|---|---|---|
| **5×5 RGB LED Matrix** | `GPIO27` | FastLED NeoPixel / WS2812 driver rail |
| **Onboard Button** | `GPIO39` | Front panel tactile momentary switch |
| **Internal SHT30 SDA** | `GPIO25` | Hardware I2C data |
| **Internal SHT30 SCL** | `GPIO21` | Hardware I2C clock |
| **IR Transmitter** | `GPIO12` | Infrared emitter LED |

