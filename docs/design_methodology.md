# Design & Mathematical Methodology

This document outlines the mathematical formulations and design procedures used to engineer the Hexagonal Fractal Microstrip Patch Antenna operating at 2.4 GHz.

---

## 📐 Standard Microstrip Patch Antenna Equations

A microstrip patch antenna is defined by its width ($W$) and length ($L$). For a given resonant frequency ($f_0$) and substrate height ($h$), standard design equations are as follows:

### 1. Calculation of Width ($W$)
The physical width of the radiating patch affects the radiation pattern and impedance. It is calculated as:

$$W = \frac{v_0}{2 f_0} \sqrt{\frac{2}{\epsilon_r + 1}}$$

where:
* $v_0 = 3 \times 10^8\text{ m/s}$ (speed of light in vacuum)
* $f_0 = 2.4\text{ GHz} = 2.4 \times 10^9\text{ Hz}$ (target frequency)
* $\epsilon_r = 4.4$ (FR-4 dielectric constant)

### 2. Effective Dielectric Constant ($\epsilon_{\text{eff}}$)
Due to fringing fields at the patch edges, waves travel partly in the substrate and partly in air. The effective dielectric constant accounts for this mixed medium:

$$\epsilon_{\text{eff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left[1 + 12\frac{h}{W}\right]^{-1/2}$$

where $h = 1.575\text{ mm}$ (substrate thickness).

### 3. Length Extension ($\Delta L$)
Fringing fields make the patch appear electrically larger than its physical length. This extension is approximated by:

$$\Delta L = 0.412 h \frac{(\epsilon_{\text{eff}} + 0.3) \left(\frac{W}{h} + 0.264\right)}{(\epsilon_{\text{eff}} - 0.258) \left(\frac{W}{h} + 0.8\right)}$$

### 4. Resonant Length ($L$)
The actual physical length of a rectangular patch is:

$$L = \frac{v_0}{2 f_0 \sqrt{\epsilon_{\text{eff}}}} - 2 \Delta L$$

---

## ⬢ Hexagonal Patch Formulation

To transform the standard rectangular patch into a hexagonal geometry, we equate the area of a regular hexagon to the equivalent circular patch radius ($a_{\text{circular}}$), which is then derived from rectangular dimensions.

### 1. Hexagon Area
For a regular hexagon with side length $s$ (equal to the outer radius $e$ of the vertices from the center):

$$\text{Area}_{\text{hex}} = \frac{3\sqrt{3}}{2} s^2 \approx 2.598 s^2$$

### 2. Equivalent Circular Patch Radius ($a_e$)
Equating the area of the hexagon to that of a circle ($\pi a_e^2$):

$$\pi a_e^2 = \frac{3\sqrt{3}}{2} s^2 \implies a_e = s \sqrt{\frac{3\sqrt{3}}{2\pi}} \approx 0.9094 s$$

The resonant frequency of a circular patch is given by:

$$f_0 = \frac{1.8412 v_0}{2 \pi a_e \sqrt{\epsilon_r}}$$

Substituting $a_e$ and solving for the hexagon side length $s$ yields the initial dimension for the hexagonal patch.

---

## 🌀 Fractal Geometry and Iteration Stages

Fractal structures utilize self-similarity—repeating a geometric shape at smaller scales. This technique increases the electrical length (perimeter) of the antenna while maintaining the same outer volume, facilitating miniaturization and multi-band behavior.

```mermaid
graph LR
    I0[Iteration 0: <br> Solid Hexagon] --> I1[Iteration 1: <br> Center Slot Carved]
    I1 --> I2[Iteration 2: <br> Multiple Smaller Slots]
```

### 1. Iteration 0 (Base Structure)
* **Description**: A solid hexagonal patch of radius $e = 17.39\text{ mm}$.
* **Behavior**: Resonates at a higher frequency. The return loss and bandwidth are limited.

### 2. Iteration 1 (First Fractal Stage)
* **Description**: A central hexagonal slot is subtracted from the patch.
* **Scale Factor ($k_1$)**: $1/3$ ($5.8\text{ mm}$).
* **Behavior**: Current is forced to flow along the boundaries of the slot, lengthening the electrical path. This lowers the resonant frequency closer to 2.4 GHz.

### 3. Iteration 2 (Proposed Fractal Stage)
* **Description**: Secondary, smaller hexagonal slots are subtracted along the vertices or adjacent edges.
* **Scale Factor ($k_2$)**: $1/9$ ($1.93\text{ mm}$).
* **Behavior**: Greatly increases the capacitive loading and edge complexity. This optimizes impedance matching ($50\,\Omega$), resulting in the simulated return loss ($S_{11}$) of $-44\text{ dB}$ at $2.4\text{ GHz}$.
