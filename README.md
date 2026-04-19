#  DUT-E Fuel Sensor Calibration Tool

This project was built to calibrate the **DUT-E 232** and **DUT-E 485** fuel level sensors. You only need to input your tank measurements and sensor size — the program automatically generates the calibration CSV table ready to be loaded into the **Service DUT-E** software.

---

##  Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Calibration Process](#calibration-process)
- [Tank Types Supported](#tank-types-supported)
- [Output](#output)
- [Contact](#contact)
- [Support](#support)

---

## Overview

The DUT-E fuel level sensor requires a calibration table that maps millimeter readings (sensor level) to liters (volume). Calculating this table manually is tedious and error-prone. This tool automates the entire process:

1. You input the tank dimensions and sensor length.
2. The program calculates the total volume.
3. It generates a 30-row CSV calibration table (Level mm → Volume L).
4. You load the CSV into the **Service DUT-E** software under the **Calibration Table** section.

---

## Requirements

- Python 3.x
- [`cowsay`](https://pypi.org/project/cowsay/) library

Install dependencies:

```bash
pip install cowsay
```

---

## Installation

```bash
git clone https://github.com/your-username/dut-e-calibration-tool.git
cd dut-e-calibration-tool
pip install cowsay
python main.py
```

---

## Usage

Run the program:

```bash
python main.py
```

Follow the interactive menu:

```
Menú Principal:
1. Calcular Volumen de un Tanque
2. Salir
```

Select option **1**, then choose your tank type:

```
Seleccione el tipo de cálculo de volumen:
1. Tanque Cuadrado
2. Tanque Cilíndrico
3. Tanque Ovalado
4. Salir
```

Enter the requested dimensions **(in centimeters)** and the sensor size **(in millimeters)**, then provide a filename for the output CSV (e.g., `calibration.csv`).

---

## How It Works

### Volume Calculation

Depending on the tank type, the program applies the corresponding formula:

| Tank Type   | Formula |
|-------------|---------|
| Rectangular | `V = Length × Width × Height` |
| Cylindrical | `V = π × r² × Height` |
| Oval        | `V = π × r_avg² × Height` (where r_avg is the average of both radii) |

All dimensions entered in **centimeters** are converted to **millimeters** internally before calculation, and the final volume is converted to **liters**.

### Calibration Table Generation

The table contains **30 rows**:
- Row 1 is always `0 mm → 0 L` (empty tank baseline).
- The remaining 29 rows are evenly distributed across the sensor's length and the tank's total volume.

**Level (mm)** is calculated as:
```
step = sensor_length_mm / 29
row_n_mm = n × step
```

**Volume (L)** is calculated as:
```
step = total_liters / 29
row_n_L = n × step
```

This produces a linear calibration curve — when entered correctly into the Service DUT-E software, the graph should display a straight diagonal line.

---

## Calibration Process

After generating the CSV, follow these steps in the **Service DUT-E** software:

1. **Set sensor length**: Go to `Settings → Calibration` and enter the sensor length.
   >  Sensor length = tank height in mm **minus 20 mm**  
   > *Example: Tank height 1230 mm → Sensor length = 1210 mm*

2. **Load the calibration table**: Go to `Calibration Table → Read from file` and select your generated CSV.

3. **Set output unit**: Go to `Output message` and select **Volume (L)**.

4. **Set thermal compensation**: Go to `Thermal compensation` and set the fuel coefficient (default: `0.084`).

5. **Set reference points**: Use the **Set empty** and **Set full** buttons to define the empty and full levels.

6. **Verify the graph**: The calibration curve should form a straight diagonal line. If it does, the calibration is correct.

---

## Tank Types Supported

###  Rectangular Tank
Input: Length, Width, Height (cm) + Sensor size (mm)

###  Cylindrical Tank
Input: Diameter, Height (cm) + Sensor size (mm)
> The program calculates the radius automatically (`r = diameter / 2`).

###  Oval Tank
Input: Diameter A, Diameter B, Height (cm) + Sensor size (mm)
> The program averages both radii for the volume calculation.

---

## Output

The generated CSV file contains two columns:

| Milimetros | Litros |
|-----------|--------|
| 0.0       | 0.0    |
| 41.72     | 19.9   |
| 83.45     | 39.8   |
| ...       | ...    |
| 1210.0    | 579.9  |

This file can be directly loaded into the **Service DUT-E v3.26+** software via `Calibration Table → Read from file`.

---

## Hardware Used

| Component | Model |
|-----------|-------|
| Fuel Level Sensor | DUT-E 232 / DUT-E 485 |
| GPS Tracker | Teltonika FMB125 |
| Enclosure | IP67 Waterproof Box |
| Connector | PG ½ inch |
| Cable | 30 ft rubber 16 AWG |
| Drill bit | 1½ inch hole saw for metal |

---

## License

Licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Contact

Author: **Jorge Gaspar Beltre Rivera**  
Project: **DUT-E Fuel Sensor Calibration Tool**

 [![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JorgeGBeltre)
 [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jorge-gaspar-beltre-rivera/)
 [![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Jorgegaspar3021@gmail.com)

---

##  Support

This project is developed independently.

Even a small contribution helps me dedicate more time to development, testing, and releasing new features.

 [![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://www.paypal.com/donate/?hosted_button_id=2VLA8BWT967LU)
