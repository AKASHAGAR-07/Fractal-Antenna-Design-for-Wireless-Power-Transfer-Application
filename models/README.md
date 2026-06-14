# CAD & HFSS Simulation Models

This directory contains reconstruction guides and step-by-step procedures to recreate the **Hexagonal Fractal Antenna** in CAD modeling (Autodesk Fusion 360) and electromagnetic simulation (ANSYS HFSS).

Since binary CAD files (`.f3d`) and simulation mesh databases (`.aedtresults`) are proprietary, platform-specific, and bulky, we provide detailed parameters and automation scripts to reconstruct them from scratch.

---

## 🛠️ Step 1: Autodesk Fusion 360 CAD Construction
To create the physical shape of the copper radiating patch:

1. **New Design**: Open Autodesk Fusion 360 and start a new design.
2. **Create Sketch**: Select the XY plane.
3. **Base Hexagon (Iteration 0)**:
   - Go to `Create` -> `Polygon` -> `Circumscribed Polygon`.
   - Place the center at the origin `(0, 0)`.
   - Set the number of sides to **6**.
   - Input the vertex radius (radius of vertex from center) **$e = 17.39\text{ mm}$**.
4. **First Fractal Slot (Iteration 1)**:
   - Draw another circumscribed hexagon from origin `(0, 0)`.
   - Set radius to **$e / 3 = 5.80\text{ mm}$**.
   - This slot will be carved out (extruded as a cut) from the main patch.
5. **Secondary Fractal Slots (Iteration 2)**:
   - Identify the six vertices/axes of the Iteration 1 slot.
   - Sketch 6 smaller circumscribed hexagons of radius **$e / 9 = 1.93\text{ mm}$** centered along these axes (radius of center distance is **$8.70\text{ mm}$**).
6. **Microstrip Feedline**:
   - Sketch a rectangle of width **$c = 3.00\text{ mm}$** aligned with the Y-axis.
   - Set length **$d = 6.64\text{ mm}$** overlapping the bottom vertex of the main patch.
7. **Extrude**:
   - Extrude the copper patch profiles (excluding the slots) by **$0.05\text{ mm}$**.
   - Export the profile as a **STEP (`.step`)** or **IGES (`.iges`)** file for simulation.

*For precise coordinates, refer to [fusion360_model_placeholder.txt](fusion360_model_placeholder.txt).*

---

## 📡 Step 2: ANSYS HFSS Simulation Setup
To simulate the electromagnetic properties:

1. **Import Geometry**: Open ANSYS HFSS and import the STEP/IGES model from Fusion 360, OR run the Python automation script `src/hfss_automation_script.py` within HFSS (`Tools` -> `Run Script`).
2. **Substrate Setup**:
   - Create a box of dimensions: **$41.69\text{ mm}$ (X)** x **$49.41\text{ mm}$ (Y)** x **$1.575\text{ mm}$ (Z)**.
   - Assign material: **`FR4_epoxy`** ($\epsilon_r = 4.4$, $\tan \delta = 0.02$).
3. **Ground Plane Setup**:
   - Create a box at the bottom boundary ($Z = -0.07\text{ mm}$ to $Z = 0.00\text{ mm}$) of dimensions $41.69\text{ mm}$ x $49.41\text{ mm}$.
   - Assign material: **`pec`** (Perfect Electric Conductor).
4. **Boundary Conditions**:
   - Assign perfect E boundary (`PerfE`) to the ground plane box and the patch geometry.
   - Create an air box surrounding the entire board (extend by at least $\lambda/4$ in all directions, approx. **$35\text{ mm}$** at $2.4\text{ GHz}$).
   - Assign **`Radiation`** boundary condition to all outer faces of the air box.
5. **Excitation**:
   - Draw a rectangular 2D sheet between the microstrip feedline end (at $Y = 0$) and the ground plane.
   - Assign **`Lumped Port`** excitation with a reference impedance of **$50\,\Omega$**. Define the integration line from the ground plane to the feedline center.
6. **Analysis Setup**:
   - Add a solution setup with a central frequency of **$2.4\text{ GHz}$**.
   - Set maximum number of passes to **20** and target Delta S to **0.02**.
   - Add a frequency sweep from **$1.0\text{ GHz}$** to **$4.0\text{ GHz}$** (interpolating sweep, step size $0.01\text{ GHz}$).

*For step-by-step menu commands, refer to [hfss_project_placeholder.txt](hfss_project_placeholder.txt).*
