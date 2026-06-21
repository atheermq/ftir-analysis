🧪 FTIR Analysis for Scientific Research
Python-based FTIR data analysis workflow for chemical and material characterization.

📌 Project Overview
This project provides a clean and reproducible workflow for analyzing FTIR spectra using Python.
It is designed for scientific research, especially for applications in:

Material characterization

Food engineering

Chemical engineering

Drying and pretreatment studies

Functional group identification

The project includes preprocessing, peak detection, visualization, and interpretation tools.

📂 Project Structure
Code
ftir-analysis/
│
├── data/                # Raw FTIR data (CSV/TXT)
├── notebooks/           # Jupyter notebooks for analysis
├── scripts/             # Python scripts for processing
├── results/             # Generated plots and outputs
└── README.md            # Project documentation
⚙️ Features
Load FTIR spectral data

Baseline correction

Smoothing (Savitzky–Golay)

Peak detection

Functional group identification

Plotting absorbance vs. wavenumber

Exporting results

📊 Example Code (Python)
python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks

# Load FTIR data
data = pd.read_csv("data/sample_ftir.csv")
wavenumber = data["Wavenumber"]
absorbance = data["Absorbance"]

# Smoothing
smooth = savgol_filter(absorbance, window_length=11, polyorder=3)

# Peak detection
peaks, _ = find_peaks(smooth, height=0.05)

# Plot
plt.figure(figsize=(10,5))
plt.plot(wavenumber, smooth, label="Smoothed Spectrum")
plt.scatter(wavenumber[peaks], smooth[peaks], color='red')
plt.gca().invert_xaxis()
plt.xlabel("Wavenumber (cm⁻¹)")
plt.ylabel("Absorbance")
plt.title("FTIR Spectrum with Detected Peaks")
plt.legend()
plt.show()
🔬 Scientific Notes (from your research)
“FTIR analysis confirmed that ginger retained gingerol at lower temperatures, while potatoes showed starch degradation at higher temperatures.”

This project can be extended to analyze:

O–H stretching

C–H bending

C=O stretching

C–O–C functional groups

🚀 Future Extensions
Machine learning classification

PCA for spectral clustering

Comparing pretreatment effects

Automated peak assignment

👩‍🔬 Author
Atheer Mansour Alqahtani  
Chemical Engineer | AI & Digital Twins Enthusiast
