# Project Structure

This document provides a detailed overview of the directory hierarchy and contents of the **Fractal-Antenna-Design-for-Wireless-Power-Transfer-Application** repository.

---

```
fractal-antenna-wpt/
├── LICENSE                    # MIT License for the project
├── README.md                  # Main portfolio presentation and project overview
├── CONTRIBUTING.md            # Guidelines on how to contribute
├── INSTALLATION.md            # Setup guide for Python scripts and HFSS automation
├── PROJECT_STRUCTURE.md       # Directory layout and explanation (this file)
├── RESULTS.md                 # Detailed simulation results comparisons
│
├── ASSETS/                    # Visual assets and diagrams used in documentation
│   ├── Project_Banner.png     # Repository banner image
│   ├── GitHub_Cover.png       # Social media/repository preview cover
│   └── Antenna_Geometry.png   # Technical diagram showing physical parameters
│
├── docs/                      # Scientific documentation and image assets
│   ├── hardware_specs.md      # Material parameters and physical layer stackup
│   ├── design_methodology.md  # Standard patch math equations and fractal stages
│   ├── simulation_results.md  # Analysis of HFSS simulation outputs
│   └── img/                   # Plot figures and photographs
│       ├── fig_4_4_hexagonal_fractal_patch.png # Fractal geometry layout
│       ├── fig_4_5_proposed_antenna_design.png # Dimension variable schematic
│       ├── fig_4_6_fabricated_front.png        # Front view of milled PCB
│       ├── fig_4_7_fabricated_back.png         # Back ground view of milled PCB
│       ├── fig_5_1_return_loss.png             # Return loss curve S11 (DB)
│       ├── fig_5_2_vswr.png                    # Voltage Standing Wave Ratio
│       ├── fig_5_3_radiation_e_plane.png       # 2D polar plot E-Plane
│       ├── fig_5_4_gain_e_plane.png            # Gain vs frequency plot
│       ├── fig_5_5_radiation_h_plane.png       # 2D polar plot H-Plane
│       ├── fig_5_6_polar_h_plane.png           # 3D realized gain pattern
│       ├── s11_plot.png                        # Recreated S11 curve
│       ├── vswr_plot.png                       # Recreated VSWR curve
│       ├── e_plane_pattern.png                 # Recreated E-Plane polar plot
│       └── h_plane_pattern.png                 # Recreated H-Plane polar plot
│
├── models/                    # Modeling guides and placeholders
│   ├── README.md              # Recreating model in CAD and HFSS
│   ├── fusion360_model_placeholder.txt  # Fusion 360 layout steps
│   └── hfss_project_placeholder.txt     # HFSS project properties
│
├── src/                       # Simulation automation and mathematical scripts
│   ├── antenna_calculator.py  # Python script to calculate microstrip patch dims
│   ├── plot_results.py        # Generates all performance plots
│   └── hfss_automation_script.py # Automated HFSS 3D model builder script
│
└── DOCUMENTS/                 # Academic files
    ├── Project_Report.pdf     # Scanned final ECE project report
    ├── Presentation.pptx      # Generated slides deck for defense
    └── Abstract.pdf           # Generated PDF abstract sheet
```

---

## Folder Details

- **ASSETS/**: Houses graphics to enhance the repository profile view, including the main project banner, GitHub social preview card, and CAD dimensional layout.
- **docs/**: The main documentation directory hosting markdown files detailing hardware specifications, design methodology, and simulation results.
- **docs/img/**: Contains return loss curves, radiation sweeps, gain charts, and photographs of the fabricated physical prototype.
- **src/**: Python scripts that calculate patch dimensions, plot 2D/3D radiation envelopes, and execute automated geometries inside ANSYS Electronic Desktop.
- **DOCUMENTS/**: Stores the full project report, project presentation slide deck, and formal abstract.
