#!/usr/bin/env python3
"""
Antenna Calculator - Microstrip Patch & Hexagonal Geometry
Calculates the dimensions of a conventional microstrip patch antenna and an
equivalent regular hexagonal patch antenna based on physical formulations.
"""

import math
import sys


def calculate_patch_dimensions(f0_ghz, epsilon_r, h_mm):
    """
    Calculates physical dimensions for standard rectangular patch and
    equivalent hexagonal patch.
    """
    # Speed of light in vacuum (m/s)
    c = 3.0e8

    # Frequency in Hz
    f0 = f0_ghz * 1.0e9

    # Substrate height in meters
    h = h_mm * 1.0e-3

    # 1. Calculate rectangular patch width (W)
    width = (c / (2.0 * f0)) * math.sqrt(2.0 / (epsilon_r + 1.0))
    width_mm = width * 1000.0

    # 2. Calculate effective dielectric constant (epsilon_eff)
    epsilon_eff = ((epsilon_r + 1.0) / 2.0) + (
        (epsilon_r - 1.0) / 2.0
    ) * math.pow(1.0 + (12.0 * h / width), -0.5)

    # 3. Calculate length extension (delta_L) due to fringing fields
    ratio = width / h
    delta_l = (
        0.412
        * h
        * ((epsilon_eff + 0.3) * (ratio + 0.264))
        / ((epsilon_eff - 0.258) * (ratio + 0.8))
    )
    delta_l_mm = delta_l * 1000.0

    # 4. Calculate actual patch length (L)
    length = (c / (2.0 * f0 * math.sqrt(epsilon_eff))) - 2.0 * delta_l
    length_mm = length * 1000.0

    # 5. Calculate equivalent regular hexagonal patch side length (s)
    # Area of rectangle = W * L
    area_rect = width * length

    # Area of regular hexagon = (3 * sqrt(3) / 2) * s^2
    # Equating area_hex = area_rect:
    # (3 * sqrt(3) / 2) * s^2 = W * L
    # s = sqrt( (2 * W * L) / (3 * sqrt(3)) )
    const_factor = 3.0 * math.sqrt(3.0) / 2.0
    side_length = math.sqrt(area_rect / const_factor)
    side_length_mm = side_length * 1000.0

    # Calculate equivalent circular patch radius (a_e)
    # Area of circle = pi * a_e^2 = Area of hexagon
    a_circular = math.sqrt(area_rect / math.pi)
    a_circular_mm = a_circular * 1000.0

    return {
        "width_mm": width_mm,
        "length_mm": length_mm,
        "epsilon_eff": epsilon_eff,
        "delta_l_mm": delta_l_mm,
        "hex_side_mm": side_length_mm,
        "circular_radius_mm": a_circular_mm,
    }


def main():
    print("==========================================================")
    print("  Hexagonal & Microstrip Patch Antenna Geometry Calculator")
    print("==========================================================")

    # Standard parameters from the project report
    default_f0 = 2.4  # GHz
    default_eps = 4.4  # FR-4 dielectric constant
    default_h = 1.575  # mm substrate height

    # Allow custom inputs via arguments or prompts
    if len(sys.argv) == 4:
        try:
            f0 = float(sys.argv[1])
            eps = float(sys.argv[2])
            h = float(sys.argv[3])
        except ValueError:
            print("Error: Arguments must be numerical values.")
            sys.exit(1)
    else:
        print(
            f"Using default report values (Use 'antenna_calculator.py [freq_GHz] [eps_r] [height_mm]' for custom run)"
        )
        f0 = default_f0
        eps = default_eps
        h = default_h

    print(f"\nInputs:")
    print(f"  - Target Resonant Frequency (f0): {f0} GHz")
    print(f"  - Substrate Dielectric Constant (eps_r): {eps}")
    print(f"  - Substrate Thickness (h): {h} mm")

    results = calculate_patch_dimensions(f0, eps, h)

    print(f"\nCalculated Rectangular Patch Dimensions:")
    print(f"  - Width (W): {results['width_mm']:.4f} mm")
    print(f"  - Effective Dielectric Constant (eps_eff): {results['epsilon_eff']:.4f}")
    print(f"  - Edge Fringing Length Extension (delta_L): {results['delta_l_mm']:.4f} mm")
    print(f"  - Length (L): {results['length_mm']:.4f} mm")
    print(f"  - Total Patch Area: {results['width_mm'] * results['length_mm']:.2f} mm^2")

    print(f"\nCalculated Regular Hexagonal Patch Dimensions (Equivalent Area):")
    print(f"  - Hexagon Vertex Radius / Side Length (s): {results['hex_side_mm']:.4f} mm")
    print(f"  - Equivalent Circular Patch Radius (a): {results['circular_radius_mm']:.4f} mm")

    print("\nNote on Fractal Tuning:")
    print("  Adding slots / fractal geometry increases the electrical length.")
    print("  This permits scaling down the physical size further (tuned to s = 17.39 mm in report)")
    print("==========================================================\n")


if __name__ == "__main__":
    main()
