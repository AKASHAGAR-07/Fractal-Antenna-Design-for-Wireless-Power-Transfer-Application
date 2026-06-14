# Simulation Results and Performance Analysis

This document presents a comprehensive review of the electromagnetic simulation results obtained for the Hexagonal Fractal Antenna using ANSYS HFSS (High Frequency Structure Simulator).

---

## 📈 Key Performance Metrics

The simulated performance parameters demonstrate that the proposed hexagonal fractal antenna is highly optimized for the 2.4 GHz ISM band:

| Metric | Target Value | Simulated Value | Status |
| :--- | :--- | :--- | :--- |
| **Resonant Frequency** | $2.40\text{ GHz}$ | $2.40\text{ GHz}$ | **Matched** |
| **Return Loss ($S_{11}$)** | $\le -10\text{ dB}$ | **$-44.0\text{ dB}$** | **Exceeded** |
| **VSWR** | $\le 2.0$ | **$1.13$** (at resonance) | **Exceeded** |
| **Impedance Bandwidth** | $> 50\text{ MHz}$ | **$120\text{ MHz}$** (at $-10\text{ dB}$ level) | **Exceeded** |
| **Radiation Pattern** | Directional / Omnidirectional | Symmetrical E-plane, Omnidirectional H-plane | **Matched** |

---

## 📊 Detailed Metric Breakdown

### 1. Return Loss ($S_{11}$)
Return loss represents the amount of power reflected back to the source due to impedance mismatch. 
* At $2.4\text{ GHz}$, the return loss is **$-44\text{ dB}$**.
* This corresponds to a reflection coefficient of:
  $$\Gamma = 10^{\frac{S_{11}}{20}} = 10^{-2.2} \approx 0.0063$$
* The percentage of reflected power is:
  $$\text{Reflected Power (\%)} = |\Gamma|^2 \times 100 \approx 0.004\%$$
* Consequently, **$99.996\%$** of the power is successfully accepted by the antenna, making it highly efficient for wireless power harvesting/transmission.

### 2. Voltage Standing Wave Ratio (VSWR)
VSWR measures the impedance mismatch between the transmission line and the antenna.
* The simulated VSWR is **$1.13$** at $2.4\text{ GHz}$.
* Since $1.0 \le \text{VSWR} \le 1.5$ is considered excellent in RF engineering, this confirms that the microstrip feedline configuration ($3.00\text{ mm}$ width) successfully matches the patch to the standard $50\,\Omega$ coaxial connector interface.

### 3. E-Plane Radiation Pattern (Electric Field)
* **Characteristics**: Symmetrical bidirectional pattern along the elevation plane (Theta coordinate).
* **Gain Major Lobe**: Features a peak gain directed perpendicular to the patch, optimizing broadside radiation efficiency.
* **Beamwidth**: Symmetrical 3dB beamwidth of approximately $68^\circ$, which minimizes interference from surrounding metallic boundaries.

### 4. H-Plane Radiation Pattern (Magnetic Field)
* **Characteristics**: Near-omnidirectional profile along the azimuth plane (Phi coordinate).
* **Significance**: For Wireless Power Transfer (WPT) applications, an omnidirectional H-plane is highly beneficial, as it allows the receiving rectenna to capture magnetic field fields and transmit power regardless of orientation/angle.

---

## 🔀 Comparison with Existing Methods (Table 2.1 Reference)

Below is a comparative evaluation of the proposed design against traditional microstrip configurations documented in literature (as referenced in Table 2.1 of the report):

| Antenna Design | Resonant Freq. (GHz) | Return Loss ($S_{11}$) | VSWR | Relative Size (Footprint) | Main Application |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Conventional Rectangular Patch** | 2.40 | $-18.5\text{ dB}$ | 1.35 | $100\%$ (Base) | WLAN / Wi-Fi |
| **Conventional Circular Patch** | 2.45 | $-21.0\text{ dB}$ | 1.22 | $92\%$ | RFID / Sensor Nodes |
| **Hexagonal Patch (Iteration 0)** | 2.52 | $-15.2\text{ dB}$ | 1.42 | $85\%$ | Wireless Telemetry |
| **Proposed Hexagonal Fractal (Iter. 2)** | **2.40** | **$-44.0\text{ dB}$** | **1.13** | **$68\%$** | **Wireless Power Transfer (WPT)** |

### Conclusion on Size Reduction
By implementing a regular hexagon and subtracting nested fractal slots, the physical area was reduced by **$32\%$** compared to a conventional rectangular patch at the same operating frequency, while simultaneously improving return loss from $-18.5\text{ dB}$ to $-44\text{ dB}$.
