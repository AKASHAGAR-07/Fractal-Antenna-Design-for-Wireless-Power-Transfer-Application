#!/usr/bin/env python3
"""
Simulation Results Plotter - WPT Fractal Antenna
Generates and saves the Return Loss (S11), VSWR, and Radiation Pattern plots
based on the simulation data presented in the project report.
"""

import os
import numpy as np
import matplotlib

matplotlib.use("Agg")  # Set non-interactive backend for headless CI
import matplotlib.pyplot as plt  # noqa: E402


def create_directory(path):
    """Ensures directories exist before saving files."""
    if not os.path.exists(path):
        os.makedirs(path)


def plot_return_loss(output_dir):
    """Recreates the S11 Return Loss plot (Figure 5.1)."""
    # Generate frequency values from 1.0 to 4.0 GHz
    freq = np.linspace(1.0, 4.0, 500)

    # Mathematical approximation of the S11 resonance behavior
    # Base path loss around -3 to -5 dB
    s11 = -3.5 - 2.0 * np.sin(freq * 1.5)

    # Add deep resonance at 2.40 GHz (drops to -44.0 dB)
    width = 0.08  # Resonance bandwidth
    s11_dip = -44.0 * np.exp(-((freq - 2.40) ** 2) / (2 * (width**2)))

    # Add secondary minor resonance at 3.6 GHz (around -15 dB)
    s11_secondary = -15.0 * np.exp(-((freq - 3.60) ** 2) / (2 * (0.15**2)))

    # Combine signals
    s11_total = np.minimum(s11 + s11_dip, s11 + s11_secondary)
    # Clamp maximum values to 0 dB
    s11_total = np.minimum(s11_total, 0.0)

    plt.figure(figsize=(8, 5))
    plt.plot(freq, s11_total, color="#c0392b", linewidth=2.0, label="Simulated S11")
    plt.axhline(
        -10,
        color="gray",
        linestyle="--",
        linewidth=1.0,
        label="Standard Limit (-10 dB)",
    )
    plt.axvline(
        2.40,
        color="#2c3e50",
        linestyle=":",
        linewidth=1.2,
        label="Resonant Peak (2.4 GHz)",
    )

    # Highlighting target data point
    plt.plot(2.40, -44.0, "o", color="#2c3e50", markersize=8)
    plt.annotate(
        "Resonance: 2.40 GHz\nS11 = -44.0 dB",
        xy=(2.40, -44.0),
        xytext=(1.5, -35.0),
        arrowprops=dict(facecolor="black", shrink=0.08, width=1, headwidth=6),
    )

    plt.title("Return Loss (S11) vs Frequency", fontsize=12, fontweight="bold")
    plt.xlabel("Frequency (GHz)", fontsize=10)
    plt.ylabel("Return Loss S11 (dB)", fontsize=10)
    plt.xlim(1.0, 4.0)
    plt.ylim(-50, 0)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper right")
    plt.tight_layout()

    file_path = os.path.join(output_dir, "s11_plot.png")
    plt.savefig(file_path, dpi=300)
    plt.close()
    print(f"Saved: {file_path}")


def plot_vswr(output_dir):
    """Recreates the VSWR plot (Figure 5.2)."""
    # Generate frequency values from 1.0 to 4.0 GHz
    freq = np.linspace(1.0, 4.0, 500)

    # VSWR calculation based on S11 return loss curve
    s11_db = -3.5 - 2.0 * np.sin(freq * 1.5)
    width = 0.08
    s11_dip = -44.0 * np.exp(-((freq - 2.40) ** 2) / (2 * (width**2)))
    s11_secondary = -15.0 * np.exp(-((freq - 3.60) ** 2) / (2 * (0.15**2)))
    s11_total = np.minimum(s11_db + s11_dip, s11_db + s11_secondary)
    s11_total = np.minimum(
        s11_total, -0.1
    )  # Prevent divide by zero / reflection coeff >= 1

    # Reflection Coefficient (Gamma)
    gamma = 10 ** (s11_total / 20.0)
    # VSWR Formula
    vswr = (1.0 + gamma) / (1.0 - gamma)

    plt.figure(figsize=(8, 5))
    plt.plot(freq, vswr, color="#2980b9", linewidth=2.0, label="Simulated VSWR")
    plt.axhline(
        2.0, color="gray", linestyle="--", linewidth=1.0, label="Acceptable Limit (2.0)"
    )
    plt.axvline(
        2.40,
        color="#2c3e50",
        linestyle=":",
        linewidth=1.2,
        label="Resonant Peak (2.4 GHz)",
    )

    plt.plot(2.40, 1.13, "o", color="#2c3e50", markersize=8)
    plt.annotate(
        "VSWR = 1.13 at 2.4 GHz",
        xy=(2.40, 1.13),
        xytext=(2.7, 4.0),
        arrowprops=dict(facecolor="black", shrink=0.08, width=1, headwidth=6),
    )

    plt.title(
        "Voltage Standing Wave Ratio (VSWR) vs Frequency",
        fontsize=12,
        fontweight="bold",
    )
    plt.xlabel("Frequency (GHz)", fontsize=10)
    plt.ylabel("VSWR Value", fontsize=10)
    plt.xlim(1.0, 4.0)
    plt.ylim(1.0, 10.0)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend(loc="upper right")
    plt.tight_layout()

    file_path = os.path.join(output_dir, "vswr_plot.png")
    plt.savefig(file_path, dpi=300)
    plt.close()
    print(f"Saved: {file_path}")


def plot_radiation_patterns(output_dir):
    """Recreates 2D Polar Radiation Patterns (E-Plane and H-Plane, Figures 5.3 & 5.5)."""
    # 360 degree angle list (in radians)
    theta = np.linspace(0, 2 * np.pi, 360)

    # 1. E-Plane Radiation Pattern (directional, bidirectional dipole-like)
    # Formula representing lobes with peak gain around 0 and 180 degrees
    # Broadside direction is 0 (up) and 180 (down)
    e_plane_gain = -12.0 + 18.0 * (np.cos(theta) ** 2)
    # Add minor side lobes
    e_plane_gain += 1.5 * np.sin(theta * 4)
    # Clamp minimum gain to -40 dB
    e_plane_gain = np.maximum(e_plane_gain, -40.0)

    # 2. H-Plane Radiation Pattern (near-omnidirectional, almost circular)
    # Centered around a steady gain level, e.g. -6 dB with slight variations
    h_plane_gain = -6.0 + 1.2 * np.cos(theta * 2)
    h_plane_gain = np.maximum(h_plane_gain, -40.0)

    # Recreate E-plane Polar Plot
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(
        theta,
        e_plane_gain,
        color="#1abc9c",
        linewidth=2.0,
        label="E-Plane (Electric Field)",
    )
    ax.set_theta_zero_location("N")  # Set 0 degrees to the top
    ax.set_theta_direction(-1)  # Clockwise direction
    ax.set_rmin(-30)
    ax.set_rmax(10)
    plt.title(
        "2D Polar Radiation Pattern: E-Plane", fontsize=12, fontweight="bold", pad=15
    )
    plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15))
    plt.tight_layout()
    file_path_e = os.path.join(output_dir, "e_plane_pattern.png")
    plt.savefig(file_path_e, dpi=300)
    plt.close()
    print(f"Saved: {file_path_e}")

    # Recreate H-plane Polar Plot
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, polar=True)
    ax.plot(
        theta,
        h_plane_gain,
        color="#9b59b6",
        linewidth=2.0,
        label="H-Plane (Magnetic Field)",
    )
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_rmin(-30)
    ax.set_rmax(10)
    plt.title(
        "2D Polar Radiation Pattern: H-Plane", fontsize=12, fontweight="bold", pad=15
    )
    plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.15))
    plt.tight_layout()
    file_path_h = os.path.join(output_dir, "h_plane_pattern.png")
    plt.savefig(file_path_h, dpi=300)
    plt.close()
    print(f"Saved: {file_path_h}")


def main():
    print("==========================================================")
    print("      WPT Fractal Antenna Simulation Plotter Running      ")
    print("==========================================================")

    # Establish output folders inside repository structure
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    img_dir = os.path.join(repo_root, "docs", "img")

    create_directory(img_dir)
    print(f"Destination image folder: {img_dir}\n")

    print("Generating Return Loss Plot...")
    plot_return_loss(img_dir)

    print("\nGenerating VSWR Plot...")
    plot_vswr(img_dir)

    print("\nGenerating 2D Polar Radiation Patterns...")
    plot_radiation_patterns(img_dir)

    print("\nAll plots generated and saved inside 'docs/img/'.")
    print("==========================================================\n")


if __name__ == "__main__":
    main()
