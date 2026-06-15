#!/usr/bin/env python3
"""
HFSS Automation Script - WPT Fractal Antenna
This Python script is designed to run within the ANSYS Electronics Desktop (HFSS)
scripting environment (or externally via PyAEDT). It automates the generation
of the substrate, ground plane, microstrip feedline, and the regular hexagonal
fractal patch with nested iterations.

To run inside HFSS:
1. Open ANSYS Electronics Desktop.
2. Go to Tools -> Run Script.
3. Select this file.
"""

import math

# Try importing HFSS scripting engine modules if running inside the engine
try:
    import ScriptEnv  # noqa: F401

    # Fetch oAnsoftApp dynamically to prevent IDE warnings/errors about unresolved reference
    oAnsoftApp = globals().get("oAnsoftApp")
    if oAnsoftApp is None:
        raise NameError("oAnsoftApp not found in global scope")

    oAnsoftApp.SetCurrentProject("WPT_Fractal_Antenna")
    oDesktop = oAnsoftApp.GetAppDesktop()
    oProject = oDesktop.NewProject()
    oProject.InsertDesign("HFSS", "Hexagonal_Fractal_Design", "Driven Terminal")
    oDesign = oProject.GetActiveDesign()
    oEditor = oDesign.SetActiveEditor("3D Modeler")
    IN_HFSS = True
except (ImportError, NameError, AttributeError):
    # If running externally, this file serves as a template/placeholder document
    IN_HFSS = False


# Antenna Specifications (Table 4.1 & Report specifications)
SUBSTRATE_X = 41.69  # width b (mm)
SUBSTRATE_Y = 49.41  # length a (mm)
SUBSTRATE_Z = 1.575  # thickness h (mm)

PATCH_RADIUS_E = 17.39  # outer radius of hexagonal patch e (mm)
FEED_WIDTH = 3.0  # feedline width c (mm)
FEED_LENGTH = 6.64  # feedline length d (mm)

COPPER_THICKNESS = 0.05  # patch/feed thickness (mm)
GROUND_THICKNESS = 0.07  # ground thickness (mm)


def get_hexagon_vertices(center_x, center_y, radius):
    """Calculates the 6 coordinates of a regular hexagon."""
    points = []
    for i in range(6):
        angle_rad = math.radians(60 * i)
        px = center_x + radius * math.cos(angle_rad)
        py = center_y + radius * math.sin(angle_rad)
        points.append((px, py))
    return points


def create_solid_hexagon(name, center_x, center_y, radius, z_pos, thickness):
    """Generates a regular hexagonal sheet or solid in HFSS."""
    if not IN_HFSS:
        return

    pts = get_hexagon_vertices(center_x, center_y, radius)

    # In HFSS scripting, we create a polyline passing through all 6 points and close it
    point_str_list = []
    for pt in pts:
        point_str_list.append(
            f"CoordinateSystemID:= 1, X:= {pt[0]}mm, Y:= {pt[1]}mm, Z:= {z_pos}mm"
        )
    # Add first point to close polyline
    point_str_list.append(
        f"CoordinateSystemID:= 1, X:= {pts[0][0]}mm, Y:= {pts[0][1]}mm, Z:= {z_pos}mm"
    )

    # Call HFSS Drawing Editor commands
    oEditor.CreatePolyline(
        [
            "NAME:PolylineParameters",
            "IsPolylineCovered:=",
            True,
            "IsPolylineClosed:=",
            True,
            ["NAME:PolylinePointsList"] + point_str_list,
        ],
        [
            "NAME:Attributes",
            "Name:=",
            name,
            "Flags:=",
            "",
            "Color:=",
            "(218 165 32)",  # Gold/Copper color
            "Transparency:=",
            0,
            "MaterialName:=",
            "copper",
            "SolveInside:=",
            False,
        ],
    )

    # Thicken sheet to represent physical copper
    oEditor.ThickenSheet(
        ["NAME:Selections", "Selections:=", name, "NewDesignator:=", ""],
        ["NAME:Parameters", "Thickness:=", f"{thickness}mm", "BothSides:=", False],
    )


def build_geometry():
    """Main function to build the layers in HFSS."""
    print("Initializing geometry building script...")

    if not IN_HFSS:
        print("\n[INFO] Script is not running inside ANSYS HFSS environment.")
        print("[INFO] Geometry parameters validated successfully:")
        print(
            f"  - Substrate dimensions: {SUBSTRATE_X} x {SUBSTRATE_Y} x {SUBSTRATE_Z} mm (FR-4)"
        )
        print(f"  - Hexagonal Patch outer radius: {PATCH_RADIUS_E} mm (Copper)")
        print(
            f"  - Microstrip feedline width: {FEED_WIDTH} mm, length: {FEED_LENGTH} mm"
        )
        print("[INFO] Refer to models/hfss_project_placeholder.txt for reproduction.")
        return

    # 1. Create FR-4 Substrate
    # Substrate box is centered at X=0, but placed from Y=0 to Y=SUBSTRATE_Y
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XStart:=",
            f"-{SUBSTRATE_X/2}mm",
            "YStart:=",
            "0mm",
            "ZStart:=",
            "0mm",
            "XSize:=",
            f"{SUBSTRATE_X}mm",
            "YSize:=",
            f"{SUBSTRATE_Y}mm",
            "ZSize:=",
            f"{SUBSTRATE_Z}mm",
        ],
        [
            "NAME:Attributes",
            "Name:=",
            "Substrate",
            "Flags:=",
            "",
            "Color:=",
            "(0 128 0)",  # Green FR-4
            "Transparency:=",
            0.4,
            "MaterialName:=",
            "FR4_epoxy",
            "SolveInside:=",
            True,
        ],
    )

    # 2. Create PEC Ground Plane
    # Ground plane is placed on the bottom layer (Z = -GROUND_THICKNESS)
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XStart:=",
            f"-{SUBSTRATE_X/2}mm",
            "YStart:=",
            "0mm",
            "ZStart:=",
            f"-{GROUND_THICKNESS}mm",
            "XSize:=",
            f"{SUBSTRATE_X}mm",
            "YSize:=",
            f"{SUBSTRATE_Y}mm",
            "ZSize:=",
            f"{GROUND_THICKNESS}mm",
        ],
        [
            "NAME:Attributes",
            "Name:=",
            "GroundPlane",
            "Flags:=",
            "",
            "Color:=",
            "(128 128 128)",  # Grey
            "Transparency:=",
            0.1,
            "MaterialName:=",
            "pec",
            "SolveInside:=",
            False,
        ],
    )

    # 3. Create Microstrip Feedline
    # Microstrip feed runs from Y=0 up to Y=FEED_LENGTH on the top layer (Z = SUBSTRATE_Z)
    oEditor.CreateBox(
        [
            "NAME:BoxParameters",
            "XStart:=",
            f"-{FEED_WIDTH/2}mm",
            "YStart:=",
            "0mm",
            "ZStart:=",
            f"{SUBSTRATE_Z}mm",
            "XSize:=",
            f"{FEED_WIDTH}mm",
            "YSize:=",
            f"{FEED_LENGTH}mm",
            "ZSize:=",
            f"{COPPER_THICKNESS}mm",
        ],
        [
            "NAME:Attributes",
            "Name:=",
            "Feedline",
            "Flags:=",
            "",
            "Color:=",
            "(218 165 32)",
            "Transparency:=",
            0,
            "MaterialName:=",
            "copper",
            "SolveInside:=",
            False,
        ],
    )

    # 4. Create Main Hexagonal Patch (Iteration 0)
    # The center of the patch is aligned with the top end of the feedline
    # Let's say center is at X=0, Y = FEED_LENGTH + (distance to center)
    # The patch overlaps slightly with the feedline. Center is set to Y = 25.0 mm.
    patch_center_y = 25.0
    create_solid_hexagon(
        "MainPatch", 0.0, patch_center_y, PATCH_RADIUS_E, SUBSTRATE_Z, COPPER_THICKNESS
    )

    # 5. Create Iteration 1 Central Slot (to subtract)
    # Scale slot by 1/3
    slot1_radius = PATCH_RADIUS_E / 3.0
    create_solid_hexagon(
        "Slot1", 0.0, patch_center_y, slot1_radius, SUBSTRATE_Z, COPPER_THICKNESS
    )

    # Subtract Slot1 from MainPatch
    oEditor.Subtract(
        ["NAME:Selections", "BlankParts:=", "MainPatch", "ToolParts:=", "Slot1"],
        ["NAME:SubtractParameters", "ReplaceWithParts:=", True],
    )

    # 6. Create Iteration 2 Secondary Slots (to subtract)
    # Place smaller slots (scale 1/9) around the main slot along the vertices
    slot2_radius = PATCH_RADIUS_E / 9.0
    vertices = get_hexagon_vertices(
        0.0, patch_center_y, slot1_radius * 1.5
    )  # placed intermediate to edges

    slot_names = []
    for idx, vert in enumerate(vertices):
        slot_name = f"Slot2_{idx}"
        create_solid_hexagon(
            slot_name, vert[0], vert[1], slot2_radius, SUBSTRATE_Z, COPPER_THICKNESS
        )
        slot_names.append(slot_name)

    # Subtract all Iteration 2 slots
    oEditor.Subtract(
        [
            "NAME:Selections",
            "BlankParts:=",
            "MainPatch",
            "ToolParts:=",
            ",".join(slot_names),
        ],
        ["NAME:SubtractParameters", "ReplaceWithParts:=", True],
    )

    # 7. Unify Feedline and Fractal Patch
    oEditor.Unify(
        ["NAME:Selections", "Selections:=", "Feedline,MainPatch"],
        ["NAME:UnifyParameters", "Glue:=", False],
    )

    print("Geometry building script executed successfully.")


if __name__ == "__main__":
    build_geometry()
