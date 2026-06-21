import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter, find_peaks

def load_ftir_data(path):
    """Load FTIR CSV file."""
    data = pd.read_csv(path)
    return data["Wavenumber"], data["Absorbance"]

def smooth_signal(absorbance, window=11, poly=3):
    """Apply Savitzky–Golay smoothing."""
    return savgol_filter(absorbance, window_length=window, polyorder=poly)

def detect_peaks(signal, height=0.05):
    """Detect peaks in FTIR signal."""
    peaks, properties = find_peaks(signal, height=height)
    return peaks, properties

def plot_ftir(wavenumber, signal, peaks):
    """Plot FTIR spectrum with detected peaks."""
    plt.figure(figsize=(10,5))
    plt.plot(wavenumber, signal, label="Smoothed Spectrum")
    plt.scatter(wavenumber[peaks], signal[peaks], color="red")
    plt.gca().invert_xaxis()
    plt.xlabel("Wavenumber (cm⁻¹)")
    plt.ylabel("Absorbance")
    plt.title("FTIR Spectrum with Detected Peaks")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    wn, ab = load_ftir_data("../data/sample_ftir.csv")
    smooth = smooth_signal(ab)
    peaks, _ = detect_peaks(smooth)
    plot_ftir(wn, smooth, peaks)
