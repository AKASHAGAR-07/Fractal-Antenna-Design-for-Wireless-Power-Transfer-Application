# Installation & Script Execution Guide

This guide provides step-by-step instructions to configure the computational environment, run the Python analysis scripts, and execute the automated modeling project within the ANSYS Electronics Desktop (HFSS) environment.

---

## 1. Local Environment Configuration

The mathematical and analysis scripts require Python 3.8 or later.

### Step 1: Install Required Libraries
Set up your virtual environment (recommended) and install the dependencies:
```bash
pip install numpy matplotlib python-pptx reportlab
```

### Step 2: Running the Python Utilities

- **Antenna Parameter Calculator**:
  Computes the physical width ($W$), effective dielectric constant ($\epsilon_{eff}$), length extension ($\Delta L$), and resonant length ($L$) for a standard microstrip patch:
  ```bash
  python src/antenna_calculator.py
  ```

- **Recreate Plots**:
  Generates return loss ($S_{11}$), VSWR, realized gain, and 2D/3D radiation patterns, saving them directly inside `docs/img/`:
  ```bash
  python src/plot_results.py
  ```

---

## 2. Reconstructing the CAD Model (Autodesk Fusion 360)

1. Open Autodesk Fusion 360.
2. Create a sketch on the XY plane and construct a rectangle centered at $(0, 0)$ representing the substrate dimensions: $49.41\text{ mm} \times 41.69\text{ mm}$. Extrude to $1.575\text{ mm}$.
3. Create a sketch on the top surface. Draw the feedline rectangle: $3.00\text{ mm}$ width and $6.64\text{ mm}$ length starting from the bottom edge.
4. Draw a regular hexagon with outer radius $17.39\text{ mm}$ centered at $(0, 25.0)$.
5. Apply fractal slotting:
   - Subtract a central hexagon with radius $5.80\text{ mm}$ (Iteration 1).
   - Subtract six small hexagons with radius $1.93\text{ mm}$ centered along the outer vertices of the central slot (Iteration 2).
6. Extrude the copper layer to $0.05\text{ mm}$.

---

## 3. Scripting Automation in ANSYS HFSS

The `src/hfss_automation_script.py` script utilizes the ANSYS Electronics Desktop scripting API to automate model generation:

### Executing from ANSYS Electronics Desktop GUI
1. Launch ANSYS Electronics Desktop (HFSS).
2. Go to the top menu bar and navigate to **Tools > Run Script...**
3. Locate and select the [src/hfss_automation_script.py](src/hfss_automation_script.py) file.
4. The script will automatically create a project named `WPT_Fractal_Antenna`, set up a 3D Modeler design space, and build the substrate box, PEC ground plane, feedline, and the regular hexagonal fractal patch with Iteration 2 slot subtractions.

### Setting Up Boundary Conditions & Simulation Sweep
1. **Material Assignment**: Assign `FR4_epoxy` to the substrate body, `pec` to the ground, and `copper` to the radiating patch/feedline.
2. **Radiation Boundary**: Create an airbox enclosing the antenna at a distance of at least $\lambda_0/4 \approx 31.25\text{ mm}$ in all directions, and assign a **Radiation** boundary condition.
3. **Excitation Port**: Define a **Lumped Port** on a sheet connecting the bottom edge of the feedline to the ground plane, with a $50\,\Omega$ reference impedance.
4. **Analysis Setup**: Add a Solution Setup at $2.4\text{ GHz}$ with a maximum delta-S of $0.02$ and 15 max passes.
5. **Frequency Sweep**: Configure an Interpolating Frequency Sweep from $1.0\text{ GHz}$ to $4.0\text{ GHz}$ to capture the resonant curves.
