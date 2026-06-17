# ANSYS HFSS & Autodesk Fusion 360 Modeling Manual

This guide provides step-by-step instructions to manually reconstruct the **Hexagonal Fractal Microstrip Patch Antenna** (Iteration 2) CAD model and execute the electromagnetic simulation within **ANSYS HFSS**.

---

## 1. Physical Antenna Specifications

The design utilizes a double-sided copper-clad FR-4 substrate. Verify that you configure the design parameters with these exact values during the CAD drawing phase:

- **Substrate Length ($L_{sub}$):** $49.41\text{ mm}$ (along Y-axis)
- **Substrate Width ($W_{sub}$):** $41.69\text{ mm}$ (along X-axis)
- **Substrate Thickness ($h$):** $1.575\text{ mm}$ (along Z-axis)
- **Microstrip Feedline Width ($W_f$):** $3.00\text{ mm}$
- **Microstrip Feedline Length ($L_f$):** $6.64\text{ mm}$
- **Main Hexagonal Patch Outer Radius ($R_{hex}$):** $17.39\text{ mm}$
- **Hexagon Center Coordinate:** $(0, 25.0, 1.575)$ on the top plane.
- **Copper Layer Thickness ($t_c$):** $0.05\text{ mm}$ (top patch and feedline) | $0.07\text{ mm}$ (bottom ground plane)

---

## 2. Step-by-Step Geometry Reconstruction (Autodesk Fusion 360)

1. **Draw Substrate Box**:
   - Create a sketch on the XY plane. Sketch a rectangle centered at $(0, 0)$ with dimensions $41.69\text{ mm} \times 49.41\text{ mm}$.
   - Extrude this boundary down by $1.575\text{ mm}$ (assigning the body as the dielectric substrate).
2. **Draw Feedline**:
   - Select the top surface of the substrate.
   - Sketch a centered rectangle of width $3.00\text{ mm}$ and length $6.64\text{ mm}$ extending inward from the bottom edge.
3. **Draw Hexagonal Patch**:
   - Sketch a regular hexagon (using Circumscribed Polygon tool) with radius $17.39\text{ mm}$ centered at $(0, 25.0)$ on the top surface.
4. **Implement Fractal Iteration Slots**:
   - **Iteration 1 Slot:** Draw a concentric regular hexagon with a radius of $5.80\text{ mm}$ (scale factor of $1/3$). Select the inner profile and subtract (cut) it from the main hexagonal patch body.
   - **Iteration 2 Slots:** Construct six smaller regular hexagons, each with a radius of $1.93\text{ mm}$ (scale factor of $1/9$). Center these slots at the six outer vertices of the central Iteration 1 slot. Subtract (cut) these profiles from the patch.
5. **Extrude Conductive Layer**:
   - Extrude the remaining patch profile and the feedline together by $0.05\text{ mm}$ upward.
   - Flip the layout to the bottom surface of the substrate and extrude a solid rectangle of $41.69\text{ mm} \times 49.41\text{ mm}$ by $0.07\text{ mm}$ to form the ground plane.

---

## 3. Electromagnetic Analysis Setup (ANSYS HFSS)

If you are importing the model or recreating it directly inside the HFSS 3D Modeler:

### Step 1: Assign Material Properties
- **Substrate Body:** Assign material `FR4_epoxy` ($\epsilon_r = 4.4$, $\tan\delta = 0.02$).
- **Radiating Patch & Feedline:** Assign boundary condition **Perfect E** (or set material as `copper`).
- **Ground Plane:** Assign boundary condition **Perfect E** (or set material as `copper`).

### Step 2: Define Port Excitation
- Create a rectangular sheet at the bottom edge of the microstrip feedline. The sheet must stretch along the Z-axis, connecting the feedline conductor (top) to the ground plane (bottom). Width = $3.00\text{ mm}$, Height = $1.575\text{ mm}$.
- Select the sheet, right-click, and choose **Assign Excitation > Lumped Port**.
- Set the reference impedance to $50\,\Omega$ and draw the integration line from the bottom ground edge vertically upward to the top feedline edge.

### Step 3: Set up Radiation Boundary (Airbox)
- Create a large box surrounding the antenna model. The walls of the box should be at least $\lambda_0/4 \approx 31.25\text{ mm}$ away from the antenna in all directions.
- Select the airbox, right-click, and choose **Assign Boundary > Radiation**.

### Step 4: Configure Solution Setup & Sweep
1. **Analysis Setup:** Right-click **Analysis** in the Project Tree and click **Add Solution Setup > Advanced**.
   - **Center Frequency:** Set to $2.4\text{ GHz}$.
   - **Convergence Details:** Maximum Number of Passes = $15$, Max Delta S = $0.02$.
2. **Frequency Sweep:** Right-click the newly created Setup and click **Add Frequency Sweep**.
   - **Sweep Type:** Interpolating.
   - **Frequency Range:** Start = $1.0\text{ GHz}$, Stop = $4.0\text{ GHz}$.
   - **Step Size:** $0.01\text{ GHz}$ ($10\text{ MHz}$) for high resolution.
3. **Analyze:** Click **Analyze All** to run the 3D full-wave electromagnetic simulation.

---

## 4. Plotting & Retrieving Results

After simulation completes, extract the original curves:
- **Return Loss ($S_{11}$):** Create a Terminal S-Parameter rectangular plot of $S_{11}$ in dB vs. Frequency to verify the $-44.0\text{ dB}$ dip at $2.4\text{ GHz}$.
- **VSWR:** Create a Terminal VSWR rectangular plot vs. Frequency to verify the $1.13$ value at resonance.
- **Radiation Pattern:** Create a 3D polar plot of Realized Gain at $2.4\text{ GHz}$ to view the symmetrical broadside beam profile.
